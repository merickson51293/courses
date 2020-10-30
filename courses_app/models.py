from django.db import models
from django.core.exceptions import ValidationError

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors={}
        if len(postData['name']) < 5:
            errors['title'] = "Title should be at least 5 characters"
        if len(postData['desc']) < 15:
            errors['desc'] = "Description should be at least 15 characters"
        return errors
        

class Courses(models.Model):
    name = models.CharField(max_length=45)
    desc = models.TextField(default="This Course")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()