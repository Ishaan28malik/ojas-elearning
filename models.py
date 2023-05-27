from django.db import models

# Create your models here.
class Member(models.Model):
    member_name = models.CharField(max_length = 263)
    member_details = models.TextField()
    member_origin = models.CharField(max_length = 64)
    # member_photo = models.ImageField()
    def __str__(self):
        return self.member_name

class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=263)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField('date published')
    
    def __str__(self):
        return self.tutorial_title