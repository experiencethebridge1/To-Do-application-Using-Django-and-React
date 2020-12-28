"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# backend/urls.py

from django.contrib import admin
from django.urls import path, include                 # add this
from rest_framework import routers                    # add this
from todo import views                                # add this

router = routers.DefaultRouter()                      # add this
router.register(r'todos', views.TodoView, 'todo')     # add this

urlpatterns = [
    path('admin/', admin.site.urls), path('api/', include(router.urls)) # add this
]

"""This is the final step that completes the building of the API, we can now perform CRUD operations on the Todo model. The router class allows us to make the following queries:

/todos/ - This returns a list of all the Todo items (Create and Read operations can be done here).
/todos/id - this returns a single Todo item using the id primary key (Update and Delete operations can be done here)."""

