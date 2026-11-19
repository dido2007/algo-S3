
"""Tests pour le midterm blanc CSE202 LogLog.

Run: python3 test_loglog.py
Pour cibler une question : python3 -m unittest test_loglog.TestQ2 -v
"""

import math
import ast
import inspect
import textwrap
import unittest

import loglog


class TestQ1(unittest.TestCase):
    def test_cardinality(self):
        self.assertEqual(loglog.cardinality([]), 0)
        self.assertEqual(loglog.cardinality(['aa', 'ab', 'a', 'aa', 'b', 'ab']), 4)
        self.assertEqual(loglog.cardinality([1, 1, 1, 2, 3, 2]), 3)
        self.assertEqual(loglog.cardinality(list(range(1000))), 1000)


class TestQ2(unittest.TestCase):
    def test_bucket(self):
        for bina, b, expected in [
            ('1100010', 3, 6),
            ('0000010', 3, 0),
            ('1111111', 4, 15),
            ('10101010', 1, 1),
            ('10101010', 7, 85),
        ]:
            with self.subTest(bina=bina, b=b):
                self.assertEqual(loglog.bucket(bina, b), expected)

    def test_zeros(self):
        for bina, b, expected in [
            ('1100010', 3, 2),
            ('1111000', 3, 0),
            ('1000000', 1, 6),
            ('10101010', 7, 1),
            ('0000001', 2, 4),
        ]:
            with self.subTest(bina=bina, b=b):
                self.assertEqual(loglog.zeros(bina, b), expected)


class TestQ3(unittest.TestCase):
    def test_empty_and_singletons(self):
        self.assertEqual(loglog.sketch([], 4), [0] * 16)
        for x in ['a', 'aa', 42]:
            with self.subTest(x=x):
                h = loglog.bin_hash(x)
                i = int(h[:4], 2)
                length = len(h[4:]) - len(h[4:].lstrip('0'))
                expected = [0] * 16
                expected[i] = 1 + length
                self.assertEqual(loglog.sketch([x, x], 4), expected)

    def test_multiple_values(self):
        elements = ['aa', 'ab', 'a', 'aa', 'b', 'a', 'b', 'aa', 'ba', 'ca', 'a', 'ab']
        expected = [0] * 4
        for x in set(elements):
            h = loglog.bin_hash(x)
            i = int(h[:2], 2)
            length = len(h[2:]) - len(h[2:].lstrip('0'))
            expected[i] = max(expected[i], 1 + length)
        self.assertEqual(loglog.sketch(elements, 2), expected)


class TestQ4(unittest.TestCase):
    def test_loglog_formula(self):
        for values, b in [([], 4), (['a'], 4), (list(range(100)), 5), (list(range(800)), 6)]:
            with self.subTest(n=len(values), b=b):
                m = 2**b
                indicators = loglog.sketch(values, b)
                expected = loglog.constant(b) * m**2 / sum(2.0**(-s) for s in indicators)
                self.assertTrue(math.isclose(loglog.loglog(values, b), expected, rel_tol=1e-12))


class TestQ5(unittest.TestCase):
    def test_small_range_correction(self):
        for values, b in [([], 4), (['a'], 4), (list(range(10)), 6), (list(range(100)), 5), (list(range(1000)), 4)]:
            with self.subTest(n=len(values), b=b):
                m = 2**b
                E = loglog.loglog(values, b)
                if E > 5*m/2:
                    expected = E
                else:
                    V = loglog.sketch(values, b).count(0)
                    expected = m * math.log(m/V) if V else E
                self.assertTrue(math.isclose(loglog.loglog_small_range_correction(values, b), expected, rel_tol=1e-12, abs_tol=1e-12))


def not_implemented(function_name):
    """Detect a starter function whose body is still just `pass`."""
    source = textwrap.dedent(inspect.getsource(getattr(loglog, function_name)))
    statements = ast.parse(source).body[0].body
    if statements and isinstance(statements[0], ast.Expr) and isinstance(statements[0].value, ast.Constant):
        statements = statements[1:]  # Ignore the docstring.
    return len(statements) == 1 and isinstance(statements[0], ast.Pass)


DEPENDENCIES = {
    'TestQ1': ['cardinality'],
    'TestQ2': ['bucket', 'zeros'],
    'TestQ3': ['bucket', 'zeros', 'sketch'],
    'TestQ4': ['bucket', 'zeros', 'sketch', 'loglog'],
    'TestQ5': ['bucket', 'zeros', 'sketch', 'loglog', 'loglog_small_range_correction'],
}


def run_exam_tests():
    """One short status per test, without tracebacks or exception dumps."""
    counts = {'OK': 0, 'FAIL': 0, 'NOT IMPLEMENTED': 0}
    for test_class in (TestQ1, TestQ2, TestQ3, TestQ4, TestQ5):
        for name in sorted(n for n in dir(test_class) if n.startswith('test_')):
            label = f'{test_class.__name__}.{name}'
            missing = [fn for fn in DEPENDENCIES[test_class.__name__] if not_implemented(fn)]
            # Q2 tests have separate dependencies.
            if test_class is TestQ2:
                missing = [fn for fn in missing if fn in name]
            if missing:
                status = 'NOT IMPLEMENTED'
                detail = ', '.join(missing)
            else:
                result = unittest.TestResult()
                test_class(name).run(result)
                if result.wasSuccessful():
                    status, detail = 'OK', ''
                else:
                    status = 'FAIL'
                    # A compact reason: one line, never a full Python traceback.
                    errors = result.failures + result.errors
                    first = errors[0][1].strip().splitlines()[-1]
                    detail = first[:180]
            counts[status] += 1
            print(f'{label:<43} {status}' + (f' — {detail}' if detail else ''))
    print(f"\nSummary: {counts['OK']} OK | {counts['FAIL']} FAIL | {counts['NOT IMPLEMENTED']} NOT IMPLEMENTED")


if __name__ == '__main__':
    run_exam_tests()



