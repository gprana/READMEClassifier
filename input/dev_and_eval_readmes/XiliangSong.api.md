ChineseLevel API
================

The ChineseLevel API is a Go server that provides several Chinese-related functions in one convenient RESTful JSON API.


Quickstart
----------

```shell
$ go run main.go --port 7000
```

Endpoints
----------

### /split [GET/POST]

Takes a Chinese string and returns a tokenized array built out of the words in the string.

 - Parameters:
   + text [string]

##### Example:

Request:
```
/split?text=我叫何曼
```

Response:
```
{
    "text": [
        "我",
        "叫",
        "何曼"
    ]
}
```

*******************************************

### /words [GET/POST]

Takes a Chinese string and returns a tokenized array built out of the words in the string (like /split), together with extra information, like each individual word's rank. The returned rank is -1 if the word was not found.

 - Parameters:
   + text [string]

##### Example:

Request:
```
/split?text=我叫何曼
```

Response:
```
{
    "words": [
        {
            "rank": 7,
            "word": "我"
        },
        {
            "rank": 156,
            "word": "叫"
        },
        {
            "rank": -1,
            "word": "何曼"
        }
    ]
}
```

*******************************************

### /rank [GET/POST]

##### Parameters:

 - Parameters:
   + text [string]

##### Example:

*******************************************

### /analyze [GET/POST]

##### Parameters:

 - Parameters:
   + text [string]

##### Example:

Request:
```
GET /analyze?text=她是一位患有先天小兒麻痺症的媽媽，不論刮風下雨她都每天在碼頭用自己殘疾的手腳來給他的兒子掙取學費
```

Response:
```
{
    "hsk": 6,
    "percentile": {
        "80": 19355,
        "90": 121684,
        "95": 138696,
        "99": 253514
    },
    "score": 100
}
```

Installation
------------

The easiest way to get ChineseLevel running is using Docker. But first we need a working installation of Ubuntu 12.04. Start by installing Virtualbox and Vagrant (if you have Ubuntu 12.04 running already, you don't need to install VirtualBox and Vagrant, but you might still want to). Follow these instructions for your OS:

 1. Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
 2. Install [Vagrant](http://www.vagrantup.com/downloads)

With these installed, we can create a new Ubuntu box and install Docker in it:

```
# create a new box in the current directory, and ssh into it:
vagrant box add base http://files.vagrantup.com/precise64.box
vagrant init
vagrant up
vagrant ssh

# install the Docker linux dependencies:
sudo apt-get update
sudo apt-get install linux-image-generic-lts-raring linux-headers-generic-lts-raring
sudo reboot

# ssh back in and install docker:
vagrant ssh
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 36A1D7869245C8950F966E92D8576A8BA88D21E9
sudo sh -c "echo deb http://get.docker.io/ubuntu docker main\
> /etc/apt/sources.list.d/docker.list"
sudo apt-get install lxc-docker

# check that it worked by pulling down the ubuntu image and launching a container:
sudo docker run -i -t ubuntu /bin/bash
```

Great! Hopefully it's all working. Now it's time to install ChineseLevel specific packages. First, pull down the Redis Docker image:

```
sudo docker pull dockerfile/redis
sudo docker run -d -name redis -p 6379:6379 dockerfile/redis
```
