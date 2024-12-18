from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path("update_pw/", views.update_pw, name="update_pw"),
    path("update_user/", views.update_user, name="update_user"),
    path("update_info/", views.update_info, name="update_info"),
    path("product/<int:pk>", views.product, name="product"),
    path("category/<str:foo>", views.category, name="category")
]