import uuid

from django.db import models


class Project(models.Model):
    # owner = 
    # image = 

    title = models.CharField(max_length=200, editable=True, help_text='Enter project title')
    description = models.TextField(blank=True, null=True, editable = True, help_text='Enter project description')
    demo_link = models.CharField(max_length=2000, blank=True, null=True, editable = True, help_text='Demonstration Link')
    code_link = models.CharField(max_length=2000, blank=True,null=True, editable=True, help_text='Code Link')
    
    tags = models.ManyToManyField('Tag', blank=True)
    # likes = models.PositiveIntegerField(default=0, null=True, blank=True)
    # user_likes=models.ManyToManyField(User)
    # dislike = models.IntegerField(default=0, null=True, blank=True)

    created = models.DateField(auto_now_add=True, editable=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    

    def __str__(self):
        return str(self.title)


# class Like(models.Model):

#     # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     already_liked = models.BooleanField(default=False)


#     def __str__(self):
#         return f"{self.user} liked {self.project}"


class Tag(models.Model):
    name = models.CharField(max_length=200, editable=True)
    created = models.DateField(auto_now_add=True, editable = False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    
    def __str__(self):
        return self.name
