# A boilerplate project for python packages

A boilerplate project to use when bootstrapping new Python 3 projects with FastApi.
Copy the source code (no need to fork it), tweak the `setup.py` file to suit your needs and start doing things.


## Features

* Test automation and environment provisioning using [Tox](https://tox.readthedocs.io/)  
* Static code analysis using [Flake8](http://flake8.pycqa.org/en/latest/)
* Unit testing using [pytest](https://docs.pytest.org/en/latest/)  
* Enforced code coverage threshold using [coverage](https://coverage.readthedocs.io)  
* Dependencies pinned to the major version, allowing for backwards-compatible updates when upstream
* Licensed under [CC0 Public Domain Dedication](http://creativecommons.org/publicdomain/zero/1.0/)  

You can copy/paste anything and not worry about a thing, not even giving original authors attribution.

## Models

- "Account", a given customer account (a company), has a unique ID and a name  
- "Mall", a given shopping mall, has a unique ID, a name and a foreign key to a given Account 
- "Unit", a given store inside a shopping mall, has a unique ID, a name and a foreign key to a given Mall

The current version is using a SQLite database (see .env file) and a very basic ORM.

## Usage

*Remember only to follow those instructions after editing the source code to bootstrap your new project.*

### Install the application

```shell
pip install -e .
```

### Run the application in development mode

```shell
uvicorn api.main:app --reload
```

You will see the automatic interactive API documentation (provided by Swagger UI) here :
[Interactive API docs](http://127.0.0.1:8000/docs)  

You will see the alternative automatic documentation (provided by ReDoc) here :
[Interactive API docs - Redoc](http://127.0.0.1:8000/redoc)    

[API description](http://127.0.0.1:8000/openapi.json)

### Run test suite

```shell
tox
```

OR

```shell
coverage run -m pytest
coverage report
coverage html
```

### Collection endpoints and pagination

The collection entities are : accounts, malls, units
A summary of the endpoints can be seen here when the app is running : [Interactive API docs](http://127.0.0.1:8000/docs)

The collection endpoints ( /<entities> ) expose a simple pagination mechanism

#### Requests

Several requests may be necessary to get all the data (pagination) 

The query parameters are 
- skip (an offset number) : this parameter must be increased for each new request to skip the previous retrievec lines 
- limit : this value defines the maximum number of "rows" that are retrieved each time

#### Responses

Each response gives the total number of "rows" and a certain number of "rows".
So it is possible to compute the necessary number of requests given the maximum number of "rows" (limit parameter) 
that are retrieved each time.
