"""CSE202 practice midterm, Problem 2 -- Closest pair of points.

Run: python3 test_closest_pair.py
Shows exact failed examples, without Python tracebacks.
"""

import ast
import copy
import inspect
import textwrap

import closest_pair as cp


def missing_function(name):
    source = ast.parse(textwrap.dedent(inspect.getsource(getattr(cp, name))))
    body = source.body[0].body
    if body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant):
        body = body[1:]
    body = [n for n in body if not isinstance(n, ast.Expr)]
    return len(body) == 0 or (len(body) == 1 and isinstance(body[0], ast.Pass))


DEPENDENCIES = {
    'Q1': ['dist2'],
    'Q2': ['dist2', 'closest_pair_naive'],
    'Q3': ['closest_pair_strip'],
    'Q4': ['dist2', 'closest_pair_naive', 'closest_pair_strip', 'closest_pair_rec'],
    'Q5': ['dist2', 'closest_pair_naive', 'closest_pair_strip', 'closest_pair_rec', 'closest_pair'],
}


def as_set(pair):
    return frozenset(pair)


def run_pair_d2(question, fn, n, args, expected_set, expected_d2):
    label = f'{question} test {n:02d} ({fn})'
    missing = [f for f in DEPENDENCIES[question] if missing_function(f)]
    if missing:
        return label, 'NOT IMPLEMENTED', ', '.join(missing)
    try:
        actual = getattr(cp, fn)(*copy.deepcopy(args))
        pair, d2 = actual
        ok = as_set(pair) == frozenset(expected_set) and d2 == expected_d2
        status = 'OK' if ok else 'FAIL'
        reason = '' if ok else (f'input={args!r} | expected=(pair(any order)={expected_set!r}, '
                                 f'd2={expected_d2!r}) | got=(pair={pair!r}, d2={d2!r})')
        return label, status, reason
    except Exception as exc:
        return label, 'FAIL', f'input={args!r} | {type(exc).__name__}: {exc}'


def run_pair_only(question, fn, n, args, expected_set):
    label = f'{question} test {n:02d} ({fn})'
    missing = [f for f in DEPENDENCIES[question] if missing_function(f)]
    if missing:
        return label, 'NOT IMPLEMENTED', ', '.join(missing)
    try:
        pair = getattr(cp, fn)(*copy.deepcopy(args))
        ok = as_set(pair) == frozenset(expected_set)
        status = 'OK' if ok else 'FAIL'
        reason = '' if ok else f'input={args!r} | expected(any order)={expected_set!r} | got={pair!r}'
        return label, status, reason
    except Exception as exc:
        return label, 'FAIL', f'input={args!r} | {type(exc).__name__}: {exc}'


def run_simple(question, fn, n, args, expected):
    label = f'{question} test {n:02d} ({fn})'
    missing = [f for f in DEPENDENCIES[question] if missing_function(f)]
    if missing:
        return label, 'NOT IMPLEMENTED', ', '.join(missing)
    try:
        actual = getattr(cp, fn)(*copy.deepcopy(args))
        status = 'OK' if actual == expected else 'FAIL'
        reason = '' if status == 'OK' else f'input={args!r} | expected={expected!r} | got={actual!r}'
        return label, status, reason
    except Exception as exc:
        return label, 'FAIL', f'input={args!r} | {type(exc).__name__}: {exc}'


PTS = [(1, 7), (4, 2), (6, 9), (8, 1), (10, 5), (13, 8), (15, 2), (17, 6), (3, 13), (11, 12)]
PTS_PX = [(1, 7), (3, 13), (4, 2), (6, 9), (8, 1), (10, 5), (11, 12), (13, 8), (15, 2), (17, 6)]
PTS_PY = [(8, 1), (4, 2), (15, 2), (10, 5), (17, 6), (1, 7), (13, 8), (6, 9), (11, 12), (3, 13)]
PTS_STRIP = [(8, 1), (10, 5), (13, 8), (6, 9), (11, 12)]

PTS2 = [(0, 0), (0, 20), (9, 10), (11, 10), (20, 0), (20, 20)]
PTS2_PX = [(0, 0), (0, 20), (9, 10), (11, 10), (20, 0), (20, 20)]
PTS2_PY = [(0, 0), (20, 0), (9, 10), (11, 10), (0, 20), (20, 20)]
PTS2_PXL = [(0, 0), (0, 20), (9, 10)]
PTS2_PYL = [(0, 0), (9, 10), (0, 20)]
PTS2_STRIP = [(0, 0), (20, 0), (9, 10), (11, 10), (0, 20), (20, 20)]


