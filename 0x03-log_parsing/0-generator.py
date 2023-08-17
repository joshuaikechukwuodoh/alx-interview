#!/usr/bin/python3
import sys
import signal

def print_stats(file_size, status_counts):
    print("File size: {:d}".format(file_size))
    for code, count in sorted(status_counts.items()):
        print("{:d}: {:d}".format(code, count))

def main():
    file_size = 0
    status_counts = {}

    try:
        for i, line in enumerate(sys.stdin, start=1):
            parts = line.split()
            if len(parts) != 9:
                continue

            try:
                status_code = int(parts[7])
                size = int(parts[8])
            except (ValueError, IndexError):
                continue

            file_size += size
            status_counts[status_code] = status_counts.get(status_code, 0) + 1

            if i % 10 == 0:
                print_stats(file_size, status_counts)

    except KeyboardInterrupt:
        pass

    print_stats(file_size, status_counts)

if __name__ == "__main__":
    main()
