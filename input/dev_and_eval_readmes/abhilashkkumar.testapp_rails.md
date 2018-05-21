Test Rails App
==============

([For this DigitalOcean guide](https://www.digitalocean.com/community/tutorials/deploying-a-rails-app-on-ubuntu-14-04-with-capistrano-nginx-and-puma))

This Rails App has been fully configured with Nginx, Puma and Capistrano. This app isn't meant to be used 
as a starting point for your Application, this is just an example to take help from.


App Details
-----------

This app uses:

 - __Ruby Version:__ `2.2.1`
 - __Rails Version:__ `4.2.0`
 - __Web Server:__ `Puma 2.11.1`
 - __Database:__ `MongoDB`
 - __Database Driver:__ `Mongoid 4.0.2`
 - __Automation Tool:__ `Capistrano 3.4.0`


Test Droplet Details
--------------------

The Droplet where this App was hosted had:

 - __Server IP:__ `178.62.88.94`
 - __SSH Port:__ `7171`
 - __User:__ `deploy`
 - __App Name (For Capistrano):__ `testapp`

In the DB Installation Step, I installed `MongoDB` since this app uses `Mongoid`.


Testing on Your own Droplet
---------------------------

If you'd like to test this app on your own droplet, [fork](https://github.com/sheharyarn/testapp_rails/fork)
this repo and follow the DigitalOcean Guide step-by-step replacing parameters (such as Droplet IP, SSH Port, User, etc.)
with your Repo URL and Droplet's information.


