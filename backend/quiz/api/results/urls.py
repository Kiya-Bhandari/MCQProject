'''
defines the urls for the results app
'''
from django.urls import path
from api.results import views


urlpatterns = [
    path('history/<int:user_id>/', views.history, name='history'),
    path('save_quiz_view/<int:user_id>/<int:quiz_id>/',views.save_quiz_view,name='save')
]
