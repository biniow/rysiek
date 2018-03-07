from django.contrib.auth.models import User
from django.db import models


class RepositoryType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Commit(models.Model):
    revision = models.CharField(max_length=40)
    author = models.CharField(max_length=255)
    author_email = models.CharField(max_length=255)
    commiter = models.CharField(max_length=255)
    commiter_email = models.CharField(max_length=255)
    parent_revision = models.CharField(max_length=40)
    lines_inserted = models.PositiveIntegerField()
    lines_deleted = models.PositiveIntegerField()
    files_changed = models.PositiveIntegerField()


class Repository(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    branch = models.CharField(max_length=255)
    description = models.TextField()
    public = models.BooleanField()
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='created_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='updated_by', null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    repo_type = models.ForeignKey(RepositoryType, on_delete=models.PROTECT)
    last_revision = models.ForeignKey(Commit, on_delete=models.PROTECT, null=True, blank=True)
    last_scan = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = (('address', 'branch'),)
        verbose_name_plural = 'Repositories'


class UserRepository(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)