def main():
    results = []

    # --- Q1: dist2 ----------------------------------------------------
    results.append(run_simple('Q1', 'dist2', 1, ((1, 7), (4, 2)), 34))
    results.append(run_simple('Q1', 'dist2', 2, ((8, 1), (10, 5)), 20))
    results.append(run_simple('Q1', 'dist2', 3, ((0, 0), (3, 4)), 25))
    results.append(run_simple('Q1', 'dist2', 4, ((9, 10), (11, 10)), 4))

    # --- Q2: closest_pair_naive ----------------------------------------
    results.append(run_pair_d2('Q2', 'closest_pair_naive', 1,
                                (PTS,), {(4, 2), (8, 1)}, 17))
    results.append(run_pair_d2('Q2', 'closest_pair_naive', 2,
                                (PTS2,), {(9, 10), (11, 10)}, 4))
    results.append(run_pair_d2('Q2', 'closest_pair_naive', 3,
                                ([(0, 0), (3, 4)],), {(0, 0), (3, 4)}, 25))
    results.append(run_pair_d2('Q2', 'closest_pair_naive', 4,
                                (PTS2_PXL,), {(0, 0), (9, 10)}, 181))

    # --- Q3: closest_pair_strip -----------------------------------------
    # Case A: the strip does NOT improve on the best found elsewhere.
    results.append(run_pair_d2('Q3', 'closest_pair_strip', 1,
                                (PTS_STRIP, ((4, 2), (8, 1)), 17),
                                {(4, 2), (8, 1)}, 17))
    # Case B: the strip DOES contain a closer pair than the current best.
    results.append(run_pair_d2('Q3', 'closest_pair_strip', 2,
                                (PTS2_STRIP, ((0, 0), (9, 10)), 181),
                                {(9, 10), (11, 10)}, 4))

    # --- Q4: closest_pair_rec -------------------------------------------
    results.append(run_pair_d2('Q4', 'closest_pair_rec', 1,
                                (PTS2_PXL, PTS2_PYL), {(0, 0), (9, 10)}, 181))
    results.append(run_pair_d2('Q4', 'closest_pair_rec', 2,
                                (PTS2_PX, PTS2_PY), {(9, 10), (11, 10)}, 4))
    results.append(run_pair_d2('Q4', 'closest_pair_rec', 3,
                                (PTS_PX, PTS_PY), {(4, 2), (8, 1)}, 17))

    # --- Q5: closest_pair -------------------------------------------------
    results.append(run_pair_only('Q5', 'closest_pair', 1,
                                  ([(0, 0), (3, 4)],), {(0, 0), (3, 4)}))
    results.append(run_pair_only('Q5', 'closest_pair', 2, (PTS2,),
                                  {(9, 10), (11, 10)}))
    results.append(run_pair_only('Q5', 'closest_pair', 3, (PTS,),
                                  {(4, 2), (8, 1)}))

    import random
    random.seed(0)
    grid = [(x, y) for x in range(-30, 30) for y in range(-30, 30)]
    i = 0
    while i < 10:
        n = random.randint(2, 18)
        pts = random.sample(grid, n)
        if not unique_minimum(pts):
            continue
        expected_pair, expected_d2 = cp_naive_ref(pts)
        results.append(run_pair_only('Q5', 'closest_pair', 10 + i, (pts,), expected_pair))
        i += 1

    counts = {'OK': 0, 'FAIL': 0, 'NOT IMPLEMENTED': 0}
    for label, status, reason in results:
        counts[status] += 1
        print(f'{label:<34} {status}' + (f' -- {reason}' if reason else ''))
    print(f"\nSummary: {counts['OK']} OK | {counts['FAIL']} FAIL | "
          f"{counts['NOT IMPLEMENTED']} NOT IMPLEMENTED")
    print("\nNote: Q3's written justification (in a comment) is graded by hand,")
    print("it is not checked by this script.")


def unique_minimum(points):
    import itertools
    best2 = None
    count = 0
    for p, q in itertools.combinations(points, 2):
        d = (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
        if best2 is None or d < best2:
            best2, count = d, 1
        elif d == best2:
            count += 1
    return count == 1


def cp_naive_ref(points):
    """Reference brute force used only to build expected values for the
    randomized Q5 tests above (independent of the student's code)."""
    import itertools
    best_pair, best2 = None, None
    for p, q in itertools.combinations(points, 2):
        d = (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
        if best2 is None or d < best2:
            best2, best_pair = d, {p, q}
    return best_pair, best2


if __name__ == '__main__':
    main()
