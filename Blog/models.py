
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Posts(models.Model):
    title=models.CharField(max_length=100)
    content = models.TextField()
    dated_post = models.DateTimeField(default=timezone.now)
    auther = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
