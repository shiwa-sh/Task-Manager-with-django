from django.db import models
from django.utils import timezone
from django.urls import reverse


# def one_week_hence():
#     return timezone.now() + timezone.timedelta(days=7)


class AllTasks(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse("list", args=[self.id])

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=250)
    # slug = models.SlugField(default='', null=False)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True)
    all_tasks = models.ForeignKey(AllTasks, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("item-update", args=[str(self.all_tasks.id), str(self.id)])

    class Meta:
        ordering = ["due_date"]
