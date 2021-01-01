from onurbilgic import settings
from random import randint
from core.models import *
from django.forms import ModelForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, HTML, Div


class SubjectSearchForm(forms.Form):
    text_search = forms.CharField(
        label="Text", required=False,
    widget = forms.TextInput(

        attrs={
            'class': 'form-control', 'autocomplete': "off"
        },
    )
    )

    label= forms.ModelMultipleChoiceField(
        queryset=Label.objects.all(), required=False,
        label="Labels"
    )
    label.empty_label = 'All'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.fields['text_search'].widget.attrs['class'] = 'form-control'
        self.fields['label'].widget.attrs['class'] = 'form-control'
        self.fields['label'].widget.attrs['size'] = '6'
        self.helper.layout = Layout(
            Row(
                Column('text_search', css_class='form-group col-md-6 mb-0'),
                Column('label', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit',  "Search" )
        )

class SubtopicSearchForm(forms.Form):
    subject=forms.ModelMultipleChoiceField(
        queryset=Subject.objects.filter(status=Subject.ACTIVE), required=False,
        label="Subjects"
    )
    subject.empty_label = 'All'
    text_search = forms.CharField(
        label="Text", required=False,
    widget = forms.TextInput(

        attrs={
            'class': 'form-control', 'autocomplete': "off"
        },
    )
    )

    label= forms.ModelMultipleChoiceField(
        queryset=Label.objects.all(), required=False,
        label="Labels"
    )
    label.empty_label = 'All'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.fields['text_search'].widget.attrs['class'] = 'form-control'
        self.fields['label'].widget.attrs['class'] = 'form-control'
        self.fields['subject'].widget.attrs['class'] = 'form-control'
        self.fields['subject'].widget.attrs['size'] = '6'
        self.fields['label'].widget.attrs['size'] = '6'
        self.helper.layout = Layout(
            Row(
                Column('text_search', css_class='form-group col-md-4 mb-0'),
                Column('subject', css_class='form-group col-md-4 mb-0'),

                Column('label', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Submit('submit',  "Search" )
        )

class GoalSearchForm(forms.Form):
    subject=forms.ModelMultipleChoiceField(
        queryset=Subject.objects.filter(status=Subject.ACTIVE), required=False,
        label="Subjects"
    )
    subject.empty_label = 'All'
    subtopic=forms.ModelMultipleChoiceField(
        queryset=Subtopic.objects.filter(status=Subtopic.ACTIVE), required=False,
        label="Subtopics"
    )
    subtopic.empty_label = 'All'
    text_search = forms.CharField(
        label="Text", required=False,
    widget = forms.TextInput(

        attrs={
            'class': 'form-control', 'autocomplete': "off"
        },
    )
    )

    label= forms.ModelMultipleChoiceField(
        queryset=Label.objects.all(), required=False,
        label="Labels"
    )
    label.empty_label = 'All'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.fields['text_search'].widget.attrs['class'] = 'form-control'
        self.fields['label'].widget.attrs['class'] = 'form-control'
        self.fields['subject'].widget.attrs['class'] = 'form-control'
        self.fields['subject'].widget.attrs['size'] = '6'
        self.fields['subtopic'].widget.attrs['class'] = 'form-control'
        self.fields['subtopic'].widget.attrs['size'] = '6'
        self.fields['label'].widget.attrs['size'] = '6'
        self.helper.layout = Layout(
            Row(
                Column('text_search', css_class='form-group col-md-3 mb-0'),
                Column('subject', css_class='form-group col-md-3 mb-0'),
                Column('subtopic', css_class='form-group col-md-3 mb-0'),
                Column('label', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Submit('submit',  "Search" )
        )

class TaskSearchForm(forms.Form):
    subject=forms.ModelMultipleChoiceField(
        queryset=Subject.objects.filter(status=Subject.ACTIVE), required=False,
        label="Subjects"
    )
    subject.empty_label = 'All'

    text_search = forms.CharField(
        label="Text", required=False,
    widget = forms.TextInput(

        attrs={
            'class': 'form-control', 'autocomplete': "off"
        },
    )
    )
    date=forms.ChoiceField(label="Date",choices=(('all','All'),('today','Today'),('tomorrow','Tomorrow'),('two_weeks','2 Weeks'),('thirty_days','30 Days'),))
    closed=forms.ChoiceField(label="Closed",choices=(('all','All'),('closed','Closed'),('open','Not Closed'),))
    label= forms.ModelMultipleChoiceField(
        queryset=Label.objects.filter(status=Label.ACTIVE).order_by('name'), required=False,
        label="Labels"
    )
    label.empty_label = 'All'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.fields['text_search'].widget.attrs['class'] = 'form-control'
        self.fields['date'].widget.attrs['class'] = 'form-control'
        self.fields['closed'].widget.attrs['class'] = 'form-control'
        self.fields['text_search'].widget.attrs['class'] = 'form-control'
        self.fields['subject'].widget.attrs['class'] = 'form-control'
        self.fields['subject'].widget.attrs['size'] = '6'
        self.fields['label'].widget.attrs['class'] = 'form-control'
        self.fields['label'].widget.attrs['size'] = '6'

        self.helper.layout = Layout(
            Row(
                Column('text_search', css_class='form-group col-md-3 mb-0'),
                Column('date', css_class='form-group col-md-2 mb-0'),
                Column('label', css_class='form-group col-md-2 mb-0'),
                Column('subject', css_class='form-group col-md-3 mb-0'),
                Column('closed', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Submit('submit',  "Search" )
        )



class PostForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.fields['author'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.helper.layout = Layout(
            Row(
                Column('author', css_class='form-group col-md-6 mb-0'),
                Column('title', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('text', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', "Save", css_class='btn-success'),
            HTML("""<a class="btn btn-secondary" href="{{request.META.HTTP_REFERER}}">%s</a>""" % "Cancel")

        )

    class Meta:
        model = Post
        fields =('author','title', 'text',)




class CommentForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.fields['author'].widget.attrs['class'] = 'form-control'
        self.fields['text'].widget.attrs['class'] = 'form-control'
        self.helper.layout = Layout(
            Row(
                Column('author', css_class='form-group col-md-6 mb-1'),
                css_class='form-row'
            ),
            Row(
                Column('text', css_class='form-group col-md-12 mb-1'),
                css_class='form-row'
            ),
            Submit('submit', "Save", css_class='btn-success'),
            HTML("""<a class="btn btn-secondary" href="{{request.META.HTTP_REFERER}}">%s</a>""" % "Cancel")

        )

    class Meta:
        model = Comment
        fields =('author', 'text',)


    title = models.CharField(max_length=128)



class TaskCreateAndEditForm(ModelForm):
    subject= forms.ModelMultipleChoiceField(
        queryset=Subject.objects.filter(status=Subject.ACTIVE).order_by('name'), required=False,
        label="Subject"
    )
    subject.empty_label = 'All'
    subtopic= forms.ModelMultipleChoiceField(
        queryset=Subtopic.objects.filter(status=Subtopic.ACTIVE).order_by('name'), required=False,
        label="Subtopic"
    )
    goal= forms.ModelMultipleChoiceField(
        queryset=Goal.objects.filter(status=Goal.ACTIVE).order_by('name'), required=False,
        label="Goal"
    )
    goal.empty_label = 'All'
    label= forms.ModelMultipleChoiceField(
        queryset=Label.objects.filter(status=Label.ACTIVE).order_by('name'), required=False,
        label="Label"
    )
    label.empty_label = 'All'
    note= forms.ModelMultipleChoiceField(
        queryset=Note.objects.filter(status=Note.ACTIVE).order_by('title'), required=False,
        label="Note"
    )
    note.empty_label = 'All'
    action_date = forms.DateTimeField(
        label="Action Date",
        required=False,
        widget=forms.DateTimeInput(
            format=settings.DATE_TIME_FORMAT,
            attrs={
                'class': 'form-control dateTimeInput', 'autocomplete': "off"
            },
        )
    )
    due_date = forms.DateTimeField(
        label="Due Date",
        required=False,
        widget=forms.DateTimeInput(
            format=settings.DATE_TIME_FORMAT,
            attrs={
                'class': 'form-control dateTimeInput', 'autocomplete': "off"
            },
        )
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['subject'].widget.attrs['class'] = 'form-control'
        self.fields['subtopic'].widget.attrs['class'] = 'form-control'
        self.fields['goal'].widget.attrs['class'] = 'form-control'
        self.fields['label'].widget.attrs['class'] = 'form-control'
        self.fields['note'].widget.attrs['class'] = 'form-control'
        self.fields['points'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['subject'].widget.attrs['size'] = '8'
        self.fields['goal'].widget.attrs['size'] = '8'
        self.fields['subtopic'].widget.attrs['size'] = '8'
        self.fields['label'].widget.attrs['size'] = '8'
        self.fields['note'].widget.attrs['size'] = '8'
        self.helper.form_method = 'get'
        self.helper.layout = Layout(Div(
            Row(
                Column('title', css_class='form-group col-md-8 mb-0'),
                Column('action_date', css_class='form-group col-md-2 mb-0'),
                Column('due_date', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('subject', css_class='form-group col-md-4 mb-0'),
                Column('goal', css_class='form-group col-md-4 mb-0'),
                Column('subtopic', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('label', css_class='form-group col-md-4 mb-0'),
                Column('note', css_class='form-group col-md-5 mb-0'),
                Column('points', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('description', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', "Save", css_class='btn-success'),
            HTML("""<a class="btn btn-secondary" href="{{request.META.HTTP_REFERER}}">%s</a>""" % "Cancel")
                , style="display:block;overflow:auto", css_class="container  mt-2 mb-2")
        )

    class Meta:
        model = Task
        fields = ( "title","description","label","action_date","due_date",'subject','subtopic','goal','note','points')



class NoteCreateAndEditForm(ModelForm):
    subject= forms.ModelMultipleChoiceField(
        queryset=Subject.objects.filter(status=Subject.ACTIVE).order_by('name'), required=False,
        label="Subject"
    )
    subject.empty_label = 'None'
    subtopic= forms.ModelMultipleChoiceField(
        queryset=Subtopic.objects.filter(status=Subtopic.ACTIVE).order_by('name'), required=False,
        label="Subtopic"
    )
    subtopic.empty_label = 'None'
    goal= forms.ModelMultipleChoiceField(
        queryset=Goal.objects.filter(status=Goal.ACTIVE).order_by('name'), required=False,
        label="Goal"
    )
    goal.empty_label = 'None'
    label= forms.ModelMultipleChoiceField(
        queryset=Label.objects.filter(status=Label.ACTIVE).order_by('name'), required=False,
        label="Label"
    )
    label.empty_label = 'None'
    task= forms.ModelMultipleChoiceField(
        queryset=Task.objects.filter(status=Task.ACTIVE).order_by('-id'), required=False,
        label="Task"
    )
    task.empty_label = 'None'
    note_date = forms.DateTimeField(
        label="Note Date",
        required=False,
        widget=forms.DateTimeInput(
            format=settings.DATE_TIME_FORMAT,
            attrs={
                'class': 'form-control dateTimeInput', 'autocomplete': "off"
            },
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['subject'].widget.attrs['class'] = 'form-control'
        self.fields['subtopic'].widget.attrs['class'] = 'form-control'
        self.fields['goal'].widget.attrs['class'] = 'form-control'
        self.fields['label'].widget.attrs['class'] = 'form-control'
        self.fields['task'].widget.attrs['class'] = 'form-control'
        self.fields['text'].widget.attrs['class'] = 'form-control'
        self.fields['subject'].widget.attrs['size'] = '8'
        self.fields['goal'].widget.attrs['size'] = '8'
        self.fields['subtopic'].widget.attrs['size'] = '8'
        self.fields['label'].widget.attrs['size'] = '8'
        self.fields['task'].widget.attrs['size'] = '8'
        self.helper.form_method = 'get'
        self.helper.layout = Layout(Div(
            Row(
                Column('title', css_class='form-group col-md-9 mb-0'),
                Column('note_date', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('subject', css_class='form-group col-md-4 mb-0'),
                Column('goal', css_class='form-group col-md-4 mb-0'),
                Column('subtopic', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('label', css_class='form-group col-md-4 mb-0'),
                Column('task', css_class='form-group col-md-5 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('text', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', "Save", css_class='btn-success'),
            HTML("""<a class="btn btn-secondary" href="{{request.META.HTTP_REFERER}}">%s</a>""" % "Cancel")
                , style="display:block;overflow:auto", css_class="container  mt-2 mb-2")
        )

    class Meta:
        model = Note
        fields = ( "title","text","label","note_date",'subject','subtopic','goal','task')


class PomodoroReportSearchForm(forms.Form):

    text_search = forms.CharField(
        label="Text", required=False,
    widget = forms.TextInput(

        attrs={
            'class': 'form-control', 'autocomplete': "off"
        },
    )
    )
    start_date = forms.DateField(
        label="Start Date",
        required=False,
        widget=forms.DateInput(
            format=settings.DATE_FORMAT,
            attrs={
                'class': 'form-control dateInput', 'autocomplete': "off"
            },
        )
    )
    end_date = forms.DateField(
        label="End Date",
        required=False,
        widget=forms.DateInput(
            format=settings.DATE_FORMAT,
            attrs={
                'class': 'form-control dateInput', 'autocomplete': "off"
            },
        )
    )
    subject= forms.ModelMultipleChoiceField(
        queryset=Subject.objects.filter(status=Subject.ACTIVE).order_by('name'), required=False,
        label="Subject"
    )
    subject.empty_label = 'All'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.fields['subject'].widget.attrs['class'] = 'form-control'
        self.fields['text_search'].widget.attrs['class'] = 'form-control'
        self.fields['start_date'].widget.attrs['class'] = 'form-control'
        self.fields['end_date'].widget.attrs['class'] = 'form-control'
        self.helper.layout = Layout(
            Row(Column('text_search', css_class='form-group col-md-4 mb-0'),
                Column('subject', css_class='form-group col-md-4 mb-0'),
                Column('start_date', css_class='form-group col-md-2 mb-0'),
                Column('end_date', css_class='form-group col-md-2 mb-0'),
                css_class='form-row mb-1'
            ),
            Submit('submit',  "Search" )
        )
