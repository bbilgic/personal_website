from django.conf.urls import url
from django.urls import path, include
from .views import *

app_name='core'

urlpatterns = [
    path('subject-list/', SubjectListView.as_view(), name='subject_list'),
    path('subject/<int:pk>/detail/', SubjectDetailView.as_view(), name='subject_detail'),
    path('subtopic-list/', SubtopicListView.as_view(), name='subtopic_list'),
    path('subtopic/<int:pk>/detail/', SubtopicDetailView.as_view(), name='subtopic_detail'),
    path('goal-list/', GoalListView.as_view(), name='goal_list'),
    path('goal/<int:pk>/detail/', GoalDetailView.as_view(), name='goal_detail'),
    path('note/new/', NoteCreateView.as_view(), name='note_new'),
    path('note/<int:pk>/update/', NoteUpdateView.as_view(), name='note_update'),
    path('note/<int:pk>/delete/', NoteDeleteView.as_view(), name='note_delete'),
    path('note-list/', NoteListView.as_view(), name='note_list'),
    path('note/<int:pk>/detail/', NoteDetailView.as_view(), name='note_detail'),
    path('task/new/', TaskCreateView.as_view(), name='task_new'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('task/<int:pk>/copy/', TaskCopyView.as_view(), name='task_copy'),
    path('task-list/', TaskListView.as_view(), name='task_list'),
    path('task/<int:pk>/detail/',TaskDetailView.as_view(), name='task_detail'),
    path('pomodoro-add/<int:pk>', pomodoro_add, name='pomodoro_add'),
    path('pomodoro-remove/<int:pk>', pomodoro_remove, name='pomodoro_remove'),
    path('task-date/<int:pk>', task_date, name='task_date'),
    path('task-closed/<int:pk>', task_closed, name='task_closed'),
    path('value-vision-mission/', ValueVisionMissionDetailView.as_view(), name='value_vision_mission'),
    url(r'^post/$', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/detail/', PostDetailView.as_view(), name='post_detail'),
    url(r'^post/new/$', CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_edit'),
    url(r'^drafts/$', DraftListView.as_view(), name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/remove/$', PostDeleteView.as_view(), name='post_remove'),
    url(r'^post/(?P<pk>\d+)/publish/$', post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/comment/$', add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', comment_remove, name='comment_remove'),
    path('pomodoro-report/', PomodoroReportView.as_view(), name='pomodoro_report'),
    url(r'^diary/$', DiaryListView.as_view(), name='diary_list'),
    path('diary/<int:pk>/detail/', DiaryDetailView.as_view(), name='diary_detail'),
]