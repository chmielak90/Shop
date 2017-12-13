# Shop

This is a project of web store

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python 3.5.4
* All other things you need to run this project you find in [requirements.txt](requirements.txt).

### Starting the project

Start virtual env for this project with Python 3.5.4 and run it.

Install [requirements.txt](requirements.txt)
```
$ pip install -r requirements.txt
```

Make migrations
```
$ python manage.py makemigrations
$ python manage.py migrate
```

Create superuser (admin)
```
$ python manage.py createsuperuser
```

Run server
```
$ python manage.py runserver
```

Go to `127.0.0.1:8000/shop` and then Log in at admin account. To see any result add new category and then add new product (all of this functions, you see on admin account in up secction)

## Built With

* [Python 3.5.4](https://docs.python.org/3.5/)
* [Django](https://docs.djangoproject.com/en/1.11/) - The web framework used
* [Bootstrap](https://getbootstrap.com/) - HTML, CSS library

## Authors

* **Michał Chmielewski** - *Initial work* - [chmielak90](https://github.com/chmielak90)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
