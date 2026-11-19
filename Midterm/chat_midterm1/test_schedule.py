
"""Midterm blanc — Weighted Interval Scheduling.

Lancer : python3 test_schedule.py
Affichage court : OK / FAIL / NOT IMPLEMENTED, sans traceback.
"""

import schedule as s


CASES = [
    ("Q1", "compatible", ((1, 3, 5), (3, 8, 1)), True),
    ("Q1", "compatible", ((0, 1, 2), (1, 3, 5)), True),
    ("Q1", "compatible", ((1, 3, 5), (2, 4, 3)), False),
    ("Q1", "compatible", ((1, 3, 5), (1, 3, 5)), False),
    ("Q2", "total_reward", ([],), 0),
    ("Q2", "total_reward", ([(1, 3, 5), (2, 4, 6)],), 11),
    ("Q3", "best_reward_naive", ([],), 0),
    ("Q3", "best_reward_naive", ([(1, 2, 3)],), 3),
    ("Q3", "best_reward_naive", ([(1, 3, 5), (2, 5, 6), (3, 6, 5), (6, 7, 4)],), 14),
    ("Q3", "best_reward_naive", ([(0, 10, 5), (1, 9, 8), (2, 8, 6)],), 8),
    ("Q4", "predecessors", ([],), []),
    ("Q4", "predecessors", ([(1, 3, 5)],), [-1]),
    ("Q4", "predecessors", ([(1, 3, 5), (2, 5, 6), (3, 6, 5), (6, 7, 4)],), [-1, -1, 0, 2]),
    ("Q4", "predecessors", ([(0, 2, 1), (1, 2, 2), (2, 3, 4)],), [-1, -1, 1]),
    ("Q5", "best_reward", ([],), 0),
    ("Q5", "best_reward", ([(1, 2, 3)],), 3),
    ("Q5", "best_reward", ([(6, 7, 4), (3, 6, 5), (2, 5, 6), (1, 3, 5)],), 14),
    ("Q5", "best_reward", ([(0, 2, 1), (1, 2, 2), (2, 3, 4)],), 6),
    ("Q5", "best_reward", ([(0, 10, 5), (1, 9, 8), (2, 8, 6)],), 8),
]


def main():
    import copy

    totals = {"OK": 0, "FAIL": 0, "NOT IMPLEMENTED": 0}

    for number, (question, function_name, arguments, expected) in enumerate(CASES, 1):
        label = f"{question} test {number:02d} ({function_name})"
        values = copy.deepcopy(arguments)
        before = copy.deepcopy(values)

        try:
            actual = getattr(s, function_name)(*values)
            if actual is None:
                status = "NOT IMPLEMENTED"
                detail = ""
            elif actual != expected:
                status = "FAIL"
                detail = f"input={before!r} | expected={expected!r} | got={actual!r}"
            elif question == "Q5" and values != before:
                status = "FAIL"
                detail = f"input modified: before={before!r}, after={values!r}"
            else:
                status = "OK"
                detail = ""
        except NotImplementedError:
            status = "NOT IMPLEMENTED"
            detail = ""
        except Exception as error:
            status = "FAIL"
            detail = f"input={before!r} | {type(error).__name__}: {error}"

        totals[status] += 1
        print(f"{label:<39} {status}" + (f" — {detail}" if detail else ""))

    print(
        f"\nSummary: {totals['OK']} OK | {totals['FAIL']} FAIL | "
        f"{totals['NOT IMPLEMENTED']} NOT IMPLEMENTED"
    )


if __name__ == "__main__":
    main()



