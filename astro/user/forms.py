from django import forms
from .models import register, Feedback


class registerForm(forms.ModelForm):
    class Meta:
        model = register
        fields = "__all__"
        labels = {"name": "Full Name", "gender": "Gender", "email": "Email", "contact": "Phone Number"}


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = "__all__"
