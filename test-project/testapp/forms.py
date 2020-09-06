from django.forms import ModelForm
from django.core.exceptions import ValidationError

from .models import TextBlob
from .constants import MIN_WORD_COUNT, MAX_WORD_COUNT
from .tools import splitWords

# form and validation for text input
class TextBlobForm(ModelForm):
    class Meta:
        model = TextBlob
        fields = ['text']

    def clean(self):
        # enforce min/max rules about sentence words
        words = splitWords(self.cleaned_data['text'])
        if len(words) < MIN_WORD_COUNT:
            raise ValidationError('Not enough words. We need at least {count} words.'.format(count=MIN_WORD_COUNT), 'word_count')
        if len(words) > MAX_WORD_COUNT:
            raise ValidationError('Too many words. We need no more than {count} words.'.format(count=MAX_WORD_COUNT), 'word_count')
