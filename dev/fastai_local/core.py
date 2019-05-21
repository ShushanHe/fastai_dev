#AUTOGENERATED! DO NOT EDIT! File to edit: dev/01_core.ipynb (unless otherwise specified).

__all__ = ['chk', 'ifnone', 'noop', 'noops', 'range_of', 'is_listy', 'is_iter', 'listify', 'tuplify', 'tensor',
           'compose', 'mask2idxs', 'uniqueify', 'setify']

from .test import *
from .imports import *


def chk(f): return typechecked(always=True)(f)

Tensor.ndim = property(lambda x: x.dim())

def ifnone(a, b):
    "`b` if `a` is None else `a`"
    return b if a is None else a

def noop (x, *args, **kwargs):
    "Do nothing"
    return x

def noops(self, x, *args, **kwargs):
    "Do nothing (method)"
    return x

def range_of(x):
    "All indices of collection `x` (i.e. `list(range(len(x)))`)"
    return list(range(len(x)))

def is_listy(x):
    "`isinstance(x, (tuple,list))`"
    return isinstance(x, (tuple,list))

def is_iter(o):
    "Test whether `o` can be used in a `for` loop"
    #Rank 0 tensors in PyTorch are not really iterable
    return isinstance(o, (Iterable,Generator)) and getattr(o,'ndim',1)

def listify(o):
    "Make `o` a list."
    if o is None: return []
    if isinstance(o, list): return o
    if isinstance(o, (str,np.ndarray,Tensor)): return [o]
    if is_iter(o): return list(o)
    return [o]

def tuplify(o):
    "Make `o` a tuple"
    return tuple(listify(o))

def tensor(x, *rest):
    "Like `torch.as_tensor`, but handle lists too, and can pass multiple vector elements directly."
    if len(rest): x = tuplify(x)+rest
    # Pytorch bug in dataloader using num_workers>0
    if is_listy(x) and len(x)==0: return tensor(0)
    res = torch.tensor(x) if is_listy(x) else as_tensor(x)
    if res.dtype is torch.int32:
        warn('Tensor is int32: upgrading to int64; for better performance use int64 input')
        return res.long()
    return res

@chk
def compose(*funcs: Callable):
    "Create a function that composes all functions in `funcs`, passing along remaining `*args` and `**kwargs` to all"
    def _inner(x, *args, **kwargs):
        for f in listify(funcs): x = f(x, *args, **kwargs)
        return x
    return _inner

def mask2idxs(mask):
    "Convert bool mask list to index list"
    return [i for i,m in enumerate(mask) if m]

def uniqueify(x, sort=False, bidir=False, start=None):
    "Return the unique elements in `x`, optionally `sort`-ed, optionally return the reverse correspondance."
    res = list(OrderedDict.fromkeys(x).keys())
    if start is not None: res = listify(start)+res
    if sort: res.sort()
    if bidir: return res, {v:k for k,v in enumerate(res)}
    return res

def setify(o): return o if isinstance(o,set) else set(listify(o))