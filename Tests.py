tests = [
    {
        # Example from PDF file
        "title": "Aswar example",
        "frames": [1, 2, 3, 5, 6, 10, 11, 16],
        "expected": {
            "gaps": [[4, 4], [7, 9], [12, 15]],
            "longest_gap": [12, 15],
            "missing_count": 8,
        },
    },
    {
        "title": "Empty list of frames",
        "frames": [],
        "expected": {
            "gaps": [],
            "longest_gap": [],
            "missing_count": 0,
        },
    },
    {
        "title": "Single gap",
        "frames": [1, 2, 3, 5, 6, 7, 8, 9, 10],
        "expected": {
            "gaps": [[4, 4]],
            "longest_gap": [4, 4],
            "missing_count": 1,
        },
    },
    {
        "title": "Multiple gaps with longest in the middle",
        "frames": [1, 2, 5, 6, 11, 12, 13],
        "expected": {
            "gaps": [[3, 4], [7, 10]],
            "longest_gap": [7, 10],
            "missing_count": 6,
        },
    },
    {
        "title": "Full list with no gaps",
        "frames": [1, 2, 3, 4, 5, 6, 7],
        "expected": {
            "gaps": [],
            "longest_gap": [],
            "missing_count": 0,
        },
    },
    {
        "title": "Descending order frames",
        "frames": [10, 8, 6, 4, 2],
        "expected": {
            "gaps": [[1, 1], [3, 3], [5, 5], [7, 7], [9, 9]],
            "longest_gap": [1, 1],
            "missing_count": 5,
        },
    },
    {
        "title": "Single frame received",
        "frames": [5],
        "expected": {
            "gaps": [[1, 4]],
            "longest_gap": [1, 4],
            "missing_count": 4,
        },
    },
    {
        "title": "Missing frames from the beginning",
        "frames": [5, 6, 7, 8],
        "expected": {
            "gaps": [[1, 4]],
            "longest_gap": [1, 4],
            "missing_count": 4,
        },
    },
    {
        "title": "Missing frames at the end",
        "frames": [1, 2, 3, 4, 5],
        "expected": {
            "gaps": [],
            "longest_gap": [],
            "missing_count": 0,
        },
    },
    {
        "title": "Randomly shuffled list with multiple gaps",
        "frames": [11, 2, 1, 8, 10, 5, 4],
        "expected": {
            "gaps": [[3, 3], [6, 7], [9, 9]],
            "longest_gap": [6, 7],
            "missing_count": 4,
        },
    },
    {
        "title": "All frames are missing",
        "frames": [10],
        "expected": {
            "gaps": [[1, 9]],
            "longest_gap": [1, 9],
            "missing_count": 9,
        },
    },
]
