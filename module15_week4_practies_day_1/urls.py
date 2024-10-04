
from django.contrib import admin
from django.urls import path, include
from .views import show_data, edit_album,edit_musician,delete_album

urlpatterns = [
    path('admin/', admin.site.urls),
    path('musician/',include('musician.urls')),
    path('album/',include('album.urls')),
    path('',show_data,name="show_data"),
    path('edit_album/<int:id>/',edit_album,name="edit_album"),
    path('edit_musician/<int:id>/',edit_musician,name="edit_musician"),
    path('delete_album/<int:id>/',delete_album,name="delete_album"),
]
