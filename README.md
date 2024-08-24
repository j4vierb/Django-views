# Django views assignment

## Tasks

 - [ ] implement views in measurements application.

## Steps to include an URL application in the project

1. Create the `./app/logic/{}_logic.py`.
2. Import it in the `./views.py` and create `{}_view()` to use the logic functions.
3. Create an urlpatterns in `./urls.py` and include `from django.urls import path` to create the path.
4. include the urls of the application in the project using `from django.urls import path, include` (`path('{}/', include('{}.urls'))`).
