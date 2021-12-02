# Day 1
# How many measurements are larger than the previous measurement using day1_input?

import os
import itertools

depth_measurement = []

with open("day1_input", mode="r") as fh:
    for line in fh:
        depth_measurement.append(int(line.strip()))

# print(depth_measurement)

# compare lines and add to total count
depth_increase_counter = 0

for a, b in zip(depth_measurement, depth_measurement[1:]):
    if b > a:
        depth_increase_counter += 1

print(depth_increase_counter)