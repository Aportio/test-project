from django.forms import ModelForm

from .models import TextBlob

class TextBlobForm(ModelForm):
    class Meta:
        model = TextBlob
        fields = ['text']
