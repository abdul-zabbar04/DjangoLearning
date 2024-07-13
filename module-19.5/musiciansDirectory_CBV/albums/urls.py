from django.urls import path
from .import views

urlpatterns = [
    path('add_album/', views.add_album, name='addAlbum'),
    path('edit_album/<int:id>', views.edit_album, name='editAlbum'),
    path('delete_album/<int:id>', views.delete_album, name='deleteAlbum'),
]
