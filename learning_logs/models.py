from django.db import models
from django.contrib. auth.models import User

# Create your models here.

class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Entry(models.Model):
    """something specific learned about a topic"""
    topic = models.ForeignKey('Topic', on_delete=models.PROTECT)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text) < 50:
            return self.text
        else:
            return self.text[:50] + "..."

class Details(models.Model):
    """Details on the name and email and other details of the user."""
    topic = models.ForeignKey('Topic', on_delete=models.PROTECT)
    name = models.CharField(max_length = 50)
    emailanddetails = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.name
        
    
