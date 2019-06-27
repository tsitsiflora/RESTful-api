.. MoviesAPI documentation master file, created by
   sphinx-quickstart on Thu Jun 27 10:01:15 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to MoviesAPI's documentation!
=====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
++++++++++++++++++

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
 
    
Configuration of Project Environment 
------------------------------------


This is an API that manages a collection of movies using Python3.6, Django Rest Framework and sqlite database. 

How to run the API:
+++++++++++++++++++

1. create a Python virtual environment and install requirements
2. install Postman to query the API

**1. Python Virtual Environment**


In Ubuntu/Linux terminal:

- First clone the project repository::

    git clone https://github.com/tsitsiflora/RESTful-api.git

    cd RESTful-api

- Create the virtual environment and activate it::

    python3 -m virtualenv env 

    source env/bin/activate

-  packages in requirements.txt::

    pip3 install -r requirements.txt

- Run the project::

    python3 manage.py runserver

.. attention::
    You need Python3.6+ to run this API.

**2. Install Postman**

`Follow this link <https://www.getpostman.com/>`_ to download Postman.

After installing Postman, you can query the API using the following url::
     
    127.0.0.1:8000/<endpoint>

For example::

    127.0.0.1:8000/getmovies

See `Endpoints of the MovieAPI`_ for all the endpoints.

Endpoints of the MovieAPI 
--------------------------


- get all movies
- get all directors
- get all actors
- post new movies
- post new directors
- post new actors
- patch existing movie
- patch existing director
- patch existing actor
- delete movie
- delete director
- delete actor

Source code documentation  
--------------------------

**MoviesAPI models**

.. automodule:: movies.models
    :members:






 
