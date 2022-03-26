from django.urls import path, include
from .views import *


urlpatterns = [

    # Account Urls
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('logout/', logoutview,name='logout'),
	path('forget/', forget, name='forget'),

    # Verification And Activattion Urls
	path('verification/', verification, name='verification'),
	path('activate/<username>/<token>/', activate_user, name='activate'),

    # Reset Urls
	path('reset-sent/', resest_send, name='reset-sent'),
	path('reset-password/<username>/<token>/', reset_user, name='reset-password'),
	path('new-password/', new_password, name='new-password'),

    # Profile
    path('profile/', profile, name="profile"),

    # Google Auth 
    path('accounts/', include('allauth.urls')),
#    path('', include("googleauthentication.urls"))
]