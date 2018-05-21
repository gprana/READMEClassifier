# tcp-qa

Default template used here requires 20 vCPU and 52Gb host RAM.

Clone the repo
--------------
```
git clone https://github.com/Mirantis/tcp-qa
cd ./tcp-qa
```

Install requirements
--------------------
```
pip install -r ./tcp_tests/requirements.txt
```
* Note: Please read [1] if you don't have fuel-devops installed, because there are required some additional packages and configuration.

Get cloudinit images
--------------------
```
wget https://cloud-images.ubuntu.com/trusty/current/trusty-server-cloudimg-amd64-disk1.img -O ./trusty-server-cloudimg-amd64.qcow2
wget https://cloud-images.ubuntu.com/xenial/current/xenial-server-cloudimg-amd64-disk1.img -O ./xenial-server-cloudimg-amd64.qcow2
```
Export variables
----------------

Required:
```
export IMAGE_PATH1404=./trusty-server-cloudimg-amd64.qcow2
export IMAGE_PATH1604=./xenial-server-cloudimg-amd64.qcow2
```

Optional:
```
export SHUTDOWN_ENV_ON_TEARDOWN=false  # Optional
```

Run deploy test for mk22-lab-dvr
--------------------------------
Note: This lab is not finished yet. TBD: configure vsrx node
```
export ENV_NAME=tcpcloud-mk22-dvr  # You can set any env name
export LAB_CONFIG_NAME=mk22-lab-dvr  # Name of set of templates

LC_ALL=en_US.UTF-8  py.test -vvv -s -k test_tcp_install_default


Run deploy test for mk22-lab-ovs
--------------------------------
Note: This lab is not finished yet. TBD: configure vsrx node
```
export ENV_NAME=tcpcloud-mk22-ovs  # You can set any env name
export LAB_CONFIG_NAME=mk22-lab-ovs  # Name of set of templates

LC_ALL=en_US.UTF-8  py.test -vvv -s -k test_tcp_install_default


Run deploy test for mk22-qa-lab01
---------------------------------
Note: This lab is not finished yet. TBD: configure vsrx node
```
export ENV_NAME=tcpcloud-mk22  # You can set any env name
export LAB_CONFIG_NAME=mk22-qa-lab01  # Name of set of templates
export VSRX_PATH=./vSRX.img           # /path/to/vSRX.img, or to ./xenial-server-cloudimg-amd64.qcow2 as a temporary workaround

LC_ALL=en_US.UTF-8  py.test -vvv -s -k test_tcp_install_default
```
, or as an alternative there is another test that use deploy scripts from models repository written on bash [2]:
```
LC_ALL=en_US.UTF-8  py.test -vvv -s -k test_tcp_install_with_scripts
```

Labs with names mk22-lab-basic and mk22-lab-avdanced are deprecated and not recommended to use.


Create and start the env for manual tests
-----------------------------------------
```
dos.py create-env ./tcp_tests/templates/underlay/mk22-lab-basic.yaml
dos.py start "${ENV_NAME}"
```

Then, wait until cloud-init is finished and port 22 is open (~3-4 minutes), and login with root:r00tme

[1] https://github.com/openstack/fuel-devops/blob/master/doc/source/install.rst

[2] https://github.com/Mirantis/mk-lab-salt-model/tree/dash/scripts
