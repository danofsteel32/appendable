# Appendable

```
| list | list | list |
---------------------
| item | item | item |
```

Simple list/queue datastructures displayed on a dashboard.

```
/dashboard/<app_name>
GET = Get all lists for the app_name
PUT = create the app_name
DELETE = Delete the app_name

/dashboard/<app_name>/list/<listname>
GET = Get items in list
PUT = Create new list
DELETE = Delete list

/dashboard/<app_name>/list/<listname>/put
POST = Append an item to the list

/dashboard/<appname>/list/<listname>/pop
GET = Remove oldest item from list and return it

```
