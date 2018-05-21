# DESCRIPTION:

Installs Redis. Redis is an open source, advanced key-value store.

It is often referred to as a data structure server since keys can contain strings, hashes, lists, sets and sorted sets.

Details http://redis.io/

[![Build Status](https://travis-ci.org/ctrabold/chef-redis.png?branch=master)](https://travis-ci.org/ctrabold/chef-redis)

# How to add to your cookbook repository #

Consider using our chef-solo bootstrap project (includes a simple deployment script for synching with your remote servers).

More information at: https://github.com/aforward/chef-bootstrap

```
git clone https://github.com/aforward/chef-bootstrap YOUR_REPO_ROOT
cd YOUR_REPO_ROOT
cp ~/.ssh/id_dsa.pub ./bootstrap/root_authorized_keys
bundle install
```

Then, consider using a git submodule so that you can monitor changes in this cookbook separately.

For more info, check out the [Pro Git](http://progit.org/book/ch6-6.html) book.

```
cd YOUR_REPO_ROOT
git submodule add https://github.com/aforward/chef-redis.git chef/cookbooks/redis
```


# REQUIREMENTS:

None (please correct if you encounter issues).

Currently tested on Ubuntu 10.04 and 12.04.

# ATTRIBUTES:

	['redis']['bind']         			# "127.0.0.1"
	['redis']['port']         			# "6379"
	['redis']['config_path']  			# "/etc/redis/redis.conf"
	['redis']['daemonize']    			# "yes"
	['redis']['timeout']      			# "300"
	['redis']['loglevel']     		 	# "notice"
	['redis']['password']     		 	# nil
	['redis']['include_monit']     	# nil

	['redis']['source']['version']          # "2.4.1"
	['redis']['source']['prefix']           # "/usr/local"
	['redis']['source']['tar_url']          # "http://redis.googlecode.com/files/redis-2.4.1.tar.gz"
	['redis']['source']['tar_checksum']     # "38e02..."
	['redis']['source']['create_service']   # true
	['redis']['source']['user']             # "redis"
	['redis']['source']['group']            # "redis"

# USAGE:

* Add cookbook ``redis`` to your runlist. This will install redis on your machine.
* Add cookbook ``redis::source`` to your runlist. This will build redis on your machine from source.
* Add cookbook ``redis::gem`` to your runlist. This will install the redis Rubygem.
* Add cookbook ``redis::remove`` to your runlist if you want to remove redis on your machine.
