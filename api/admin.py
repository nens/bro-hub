from django.contrib import admin
from . import models

admin.site.register(models.Organisation)
admin.site.register(models.UserProfile)
