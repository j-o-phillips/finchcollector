from django.shortcuts import render, redirect
from .models import Finch, Hat
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .forms import FeedingForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# def finch_index(request):
#     finches = Finch.objects.all()
#     return render(request, 'finches/index.html', { 'finches': finches})

def finch_details(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    id_list = finch.hats.all().values_list('id')
    hats_finch_doesnt_have = Hat.objects.exclude(id__in=id_list)
    feeding_form = FeedingForm()
    return render(request, 'main_app/finch_detail.html', { 'finch': finch, 'feeding_form': feeding_form, 'hats': hats_finch_doesnt_have})

def add_feeding(request, finch_id):
  # create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST)
  # validate the form
    if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)

def assoc_hat(request, finch_id, hat_id):
    Finch.objects.get(id=finch_id).hats.add(hat_id)
    return redirect('detail', finch_id=finch_id)

def unassoc_hat(request, finch_id, hat_id):
    Finch.objects.get(id=finch_id).hats.remove(hat_id)
    return redirect('detail', finch_id=finch_id)



class FinchList(ListView):
    model = Finch

# class FinchDetail(DetailView):
#     model = Finch
    
class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['territory', 'description', 'color']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'

class HatList(ListView):
    model = Hat



class HatCreate(CreateView):
    model = Hat
    fields = '__all__'

class HatDetail(DetailView):
    model = Hat
    
class HatUpdate(UpdateView):
    model = Hat
    fields = ['name', 'color']

class HatDelete(DeleteView):
    model = Hat
    success_url = '/hats'



