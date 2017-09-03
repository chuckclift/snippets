from django.db import models
from django.conf import settings

class Snippet(models.Model):
    content = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    public = models.BooleanField(default=0)
    
    def __str__(self):
        return self.content

class Tag(models.Model):
    tag = models.CharField(max_length=50)
    snippet = models.ForeignKey(Snippet)

    def __str__(self):
        return self.tag

