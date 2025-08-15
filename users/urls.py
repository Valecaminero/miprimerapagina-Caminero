from django.urls import path
from .views import UserRegisterView, CustomLoginView, CustomLogoutView, ProfileView, AvatarUpdateView, ProfileUpdateView, aboutmeView 

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('avatar/', AvatarUpdateView.as_view(), name='avatar-update'),
    path("profile/edit/", ProfileUpdateView.as_view(), name="edit_profile"),
    path("aboutme/", aboutmeView.as_view(), name="aboutme"),
     
   ]