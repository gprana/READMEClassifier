Simple node server
=============

This is a simple implementation of a node server for who is starting to learn Angular JS and needs API comsumption.

To use this server:

### First install the dependencies

- Run `npm install`. It will create a `node_modules` folder with express, bodyparser and mongoose

### Install Mongodb

If you don't have mongodb installed, you will need it to save data.

To install:

- http://docs.mongodb.org/manual/installation/

Once installed, create a database called `flisol-dogs`, or call it what you want (don't forget to change it on server.js)
Run the server with `mongod` and be sure that the server port and address is the same on server.js

## Create a user

Add a user with bcrypted password. To get a hashed password, run:
```
var bcrypt = require('bcrypt')
bcrypt.hash('teste123', 10, function(err, hash){ console.log(hash) })
```

then at mongo console, run select the db with `use flisol-dogs` and then:
```
db.users.insert({email: 'teste@email.com', password: <hashed_password_here>});
```

### To make the requisitions

You can use Postman, or any other way. I like to test it with HTTParty (ruby gem).
You can make requisitions in this way.

Post: `HTTParty.post('http://localhost:8080/api/contatos', :body => {name: 'Robson', phone: '8888-9999', operator: {name: 'Oi', code: '21', category: 'Celular'}, date: DateTime.now}.to_json, :headers => {'content-type' => 'application/json'})`

Get: `HTTParty.get('http://localhost:8080/api/contatos/557cad4954d5940710000001')`

Put: `HTTParty.put('http://localhost:8080/api/contatos/557cad4954d5940710000001', :body => {name: 'Robson', phone: '8888-9999', operator: {name: 'Claro', code: '15', category: 'Celular'}, date: DateTime.now}.to_json, :headers => {'content-type' => 'application/json'})`

Delete: `HTTParty.delete.('http://localhost:8080/api/contatos/557cad4954d5940710000001')`

### Create new models

Just create new models at /models folder, don't forget to call it on server js like this `var Dog = require('./models/dog');` and don't forget to add the new routes.

Now run it and be happy :)
