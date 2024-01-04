from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from . import models 

class MoominmugListView(ListView): 
    model = models.Moominmug

class MoominmugDetailView(DetailView): 
    model = models.Moominmug

class MoominmugUpdateView(UpdateView):
	model = models.Moominmug
	fields = ["name", "officialName", "image", "count", "color", "figure", "theme"]
	success_url = "/moominmugs"

class MoominmugCreateView(CreateView):
	model = models.Moominmug
	fields = ["name", "officialName", "image", "count", "color", "figure", "theme"]
	success_url = "/moominmugs"

class MoominmugDeleteView(DeleteView):
	model = models.Moominmug
	success_url = "/moominmugs"
