from django.db import models
from folder.models import Folder  
class Diary(models.Model):
    diary_id = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=255)
    content = models.TextField()
    hint = models.CharField(max_length=255, blank=True, null=True)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='diaries')

    def __str__(self):
        return self.topic
