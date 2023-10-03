#!/usr/bin/env python
""" Log Passing """
from sys import stdin, exit
from signal import signal, SIGINT
total_file_size = 0
codes = {}

line_counts = 0


def help_print():
    """ Helper Function to print """
    print(f"File size: {total_file_size}")
    for code, count in sorted(codes.items()):
        print(f"{code}: {count}")


def handle_signal(signum, frame):
    """ Handle signal """
    help_print()
    # exit(0)


signal(SIGINT, handle_signal)

for line in stdin:
    try:
        line_parts = line.split()

        total_file_size += int(line_parts[-1])
        status = line_parts[-2]

        if status in codes:
            codes[status] += 1
        else:
            codes[status] = 1
        line_counts += 1

        if line_counts % 10 == 0:
            help_print()
    except (ValueError, IndexError):
        continue
