from django.shortcuts import render
from tijdschrijven.models import Project,Persoon,Abonnement
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import tijdschrijfForm
# Create your views here.

def index(request):
    """View function for home page of site."""
    return render(request, 'index.html')


def projecten(request):
   projecten = Project.objects.all()
   context = {'projecten': projecten,}
   # Render the HTML template index.html with the data in the context variable
   return render(request, 'projecten.html', context=context)


class ProjectCreate(CreateView):
    model = Project
    fields=['Titel', 'ProjectTemplateID', 'Omschrijving', 'ParentID', 'AanmakerID', 'GeldigVan', 'GeldigTot', 'Actief']
    success_url = reverse_lazy('projecten')


class ProjectUpdate(UpdateView):
    model = Project
    fields=['Titel', 'ProjectTemplateID', 'Omschrijving', 'ParentID', 'AanmakerID', 'GeldigVan', 'GeldigTot', 'Actief']
    success_url = reverse_lazy('projecten')


class ProjectDelete(DeleteView):
    model = Project
    success_url = reverse_lazy('projecten')


def abonnementen(request):
    abonnementen = Abonnement.objects.all()
    context = {'abonnementen': abonnementen,}
    return render(request,'abonnement.html', context=context)


class AbonnementCreate(CreateView):
    model = Abonnement
    fields=['PersoonID', 'ProjectID','OriginalObjectID']
    success_url = reverse_lazy('abonnementen')


def urenschrijven(request):

    if request.method == 'POST':
    
        form = tijdschrijfForm(request.POST)
        
        test = form['testvak']
        #if form.is_valid():

    else:
        test=1

    context = {'abonnementen': Abonnement.objects.all(),
               'dagenindeweek':['ma','di','wo','do','vr','za','zo'],
               'wekenperjaar': 52,
               'test':test}

    return render(request,'urenschrijven.html',context=context)