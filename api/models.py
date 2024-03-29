import uuid

from django.contrib.auth.models import User
from django.db import models
from django.db.models import JSONField
from encrypted_model_fields.fields import EncryptedCharField

from . import choices


class Organisation(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    kvk_number = models.CharField(max_length=8)
    bro_user_token = EncryptedCharField(max_length=100, blank=True, null=True)
    bro_user_password = EncryptedCharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    organisation = models.ForeignKey(
        Organisation, on_delete=models.CASCADE, null=True, blank=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class ImportTask(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    data_owner = models.ForeignKey(
        Organisation, on_delete=models.CASCADE, null=True, blank=True
    )
    bro_domain = models.CharField(
        max_length=3, choices=choices.BRO_DOMAIN_CHOICES, default=None
    )
    kvk_number = models.CharField(max_length=8, blank=True, null=True)
    status = models.CharField(
        max_length=20, choices=choices.STATUS_CHOICES, default="PENDING", blank=True
    )
    log = models.TextField(blank=True)
    progress = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.bro_domain} import - {self.data_owner}"


class UploadTask(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    data_owner = models.ForeignKey(
        Organisation, on_delete=models.SET_NULL, null=True, blank=True
    )
    bro_domain = models.CharField(
        max_length=3, choices=choices.BRO_DOMAIN_CHOICES, default=None
    )
    project_number = models.CharField(max_length=20, blank=False)
    registration_type = models.CharField(
        blank=False, max_length=235, choices=choices.REGISTRATION_TYPE_OPTIONS
    )
    request_type = models.CharField(
        blank=False, max_length=235, choices=choices.REQUEST_TYPE_OPTIONS
    )
    metadata = JSONField("Metadata", default=dict, blank=False)
    sourcedocument_data = JSONField("Sourcedocument data", default=dict, blank=False)
    status = models.CharField(max_length=500, blank=True, null=True)
    bro_id = models.CharField(max_length=500, blank=True, null=True)
    log = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.data_owner}: {self.registration_type} ({self.request_type})"
