#AUTOGENERATED! DO NOT EDIT! File to edit: dev/00_test.ipynb (unless otherwise specified).

__all__ = ['test_fail', 'test', 'nequals', 'test_eq', 'test_eq_type', 'test_ne', 'is_close', 'test_close', 'test_is',
           'test_shuffled', 'test_stdout', 'TEST_IMAGE', 'test_fig_exists']

#Cell 1
from .imports import *
from .notebook.showdoc import show_doc

#Cell 6
def test_fail(f, msg='', contains=''):
    "Fails with `msg` unless `f()` raises an exception and (optionally) has `contains` in `e.args`"
    try: f()
    except Exception as e:
        assert not contains or contains in str(e)
        return
    assert False,f"Expected exception but none raised. {msg}"

#Cell 8
def test(a, b, cmp,cname=None):
    "`assert` that `cmp(a,b)`; display inputs and `cname or cmp.__name__` if it fails"
    if cname is None: cname=cmp.__name__
    assert cmp(a,b),f"{cname}:\n{a}\n{b}"

#Cell 14
def nequals(a,b):
    "Compares `a` and `b` for `not equals`"
    return not equals(a,b)

#Cell 18
def test_eq(a,b):
    "`test` that `a==b`"
    test(a,b,equals, '==')

#Cell 21
def test_eq_type(a,b):
    "`test` that `a==b` and are same type"
    test_eq(a,b)
    test_eq(type(a),type(b))
    if isinstance(a,(list,tuple)): test_eq(map(type,a),map(type,b))

#Cell 23
def test_ne(a,b):
    "`test` that `a!=b`"
    test(a,b,nequals,'!=')

#Cell 25
def is_close(a,b,eps=1e-5):
    "Is `a` within `eps` of `b`"
    if hasattr(a, '__array__') or hasattr(b,'__array__'):
        return (abs(a-b)<eps).all()
    if isinstance(a, (Iterable,Generator)) or isinstance(b, (Iterable,Generator)):
        return is_close(np.array(a), np.array(b), eps=eps)
    return abs(a-b)<eps

#Cell 26
def test_close(a,b,eps=1e-5):
    "`test` that `a` is within `eps` of `b`"
    test(a,b,partial(is_close,eps=eps),'close')

#Cell 28
def test_is(a,b):
    "`test` that `a is b`"
    test(a,b,operator.is_, 'is')

#Cell 30
def test_shuffled(a,b):
    "`test` that `a` and `b` are shuffled versions of the same set of items"
    test_ne(a, b)
    test_eq(set(a), set(b))

#Cell 32
def test_stdout(f, exp, regex=False):
    "Test that `f` prints `exp` to stdout, optionally checking as `regex`"
    s = io.StringIO()
    with redirect_stdout(s): f()
    if regex: assert re.search(exp, s.getvalue()) is not None
    else: test_eq(s.getvalue(), f'{exp}\n' if len(exp) > 0 else '')

#Cell 34
TEST_IMAGE = 'images/puppy.jpg'

#Cell 36
def test_fig_exists(ax):
    assert ax and len(np.frombuffer(ax.figure.canvas.tostring_argb(), dtype=np.uint8))