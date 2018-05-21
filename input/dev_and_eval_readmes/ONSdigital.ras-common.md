# ras-common
Common code for RAS Micro-services based on work originally done as
a part of the code auto-generation project and common components
extracted from pre-existing services.

This code is published on the Python Package Index here;
[https://pypi.python.org/pypi/ons-ras-common](https://pypi.python.org/pypi/ons-ras-common)

#### How to use this code

The easy way is to pip install the package and import the core global
variable into your code. Note that at the time of writing this procedure
should be considered 'alpha' and has only thus far been tested locally.

```bash
$ .. (create config.ini and local.ini, sourced from the repo source)
$virtualenv .build -p python3

Running virtualenv with interpreter .build/bin/python3
Using real prefix '/usr'
Installing setuptools, pkg_resources, pip, wheel...done.
(.build) $ source .build/bin/activate
(.build) $ pip install ons_ras_common
Collecting ons_ras_common
  Downloading ons_ras_common-0.1.1.tar.gz

(.. lots of depency stuff ..)
Successfully built ons-ras-common
Installing collected packages: attrs, six, Automat, certifi, chardet, click, PyYAML, clickclick, jsonschema, inflection, itsdangerous, MarkupSafe, Jinja2, Werkzeug, Flask, typing, swagger-spec-validator, idna, urllib3, requests, connexion, constantly, ecdsa, Flask-Cors, incremental, zope.interface, hyperlink, Twisted, observable, Flask-Twisted, future, psycopg2, pycrypto, python-jose, SQLAlchemy, ons-ras-common
Successfully installed Automat-0.6.0 Flask-0.12.2 Flask-Cors-3.0.2 Flask-Twisted-0.1.2 Jinja2-2.9.6 MarkupSafe-1.0 PyYAML-3.12 SQLAlchemy-1.1.10 Twisted-17.5.0 Werkzeug-0.12.2 attrs-17.2.0 certifi-2017.4.17 chardet-3.0.4 click-6.7 clickclick-1.2.1 connexion-1.1.10 constantly-15.1.0 ecdsa-0.13 future-0.16.0 hyperlink-17.1.1 idna-2.5 incremental-17.5.0 inflection-0.3.1 itsdangerous-0.24 jsonschema-2.6.0 observable-0.3.2 ons-ras-common-0.1.1 psycopg2-2.7.1 pycrypto-2.6.1 python-jose-1.3.2 requests-2.17.3 six-1.10.0 swagger-spec-validator-2.1.0 typing-3.6.1 urllib3-1.21.1 zope.interface-4.4.1

(.build) $ python3
Python 3.5.3 (default, Jan 19 2017, 14:11:04)
[GCC 6.3.0 20170118] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from ons_ras_common import ons_env
>>> ons_env.activate()
2017-06-14 09:14:08+0100 [-] Log opened.
2017-06-14 09:14:08+0100 [-] [log] Logger activated [environment=development]
2017-06-14 09:14:08+0100 [-] [cf] Platform: LOCAL (no CF detected)
2017-06-14 09:14:08+0100 [-] [db] [warning] [swagger_server/models_local/_models.py] file is missing
2017-06-14 09:14:08+0100 [-] [swagger] Swagger API NOT detected
2017-06-14 09:14:08+0100 [-] [crypto] Setting crypto key to "ONS_DUMMY_KEY"
2017-06-14 09:14:08+0100 [-] [reg] Activating service registration
2017-06-14 09:14:08+0100 [-] [reg] ping failed for "http://localhost:8080/api/1.0.0/ping/localhost/59733"
2017-06-14 09:14:08+0100 [-] [reg] ping return = "<urllib3.connection.HTTPConnection object at 0x7fd08c387278>: Failed to establish a new connection: [Errno 111] Connection refused"
2017-06-14 09:14:08+0100 [-] Site starting on 59733
2017-06-14 09:14:08+0100 [-] Starting factory <twisted.web.server.Site object at 0x7fd08c387e80>
2017-06-14 09:14:13+0100 [-] [reg] ping failed for "http://localhost:8080/api/1.0.0/ping/localhost/59733"
2017-06-14 09:14:13+0100 [-] [reg] ping return = "<urllib3.connection.HTTPConnection object at 0x7fd08c11fb70>: Failed to establish a new connection: [Errno 111] Connection refused"
```

More detail to come once it's been full tested ...

