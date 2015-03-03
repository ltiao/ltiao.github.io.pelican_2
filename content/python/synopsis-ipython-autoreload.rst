========================================
Synopsis: Autoloading modules in IPython
========================================

:date: 2015-03-03 00:30
:tags: python, ipython, synopsis
:authors: Louis Tiao

Simply execute::

	In [1]: %load_ext autoreload
	In [2]: %autoreload 2

and modules will be auto-reloaded by default.

References:

- http://ipython.org/ipython-doc/dev/config/extensions/autoreload.html#module-IPython.extensions.autoreload