from django.db import models

# Create your models here.


class Committee (models.Model):
    name = models.CharField(max_length=50)
    members_no = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Member (models.Model):
    name = models.CharField(max_length=50)
    committee = models.ForeignKey(Committee)
    tasks = models.IntegerField()

    def __str__(self):
        return self.name
