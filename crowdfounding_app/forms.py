from django import forms
from .models import Project, Contribution

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'goal_amount']

class ContributionForm(forms.ModelForm):
    class Meta:
        model = Contribution
        fields = ['amount']