README for simple\_rsa
======================
Developed by Johabu <http://johabu.spheniscida.de>; <http://github.com/johabu>
This file is part of simple\_rsa.
simple\_rsa is free software; you can modify it or redistribute it 
under the terms of the GNU General Public License as published by
the Free Software Foundation <http://www.fsf.org>, either version 3,
or (at your option) any later version.
See <http://www.gnu.org/licenses> for the license, if you haven't received a copy of it (GNU\_GPL.txt).
simple\_rsa is distributed without any warranty!

simple\_rsa is a very simple implementation of the basic RSA encryption algorithm

IMPORTANT NOTE
---------------
This program does NOT fulfil any safety standards! It should NOT be used for real
encryption, because it does not provide any safety! This program is only written 
for teaching purposes.

simple\_rsa is distributed without any warranty!

Platforms
----------
simple\_rsa should work on most platforms, but has been tested on Linux amd64 system using gcc

Installing
-----------
To install simple\_rsa, you have to compile it, for instance with GCC:

	gcc -W -Wall -o RSA simple_rsa.c -lm

Using
------
simple\_rsa is able to create a RSA key pair including public and private key.
While key generation important variables of the generation process are displayed.
(See <http://en.wikipedia.org/wiki/RSA_(cryptosystem)> for RSA algorithm)

To start simple\_rsa, just type the following command in a shell

	RSA
