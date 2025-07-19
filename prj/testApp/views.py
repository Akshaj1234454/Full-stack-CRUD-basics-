from django.shortcuts import render, redirect
from .models import data

# Create your views here.
def dataApp(request):
    if request.method == 'POST':
        num = len(data.objects.all())
        
        name = request.POST.get('name')
        age = request.POST.get('age')
        contact = request.POST.get('contact')
        city = request.POST.get('city')

        data.objects.create(
            srNo = num+1,
            name = name,
            age = age,
            contact = contact,
            city = city,
        )

        return redirect("homePage")
    return render(request, 'testApp/testApp.html')


def scrollPage(request):
    query = request.GET.get('q')
    if query:
        entries = data.objects.filter(name__icontains=query)
    else:
        entries = data.objects.all()
    return render(request, 'testApp/scrollPage.html', {'entries': entries})


def editEntry(request, srNo):
    entry = data.objects.get(srNo=srNo)
    if request.method == 'POST':
        entry.name = request.POST.get('name')
        entry.age = request.POST.get('age')
        entry.contact = request.POST.get('contact')
        entry.city = request.POST.get('city')
        entry.save()
        return redirect("scrollPage")
    return render(request, 'testApp/editEntry.html', {'entry':entry})

    