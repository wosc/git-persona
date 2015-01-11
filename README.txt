===========
git-persona
===========

.. pandoc -f rst -t markdown -o README.md README.txt

.. image:: https://travis-ci.org/wosc/git-persona.png
   :target: https://travis-ci.org/wosc/git-persona

git-persona provides an easy way to configure the git username on a per
repository basis. It is inspired by the mercurial extension `hg-persona`_.

.. _`hg-persona`: https://bitbucket.org/0branch/hg-persona

git-persona requires at least Python 2.7 or Python 3.3.
You can install it from PyPI like this::

    $ pip install ws.gitpersona

You can configure invidual personas in your ``~/.gitconfig`` as follows::

    [persona]
    home = Firstname Lastname <firstname@home.domain>
    work = Firstname Lastname <firstname.lastname@work.domain>

and you'll probably want to set up an alias like this::

    [alias]
    persona = !git-persona

Then you can switch the persona of a repository::

    $ git persona -n home
    $ git persona -n work

And list all known personas::

    $ git persona
