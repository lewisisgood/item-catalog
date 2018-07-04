# Item Catalog
Source code for a item catalog tool.

Item Catalog is a web application that provides a list of items within a variety of categories, and integrates third party user registration and authentication. Authenticated users have the ability to add, edit, and delete their own items to a set of pre-determined categories.

A JSON API is accessible for the whole catalog at http://localhost:8000/catalog.json , and for items in a category at http://localhost:8000/catalog/`category_name`/items.json , where category_name is substituted for a category e.g. Soccer.


### Prerequesites
Ensure that Python and git are installed:
```
python --version
git --version
```


### Installing

From the Terminal, clone this repo onto your computer with:

```
git clone https://github.com/lewisisgood/item-catalog
```

Move into the new directory:

```
cd item-catalog/
```

Create the database:

```
python database_setup.py
```

Load the database with items:

```
python lotsofitems.py
```

Run the program with:

```
python project.py
```

Naviage to http://localhost:8000/ to log in and interact with the item catalog.


## Built With

* Python 2.7.14
* git 2.14.1
* [Flask](http://flask.pocoo.org/)
* [SQLAlchemy](http://www.sqlalchemy.org/)
* [Google Identity](https://developers.google.com/identity/)


## Authors

* **Lewis King** - [Github](https://github.com/lewisisgood)


## Acknowledgments

* Thanks to Udacity for the Ubuntu VM, and CRUD and API lesson code from the backend lessons, which helped me make this project!