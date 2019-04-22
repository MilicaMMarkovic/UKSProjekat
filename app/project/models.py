from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from .managers import ProjectManager


# Create your models here.

def default_user():
    try:
        return User.objects.get(username="MilicaMM")
    except:
        return User.objects.create_user(username="MilicaMM", email="milicamarkovic94@yahoo.com", password="Milicica")


class Project(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="owned_projects", blank=False)
    members = models.ManyToManyField(to=User, related_name="member_of_projects")
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=250)
    date_created = models.DateField('Date created', auto_now_add=True)

    objects = ProjectManager()

    class Meta:
        unique_together = (("owner", "title"),)

    def get_absolute_url(self):
        return reverse('project:project_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "%s (%s)" % (self.title, self.owner)


class Milestone(models.Model):
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, related_name="milestones", blank=False)
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=250)
    start_date = models.DateField('Date created', auto_now_add=True)
    due_date = models.DateField('Due date')

    class Meta:
        unique_together = (("project", "title"),)

    def get_absolute_url(self):
        return reverse('project:milestone_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "Milestone: %s (%s)" % (self.title, self.project.title)


class Label(models.Model):
    name = models.CharField(max_length=50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('project:label_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "Label: " + self.name


class Issue(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    assignees = models.ManyToManyField(User, related_name='assignees')
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    label = models.ManyToManyField(to=Label)
    milestone = models.ForeignKey(to=Milestone, null=True, on_delete=models.SET_NULL)

    def get_absolute_url(self):
       return reverse('project:issue_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "Issue: %s (%s)" % (self.title, self.description)
