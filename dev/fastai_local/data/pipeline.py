#AUTOGENERATED! DO NOT EDIT! File to edit: dev/02_data_pipeline.ipynb (unless otherwise specified).

__all__ = ['opt_call', 'Transform']

from ..imports import *
from ..test import *
from ..core import *


def opt_call(f, fname='__call__', *args, **kwargs):
    "Call `f.{fname}(*args, **kwargs)`, or `noop` if not defined"
    return getattr(f,fname,noop)(*args, **kwargs)

class Transform():
    "A function that `encodes` if `filt` matches, and optionally `decodes`, with an optional `setup`"
    order,filt = 0,None

    def __init__(self, encodes=None, **kwargs):
        if encodes is not None: self.encodes=encodes
        for k,v in kwargs.items(): setattr(self, k, v)

    @classmethod
    def create(cls, f, filt=None):
        "classmethod: Turn `f` into a `Transform` unless it already is one"
        return f if hasattr(f,'decode') or isinstance(f,Transform) else cls(f)

    def __call__(self, o, filt=None, **kwargs):
        "Call `self.encodes` unless `filt` is passed and it doesn't match `self.filt`"
        if self.filt is not None and self.filt!=filt: return o
        return self.encodes(o, **kwargs)

    def decode(self, o, filt=None, **kwargs):
        "Call `self.decodes` unless `filt` is passed and it doesn't match `self.filt`"
        if self.filt is not None and self.filt!=filt: return o
        return self.decodes(o, **kwargs)

    def __repr__(self): return str(self.encodes) if self.__class__==Transform else str(self.__class__)
    def decodes(self, o, *args, **kwargs): return o