ZeroDivision
============

Python based zeromq proxy helpers

Goal
====

Help offload work in a more dynamic way.

There will be several connection models:

  1. Connect to load pull worker, worker joins master socket for bidirectional access
  2. Connect to load pull worker, worker uses a callback socket to reply via push
  3. Pair based

Why?
====

  - Connect to remote systems running specific versions of software
  - Distribute work away from web frameworks
    - On top of using mongodb.. also incorporate redis and reduction functions in remote calls and simply return the result
  - Allow fast and simple multi-protocol interaction with web frameworks
    - Create an XMPP client that integrates in with web frameworks easily
    - Offload report generation and send report via SMTP and store somewhere

Requirements
============

  - python
  - pyzmq

Recommended
===========

  - inetd

Why inetd?
==========

By creating a stdio socket pyzmq can utilize this socket and helpers can spin up simply by being connected to.

Proxies
=======

- mongodb (pymongo)
- redis (pyredis)
- popen (local or via ssh)