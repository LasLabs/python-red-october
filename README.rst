| |Build Status| | |Coveralls Status| | |Codecov Status| | |Code Climate|

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
------------

Setup
-----

Usage
-----

* `Read The API Documentation <https://laslabs.github.io/python-red-october>`_

Known Issues / Road Map
-----------------------

-  Installation, setup, usage - in ReadMe

.. |Build Status| image:: https://api.travis-ci.org/laslabs/Python-Red-October.svg?branch=master
   :target: https://travis-ci.org/laslabs/Python-Red-October
.. |Coveralls Status| image:: https://coveralls.io/repos/laslabs/Python-Red-October/badge.svg?branch=master
   :target: https://coveralls.io/r/laslabs/Python-Red-October?branch=master
.. |Codecov Status| image:: https://codecov.io/gh/laslabs/Python-Red-October/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/laslabs/Python-Red-October
.. |Code Climate| image:: https://codeclimate.com/github/laslabs/Python-Red-October/badges/gpa.svg
   :target: https://codeclimate.com/github/laslabs/Python-Red-October
