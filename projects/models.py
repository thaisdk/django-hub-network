from django.db import models

# Create your models here.
class Project(models.Model):
    # owner = 
    project_name = models.CharField(max_length=500)


class Voting(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)