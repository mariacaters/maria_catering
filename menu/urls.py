from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("login/",LoginView.as_view(template_name="login.html"),name="login"),
    path("logout/",LogoutView.as_view(),name="logout"),
    path("", views.home, name="home"),
    path("new/",views.new_order,name="new_order"),
    path("edit/<int:order_id>/",views.edit_order,name="edit_order"),
    path("delete/<int:order_id>/",views.delete_order,name="delete_order"),
    path("print/<int:order_id>/",views.print_order,name="print_order"),
]