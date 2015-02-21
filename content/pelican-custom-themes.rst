==========================
Customizing Pelican Themes
==========================

:date: 2015-01-27 20:00
:tags: pelican, themes
:category: python
:authors: Louis Tiao
:summary: Setting up the Pelican environment for customized themes
:status: draft

I want to design and create most of the templates myself and use 
Bootstrap 3. There seems to be an inexhaustible number of potentially 
useful features that can be supported in a theme, and rather than 
spending all my time coming up features I should support, I will 
simply fork the project `pelican-bootstrap3 from DandyDev`_ 
and basically reinvent it. Essentially, all that will remain the
same are the features it will support.

#. Create a ``themes`` directory::

     $ cd <pelican-site-root>
     $ mkdir themes

#. Fork https://github.com/DandyDev/pelican-bootstrap3 and clone 
   into ``<pelican-site-root>/themes``::

     $ cd themes
     $ git clone https://github.com/ltiao/pelican-bootstrap3

In a previous project, I would add this repository as a submodule
but I now realized there is no compelling reason for doing this.
The theme can actually exist independently of my Pelican project 
files and not be married to this particular project. In fact, I 
didn't even need to create the ``themes`` subdirectory and clone
the repository into it - there are so many ways of incorporating
themes into Pelican, I may as well document it here for posterity.

Intermezzo
==========

#. Provide the theme path to ``pelican`` in the ``-t`` or 
   ``--theme-path`` argument. Path can be relative to ``<pelican-site-root>``.
#. Provide the theme path in the ``THEME`` variable in the settings
   file. Path can be relative to ``<pelican-site-root>``.
#. Install the theme using ``pelican-themes`` by supplying the
   theme path in either the ``-i`` or ``-s`` argument. Again, path
   can be relative to ``<pelican-site-root>``. The former copies 
   the theme while the later creates a symbolic link.

   The theme should now appear the themes list ``pelican-themes -l``
   and you should now be able to use this theme with approach
   1 or 2 by simply supplying the theme name rather than the path.

   Use ``pelican-themes -r`` to remove the theme.

If the theme is under development, then using symlinks with the 3rd 
method is recommended. However, since I have already cloned the repo
as a descendant of ``<pelican-site-root>``, this may be redundant.
Otherwise, if the theme lives outside of the ``<pelican-site-root>``
hierarchy, this is highly recommended. I anticipate that this theme
will be tightly coupled with this particular Pelican project. 
Furthermore, I doubt I will be reusing this theme elsewhere, hence
the reason I have organized it this way.

Continuing on...
================

I almost start all of my projects with HTML5 Boilerplate, pre-configured
with Bootstrap [#]_. Download, unzip it and move ``index.html`` to ``templates/``
and the rest of the files to ``static/``::

  $ unzip initializr-verekia-4.0.zip
  $ mv initializr/index.html <pelican-site-root>/themes/<theme_name>/templates/boilerplate.html
  $ mv initializr/* <pelican-site-root>/themes/<theme_name>/static

Replace everything in the ``body`` tag between::

    <!--[if lt IE 7]>
        <p class="browsehappy">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> to improve your experience.</p>
    <![endif]-->

and::

  <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
  ...

with::
  
  {% block body %}{% endblock %}

Now, create ``base.html``, inherit from ``boilerplate.html`` and begin designing::

  $ cat >> base.html
  {% extends "boilerplate.html" %}
  {% block body %}
  One fine body...
  {% endbody %}

.. _pelican-bootstrap3 from DandyDev: https://github.com/DandyDev/pelican-bootstrap3

.. [#] Go to http://www.initializr.com/ and select `Bootstrap`.
