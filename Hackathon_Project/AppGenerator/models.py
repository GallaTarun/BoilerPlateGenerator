from django.db import models

class Project(models.Model):
    projectID = models.IntegerField(primary_key=True, default=0)
    projectFolder = models.FileField(upload_to='media')
    frontend = models.CharField(max_length=30)
    backend = models.CharField(max_length=30)

    def __str__(self):
        return self.frontend + " <=> " + self.backend

class Backend(models.Model):
    bId = models.IntegerField(primary_key=True, default=0)
    bName = models.CharField(max_length=30)

    def __str__(self):
        return self.bName

class Frontend(models.Model):
    fId = models.IntegerField(primary_key=True, default=0)
    fName = models.CharField(max_length=30)
    backends = models.ManyToManyField(to=Backend)

    def __str__(self):
        return self.fName