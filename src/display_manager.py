import board
import digitalio

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import adafruit_rgb_display.st7735 as st7735

# ================= TFT SETUP =================

cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = digitalio.DigitalInOut(board.D24)

spi = board.SPI()

disp = st7735.ST7735R(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=24000000
)

WIDTH = 128
HEIGHT = 160

try:

    title_font = ImageFont.truetype(
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        12
    )

    label_font = ImageFont.truetype(
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        10
    )

    value_font = ImageFont.truetype(
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        12
    )

except:

    title_font = ImageFont.load_default()
    label_font = ImageFont.load_default()
    value_font = ImageFont.load_default()


def update_display(prediction, confidence, category):

    image = Image.new("RGB", (WIDTH, HEIGHT), "white")
    draw = ImageDraw.Draw(image)

    # ================= TITLE =================

    draw.text(
        (5, 5),
        "Object Detected",
        fill="blue",
        font=title_font
    )

    draw.line(
        (0, 22, WIDTH, 22),
        fill="blue"
    )

    # ================= PREDICTION =================

    draw.text(
        (5, 30),
        "Prediction:",
        fill="black",
        font=label_font
    )

    draw.text(
        (5, 45),
        prediction,
        fill="red",
        font=value_font
    )

    # ================= CONFIDENCE =================

    draw.text(
        (5, 75),
        "Confidence:",
        fill="black",
        font=label_font
    )

    draw.text(
        (5, 90),
        f"{confidence:.1f}%",
        fill="green",
        font=value_font
    )

    # ================= CATEGORY =================

    draw.text(
        (5, 115),
        "Category:",
        fill="black",
        font=label_font
    )

    if category.endswith("_light"):

        cat1 = category.replace("_light", "")
        cat2 = "LIGHT"

    elif category.endswith("_heavy"):

        cat1 = category.replace("_heavy", "")
        cat2 = "HEAVY"

    else:

        cat1 = category
        cat2 = ""

    draw.text(
        (5, 130),
        cat1[:20],
        fill="blue",
        font=label_font
    )

    draw.text(
        (5, 145),
        cat2,
        fill="red",
        font=value_font
    )

    disp.image(image)
