from django.conf.urls import url
from django.urls import path, include
from .views import *

app_name='language'

urlpatterns = [
    path('flashcards/', FlashCardsView.as_view(), name='flashcards'),

]