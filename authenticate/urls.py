from django.urls import path
from . import views
urlpatterns = [
    path('', views.redirect_login, name='login'),
    path('signup/', views.signup_form, name='signup'),
    path('logout/', views.log_out)
    # path('login/', views.login_form, name='signup'),

]