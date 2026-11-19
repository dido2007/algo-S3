"""CSE202 Skyline — short, exam-style test output.

Run: python3 test_skyline.py
Shows exact failed examples, without Python tracebacks.
"""

import ast
import inspect
import textwrap

import skyline


RECTS1 = [(1, 11, 5), (2, 6, 7), (3, 13, 9), (12, 7, 16),
          (14, 3, 25), (19, 18, 22), (23, 13, 29), (24, 4, 28)]
SKY1 = [(1, 11), (3, 13), (9, 0), (12, 7), (16, 3),
        (19, 18), (22, 3), (23, 13), (29, 0)]
S3 = [(1, 11), (5, 6), (7, 0), (12, 7), (16, 0), (19, 18), (22, 0), (24, 4), (28, 0)]
S4 = [(3, 13), (9, 0), (14, 3), (23, 13), (29, 0)]
S5 = [(1, 10), (3, 5), (8, 0)]
S6 = [(1, 20), (3, 2), (10, 0)]


def missing_function(name):
    source = ast.parse(textwrap.dedent(inspect.getsource(getattr(skyline, name))))
    body = source.body[0].body
    if body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant):
        body = body[1:]
    return len(body) == 1 and isinstance(body[0], ast.Pass)


CASES = [
    ('Q1', 'rects_height_at', ([], 4), 0),
    ('Q1', 'rects_height_at', ([(1, 4, 5)], 1), 4),
    ('Q1', 'rects_height_at', ([(1, 4, 5)], 5), 0),
    ('Q1', 'rects_height_at', ([(1, 4, 5), (2, 8, 6)], 3), 8),
    ('Q1', 'rects_height_at', (RECTS1, 22), 3),
    ('Q2', 'simplify_skyline', ([],), []),
    ('Q2', 'simplify_skyline', ([(1, 3), (2, 3), (5, 2), (6, 2), (7, 0)],), [(1, 3), (5, 2), (7, 0)]),
    ('Q2', 'simplify_skyline', ([(1, 4), (3, 0), (5, 0), (6, 2), (8, 0)],), [(1, 4), (3, 0), (6, 2), (8, 0)]),
    ('Q3', 'skyline_naive', ([(1, 4, 5)],), [(1, 4), (5, 0)]),
    ('Q3', 'skyline_naive', ([(1, 4, 5), (2, 8, 6)],), [(1, 4), (2, 8), (6, 0)]),
    ('Q3', 'skyline_naive', ([(1, 3, 2), (4, 5, 7)],), [(1, 3), (2, 0), (4, 5), (7, 0)]),
    ('Q3', 'skyline_naive', (RECTS1,), SKY1),
    ('Q4', 'merge_skylines', ([(1, 4), (5, 0)], [(2, 8), (6, 0)]), [(1, 4), (2, 8), (6, 0)]),
    ('Q4', 'merge_skylines', (S3, S4), SKY1),
    ('Q4', 'merge_skylines', (S5, S6), [(1, 20), (3, 5), (8, 2), (10, 0)]),
    ('Q4', 'merge_skylines', ([(1, 3), (5, 0)], [(5, 4), (7, 0)]), [(1, 3), (5, 4), (7, 0)]),
    ('Q4', 'merge_skylines', ([(1, 3), (5, 0)], []), [(1, 3), (5, 0)]),
    ('Q5', 'skyline_dac', ([(1, 4, 5)],), [(1, 4), (5, 0)]),
    ('Q5', 'skyline_dac', ([(1, 3, 2), (4, 5, 7)],), [(1, 3), (2, 0), (4, 5), (7, 0)]),
    ('Q5', 'skyline_dac', (RECTS1,), SKY1),
]

DEPENDENCIES = {
    'Q1': ['rects_height_at'],
    'Q2': ['simplify_skyline'],
    'Q3': ['rects_height_at', 'simplify_skyline', 'skyline_naive'],
    'Q4': ['simplify_skyline', 'merge_skylines'],
    'Q5': ['simplify_skyline', 'merge_skylines', 'skyline_dac'],
}


def main():
    counts = {'OK': 0, 'FAIL': 0, 'NOT IMPLEMENTED': 0}
    for n, (question, fn, args, expected) in enumerate(CASES, 1):
        label = f'{question} test {n:02d} ({fn})'
        missing = [f for f in DEPENDENCIES[question] if missing_function(f)]
        if missing:
            status, reason = 'NOT IMPLEMENTED', ', '.join(missing)
        else:
            try:
                # Use copies: some implementations consume/mutate lists during merging.
                import copy
                actual = getattr(skyline, fn)(*copy.deepcopy(args))
                status = 'OK' if actual == expected else 'FAIL'
                reason = '' if status == 'OK' else f'input={args!r} | expected={expected!r} | got={actual!r}'
            except Exception as exc:
                status, reason = 'FAIL', f'input={args!r} | {type(exc).__name__}: {exc}'
        counts[status] += 1
        print(f'{label:<39} {status}' + (f' — {reason}' if reason else ''))
    print(f"\nSummary: {counts['OK']} OK | {counts['FAIL']} FAIL | {counts['NOT IMPLEMENTED']} NOT IMPLEMENTED")


if __name__ == '__main__':
    main()
