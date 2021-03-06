from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect

from django.http import JsonResponse
from django.forms.models import model_to_dict

from .models import Task
from .forms import TaskFrom
# Create your views here.
class TaskView(View):

	def get(self, request):
		tasks = list(Task.objects.values())
		if request.is_ajax():
			return JsonResponse({'tasks':tasks}, status=200)

		return render(request, 'task/tasks.html')

	def post(self, request):
		form = TaskFrom(request.POST)

		if form.is_valid():
			new_task = form.save()
			return JsonResponse({'task':model_to_dict(new_task)}, status=200)
		
		return redirect('tasks_list_url')

class TaskCompleteView(View):
	def post(self, request, id):
		task = Task.objects.get(id=id)
		task.completed = True
		task.save()

		return JsonResponse({'task': model_to_dict(task)}, status=200)

class TaskDeleteView(View):

	def post(self, request, id):

		task = Task.objects.get(id=id)
		task.delete()

		return JsonResponse({'result':'ok'}, status=200)
