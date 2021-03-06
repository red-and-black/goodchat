========
GoodChat
========

GoodChat is an app which makes it easier to meet new people with similar
interests at conferences.

The story
---------

It was the afternoon of the final day of 36C3.

As we sat around enjoying the last hours of the event and watching the crowds
slowly thinning out, we started to reflect on the fact that it's often
difficult to meet new people at conferences.

And we thought "What if we made an app to help people meet new people at
conferences?".

So we found a table in what was left on the Python assembly, sat down, and
started building one.

Setting up a development instance
---------------------------------

These steps are for Debian and Debian derivatives.

They assume that your Python3 version is at least 3.6.

Step 1 - Install build tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can skip this step if you already have these installed.

Install pip::

    $ sudo apt update
    $ sudo apt install python-pip

Install virtualenv and virtualenvwrapper::

    $ pip install --user virtualenv virtualenvwrapper

Add these lines to the end of your ``~/.bashrc`` file::

    export WORKON_HOME="${HOME}/.virtualenvs"
    source ~/.local/bin/virtualenvwrapper.sh

Reload ``~/.bashrc``::

    $ source ~/.bashrc

It's assumed that you have Node installed. Use it to install `sass`::

    $ npm install -g sass

Step 2 - Set up a virtualenv
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set up a virtualenv called ``goodchat``::

    $ mkvirtualenv --python=`which python3` goodchat

Then add these lines to ``~/.virtualenvs/goodchat/bin/postactivate``::

    export GOODCHAT_DATABASE_NAME=goodchat
    export GOODCHAT_DATABASE_PASSWORD=password
    export GOODCHAT_DATABASE_USER=goodchat
    export GOODCHAT_ENVIRONMENT=development
    export GOODCHAT_TIMEZONE=Europe/Prague
    export GOODCHAT_SECRET_KEY=123456789

Then restart the virtualenv to pick up those environment variables::

    $ deactivate
    $ workon goodchat

Step 3 - Clone the repo
~~~~~~~~~~~~~~~~~~~~~~~

Clone the repo::

    $ cd /path/to/your/projects/directory
    $ git clone git@github.com:red-and-black/goodchat.git

Step 4 - Install dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Install the required Python packages in your virtualenv::

    $ cd goodchat
    $ pip install -r requirements.txt

Step 5 - Create the database
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a Postgres database and database user, setting the password for the new
user to ``password`` when prompted::

    $ sudo su postgres
    $ createuser -P goodchat
    $ createdb -O goodchat goodchat
    $ exit

Then initialise the database with::

    $ ./manage.py migrate

Step 6 - Create a superuser
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a superuser with::

    $ ./manage.py createsuperuser

Open a Django shell with::

    $ ./manage.py shell

Give the superuser a profile with these lines::

    >>> from django.contrib.auth.models import User
    >>> from profiles.models import Profile
    >>> user = User.objects.get()
    >>> Profile.objects.create(user=user)

Step 7 - Start the server
~~~~~~~~~~~~~~~~~~~~~~~~~

Start the server with::

    $ ./manage.py runserver

Step 8 - Access the app
~~~~~~~~~~~~~~~~~~~~~~~

Browse to http://localhost:8000.

Rebuilding the css
------------------

The ``css`` is managed by ``sass``.

When any ``.scss`` files are changed, rebuild ``main.css`` with::

    $ sass /path/to/static/scss/main.scss /path/to/static/css/main.css

Generating a usage report
-------------------------

After an event has run, a usage report can be generated with::

    $ ./manage.py usage
