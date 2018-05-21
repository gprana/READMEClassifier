![General Assembly Logo](http://i.imgur.com/ke8USTq.png)

# Angular + Token Authentication

## Objectives

By the end of this, students should be able to:

- Authenticate users on an AngularJS front end by consuming tokens delivered from a Rails API
- Use `localStorage` for storing session information (as a JSON string)
- Restrict access to any routes unless users are authorized

## Instructions

- Fork/Clone
- `$ npm install && bower install`
- `$ grunt serve`

The API endpoints look like this:

```sh
 posts GET    /posts(.:format)     posts#index
       POST   /posts(.:format)     posts#create
  post GET    /posts/:id(.:format) posts#show
       PATCH  /posts/:id(.:format) posts#update
       PUT    /posts/:id(.:format) posts#update
       DELETE /posts/:id(.:format) posts#destroy
 users GET    /users(.:format)     users#index
       POST   /users(.:format)     users#create
  user GET    /users/:id(.:format) users#show
       PATCH  /users/:id(.:format) users#update
       PUT    /users/:id(.:format) users#update
       DELETE /users/:id(.:format) users#destroy
 login POST   /login(.:format)     users#login
logout GET    /logout(.:format)    users#logout
```

We've seeded the db with two users:

```ruby
# User 1:
#————————————
username: tyriol
password: myjam

# User 2:
#————————————
username: dsquare
password: myjam
```

To login a user, you must make a post request that looks like this: 
```javascript
$http.post('http://localhost:3000/login', { username: 'tyriol', password: 'myjam' });
```

You will receive a response that looks like this:

```javascript
{"id":5,"username":"tyriol","first_name":"Tyroil","last_name":"Smoochie-Wallace","role":"super_admin","email":"tyriol@kp.com","token":"ca63da06464f4c6f8f33c0ddf254195f","created_at":"2015-03-26T23:37:19.670Z","updated_at":"2015-03-26T23:37:19.670Z"}
```

We will manipulate this object and store it in the browser's localStorage so that we may use this data to authorize the current user. At this point, follow along and we will code this together.

## Bonus (Optional Section)

Implement some of the concepts in this article: [Techniques for authentication in AngularJS applications](https://medium.com/opinionated-angularjs/techniques-for-authentication-in-angularjs-applications-7bbf0346acec).

You might think about displaying some user data on the screen (maybe as a dropdown in the navbar).

## Additional 

Read this article: [Cookies vs Tokens. Getting auth right with Angular.JS](https://auth0.com/blog/2014/01/07/angularjs-authentication-with-cookies-vs-token/)
