from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Edition)
admin.site.register(models.HeroImage)
admin.site.register(models.Kit)
admin.site.register(models.Partenaire)
admin.site.register(models.Activite)
admin.site.register(models.Commande)
admin.site.register(models.LieuRetrait)


