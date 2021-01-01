from language.models import *
from onurbilgic import settings
from random import randint
from core.models import *
from django.forms import ModelForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, HTML, Div



class FlashCardsForm(forms.Form):

    category=forms.ModelChoiceField(
        queryset=Category.objects.filter(status=Subject.ACTIVE).order_by('name'), required=False,
        label="Category"
    )
    category.empty_label = '------'
    language=forms.ModelChoiceField(
        queryset=Language.objects.filter(status=Subject.ACTIVE), required=False,
        label="Language"
    )
    category.empty_label = '------'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.fields['category'].widget.attrs['class'] = 'form-control'
        self.fields['language'].widget.attrs['class'] = 'form-control'
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Row(
                Column('language', css_class='form-group col-sm-2 mb-0'),
                Column('category', css_class='form-group col-sm-2  mb-0'),
                Column(Row(
                    Column(Submit('submit',  "Get" ,css_class="mt-2" ),css_class='col-4  mt-4' ),
                    Column( HTML('<button type="button" id="start-learning" class="btn btn-success mt-2">Start</button>'),css_class='col-4 mt-4' )
                    , css_class='form-row'  ) , css_class='col-6  mb-0')
                , css_class='form-row'
                ) ,
            )

