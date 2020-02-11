
{{ cookiecutter.project }}
******

.. image:: https://readthedocs.org/projects/{{ cookiecutter.project }}/badge
   :alt: readthedocs

{{ cookiecutter.description }}

.. image:: https://git.beta.ucr.ac.cr/{{ cookiecutter.author }}/{{ cookiecutter.project }}/raw/master/img/avatar.png
   :alt: avatar

Full documentation on `Readthedocs <https://{{ cookiecutter.project }}.readthedocs.io>`_.

Source code on:

`Github <https://github.com/{{ cookiecutter.author }}/{{ cookiecutter.project }}>`_.

`Gitlab <https://git.beta.ucr.ac.cr/{{ cookiecutter.author }}/{{ cookiecutter.project }}>`_.


Contents
********

* `Description <#Description>`_
* `Usage <#Usage>`_
* `Parameters <#Parameters>`_
   * `help <#help>`_
* `Compatibility <#Compatibility>`_
* `License <#License>`_
* `Links <#Links>`_
* `UML <#UML>`_
   * `Flow <#flow>`_
* `Author <#Author>`_

API Contents
************

* `API <#API>`_
* `Scripts <#scripts>`_
   * `{{ cookiecutter.project }} <#{{ cookiecutter.project }}>`_
      * `Globals <#globals>`_
      * `Functions <#functions>`_

Description
***********

{{ cookiecutter.description }}


Usage
*****

Download the script, give it execution permissions and execute it:

::

   wget https://git.beta.ucr.ac.cr/{{ cookiecutter.author }}/{{ cookiecutter.project }}/raw/master/script.sh
   chmod +x script.sh
   ./script.sh -h

* To run tests:

..

   ::

      cd {{ cookiecutter.project }}
      bats tests

   On some tests you may need to use *sudo* to succeed.


Parameters
**********

The following parameters are supported:


help
====

* *-h* (help): Show help message and exit.

..

   ::

      ./script.sh -h


Compatibility
*************

* `Debian Buster <https://wiki.debian.org/DebianBuster>`_.

* `Debian Raspbian <https://raspbian.org/>`_.

* `Debian Stretch <https://wiki.debian.org/DebianStretch>`_.

* `Ubuntu Bionic <http://releases.ubuntu.com/18.04/>`_.

* `Ubuntu Xenial <http://releases.ubuntu.com/16.04/>`_.


License
*******

GPL 3. See the LICENSE file for more details.


Links
*****

`Github <https://github.com/{{ cookiecutter.author }}/{{ cookiecutter.project }}>`_.

`Gitlab <https://git.beta.ucr.ac.cr/{{ cookiecutter.author }}/{{ cookiecutter.project }}>`_.

`Readthedocs <https://{{ cookiecutter.project }}.readthedocs.io>`_.


UML
***


Flow
====

The program flow is shown below:

.. image:: https://git.beta.ucr.ac.cr/{{ cookiecutter.author }}/{{ cookiecutter.project }}/raw/master/img/flow.png
   :alt: flow


Author
******

.. image:: https://git.beta.ucr.ac.cr/{{ cookiecutter.author }}/{{ cookiecutter.project }}/raw/master/img/author.png
   :alt: author

Comunidad de Software Libre de la Universidad de Costa Rica.


API
***


Scripts
*******


**{{ cookiecutter.project }}**
==========

{{ cookiecutter.description }}


Globals
-------

..

   **UPGRADE**

   ..

      Indicates if upgrade the system or not. Defaults to *false*.


Functions
---------

..

   **get_parameters()**

   ..

      Get bash parameters.

      Accepts:

      ..

         * *h* (help).

      :Parameters:
         **$@** (*str*) – Bash arguments.

      :Returns:
         0 if successful, 1 on failure.

      :Return type:
         int

   **help()**

   ..

      Shows help message.

      :Parameters:
         Function has no arguments.

      :Returns:
         0 if successful, 1 on failure.

      :Return type:
         int

   **main()**

   ..

      {{ cookiecutter.description }}

      :Parameters:
         **$@** (*str*) – Bash arguments string.

      :Returns:
         0 if successful, 1 on failure.

      :Return type:
         int

   **sanitize()**

   ..

      Sanitize input.

      The applied operations are:

      ..

         * Trim.

      :Parameters:
         **$1** (*str*) – Text to sanitize.

      :Returns:
         The sanitized input.

      :Return type:
         str

