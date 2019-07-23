from django.shortcuts import render
from gestpermis.models import CapitalPoint,Categorie,Candidat
from gestpermis.forms import CandidatForm
# Create your views here.


def consulersolde(request):
    solde = CapitalPoint.objects.all()
    context = {
        'solde':solde
    }
    return render(request,'gestpermis/solde.html',context)


def stage(request):
    return render(request,'gestpermis/stage.html')


def candidat(request):
    user = User.objects.get(pk=pk)
    form = CandidatForm()
    if request.method == 'POST':
        form = CandidatForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            #if data['password'] == data['password_confirm']:
                #print(data)
            new_candidat = Candidat(
                data_burth= data['date'],
                lieu_burth= data['lieu'],
            )
            new_candidat.save()
            return redirect('article:home')
    context = {
        'form':form,
        'user':user
    }
    return render(request,'gestpermis/candidat.html',context)

   