from django.db import connection
from django.utils import timezone


def db_table_exists(table_name):
    return table_name in connection.introspection.table_names()


def one_day_later_than_now():
    return timezone.now() + timezone.timedelta(days=1)
