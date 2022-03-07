
'''
defines the urls for the api app
'''
from django.urls import path, include

urlpatterns = [
    path('user/', include('api.user.urls')),
    path('quizes/', include('api.quizes.urls')),
    path('results/', include('api.results.urls')),
    # path('questions/', include('api.questions.urls')),
    # path('results/', include('api.results.urls')),

]
