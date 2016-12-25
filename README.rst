|License MIT| | |Build Status| | |Coveralls Status| | |Codecov Status| | |Code Climate|

==========================
Python Red October Library
==========================

This library allows you to interact with a remote Red October Instance using Python.

Red October is a cryptographically-secure implementation of the two-person rule to
protect sensitive data. From a technical perspective, Red October is a software-based
encryption and decryption server. The server can be used to encrypt a payload in such
a way that no one individual can decrypt it. The encryption of the payload is
cryptographically tied to the credentials of the authorized users.

Authorized persons can delegate their credentials to the server for a period of time.
The server can decrypt any previously-encrypted payloads as long as the appropriate number
of people have delegated their credentials to the server.

This architecture allows Red October to act as a convenient decryption service. Other
systems, including CloudFlare’s build system, can use it for decryption and users can
delegate their credentials to the server via a simple web interface. All communication
with Red October is encrypted with TLS, ensuring that passwords are not sent in the clear.

* `Read more on the CloudFlare blog
  <https://blog.cloudflare.com/red-october-cloudflares-open-source-implementation-of-the-two-man-rule/>`_.
* `View the Red October source
  <https://github.com/cloudflare/redoctober>`_.

Installation
============

* Install Python requirements ``pip install -r ./requirements``

Setup
=====

A pre-existing Red October server is required to use this library.

Usage
=====

* `Read The API Documentation <https://laslabs.github.io/python-red-october>`_

Connect to Red October
----------------------

Connect to a Red October instance ``https://172.17.0.2:8080`` as ``Admin`` with the password ``password``:

.. code-block:: python

    from red_october import RedOctober
    ro = RedOctober('172.17.0.2', 8080, 'Admin', 'password')

Turn off certificate verification:

.. code-block:: python

    from red_october import RedOctober
    ro = RedOctober('172.17.0.2', 8080, 'Admin', 'password', verify=False)

Create a Vault
--------------

This will create a vault using the currently logged in credentials as the first admin:

.. code-block:: python

    ro.create_vault()

Create a User
-------------

If you would like to create a user for the currently logged in session:

.. code-block:: python

    ro.create_user('rsa')

If you are currently playing the role of an administrator, you can also create a user for someone else:

.. code-block:: python

   ro.create_user('ecc', name="Ashley", password="@shl3y!")

Delegate Decryption Rights
--------------------------

In order to decrypt a piece of data, the Vault will need to be delegated decryption rights
by document owners.

In order to delegate rights to a Vault, and subsequently grant access to your data:

.. code-block:: python

    from datetime import timedelta
    delegate_time = timedelta(days=1)
    delegate_uses = 20
    ro.delegate(delegate_time, delegate_uses)

The above delegation will expire in 1 day or 20 uses, whichever comes first.

Encrypt Some Data
-----------------

To encrypt some data so that only you can decrypt it:

.. code-block:: python

    data = 'Super Secret Stuff!'
    encrypted = ro.encrypt(data)

To encrypt some data with multiple owners, also setting a minimum amount of delegations
that are required for decryption:

.. code-block:: python

    owners = ['Admin', 'Ashley', 'Bob', 'Jenna']
    minimum_delegations = 2
    data = 'Super Secret Stuff!'
    encrypted = ro.encrypt(data, owners, minimum_delegations)

To encrypt data as another user:

.. code-block:: python

    data = 'Super Secret Stuff!'
    encrypted_string = ro.encrypt(data, name='Todd', password='Todd Pass')

Decrypt Some Data
-----------------

Decryption will use the current session credentials by default:

.. code-block:: python

    decrypted_string = ro.decrypt(encrypted_string)

To decrypt as another user:

.. code-block:: python
    
    decrypted_string = ro.decrypt(encrypted_string, name='Todd', password='Todd Pass')

Known Issues / Road Map
=======================

-  Installation, setup, usage - in ReadMe

Credits
=======

Images
------

* LasLabs: `Icon <https://repo.laslabs.com/projects/TEM/repos/odoo-module_template/browse/module_name/static/description/icon.svg?raw>`_.

Contributors
------------

* Dave Lasley <dave@laslabs.com>

Maintainer
----------

.. image:: https://laslabs.com/logo.png
   :alt: LasLabs Inc.
   :target: https://laslabs.com

This module is maintained by LasLabs Inc.

.. |Build Status| image:: https://api.travis-ci.org/LasLabs/python-red-october.svg?branch=master
   :target: https://travis-ci.org/LasLabs/python-red-october
.. |Coveralls Status| image:: https://coveralls.io/repos/LasLabs/python-red-october/badge.svg?branch=master
   :target: https://coveralls.io/r/LasLabs/python-red-october?branch=master
.. |Codecov Status| image:: https://codecov.io/gh/laslabs/python-red-october/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/LasLabs/python-red-october
.. |Code Climate| image:: https://codeclimate.com/github/laslabs/Python-Red-October/badges/gpa.svg
   :target: https://codeclimate.com/github/laslabs/Python-Red-October
.. |License MIT| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://opensource.org/licenses/MIT
   :alt: License: AGPL-3
