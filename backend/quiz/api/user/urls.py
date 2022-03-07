'''
defines the urls for the user app
'''
from django.urls import path
from api.user import views
# from rest_framework import routers


# router = routers.DefaultRouter()
# router.register(r'', views.UserViewSet)

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/<int:user_id>/', views.signout, name='signout'),
    # path('', include(router.urls))
]
