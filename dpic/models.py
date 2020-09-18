from django.db import models

class Instapic(models.Model):
    pic_user_name = models.CharField(max_length=200)
    downdate= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pic_user_name