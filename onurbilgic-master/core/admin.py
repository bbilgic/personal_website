from django.contrib import admin
from core.models import *

# Register your models here.


admin.site.register(Label)
admin.site.register(Subject)
admin.site.register(Subtopic)
admin.site.register(Goal)

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id','title','closed','created_date','action_date' ,'due_date','status']
    list_filter = [ 'closed','status','action_date','due_date']
    list_editable = ['closed']
    search_fields = ['title','description']
    ordering = ['due_date']
    readonly_fields = ('id',)


admin.site.register(Task,TaskAdmin)
admin.site.register(HomePage)
admin.site.register(AboutPage)
admin.site.register(Note)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(ValueVisionMission)
admin.site.register(Diary)



class PomodoroAdmin(admin.ModelAdmin):
    list_display = ['id','task','pomodoro_date','pomodoro_count']
    search_fields = ['task__name']
    list_filter = ['pomodoro_date']
    ordering = ['pomodoro_date']
    readonly_fields = ('id',)

admin.site.register(Pomodoro,PomodoroAdmin)