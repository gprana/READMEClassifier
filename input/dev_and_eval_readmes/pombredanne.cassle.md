Advanced Architecture to validate TLS certificates

Introduction
============

The aim of this work is to try validate each TLS-connection with different techniques that exist nowadays. We are living in a world that everything is connected through internet and to provide security on this connections the majority of them use TLS. But we have seen how some governments use different aproach to circumvent them. Some of this vulnerabilities can be due to bugs in the implementations, bad deployments ... etc, but one of the vulnerability that this work try to resolve is the bad or poor validation of certificates.

Before to send our private data to the other entity, usually in TLS, we have to validate the authenticity of the server with the goal to know that it is who claim it is. We have seen how apple failed in this due to the famous goto fail bug  <https://www.imperialviolet.org/2014/02/22/applebug.html>. Although is true that this vulnerability is because of a bad implementation is true that if apple had provided other techniques this situation could be discovered before. Our goal will be to validate each connection with different techniques because maybe an approach says that our connection is secure but perhaps there is another one that says the opposite providing a better solution.

Techniques
==========

A continuation the list of different techniques that the project is using:

* RFC -standard way- to validate it we are using the library NSS
* SSLBlacklist - <https://sslbl.abuse.ch/blacklist/>
* Revoke status - OCSP
* DANE
* ICSI-NOTARY - <http://notary.icsi.berkeley.edu/>
* Certificate-transparency - <http://www.certificate-transparency.org/>
* Pinning


Installation
============


#### Prerequisites



  * Python >= 2.7 (www.python.org)
  * libpcap-python - <http://sourceforge.net/projects/pylibpcap/>

  ```
  $ pip install -r requirements.txt
  ```

-
Once installed all packages and before to launch the program we have to set our root certificates. First we have to configure the directory that hold them.

```bash
$ mkdir -p ~/.pki/nssdb
$ cd ~/.pki/nssdb
$ certutil -N -d .
```
I use this but any directory is fine. If you change the directory you have to change the config file and set `NSS_DB_DIR`. By the default is `"~/.pki/nssdb"`. Also we have to set the variable `CERTS_DIR`in the config file to say where reside our certificates. This project provide the root Mozilla's certificates in the `certs` folder. Also you should set the log directory `LOG_DIR`.

```bash
$ cd {project}
$ cd utils
$ python nssdb.py --add
```

In case that you want to remove it from the database

```bash
$ python nssdb.py --delete
```

-
###### OPTIONAL

To configure for example a pin, to be protected against attacks to Facebook. The information provide may be fake since by now there is no way to extract such information securely.

```bash
$ cd utils
$ python gatherinfo.py -s www.facebook.com -p
[+] PIN
         _id: *.facebook.com
         issuer : DigiCert High Assurance CA-3
                 Base64 of SPKI with sha256: N2E2YWQ4ODI5OGNiYTY1YjE3NmJhM2E3YWIyNWVlOGY5MDYwNDAzM2RhNmE5OGFjMDc5NTlmNTY2ZmEzYWM1NA==
Do you want to include it in the DB (y/n): y
Database updated
```

Once that everything is ready execute.

```bash
$ ./cassle.py -i <interface> -p <port>
```


TODO
====

+ Add DNSSEC support since by now we do not provide DANE verification

+ Verify SCT from CT. There is no way to extract the log's public key

+ We are thinking to write it in golang since is more easy to write concurrent programs thanks to goroutines and channels. We want real time detection. The packages that golang provides offer the majority of all functionality. The application would have less dependencies.

State
=====
#### WIP
The project try to study some techniques that exist nowadays to validate the certificate. Some of them are not mature enough and have some limitations. Try your own methodology and change whatever you think.
