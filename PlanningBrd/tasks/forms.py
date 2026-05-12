from django import forms
from django.contrib.auth.models import User
from .models import Task, Project, Calendar, Tag, UserSettings, Todo


class SignUpForm(forms.ModelForm):
    password = forms.CharField(
        label="Heslo",
        widget=forms.PasswordInput(attrs={"placeholder": "Heslo"}),
    )

    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Uživatelské jméno"}),
        }

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Toto uživatelské jméno je již obsazené.")
        return username

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class CalendarForm(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = ["field"]


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description", "start_date", "end_date"]
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
        }


class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = UserSettings
        fields = ["default_priority", "default_recurrence", "show_completed_tasks"]


class TaskForm(forms.ModelForm):
    project = forms.ModelChoiceField(
        queryset=Project.objects.none(),
        required=True,
        label="Projekt"
    )

    class Meta:
        model = Task
        fields = ["title", "description", "date", "start_time", "end_time", "priority", "completed", "project"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "start_time": forms.TimeInput(attrs={"type": "time"}),
            "end_time": forms.TimeInput(attrs={"type": "time"}),
        }
    
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            self.fields['project'].queryset = Project.objects.filter(user=user)
            self.fields['project'].label = "Projekt"

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "description", "due_date", "completed"]
        widgets = {
            "due_date": forms.DateInput(attrs={"type": "date"}),
        }
