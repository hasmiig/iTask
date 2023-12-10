'''
from django import forms
from django.forms import ModelForm
from .models import Task

class TaskForm(forms.ModelForm):
  title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new task...'}))

  class Meta:
    model = Task
    fields = '__all__' # ['title', 'complete'


'''

'''

# forms.py
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']

    def __init__(self, *args, user=None, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.user = user  # Store the user information in the form

    def save(self, commit=True):
        instance = super(TaskForm, self).save(commit=False)
        instance.user = self.user  # Set the user for the Task instance
        if commit:
            instance.save()
        return instance
'''


# forms.py
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','complete', 'deadline']  # Include the deadline field in the form

    def __init__(self, *args, user=None, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.user = user  # Store the user information in the form

    def save(self, commit=True):
        instance = super(TaskForm, self).save(commit=False)
        instance.user = self.user  # Set the user for the Task instance
        if commit:
            instance.save()
        return instance

    