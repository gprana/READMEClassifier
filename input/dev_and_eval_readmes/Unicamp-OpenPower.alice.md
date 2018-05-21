# Alice


Alice is a command-line interface for managing Openstack user accounts. It creates a project, user and network configuration which just one line.  


## Getting Started


This guide assumes that you have a full running Openstack installation on your server. Alice's stable version runs on Openstack Liberty release under Ubuntu 14.04.  

### Prerequisities


Your server must support Keystone v3, Neutron Client v2 authentication methods, and you should also be able to create a new Postqresql or MariaDB table, since it will be needed to store user data. You can use the same database used by Openstack, but if you run more than 2000 simultaneous connections on MariaDB, it might be safer to use a separate database. 


### Create database


Connect to the database server as the `root` user:
    
    $ mysql -u root -p

Create `alice` database:

    CREATE DATABASE alice;
    
Grant access to `alice` database:
    
    GRANT ALL PRIVILEGES ON alice.* TO 'alice'@'localhost' \
      IDENTIFIED BY 'ALICE_DBPASS';
    GRANT ALL PRIVILEGES ON alice.* TO 'alice'@'%' \
      IDENTIFIED BY 'ALICE_DBPASS';

Replacing `ALICE_DBPASS` with a suitable password.

## Install

Clone the repository:

```
$ git clone git@github.com:jwnx/alice.git
```

Go inside the new folder and run the install script

```
$ cd alice && python setup.py install 
```

### Configuration

First, add `DATABASE_URL` variable to your `admin-openrc.sh`.

    DATABASE_URL=mysql://alice:ALICE_DBPASS@controller/alice 

In order create user's network configuration, you'll also need to add your external network ID.

    OS_EXT_NET=<your_ext_network_id>

Inside the `config` file, you'll find the standart network, subnet and quota configurations. You can customize it to fit your cloud needs.

## Usage

Bellow we have a list of a few common usages of alice with explanations:

### Add new user

    $ alice add [OPTIONS] NAME EMAIL
    
**OPTIONS**:
- `--enable/--disable`: Enables or disables user account. This user will not be allowed to login in her/his horizon account.
- `--expire`: Set expiration date
- `--yes`: Disables confirmation

#### Example:

    $ alice add maria maria@email.com --expire "12 jan 2017 --yes" 

### List

    $ alice list [OPTIONS] [FILTER]
    
**OPTIONS**:
- `--hightlight`: Hightlights **[expired]** or **[on hold]** user accounts.

**FILTERS**: `{enabled, disabled, active, hold, expired}`

#### Example: 
     
     $ alice list enabled --highlight

### Modify

    $ alice modify ID [ATTRIBUTES]

Where **ID** can be name, email or db's ID.

**Attributes**: `{name, email, password, project_name, description, enabled, expiration}`

#### Examples: 
     
     $ alice modify amanda@mail.com expiration:'in 30d'
     $ alice modify amanda email:amanda@mail.com
     $ alice modify 1 name:amanda enabled:false

### Show

    $ alice show ID

Where **ID** can be name, email or db's ID.

#### Examples: 
     
     $ alice show maria

### Migrate

    $ alice migrate

Copies user entries from Openstack to Alice database in order to be managable by Alice. Ignores services, admin and duplicates. 

## TODO:

* Implement full deletion method: includes deleting all user Openstack data.
* Integrate mail notification
* Add tests

## License
This project is licensed under the GPL3.0 License.

