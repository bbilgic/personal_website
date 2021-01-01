import datetime

import pytz
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Value, TextField, Sum
from django.db.models.functions import Concat
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.dateparse import parse_date, parse_datetime
from django.views.generic import  DetailView, ListView, CreateView, DeleteView, UpdateView, FormView

# Create your views here.
from psycopg2._psycopg import Date

from core.forms import *
from core.models import *


class HomePageDetailView(DetailView):
    template_name = "index.html"
    model = HomePage

    def get_object(self):
        qs = HomePage.objects.filter(status=HomePage.ACTIVE).order_by('order').first()
        return qs


class AboutPageDetailView(DetailView):
    template_name = "about.html"
    model = AboutPage

    def get_object(self):
        qs = AboutPage.objects.filter(status=AboutPage.ACTIVE).order_by('order').first()
        return qs


class SubjectListView(LoginRequiredMixin, ListView, FormView):
    template_name = "core/subject_list.html"
    model = Subject
    form_class = SubjectSearchForm
    paginate_by = 20

    def get_queryset(self):
        qs = self.model.objects.filter(status=Subject.ACTIVE).order_by('id').prefetch_related('label')
        text_search = self.request.GET.get('text_search')
        label = self.request.GET.getlist('label')
        if text_search:
            qs = qs.annotate(
                search=Concat('name', Value(' '), 'description', Value(' '), 'label',
                              output_field=TextField())).filter(
                search__icontains=text_search)
        if label and '' not in label:
            qs = qs.filter(label__in=label)
        qs = qs.prefetch_related('label').order_by('id')
        return qs


class SubjectDetailView(LoginRequiredMixin, DetailView):
    template_name = "core/subject_detail.html"
    model = Subject


class SubtopicListView(LoginRequiredMixin, ListView, FormView):
    template_name = "core/subject_list.html"
    model = Subtopic
    form_class = SubtopicSearchForm
    paginate_by = 20

    def get_queryset(self):
        qs = self.model.objects.filter(status=Subject.ACTIVE).order_by('id').prefetch_related('label').select_related(
            'subject')
        text_search = self.request.GET.get('text_search')
        label = self.request.GET.getlist('label')
        subject = self.request.GET.getlist('subject')
        if text_search:
            qs = qs.annotate(
                search=Concat('name', Value(' '), 'description', Value(' '), 'label',
                              output_field=TextField())).filter(
                search__icontains=text_search)
        if label and '' not in label:
            qs = qs.filter(label__in=label)
        if subject and '' not in subject:
            qs = qs.filter(subject__in=subject)
        qs = qs.prefetch_related('label').order_by('id')
        return qs


class SubtopicDetailView(LoginRequiredMixin, DetailView):
    template_name = "core/subtopic_detail.html"
    model = Subtopic


class GoalListView(LoginRequiredMixin, ListView, FormView):
    template_name = "goal_list.html"
    model = Goal
    form_class = GoalSearchForm
    paginate_by = 20

    def get_queryset(self):
        qs = self.model.objects.filter(status=Subject.ACTIVE).order_by('id').prefetch_related('label').prefetch_related(
            'subject').prefetch_related('subtopic').order_by('due_date')
        text_search = self.request.GET.get('text_search')
        label = self.request.GET.getlist('label')
        subject = self.request.GET.getlist('subject')
        subtopic = self.request.GET.getlist('subtopic')
        if text_search:
            qs = qs.annotate(
                search=Concat('name', Value(' '), 'description', Value(' '), 'label', Value(' '), 'subject', Value(' '),
                              'subtopic',
                              output_field=TextField())).filter(
                search__icontains=text_search)
        if label and '' not in label:
            qs = qs.filter(label__in=label)
        if subject and '' not in subject:
            qs = qs.filter(subject__in=subject)
        if subtopic and '' not in subtopic:
            qs = qs.filter(subtopic__in=subtopic)
        return qs


class GoalDetailView(LoginRequiredMixin, DetailView):
    template_name = "core/goal_detail.html"
    model = Goal

class NoteCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Note
    form_class = NoteCreateAndEditForm
    success_message = "Note created successfully"
    template_name = 'core/note_new.html'

    def get_success_url(self):
        return reverse('core:note_detail', kwargs={'pk': self.object.pk})



class NoteUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'core/note_update.html'
    form_class =NoteCreateAndEditForm
    model = Note

    def get_success_url(self):
        return reverse('core:note_detail', kwargs={'pk': self.object.pk})


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = "core/note_delete.html"

    def get_success_url(self):
        return reverse_lazy('core:note_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.status = Task.DELETED
        self.object.save()
        messages.success(request, "Note has been deleted successfully.")
        return HttpResponseRedirect(self.get_success_url())

class NoteListView(LoginRequiredMixin, ListView, FormView):
    template_name = "core/note_list.html"
    model = Note
    form_class = GoalSearchForm
    paginate_by = 20

    def get_queryset(self):
        qs = self.model.objects.filter(status=Subject.ACTIVE).order_by('id').prefetch_related('task').prefetch_related(
            'subject').prefetch_related('subtopic').prefetch_related('goal').order_by('-created_date')
        text_search = self.request.GET.get('text_search')
        subject = self.request.GET.getlist('subject')
        subtopic = self.request.GET.getlist('subtopic')
        if text_search:
            qs = qs.annotate(
                search=Concat('title', Value(' '), 'text', Value(' '), 'subject', Value(' '), 'subtopic',
                              output_field=TextField())).filter(
                search__icontains=text_search)
        if subject and '' not in subject:
            qs = qs.filter(subject__in=subject)
        if subtopic and '' not in subtopic:
            qs = qs.filter(subtopic__in=subtopic)
        return qs


class NoteDetailView(LoginRequiredMixin, DetailView):
    template_name = "core/note_detail.html"
    model = Note


class TaskCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskCreateAndEditForm
    success_message = "Task created successfully"
    template_name = 'core/task_new.html'

    def get_success_url(self):
        return reverse('core:task_detail', kwargs={'pk': self.object.pk})



class TaskUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'core/task_update.html'
    form_class = TaskCreateAndEditForm
    model = Task

    def get_success_url(self):
        return reverse('core:task_detail', kwargs={'pk': self.object.pk})


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "core/task_delete.html"

    def get_success_url(self):
        return reverse_lazy('core:task_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.status = Task.DELETED
        self.object.save()
        messages.success(request, "Task has been deleted successfully.")
        return HttpResponseRedirect(self.get_success_url())

class TaskCopyView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskCreateAndEditForm
    template_name = 'core/task_new.html'
    success_message = "Task created successfully"


    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.pk = None
        return super(TaskCopyView, self).form_valid(form)

    def get_success_url(self):
        return reverse('core:task_detail', kwargs={'pk': self.object.pk})



class TaskListView(LoginRequiredMixin, ListView, FormView):
    template_name = "core/task_list.html"
    model = Task
    form_class = TaskSearchForm
    paginate_by = 10

    def get_initial(self):
        initial = super().get_initial()
        closed = self.request.GET.get('closed')
        date = self.request.GET.get('date')
        initial['subject'] = self.request.GET.getlist('subject')
        initial['text_search'] = self.request.GET.get('text_search')
        if closed:
            initial['closed'] = closed
        else:
            initial['closed'] = 'open'
        if closed:
            initial['date'] = date
        else:
            initial['date'] = 'today'
        return initial

    def get_queryset(self):
        qs = self.model.objects.filter(status=Task.ACTIVE).order_by('-id').prefetch_related('subject').prefetch_related(
            'label').prefetch_related('subtopic').prefetch_related('goal').order_by('action_date')
        text_search = self.request.GET.get('text_search')
        subject = self.request.GET.getlist('subject')
        label = self.request.GET.getlist('label')
        closed = self.request.GET.get('closed')
        date = self.request.GET.get('date')
        if text_search:
            qs = qs.annotate(
                search=Concat('title', Value(' '), 'description', Value(' '), 'subject', Value(' '), 'subtopic',
                              output_field=TextField())).filter(
                search__icontains=text_search)
        if subject and '' not in subject:
            qs = qs.filter(subject__in=subject)
        if label and '' not in label:
            qs = qs.filter(label__in=label)
        if closed:
            if closed == 'closed':
                qs = qs.filter(closed=True)
            elif closed == 'open':
                qs = qs.filter(closed=False)
        else:
            qs = qs.filter(closed=False)
        now = timezone.now().date()
        now = datetime.datetime(now.year, now.month, now.day)
        if date:
            if date == 'today':
                qs = qs.filter(action_date__gte=now, action_date__lt=now + datetime.timedelta(days=1))
            if date == 'tomorrow':
                qs = qs.filter(action_date__gte=now, action_date__lt=now + datetime.timedelta(days=2))
            if date == 'two_weeks':
                qs = qs.filter(action_date__gte=now, action_date__lt=now + datetime.timedelta(days=14))
            if date == 'thirty_days':
                qs = qs.filter(action_date__gte=now, action_date__lt=now + datetime.timedelta(days=30))
        else:
            qs = qs.filter(action_date__gte=now, action_date__lt=now + datetime.timedelta(days=1))
        return qs

    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        return ctx

class TaskDetailView(LoginRequiredMixin, DetailView):
    template_name = "core/task_detail.html"
    model = Task


@login_required
def pomodoro_add(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.pomodoro_count = task.pomodoro_count + 1
    task.save()
    pomodoro = Pomodoro(task=task, pomodoro_date=timezone.now(), pomodoro_count=1)
    pomodoro.save()
    data = {'task': task.id,
            'pomodoro': task.pomodoro_count
            }
    return JsonResponse(data, safe=False)


@login_required
def pomodoro_remove(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.pomodoro_count = task.pomodoro_count - 1
    task.save()
    pomodoro = Pomodoro(task=task, pomodoro_date=timezone.now(), pomodoro_count=-1)
    pomodoro.save()
    data = {'task': task.id,
            'pomodoro': task.pomodoro_count
            }
    return JsonResponse(data, safe=False)


@login_required
def task_date(request, pk):
    task = get_object_or_404(Task, pk=pk)
    date_time = parse_datetime(request.POST['date_time'])
    task.action_date = date_time
    task.save()
    date_time = task.action_date.strftime('%Y.%m.%d %H:%M')
    data = {'task': task.id,
            'date_time': date_time
            }
    return JsonResponse(data, safe=False)

@login_required
def task_closed(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task_closed = request.POST.get('task_closed')
    if task_closed==True or task_closed=='True' or task_closed=='true':
            task.closed = False
    elif task_closed==False or task_closed=='False' or task_closed=='false':
            task.closed = True
    task.save()
    data = {'task': task.id,
            'task_closed': task.closed
            }
    return JsonResponse(data, safe=False)


class ValueVisionMissionDetailView(DetailView):
    template_name = "core/value_vision_mission.html"
    model = ValueVisionMission

    def get_object(self):
        qs = ValueVisionMission.objects.filter(status=ValueVisionMission.ACTIVE).order_by('-publish_date').first()
        return qs


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date').select_related(
            'author').prefetch_related('comments')


class PostDetailView(DetailView):
    model = Post


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "core/post_new.html"
    form_class = PostForm

    def get_success_url(self):
        return reverse('core:post_detail', kwargs={'pk': self.object.pk})

    def get_initial(self):
        initial = super().get_initial()
        initial['author'] = self.request.user
        return initial


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "core/post_new.html"
    form_class = PostForm


class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'core/post_draft_list.html'

    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('core:post_list')


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('core:post_detail', pk=pk)


# @login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('core:post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'core/comment_form.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('core:post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('core:post_detail', pk=post_pk)


class PomodoroReportView(LoginRequiredMixin, ListView, FormView):
    template_name = "core/pomodoro_report.html"
    model = Pomodoro
    form_class = PomodoroReportSearchForm
    paginate_by = 20

    def get_initial(self):
        initial = super().get_initial()
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        initial['subject'] = self.request.GET.getlist('subject')
        initial['text_search'] = self.request.GET.get('text_search')
        if start_date and end_date:
            initial['start_date'] = start_date
            initial['end_date'] = end_date
        else:
            initial['end_date'] = timezone.now().date()+ datetime.timedelta(days=1)
            initial['start_date'] = timezone.now().date()
        return initial

    def get_queryset(self):
        qs=self.model.objects.all().select_related('task')
        text_search = self.request.GET.get('text_search')
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        subject = self.request.GET.getlist('subject')

        if text_search:
            qs = qs.annotate(
                search=Concat('task__title', Value(' '), 'task__description', Value(' ')  ,output_field=TextField())).filter(
                search__icontains=text_search)
        if subject and '' not in subject:
            qs = qs.prefetch_related('task__subject').filter(task__subject__in=subject)

        now = timezone.now().date()
        now = datetime.datetime(now.year, now.month, now.day)
        if start_date and end_date:
                start_date = parse_date(start_date)
                end_date = parse_date(end_date)
                qs = qs.filter(pomodoro_date__gte=start_date, pomodoro_date__lte=end_date)
        else:
                qs = qs.filter(pomodoro_date__gte=now, pomodoro_date__lt=now + datetime.timedelta(days=1))
        qs=qs.order_by('task__title')
        qs=qs.values('task__title','task').annotate(total_pomodoro=Sum('pomodoro_count'))
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        grand_total = 0
        for item_ in self.get_queryset():
            grand_total += item_.get('total_pomodoro')
        ctx['grand_total'] = grand_total
        return ctx

class DiaryListView(LoginRequiredMixin,ListView):
    model = Diary
    template_name = "core/diary_list.html"

    def get_queryset(self):
        return Diary.objects.filter(status=Diary.ACTIVE).order_by('-id')


class DiaryDetailView(LoginRequiredMixin,DetailView):
    model = Diary
    template_name = "core/diary_detail.html"