# AwesomeAdminLayout

[![Build Status](https://img.shields.io/travis/appirits/awesome_admin_layout.svg?style=flat-square)](http://travis-ci.org/appirits/awesome_admin_layout)
[![Gem Version](https://img.shields.io/gem/v/awesome_admin_layout.svg?style=flat-square)](https://rubygems.org/gems/awesome_admin_layout)

AwesomeAdminLayout provides a simple way to add admin panel layout to your application.

## Installation

Add this line to your application's Gemfile:

```ruby
gem 'awesome_admin_layout'
```

And then execute:

```sh
$ bundle
```

Or install it yourself as:

```sh
$ gem install awesome_admin_layout
```

## Usage

- [Ruby on Rails](#a-ruby-on-rails)
- [Sinatra](#b-sinatra)

### a. Ruby on Rails

1. Install [font-awesome-rails](https://github.com/bokmann/font-awesome-rails) and [jquery-rails](https://github.com/rails/jquery-rails).

2. Import a style in `app/assets/stylesheets/application.scss`:

  ```scss
  @import "awesome_admin_layout";
  ```

3. Require a script in `app/assets/javascripts/application.coffee`:

  ```coffee
  #= require awesome_admin_layout
  ```

4. Create a file into `app/navigations`.
   And writing the definitions as follows:

  ```ruby
  #
  # NOTE: if you only use this layout in admin controller,
  #       you can write like this:
  #
  #       `AwesomeAdminLayout.define(only: Admin::ApplicationController)`
  #
  AwesomeAdminLayout.define do |controller|
    navigation do
      brand 'AwesomeAdminLayout' do
        external_link controller.root_path
      end

      item 'Dashboard' do
        link controller.dashboard_path
        icon 'dashboard'
      end

      item 'Orders' do
        link controller.orders_path
        icon 'shopping-cart'
        active true
      end

      item 'Products' do
        nest :products
        icon 'cube'
        badge true
      end

      item 'Users' do
        link controller.users_path
        icon 'user'
      end

      item 'Promotions' do
        link controller.promotions_path
        icon 'bullhorn'
      end

      item 'Analytics' do
        link controller.analytics_path
        icon 'bar-chart'
        badge true
      end

      divider

      item 'Store' do
        nest :store
        icon 'home'
      end

      divider

      item 'Extentions' do
        link controller.extentions_path
        icon 'puzzle-piece'
        badge 10
      end

      item 'Settings' do
        link controller.settings_path
        icon 'cog'
      end

      flex_divider

      item current_user.email do
        nest :profile
        icon 'gift'
      end
    end

    navigation :products do
      brand 'Products'

      item 'Products' do
        link controller.products_path
      end

      item 'Stocks' do
        link controller.stocks_path
      end

      item 'Categories' do
        link controller.categories_path
      end
    end

    navigation :store do
      brand 'Store' do
        external_link '/#external'
      end

      item 'Pages' do
        link controller.pages_path
      end

      item 'Links' do
        link controller.links_path
      end

      item 'Themes' do
        link controller.themes_path
      end
    end

    navigation :profile do
      brand current_user.email

      item 'Edit Profile' do
        link controller.edit_user_path(current_user)
      end

      item 'Logout' do
        link controller.destroy_user_session_path, method: :delete
      end
    end
  end
  ```

5. Use the helper method in your views.

  ```erb
  <%= render_admin_layout do %>
    <%# Put your main contents ... %>
  <% end %>
  ```

### b. Sinatra

pending...

## Development

To set up a dummy application for development, simply do:

```sh
$ cd test/dummy
$ bundle exec ruby sinatra_app.rb
```

And go to your browser and open `http://localhost:4567`.

## Contributing

1. Fork it ( https://github.com/appirits/awesome_admin_layout/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request
