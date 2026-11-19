"""CSE202 mock midterm -- randomized matrix product verification."""
import random


def mat_vec(A, v):
    """Q1: return the matrix-vector product A*v."""
    raise NotImplementedError


def random_vector(n, rng=random):
    """Q2: return n independent uniform random bits."""
    raise NotImplementedError


def check_vector(A, B, C, v):
    """Q3: return whether A*(B*v) equals C*v."""
    raise NotImplementedError


def check_once(A, B, C, rng=random):
    """Q4: check the product with one random binary vector."""
    raise NotImplementedError


def check_repeated(A, B, C, rounds, rng=random):
    """Q5: return False on the first failed check; otherwise return True."""
    raise NotImplementedError

# Q5: Why is the false-acceptance probability at most 2**(-rounds)?
# TODO
