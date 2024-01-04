from django.db import models

class Moominmug(models.Model):
	name = models.CharField(max_length=50)
	officialName = models.CharField(max_length=50, blank=True, null=True)
	image = models.ImageField(upload_to='images/', blank=True, null=True)
	count = models.IntegerField()
	color = models.CharField(max_length=50, blank=True, null=True)
	figure = models.CharField(max_length=50, blank=True, null=True)
	theme = models.CharField(max_length=50, blank=True, null=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
			return f"/moominmugs/{self.pk}"

	
