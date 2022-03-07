'''
defines the urls for the quizes app
'''

from django.urls import path
from api.quizes import views

# from rest_framework import routers


# router = routers.DefaultRouter()
# router.register(r'', views.QuizViewSet)

urlpatterns = [
    path('testlist/<int:user_id>/', views.test_list, name='testlist'),
    path('questions/<int:quiz_id>/', views.quiz_data_view, name='questions'),
    # path('', include(router.urls))
]
