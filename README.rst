irclogs
=======

Simple IRC logger with a Flask application to store and view logs

Technologies
++++++++++++

We will be using the following technologies

- `Python 3`_
- Flask_, a microframework
- Jinja2_, a template engine
- AngularJS_, a javascript MVC framework

.. _Flask: http://flask.pocoo.org/docs/
.. _Jinja2: http://jinja.pocoo.org/docs/
.. _Python 3: http://docs.python.org/3/
.. _AngularJS: http://angularjs.org/

Getting Started
+++++++++++++++

Here's everything you need to know to get a copy of nycpython.com running
locally.

What You Need
-------------

- Git_
- `A GitHub account`_
- `The code`_

.. _Git: http://git-scm.com/downloads
.. _A GitHub account: https://github.com
.. _The code: https://github.com/NYCPython/nycpython.com

What You Need to Know
---------------------

Once you are familiar with Flask, it is recommended that you also become
familiar with blueprints_ and `application factories`_. For more information
about application factories, please check out `this post`_ by `Matt Wright`_.

.. _application factories: http://flask.pocoo.org/docs/patterns/appfactories/
.. _blueprints: http://flask.pocoo.org/docs/blueprints/
.. _Matt Wright: https://github.com/mattupstate
.. _this post: http://mattupstate.com/python/2013/06/26/how-i-structure-my-flask-applications.html

Setup
-----

For users unable to install VirtualBox or Vagrant you can still get a copy running
locally. `Fork the code on GitHub`_ and clone it locally by executing the following command, 
replacing ``USERNAME`` with your GitHub username::

    $ git clone git@github.com:USERNAME/irclogs.git

After doing that, create a virtual environment ``irclogs`` with Python 3 as your default interpreter
and execute the following command to install all the necessary dependencies for this project::

    $ pip install -r requirements.txt 
    $ python manage.py db upgrade
    $ python manage.py runserver

The site can be accessed in your browser by visiting `localhost:5000`_.

To run the logger bot (from the project root directory)::

    $ python -m irclogs.irclogger -s "irc.freenode.net" -n "NICKNAME" -c "#nycpython" -P "NICKNAME:PASSWORD"

.. _fork the code on GitHub: https://github.com/NYCPython/irclogs/fork
.. _localhost:5000: http://localhost:5000

Contributing
++++++++++++

A list of issues can be found on GitHub_. Issues are categorized according to
specific areas of focus. The can be used to help find issues in which you are
particularly interested.

Pick one and start hacking away!

After you're done, be sure to add your name and GitHub profile to AUTHORS.rst.

.. _GitHub: https://github.com/NYCPython/irclogs/issues
