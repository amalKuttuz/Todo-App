from . import views
from django.urls import path
urlpatterns = [

path('home',views.home,name="home"),
path('add',views.add,name="add"),
path('update/<int:id>',views.updatetask,name="update/")
, path('delete/<int:id>',views.deleteTask,name="delete/")

]
      