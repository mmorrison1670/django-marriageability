from django.forms import ModelForm
from collection.models import Score

class ScoreForm(ModelForm):
    class Meta:
        model = Score
        fields = ('name', 'description',)
