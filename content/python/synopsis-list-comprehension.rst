===================================================
Synopsis: List Comprehension vs. Built-in Functions
===================================================

:date: 2015-03-03 00:30
:tags: python, synopsis
:authors: Louis Tiao
:status: draft

``map(fn, iterable)`` = ``[fn[x] for x in iterable]``

``filter(pred, iterable)`` = ``[x for x in iterable if pred(x)]``

``map(lambda x: x if cond(x) else 0, iterable)`` = ``[x if cond(x) else 0 for x in iterable]``

