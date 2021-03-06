from django.db import models

# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(max_length=1024)
    age = models.IntegerField(default=0)
    email = models.EmailField(default='')
    summary = models.CharField(max_length=1024, default='')
    phone = models.CharField(max_length=12, default='+70000000000')

    def __str__(self):
        return f"{self.username}({self.email}) -> ({self.phone})"
