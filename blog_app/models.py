from django.contrib.auth.models import User
from django.db import models
class Maqola(models.Model):
    title = models.CharField(max_length=100)
    matn = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Rasm(models.Model):
    photo = models.FileField(upload_to='static/media/')
    maqola = models.ForeignKey(Maqola,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.maqola.title}'
