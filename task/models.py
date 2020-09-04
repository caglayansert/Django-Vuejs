from django.db import models

# Create your models here.


class Task(models.Model):

	title = models.CharField(max_length=140)
	date = models.DateTimeField(auto_now_add=True)
	completed = models.BooleanField(default=False)

	class Meta:
		ordering = ['completed', 'date']

	def __str__(self):
	 	return self.title