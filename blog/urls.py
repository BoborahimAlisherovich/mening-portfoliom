from django.urls import path
from .views import home_view,blog_view
urlpatterns = [
    path('', home_view, name="home-page"),
    path('<int:id>/', blog_view, name="blog-page"),


]