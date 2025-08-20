from dataclasses import dataclass
import Tests
import timeit


@dataclass
class MissingFrames:
    gaps: list[list[int]]
    longest_gap: list[int]
    missing_count: int = 0


def find_missing_rangesV2(frames: list[int]) -> dict:
    result = MissingFrames([], [])
    if len(frames) == 0:
        return result.__dict__

    frames_set = set(frames)
    result.missing_count = max(frames_set) - len(frames_set)

    start: int | None = None
    for value in range(1, max(frames_set) + 1):

        if not start and value not in frames_set:
            start = value

        if value in frames_set:
            if not start:
                continue

            result.gaps.append([start, value - 1])
            result.longest_gap = find_longest_gap_V2(
                start, value - 1, result.longest_gap
            )
            start = None

    # using __dict__ just because I wanted to use a class
    return result.__dict__


def find_longest_gap_V2(start: int, end: int, previous: list[int]) -> list[int]:
    if len(previous) == 0:
        return [start, end]

    CurrentLength = end - start
    PreviousLength = previous[1] - previous[0]
    if CurrentLength > PreviousLength:
        return [start, end]

    return previous


def find_missing_rangesV1(frames: list[int]) -> dict:
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

            result.longest_gap = find_longest_gap_V1(gap, result.longest_gap)
            gap = []

    # using __dict__ just because I wanted to use a class
    return result.__dict__


def find_longest_gap_V1(current: list[int], previous: list[int]) -> list[int]:
    if len(previous) == 0:
        return current

    CurrentLength = current[1] - current[0]
    PreviousLength = previous[1] - previous[0]
    if CurrentLength > PreviousLength:
        return current

    return previous


def bench_v1():
    for value in Tests.tests:
        find_missing_rangesV1(value["frames"])


def test_v1():
    for value in Tests.tests:
        res = find_missing_rangesV1(value["frames"])
        print(f"test {value["title"]} result:", res == value["expected"])


def bench_v2():
    for value in Tests.tests:
        find_missing_rangesV2(value["frames"])


def test_v2():
    for value in Tests.tests:
        res = find_missing_rangesV2(value["frames"])
        print(f"test {value["title"]} result:", res == value["expected"])


def main():
    test_v2()
    count = 10000
    time_taken = timeit.timeit(bench_v2, number=count)
    print(f"tests took {time_taken} seconds to finish {count} runs .")


if __name__ == "__main__":
    main()
