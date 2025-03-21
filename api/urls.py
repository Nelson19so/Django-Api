from django.urls import path
from . import views

urlpatterns = [
  path(
    "blogposts/", views.BlogPostSerializerCreate.as_view(), 
    name="blogpostcreateview"
  ),

  path(
      "blogposts/<int:pk>/", views.BlogPostRetrieveUpdateDestroy.as_view(),
      name="update"
  ),
]