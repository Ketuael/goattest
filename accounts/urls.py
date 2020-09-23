from django.conf.urls import re_path
from accounts import views

urlpatterns = [
    re_path(r"^send_login_email$", views.send_login_email, name="send_email"),
]
