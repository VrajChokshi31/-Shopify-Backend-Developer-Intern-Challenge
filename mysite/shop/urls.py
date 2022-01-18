from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ViewItem', views.ViewItem, name='ViewItem'),
    path('AddItem', views.AddItem, name='AddItem'),
    path('ModifyItem', views.ModifyItem, name='ModifyItem'),
    path('Export', views.Export, name='Export'),
    path('DeleteItem', views.DeleteItem, name='DeleteItem'),
    path('add', views.add, name='add'),
    path('mod', views.mod, name='mod'),
    path('del', views.delete, name='delete'),
    path('myview', views.myview, name='myview')

]