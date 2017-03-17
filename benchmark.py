#!/usr/bin/env python

import os
import sys

cpu_percentage = 0
total_time = 0.0
total_memory = 0

for i in range(0, 10):
    os.system('/usr/bin/time -o output -v gzip -f -k -9 big_building.ppm')

    with open('output') as f:
        content = f.readlines()
        for i, line in enumerate(content):
            if i == 3:
                cpu_percentage += int(line.strip().split()[-1][:-1])
            elif i == 4:
                total_time += float(line.strip().split()[-1][2:])
            elif i == 9:
                total_memory += int(line.strip().split()[-1])

mean_cpu_percentage = cpu_percentage/10
mean_total_time = total_time/10
mean_total_memory = total_memory/10

print("Uso medio de CPU (%%): %.2f" % mean_cpu_percentage)
print("Tempo medio de execucao (s): %.2f" % mean_total_time)
print("Uso medio de memoria (kB): %.2f" % mean_total_memory)
