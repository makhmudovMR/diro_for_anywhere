from django.contrib import admin
from . import models


admin.site.register(models.Answer)
admin.site.register(models.Question)
admin.site.register(models.Test)
admin.site.register(models.Person)
admin.site.register(models.PersonAnswer)

admin.site.site_title = 'Система тестирования'
admin.site.index_title = 'Система тестирования'
admin.site.site_header = 'Система тестирования'
