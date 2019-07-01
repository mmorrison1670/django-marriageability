from django.contrib import admin

# import your model
from collection.models import Score

# set up automated slug creation
class ScoreAdmin(admin.ModelAdmin):
    model = Score
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

# and register it
admin.site.register(Score, ScoreAdmin)
