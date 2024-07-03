from django import forms
from .models import TaskModel
from django.forms import widgets
class TaskForm(forms.ModelForm):
    class Meta:
        model= TaskModel
        fields= '__all__'
        labels= {
            'taskTitle': 'Task Title',
            'taskDescription': 'Task Description',
            'is_completed': 'Is Completed',
            'taskAssignDate': 'Task Assign Date',
            'category': 'Category'
        }
        widgets= {
            'taskAssignDate': widgets.DateInput(attrs={'type': 'date'}),
            'taskDescription': widgets.Textarea(attrs={'rows': 3})
        }