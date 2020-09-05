from django.forms import ModelForm

from .models import TextBlob

# form and validation for text input
class TextBlobForm(ModelForm):
    class Meta:
        model = TextBlob
        fields = ['text']
