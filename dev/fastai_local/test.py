#AUTOGENERATED! DO NOT EDIT! File to edit: dev/00_test.ipynb (unless otherwise specified).

__all__ = ['test_fail', 'test', 'equals', 'nequals', 'test_eq', 'test_ne', 'test_is']

import numpy as np,operator,torch
from torch import Tensor
from numpy import ndarray,array
from typing import Iterable

def test_fail(f, msg='', contains=''):
    "Fails with `msg` unless `f()` raises an exception and (optionally) has `contains` in `e.args`"
    try:
        f()
        assert False,f"Expected exception but none raised. {msg}"
    except Exception as e: assert not contains or contains in str(e)

def test(a, b, cmp,cname=None):
    "`assert` that `cmp(a,b)`; display inputs and `cname or cmp.__name__` if it fails"
    if cname is None: cname=cmp.__name__
    assert cmp(a,b),f"{cname}:\n{a}\n{b}"

def equals(a,b):
    "Compares `a` and `b` for equality; supports sublists, tensors and arrays too"
    cmp = (torch.equal    if isinstance(a, Tensor  ) else
           np.array_equal if isinstance(a, ndarray ) else
           operator.eq    if isinstance(a, str     ) else
           _all_equal     if isinstance(a, Iterable) else
           operator.eq)
    return cmp(a,b)

def _all_equal(a,b): return len(a)==len(b) and all(equals(a_,b_) for a_,b_ in zip(a,b))

def nequals(a,b):
    "Compares `a` and `b` for `not equals`"
    return not equals(a,b)

def test_eq(a,b):
    "`test` that `a==b`"
    test(a,b,equals, '==')

def test_ne(a,b):
    "`test` that `a!=b`"
    test(a,b,nequals,'!=')

def test_is(a,b):
    "`test` that `a is b`"
    test(a,b,operator.is_, 'is')