=============================================
Synopsis: Upgrading all outdated pip packages
=============================================

:date: 2015-02-05 20:00
:tags: pip, python, synopsis
:authors: Louis Tiao

Simply execute::

  $ pip list --outdated | cut -d' ' -f1 | xargs pip install --upgrade

for versions of ``pip`` that has the ``list`` command, which I believe
is 1.3+.