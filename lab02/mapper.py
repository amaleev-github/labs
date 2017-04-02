#!/usr/bin/env python
import sys

N = 113

for line in sys.stdin:
    line_elements = line.strip().split("\t")
    if len(line_elements) != 3:
        continue
    elements_bad = False
    for element in line_elements:
        if element.strip() == "" or element.strip() == "-":
            elements_bad = True
            continue
    if elements_bad:
        continue
    uid, timestamp, url = line_elements
    if int(uid) % 256 == N:
        print(line.strip())