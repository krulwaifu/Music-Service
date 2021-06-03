from django import forms
from audio.models import Audio, Transcription


class AudioForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = "__all__"

class TranscriptionFormC(forms.ModelForm):
    class Meta:
        model = Transcription
        fields = ["audio"]

class TranscriptionFormS(forms.ModelForm):
    class Meta:
        model = Transcription
        fields = "__all__"