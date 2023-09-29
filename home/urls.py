from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('under', views.under, name='under'),
    path('submit', views.submit,name='submit'),
    path('signin', views.signin,name='signin'),
    path('signup', views.signup,name='signup'),
    path('profile', views.profile, name='profile'),
    path('share/<int:id>', views.details, name ='details')
]