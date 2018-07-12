# Django Project

This is Polling app written in [Python] and [Django]. It uses [SQLite] as database engine. 

## Download

For download u can use one of the following methods:
 - Run command below using your command line tool with GIT installed:
  ```sh
  git clone https://github.com/BudzynskiMaciej/Django-Project.git
  cd Django-Project/
  ```
  - [Download zip file](https://github.com/BudzynskiMaciej/Django-Project/archive/develop.zip)

## Running project

Make sure you have installed and activated [virtualenv].
Then u need to migrate database using command:
```sh
python manage.py migrate
```
To run project on localhost execute following command in project directory:
```sh
python manage.py runserver
```

## License

[MIT](https://github.com/BudzynskiMaciej/Django-Project/blob/develop/LICENSE)

[Python]: <https://www.python.org/>
[Django]: <https://www.djangoproject.com/>
[SQLite]: <https://www.sqlite.org/>
[virtualenv]: <https://virtualenv.pypa.io/en/stable/>
[DjangoTutorial]: <https://docs.djangoproject.com/en/2.0/intro/tutorial01/>
