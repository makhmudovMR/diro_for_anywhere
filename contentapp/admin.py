from django.contrib import admin
from . import models


admin.site.register(models.News)
admin.site.register(models.Files)
admin.site.register(models.Banner)
admin.site.register(models.BannerLinks)
