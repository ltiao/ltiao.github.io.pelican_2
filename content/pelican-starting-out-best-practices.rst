Best practices for starting a Pelican site
##########################################

:date: 2010-10-03 10:20
:modified: 2010-10-04 18:40
:tags: thats, awesome
:category: yeah
:slug: my-super-post
:authors: Alexis Metaireau, Conan Doyle
:summary: Short version for index and feeds

#. Create a new git repository at Github: https://github.com/new
  
   * Add Python to ``.gitignore``

#. Clone the newly created repository::

    $ git clone <repo_https_clone_url> <site_root>
#. Create ``virtualenv`` (command only works if you have
   ``virtualenvwrapper``)::

    $ mkvirtualenv <venv_name>
#. Install ``pelican`` (if you're not confident with ``reStructuredText`` 
   yet, then install Markdown as well)::

    $ pip install pelican markdown
#. Navigate to ``<site_root>`` and execute the ``pelican-quickstart``
   script::
     
     $ cd <site_root>
     $ pelican-quickstart
     Welcome to pelican-quickstart v3.5.0.

     This script will help you create a new Pelican-based website.

     Please answer the following questions so this script can generate the files
     needed by Pelican.

        
     > Where do you want to create your new web site? [.] 
     > What will be the title of this web site? Louis Tiao
     > Who will be the author of this web site? Louis Tiao
     > What will be the default language of this web site? [en] 
     > Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) http://ltiao.github.io
     You must answer 'yes' or 'no'
     > Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) Y
     > What is your URL prefix? (see above example; no trailing slash) http://ltiao.github.io
     > Do you want to enable article pagination? (Y/n) Y
     > How many articles per page do you want? [10] 5
     > Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n) Y
     > Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n) Y
     > Do you want to upload your website using FTP? (y/N) N
     > Do you want to upload your website using SSH? (y/N) y
     > What is the hostname of your SSH server? [localhost] cse.unsw.edu.au
     > What is the port of your SSH server? [22] 
     > What is your username on that server? [root] ctia193
     > Where do you want to put your web site on that server? [/var/www] /public_html
     > Do you want to upload your website using Dropbox? (y/N) N
     > Do you want to upload your website using S3? (y/N) N
     > Do you want to upload your website using Rackspace Cloud Files? (y/N) N
     > Do you want to upload your website using GitHub Pages? (y/N) y
     > Is this your personal page (username.github.io)? (y/N) y
     Done. Your new project is available at /Users/tiao/Dropbox/Projects/website

#. ``git checkout -b source``
#. ``git add Makefile develop_server.sh fabfile.py pelicanconf.py publishconf.py``
#. commit these files
#. ``git push origin source``
#. create an article ``<root>/keyboard-review.md``::
    
     Title: My First Review
     Date: 2010-12-03 10:20
     Category: Review 

     Following is a review of my favorite mechanical keyboard.

#. make github
