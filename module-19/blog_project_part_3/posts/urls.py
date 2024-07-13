from django.urls import path
from . import views

urlpatterns = [
    # path('add/', views.add_post, name='add_post'),
    path('add/', views.add_post.as_view(), name='add_post'),
    # path('edit/<int:id>', views.edit_post, name='edit_post'),
    path('edit/<int:id>', views.editView.as_view(), name='edit_post'),
    # path('delete/<int:id>', views.delete_post, name='delete_post'),
    path('delete/<int:id>', views.delete_view.as_view(), name='delete_post'),
    path('details/<int:pk>', views.post_details.as_view(), name='detailPage'),
]
