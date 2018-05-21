# movies
README for Movie Website Project

A Python module that provides a static web-page with a few movies with box art imagery and a movie trailer URL.  The data of several movies is served as a web page allowing visitors to browse movies and their trailers.


I. File list
--------------
media.py			- Python class to store data structure for the class Movie

fresh_tomatoes.py		- Python module that creates the HTML page and populates it with any argument movie instances 

entertainment_center.py		- Python file that creates movie class instances, populates them into an array, and passes the array to a fresh_tomatoes method to display them in an HTML page


II. How to Run the 'Movie_Website' project
--------------------------------------------
The three python files were written in Python 2.7.8 and should be run with compatible Python installations.

You will need to navigate to the location of the files, have an Internet connection, and run the python module 'entertainment_center.py'.  

Running the 'entertainment_center.py' file will create compiled python files (.pyc) for media and fresh_tomatoes. Also the newly-created fresh_tomatoes.html file should open in a default browser. You may need to use a browser with ActiveX controls, if you are on a Windows machine, else some features may not work.


To run these files from a location on your computer make sure to have the appropriate version of Python installed:

1.  Navigate to the correct folder

2.  Run the python module 'entertainment_center.py'.

3.  This should open a new tab in the default browser with the newly created page fresh_tomatoes.html.


III. Design Decisions 
---------------------

The Movie class is defined in the media.py file.  This approach separates the Movie object from other code.

The fresh_tomatoes.py file creates the HTML page and populates it with the movie instance arguments.  

The entertainment_center.py file creates movie class instances, populates them into an array, and passes it to the fresh_tomatoes method to display them in the HTML page.  This module utilizes both of the other python files to produce the final product.

Future improvements include:
	- Use YouTube API to fill in the details for the movie class instances, so there will be no hard-coding of movie class instance attributes.
	- Show movie information in separate pop-up module via a button
