from django.db import models

# Create your models here.
class Diary(models.Model):
    diary_id = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=255)
    content = models.TextField()
    hint = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.topic