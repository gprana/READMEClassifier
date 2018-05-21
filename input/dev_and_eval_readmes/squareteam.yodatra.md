Yodatra 
===
[![Build Status](https://travis-ci.org/squareteam/yodatra.png?branch=master)](https://travis-ci.org/squareteam/yodatra) [![Coverage Status](https://coveralls.io/repos/squareteam/yodatra/badge.png)](https://coveralls.io/r/squareteam/yodatra) [![Gem Version](https://badge.fury.io/rb/yodatra.png)](http://badge.fury.io/rb/yodatra) [![Code Climate](https://codeclimate.com/github/squareteam/yodatra.png)](https://codeclimate.com/github/squareteam/yodatra) [![Dependency Status](https://gemnasium.com/squareteam/yodatra.png)](https://gemnasium.com/squareteam/yodatra)

Backend development you shall do. And yodatra you shall use.

A minimalistic framework built on top of Sinatra it is.

The power of __ActiveRecord__ it gives you and the simplicity of a __Sinatra__ app. And all sort of small helpers.

## Instantly deploy your API

Based on your ActiveRecord models an API will be exposed very simply.
For every resource you want to expose, you will need to create a controller that inherits from the ```Yodatra::ModelsController```.

For example, given a `User` model
```ruby
class User < ActiveRecord::Base
# Your model definition
end
```

Creating a controller as simple as
```ruby
class UsersController < Yodatra::ModelsController
  # limit read_scope
  def read_scope
    { only: [:id, :name] }
  end

  # whitelist assignable attributes
  def user_params
    params.permit(:name)
  end
end
```
will expose all these routes:

```
GET /users
```

> retrieves all users _(attributes exposed are limited by the `read_scope` method defined in the controller)_

```
GET /users/:id
```

> retrieves a user _(attributes exposed are limited by the `read_scope` method defined in the controller)_

```
POST /users
```

> creates a user _(attributes assignable are limited by the `user_params` method defined in the controller as advised here http://guides.rubyonrails.org/action_controller_overview.html#strong-parameters)_

```
PUT /users/:id
```

> updates a user _(attributes assignable are limited by the `user_params` method defined in the controller as advised here http://guides.rubyonrails.org/action_controller_overview.html#strong-parameters)_

```
DELETE /users/:id
```

> deletes a user


If your model is referenced by another model (with a `has_many`, `has_one` or `belongs_to` relationship), nested routes are also created for you. And you don't need to worry about the references/joins, they are done automaticaly!

For example, imagine a `Team` model that has many `User`s
```ruby
class Team < ActiveRecord::Base
  has_many :users
end
```

the following routes will be exposed by the `UsersController` controller:
```
GET /team/:team_id/users
```
```
GET /team/:team_id/users/:id
```
```
POST /team/:team_id/users
```
```
PUT /team/:team_id/users/:id
```
```
DESTROY /team/:team_id/users/:id
```

### Note
You can disable __any__ of these actions by using the __::disable__ class method and providing the list of actions you want to disable
```ruby
class UsersController < Yodatra::ModelsController
  disable :read, :update, :delete, :nested_read_all, :nested_delete
end
```

### Extra
You can enable a special "search" action by using the __::enable_search_on__ class method
```ruby
class UsersController < Yodatra::ModelsController
  enable_search_on :name
end
```

## What it also provides for free

- __Logger__: Logs inside ```<your_project>/log``` in an environment named file ```env.err.log``` for all errors and ```env.log``` only for access logs.
- __Boot__: loads automaticaly all ```<your_project>/app/models/**/*.rb``` files and ```<your_project>/app/controllers/**/*.rb``` files. Establish a connection with a database by reading the ```<your_project>/config/database.yml``` file 

For that create a sinatra app that inherits from ```Yodatra::Base``` instead of ```Sinatra::Base```.

## Other useful modules

- __Throttling__: To fight against the dark side, an API throttling you will need. Example: allow only 10 requests/minute per IP: 
```ruby
use Yodatra::Throttle, {:redis_conf => {}, :rpm => 10}
```
_warning: this module requires redis_
- __ApiFormatter__:  this middleware will help you to format all your replies. Example: wrap all you replies within a ```{data: <...>}``` object:
```ruby
use Yodatra::ApiFormatter do |status, headers, response|
  body = response.empty? ? '' : response.first
  response = [{:data => body}]
  [status, headers, response]
end
```
