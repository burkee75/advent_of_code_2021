# Day 1
# How many measurements are larger than the previous measurement using day1_input?

import os
import itertools

depth_measurement = []

with open("day1_input", mode="r") as fh:
    for line in fh:
        depth_measurement.append(int(line.strip()))

depth_increase_counter = 0

# loop over each index of the list. Range stop 1 below the last, need to subtract one more for the comparison.
for line in range(len(depth_measurement) -1):
    depth_a = depth_measurement[line]
    depth_b = depth_measurement[line + 1]
    if depth_b > depth_a:
        depth_increase_counter += 1

print(depth_increase_counter)
