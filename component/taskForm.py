from django import forms
from dashboard.models import *
from dashboard.utils import getTaskUser


class TaskForm(forms.Form):
    taskname = forms.CharField(label='Short Name for task',
                                max_length=20,
                                widget=forms.TextInput(attrs={'placeholder': 'Name',
                                                             'class': 'keep-right'})
                               )
    task = forms.CharField(label='Task Details',
                            widget=forms.Textarea(attrs={'placeholder': 'Add your task details here.....',
                                                         'class': 'keep-right more-wider'})
                           )
    status = forms.ChoiceField(label='Choose Status',
                               choices=Task.STATUS_CHOICES,
                               initial='')
    duedate = forms.DateField(label='Due date for task',
                              input_formats=['%d-%m-%Y'])
    time = forms.TimeField(label='Time',
                           widget=forms.TimeInput(format='%h:%m:%s'))

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['status'].widget.attrs.update({'class': 'keep-right wider'})
        self.fields['duedate'].widget.attrs.update({'class': 'keep-right'})
        self.fields['time'].widget.attrs.update({'class': 'keep-right'})

    class Meta:
        model = Task
        fields = ('taskname', 'task', 'status', 'duadate', 'time')

    def clean(self):
        print("Cleaning form...")
        cleaned_data = super(TaskForm, self).clean()
        task = cleaned_data['task']
        if len(task) < 25:
            self.add_error('task', 'Please enter correct task details at least 100 chars')

        return self.cleaned_data

    def save(self, user_id, commit=True):
        task = Task()
        task.user_id = getTaskUser(user_id)
        task.taskname = self.cleaned_data['taskname']
        task.task = self.cleaned_data['task']
        task.status = self.cleaned_data['status']
        task.duedate = self.cleaned_data['duedate']
        task.time = self.cleaned_data['time']

        if commit:
            task.save()
        print('saving record..')
