from dataclasses import dataclass
import Tests
import timeit


@dataclass
class MissingFrames:
    gaps: list[list[int]]
    longest_gap: list[int]
    missing_count: int = 0


def find_missing_ranges(frames: list[int]) -> dict:
    result = MissingFrames([], [])
    if len(frames) == 0:
        return result.__dict__

    frames_map: dict[int, bool] = {}
    for value in range(1, max(frames) + 1):
        frames_map[value] = value in frames

    result.missing_count = len(frames_map) - len(frames)

    gap: list[int] = []
    for value in frames_map:
        if not frames_map[value]:
            gap.append(value)

        if frames_map[value]:
            if len(gap) <= 0:
                continue

            # only care about first and last
            gap = [gap[0], gap[-1]]
            result.gaps.append(gap)

            result.longest_gap = FindLongestGap(gap, result.longest_gap)
            gap = []

    if len(gap) > 0:

        gap = [gap[0], gap[-1]]
        result.longest_gap = FindLongestGap(gap, result.longest_gap)

        result.gaps.append(gap)

    # using __dict__ just because I wanted to use a class
    return result.__dict__


def FindLongestGap(current: list[int], previous: list[int]) -> list[int]:
    if len(previous) == 0:
        return current

    CurrentLength = current[1] - current[0]
    PreviousLength = previous[1] - previous[0]
    if CurrentLength > PreviousLength:
        return current

    return previous


def bench():
    for value in Tests.tests:
        find_missing_ranges(value["frames"])


def test():
    for value in Tests.tests:
        res = find_missing_ranges(value["frames"])
        print(f"test {value["title"]} result:", res == value["expected"])


def main():
    test()
    count = 10000
    time_taken = timeit.timeit(bench, number=count)
    print(f"tests took {time_taken} seconds to finish {count} runs .")


if __name__ == "__main__":
    main()
