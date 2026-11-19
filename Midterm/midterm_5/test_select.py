"""CSE202 practice midterm -- Randomized selection.

Run: python3 test_select.py
Shows exact failed examples, without Python tracebacks.
"""

import ast
import copy
import inspect
import textwrap

import select as sel


def missing_function(name):
    source = ast.parse(textwrap.dedent(inspect.getsource(getattr(sel, name))))
    body = source.body[0].body
    if body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant):
        body = body[1:]
    body = [n for n in body if not isinstance(n, ast.Expr)]  # ignore stray comments-as-exprs
    return len(body) == 0 or (len(body) == 1 and isinstance(body[0], ast.Pass))


DEPENDENCIES = {
    'Q1': ['partition_at'],
    'Q2': ['select_sort_naive'],
    'Q3': ['partition_at', 'select_fixed_pivot'],
    'Q4': ['partition_at', 'randomized_select'],
    'Q5': ['partition_at', 'randomized_select', 'k_smallest_set'],
}


def run_q1(n, L, p, r, pivot_index, expected_list, expected_index):
    label = f'Q1 test {n:02d} (partition_at)'
    missing = [f for f in DEPENDENCIES['Q1'] if missing_function(f)]
    if missing:
        return label, 'NOT IMPLEMENTED', ', '.join(missing)
    Lc = copy.deepcopy(L)
    try:
        q = sel.partition_at(Lc, p, r, pivot_index)
        if Lc == expected_list and q == expected_index:
            return label, 'OK', ''
        reason = (f'input={L!r}, p={p}, r={r}, pivot_index={pivot_index} | '
                   f'expected=(L={expected_list!r}, q={expected_index!r}) | '
                   f'got=(L={Lc!r}, q={q!r})')
        return label, 'FAIL', reason
    except Exception as exc:
        return label, 'FAIL', f'input={L!r} | {type(exc).__name__}: {exc}'


def run_simple(question, fn, n, args, expected):
    label = f'{question} test {n:02d} ({fn})'
    missing = [f for f in DEPENDENCIES[question] if missing_function(f)]
    if missing:
        return label, 'NOT IMPLEMENTED', ', '.join(missing)
    try:
        actual = getattr(sel, fn)(*copy.deepcopy(args))
        status = 'OK' if actual == expected else 'FAIL'
        reason = '' if status == 'OK' else f'input={args!r} | expected={expected!r} | got={actual!r}'
        return label, status, reason
    except Exception as exc:
        return label, 'FAIL', f'input={args!r} | {type(exc).__name__}: {exc}'


def run_set_valued(question, fn, n, args, expected_set):
    label = f'{question} test {n:02d} ({fn})'
    missing = [f for f in DEPENDENCIES[question] if missing_function(f)]
    if missing:
        return label, 'NOT IMPLEMENTED', ', '.join(missing)
    try:
        actual = getattr(sel, fn)(*copy.deepcopy(args))
        ok = isinstance(actual, list) and sorted(actual) == sorted(expected_set)
        status = 'OK' if ok else 'FAIL'
        reason = '' if status == 'OK' else f'input={args!r} | expected(any order)={expected_set!r} | got={actual!r}'
        return label, status, reason
    except Exception as exc:
        return label, 'FAIL', f'input={args!r} | {type(exc).__name__}: {exc}'


def main():
    results = []

    # --- Q1: partition_at -------------------------------------------------
    results.append(run_q1(1, [8, 3, 10, 2, 9, 7, 1], 0, 6, 4,
                           [8, 3, 2, 1, 7, 9, 10], 5))
    results.append(run_q1(2, [5], 0, 0, 0, [5], 0))
    results.append(run_q1(3, [4, 2], 0, 1, 0, [2, 4], 1))
    results.append(run_q1(4, [4, 2], 0, 1, 1, [2, 4], 0))
    results.append(run_q1(5, [6, 1, 8, 3, 2, 9, 4], 0, 6, 0,
                           [4, 1, 3, 2, 6, 9, 8], 4))
    results.append(run_q1(6, [6, 1, 8, 3, 2, 9, 4], 1, 5, 2,
                           [6, 1, 3, 2, 8, 9, 4], 4))

    # --- Q2: select_sort_naive --------------------------------------------
    results.append(run_simple('Q2', 'select_sort_naive', 1, ([5], 1), 5))
    results.append(run_simple('Q2', 'select_sort_naive', 2,
                               ([2, 2.5, -3, 9], 2), 2))
    results.append(run_simple('Q2', 'select_sort_naive', 3,
                               ([8, 3, 10, 2, 9, 7, 1], 1), 1))
    results.append(run_simple('Q2', 'select_sort_naive', 4,
                               ([8, 3, 10, 2, 9, 7, 1], 7), 10))
    results.append(run_simple('Q2', 'select_sort_naive', 5,
                               ([8, 3, 10, 2, 9, 7, 1], 3), 3))

    # --- Q3: select_fixed_pivot --------------------------------------------
    SEVEN = [8, 3, 10, 2, 9, 7, 1]
    for k, expected in enumerate([1, 2, 3, 7, 8, 9, 10], start=1):
        results.append(run_simple('Q3', 'select_fixed_pivot', k,
                                   (list(SEVEN), 0, 6, k), expected))

    OTHER = [6, 1, 8, 3, 2, 9, 4]
    for k, expected in [(1, 1), (4, 4), (7, 9)]:
        results.append(run_simple('Q3', 'select_fixed_pivot', 10 + k,
                                   (list(OTHER), 0, 6, k), expected))

    # --- Q4: randomized_select ----------------------------------------
    for k, expected in enumerate([1, 2, 3, 7, 8, 9, 10], start=1):
        results.append(run_simple('Q4', 'randomized_select', k,
                                   (list(SEVEN), k), expected))
    for k, expected in [(1, 1), (4, 4), (7, 9)]:
        results.append(run_simple('Q4', 'randomized_select', 10 + k,
                                   (list(OTHER), k), expected))
    import random as _random
    _random.seed(0)
    for i in range(20):
        n = _random.randint(1, 25)
        L = _random.sample(range(-500, 500), n)
        k = _random.randint(1, n)
        expected = sorted(L)[k - 1]
        results.append(run_simple('Q4', 'randomized_select', 100 + i,
                                   (list(L), k), expected))

    # --- Q5: k_smallest_set -------------------------------------------
    EIGHT = [15, 3, 42, 7, 9, 1, 23, 8]
    for k in [1, 3, 5, 8]:
        expected_set = sorted(EIGHT)[:k]
        results.append(run_set_valued('Q5', 'k_smallest_set', k,
                                       (list(EIGHT), k), expected_set))

    counts = {'OK': 0, 'FAIL': 0, 'NOT IMPLEMENTED': 0}
    for label, status, reason in results:
        counts[status] += 1
        print(f'{label:<34} {status}' + (f' -- {reason}' if reason else ''))
    print(f"\nSummary: {counts['OK']} OK | {counts['FAIL']} FAIL | "
          f"{counts['NOT IMPLEMENTED']} NOT IMPLEMENTED")
    print("\nNote: Q3/Q4's written justifications (in comments) are graded by hand,")
    print("they are not checked by this script.")


if __name__ == '__main__':
    main()
