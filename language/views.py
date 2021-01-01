from django.shortcuts import render

from language.forms import FlashCardsForm
from .models import *
from django.views.generic import  DetailView, ListView, CreateView, DeleteView, UpdateView, FormView

# Create your views here.
class FlashCardsView( ListView, FormView):
    template_name = "language/flashcards.html"
    model = Word
    form_class = FlashCardsForm

    def get_initial(self):
        initial = super().get_initial()
        initial['language'] = self.request.GET.getlist('language')
        initial['category'] = self.request.GET.get('category')
        return initial

    def get_queryset(self):
        language =  self.request.GET.get('language')
        category =  self.request.GET.get('category')
        if language and category:
            return self.model.objects.filter(status='A',category_id=int(category)
                                           ,language_id=int(language)).select_related('category', 'language')
        else:
            return self.model.objects.none()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)


        ctx['js_list'] = self.get_queryset().values_list('id',flat=True)
        return ctx
