from django.urls import path
from .views import *

urlpatterns = [
	path('', TaskView.as_view(), name='tasks_list_url'),
	path('<str:id>/complete/', TaskCompleteView.as_view()),
	path('<str:id>/delete/', TaskDeleteView.as_view()),


]