# Django views assignment

## Tasks

 - [x] implement views in measurements application.

## Steps to include an URL application in the project

1. Create the `./app/logic/{}_logic.py`.
2. Import it in the `./views.py` and create `{}_view()` to use the logic functions.
3. Create an urlpatterns in `./urls.py` and include `from django.urls import path` to create the path.
4. include the urls of the application in the project using `from django.urls import path, include` (`path('{}/', include('{}.urls'))`).

## Doing requests using cURL

```bash
$ cURL -s -X "GET" http://localhost:8000/{variables/measurements}/
$ cURL -s -X "POST" -H "application/json" -d '{"key": "value"}' http://localhost:8000/{variables/measurements}/

$ cURL -s -X "GET" http://localhost:8000/{variables/measurements}/{id}
$ cURL -s -X "PUT" -H "application/json" -d '{"key": "value"}' http://localhost:8000/{variables/measurements}/{id}
$ cURL -s -X "DELETE" -H "application/json" http://localhost:8000/{variables/measurements}/{id}
```
