from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, FormView, UpdateView, CreateView

# Create your views here.
class CreateCommentView(LoginRequiredMixin, CreateView):
    pass