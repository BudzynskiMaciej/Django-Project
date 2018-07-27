# Django Project

This is Internet Application that communicates with YouTube API. It is written in [Python] v3.6.6 and [Django]. It uses [SQLite] as database engine and
[Celery] as task runner.

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
After that install project requirements. To do this run following command in project directory:
```sh
pip install -r requirements.txt
```
If you want to see project requirements check [requirements.txt](requirements.txt).

Then u need to migrate database using command:
```sh
python manage.py migrate
```
You also need [rabbitmq] installed and running as a service.
Then you need to run [Celery] Worker. To do this in main project directory with [virtualenv] enabled run:
```sh
celery -A DjangoTut worker -l info
```
Then on separate terminal run [Celery] Beat:
```sh
celery -A DjangoTut beat -l info --max-interval 43200
```
Where `--max-interval` is set to `43200` sec what is 12 hours, becouse every 12 hours most viewed videos on
homepage are refreshed.

To run project on localhost execute following command in project directory:
```sh
python manage.py runserver
```

## License

[MIT](https://github.com/BudzynskiMaciej/Django-Project/blob/develop/LICENSE)

[Python]: <https://www.python.org/>
[Django]: <https://www.djangoproject.com/>
[SQLite]: <https://www.sqlite.org/>
[Celery]: <http://www.celeryproject.org>
[virtualenv]: <https://virtualenv.pypa.io/en/stable/>
[rabbitmq]: <https://www.rabbitmq.com/>
[DjangoTutorial]: <https://docs.djangoproject.com/en/2.0/intro/tutorial01/>
