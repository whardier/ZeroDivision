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