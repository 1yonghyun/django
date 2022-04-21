from django.db import models
from django.conf import settings
# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.TextField()
    completed = models.BooleanField()
    author_id = models.IntegerField()


# view에서
# def index 부분에
#     user = request.user
#     todos = user.todo_set_all()