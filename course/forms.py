from django import forms

from .models import Course


class CourseForm(forms.ModelForm):
    title = forms.CharField(
        max_length=100, label='Titel',
        widget=forms.TextInput())
    description = forms.CharField(
        label='Beschreibung',
        widget=forms.Textarea())
    image = forms.ImageField(
        label='Bild',
        widget=forms.FileInput())

    class Meta:
        model = Course
        fields = ['title', 'description', 'image']
