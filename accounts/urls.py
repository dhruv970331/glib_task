from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from .views import SignUpView,ProfileView,MainView,SearchView

urlpatterns = [
    path("signup/",SignUpView.as_view(),name="signup"),
    path("login/",LoginView.as_view(template_name="accounts/login.html"),name="login"),
    path("logout/",LogoutView.as_view(next_page="/"),name="logout"),
    path("<int:pk>/profile/",ProfileView.as_view(),name="profile"),
    path("main/",MainView.as_view(),name="main"),
    path("search/",SearchView.as_view(),name="search")
]