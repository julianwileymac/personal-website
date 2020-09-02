from django.db import models

# Create your models here.
### From the datacamp django tutorial
class Post(models.Model):
	title = models.CharField(max_length = 50)
	content = models.TextField()

	def __str__(self):
		return self.title