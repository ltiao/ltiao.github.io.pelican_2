Customizing Pelican Themes
##########################

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
   the repository into it.

  .. _pelican-bootstrap3 from DandyDev: https://github.com/DandyDev/pelican-bootstrap3
