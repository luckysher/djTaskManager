# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from taskForm import TaskForm
from django.views import View
from django.views.generic import ListView
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from dashboard.models import Task
from dashboard.utils import getUserId


class AddTaskView(View):

    BUTTON_TEXT = 'Add task'
    TEMPLATE = 'addTaskForm.html'
    target = ''
    next_url = '/tasks/addtask/'

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(AddTaskView, self).dispatch(request, *args, **kwargs)

    def render_form(self, request, form, data=None):
        return render(request, self.TEMPLATE,  {
                                                'form': form,
                                                'data': data,
                                                'button_text': self.BUTTON_TEXT,
                                                'button_target': self.target,
                                                'next': self.next_url
                                                })

    def render_form_with_status(self, request, form, status, data=None):
        messages.add_message(request, messages.SUCCESS, status)
        data = {
                 'status': status
               }
        return self.render_form(request, form, data)

    def get(self, request, *args, **kwargs):
        print("Get request for form.............")
        form = TaskForm()
        return self.render_form(request, form)

    def post(self, request, *args, **kwargs):
        try:
            form = TaskForm(request.POST)
            print("Post request for form.............")
            status = 'added task successfully..'

            if form.is_valid():
                form.save(user_id=getUserId(request))
                return self.render_form_with_status(request, form, status)
            else:
                return self.render_form(request, form)
        except Exception as e:
            print("Got exception while rendering form ,,,,,", e)
            return self.render_form(request, form)


class TaskView(ListView):
    template_name = 'tasks.html'
    model = Task

    def get_tasks_set(self, user_id):
        queryset = Task.objects.filter(user_id=user_id).all()
        return queryset

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(TaskView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.queryset = self.get_tasks_set(getUserId(request))
        return ListView.get(self, request, *args, **kwargs)
