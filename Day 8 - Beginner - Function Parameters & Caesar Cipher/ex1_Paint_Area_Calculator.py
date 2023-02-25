# Day 8 - Exercise 1 - Paint Area Calculator:
import math

def paint_calc(height, width, cover):
    cans_needed = (height * width)/coverage
    print(f"You'll need {math.ceil(cans_needed)} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
