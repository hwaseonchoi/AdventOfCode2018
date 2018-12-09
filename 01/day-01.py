#!/usr/bin/env python3
def part_one():
    frequency = 0
    with open('input.txt') as file:
        for frequency_change in file:
            frequency += int(frequency_change.strip())
        print(frequency)


def part_two():
    fqs_seen = set([0])
    frequency = 0
    while True:
        with open('input.txt') as file:
            for frequency_change in file:
                frequency += int(frequency_change.strip())
                if (frequency in fqs_seen):
                    print(frequency)
                    return
                fqs_seen.add(frequency)


part_one()
part_two()
