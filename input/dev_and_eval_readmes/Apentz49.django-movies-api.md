# Django Movie API

## Description

Create a RESTful API that you can perform CRUD actions on a basic django model.

## Learning Objectives

After completing this assignment, you should be able to:

* Create an API of CRUD views for the `Movie` model.

## Details

### Deliverables

* A Git repo called django-movies-api containing at least:
  * a `requirements.txt` file
  * a `README.md` file
  * a Django project called `crud` containing an app with API views for the Movie model.

### Normal Mode

Included is a basic app where template driven views allow a user to create/read/delete new and existing
movies in the database.  Create an app called `api` that all API requests will use and correctly perform the `verb`
you are expecting.

Required verbs to implement:
 - GET
 - POST
 - PUT
 - DELETE

Required functionality to implment:
 - Query for all movies
 - Query for a specific movie
 - Create a new movie in the database
 - Update existing fields on an existing movie
 - Delete an existing movie

How you choose to implement your API is up to you. The one hard requirement is that you do not rely on an external
API framework. Choices like class-based or function-based views are up to you. In fact for clarity you may find
function based views more of an optimal choice for this assignment.

### Hard Mode

In addition to the `normal mode` requirements adapt your movie model to be able to load in your movielens dataset (use
a small dataset if you prefer) and adapt your views to be able to work with the new fields.


### Additional Resources:

[Star Wars API](http://swapi.co)

[Retrieving the `method` verb in a django view](https://docs.djangoproject.com/en/1.8/ref/request-response/#django.http.HttpRequest.method)

[Naming RESTful resources](http://www.restapitutorial.com/lessons/restfulresourcenaming.html)
