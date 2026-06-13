from time import sleep
from servo_control import (
    arm_home,
    pick_object,
    drop_category,
    cleanup as servo_cleanup
)
from datetime import datetime
from weight_sensor import (
    get_weight,
    set_zero,
    cleanup as weight_cleanup
)
from ml_classifier import (
    classify_object,
    cleanup as camera_cleanup
)
from display_manager import update_display
from dashboard_data import (
    read_data,
    write_data
)
# =====================================
# SETTINGS
# =====================================
OBJECT_THRESHOLD = 2
try:
    print("================================")
    print(" RoboSort Pro Starting")
    print("================================")
    data = read_data()
    data["system_status"] = "Running"
    data["robot_arm_status"] = "Stopped"
    data["current_object"] = "Waiting..."
    data["weight"] = 0
    write_data(data)
    arm_home()
    set_zero()
    print("Waiting for START command...")
    while True:
        # =====================================
        # START / STOP CONTROL
        # =====================================
        data = read_data()
        if data["robot_arm_status"] != "Running":
            sleep(0.5)
            continue
        sleep(0.5)
        # =====================================
        # WEIGHT READING
        # =====================================
        weight = get_weight()
        if weight < 0:
            weight = 0
        data = read_data()
        data["weight"] = round(weight, 2)
        write_data(data)
        if weight < OBJECT_THRESHOLD:
            continue
        sleep(0.5)
        weight = get_weight()
        if weight < OBJECT_THRESHOLD:
            continue
        print("\nObject Detected")
        # =====================================
        # DETECTING
        # =====================================
        data = read_data()
        data["robot_arm_status"] = "Detecting"
        data["weight"] = round(weight, 2)
        write_data(data)
        # =====================================
        # ML CLASSIFICATION
        # =====================================
        prediction, confidence = classify_object()
        # =====================================
        # WEIGHT CLASSIFICATION
        # =====================================
        if "small" in prediction:
            if weight < 10:
                weight_type = "light"
            else:
                weight_type = "heavy"
        else:
            if weight < 25:
                weight_type = "light"
            else:
                weight_type = "heavy"

        final_category = prediction + "_" + weight_type
        # =====================================
        # DASHBOARD UPDATE
        # =====================================
        data = read_data()
        data["current_object"] = final_category
        data["weight"] = round(weight, 2)
        write_data(data)

        # =====================================
        # TFT DISPLAY UPDATE
        # =====================================

        update_display(
            prediction,
            confidence * 100,
            final_category
        )

        print("Prediction :", prediction)
        print("Confidence :", round(confidence * 100, 2), "%")
        print("Weight     :", round(weight, 2), "g")
        print("Category   :", final_category)
        # =====================================
        # DISABLED CATEGORIES
        # =====================================
        if (
            final_category == "white_big_circle_heavy"
            or final_category == "black_big_rectangle_heavy"
        ):
            print("Ignored Category")
            data = read_data()
            data["robot_arm_status"] = "Running"
            data["current_object"] = "Waiting..."
            data["weight"] = 0
            write_data(data)
            while get_weight() >= OBJECT_THRESHOLD:
                sleep(0.5)
            continue
        # =====================================
        # PICK OBJECT
        # =====================================
        data = read_data()
        data["robot_arm_status"] = "Picking"
        write_data(data)
        print("Picking Object...")
        pick_object()
        # =====================================
        # SORT OBJECT
        # =====================================
        data = read_data()
        data["robot_arm_status"] = "Sorting"
        write_data(data)
        print("Moving To Bin...")
        drop_category(final_category)
        # =====================================
        # UPDATE COUNTER
        # =====================================
        data = read_data()
        if final_category in data:
            data[final_category] += 1
        write_data(data)
        # =====================================
        # SAVE LOG
        # =====================================
        with open("sorting_logs.txt", "a") as file:
            file.write(
                f"{datetime.now()} | "
                f"{final_category} | "
                f"{round(weight, 2)}g\n"
            )

        # =====================================
        # RETURN HOME
        # =====================================

        data = read_data()
        data["robot_arm_status"] = "Returning Home"
        write_data(data)
        print("Returning Home...")
        arm_home()
        # =====================================
        # READY FOR NEXT OBJECT
        # =====================================

        data = read_data()
        data["robot_arm_status"] = "Running"
        data["current_object"] = "Waiting..."
        data["weight"] = 0
        write_data(data)
        print("Sorting Completed")
        # =====================================
        # WAIT UNTIL PLATFORM EMPTY
        # =====================================

        while True:
            weight = get_weight()
            data = read_data()
            data["weight"] = round(weight, 2)
            write_data(data)
            if weight < OBJECT_THRESHOLD:
                break
            sleep(0.5)
        sleep(1)
except KeyboardInterrupt:
    print("\nStopping...")
finally:
    data = read_data()
    data["system_status"] = "Stopped"
    data["robot_arm_status"] = "Stopped"
    data["current_object"] = "Offline"
    data["weight"] = 0
    write_data(data)
    servo_cleanup()
    camera_cleanup()
    weight_cleanup()
    print("System Shutdown Complete")
