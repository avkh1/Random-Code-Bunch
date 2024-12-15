# A TEST SET FOR
# A SIMPLE IMAGE PROCESSOR WITH GLITCHER version 1
# BY ANDREI AVKHIMOVICH
# AS FINAL PROJECT FOR CS50 Introduction to Programming with Python
# 15.12.2024

import pytest
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps, ImageChops
from project import thermal, dirty_print, twotone, scan_lines

test_image = Image.new("RGB", (10, 10), "blue")  # blue image

def test_thermal():
    img = test_image
    result = thermal(img)
    
    # get the color of the first pixel
    pixels = result.load()
    r, g, b = pixels[0, 0]
    
    # check that the channels have been adjusted
    assert r == 50   # red should be 50        - original 0 + 50
    assert g == 100  # green should be 100     - original 0 + 100
    assert b == 255  # blue should remain 255  - no change
    
 
def test_dirty_print():
    img = test_image
    img = dirty_print(img)  # apply the effect

    # check that the pixels are either 0 or 255
    # the fx should create black and white patterns
    pixels = img.load()
    for i in range(img.width):
        for j in range(img.height):
            pixel_value = pixels[i, j]
            assert pixel_value == 0 or pixel_value == 255
            
            
def test_twotone():
    img = test_image
    img = twotone(img)

    # check that all pixels are either 50 or 200
    pixels = img.load()
    for i in range(img.width):
        for j in range(img.height):
            pixel_value = pixels[i, j]
            assert pixel_value == 50 or pixel_value == 200


@pytest.fixture
def fake_interval_slider():
    class Slider:
        def get(self):
            return 2  # always 2 for line_interval
    
    class Line_Interval:
        def __init__(self):
            self.sliders = {
                "Line Interval": Slider()
            }
    return Line_Interval()  # return the object


def test_scan_lines(fake_interval_slider):
    img = Image.new("RGB", (10, 10), (255, 255, 255))  # black image
    
    result_img = scan_lines(fake_interval_slider, img)

    pixels = result_img.load()  # check the first line

    for y in range(0, result_img.height, 4):  # even numbered pixels is _black_?
        for x in range(result_img.width):
            assert pixels[x, y] == (0, 0, 0)  

    for y in range(1, result_img.height, 2):  # NON EVEN numbered is _white_?
        for x in range(result_img.width):
            assert pixels[x, y] == (255, 255, 255)  