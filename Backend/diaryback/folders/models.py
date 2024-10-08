from django.db import models
from users.models import User
from diary.models import Diary
# Create your models here.
class Folder(models.Model):
    folder_id = models.AutoField(primary_key=True)
    folder_name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE)

    def __str__(self):
        return self.folder_name