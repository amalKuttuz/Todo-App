from django.db import models

class TodoModel(models.Model):
    title=models.CharField(max_length=100)
    created=models.DateField(null=True, blank=True,auto_now_add=True)
    desc=models.TextField()
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.title
