from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.


def second(request):
    if request.method=='POST':
        topic=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=topic)[0]
        TO.save()
        #return HttpResponse('Topic uploaded successfully')
    return render(request,'second.html')



def third(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}
    if request.method=='POST':
        topic=request.POST['topic']
        name=request.POST.get('name')
        url=request.POST.get('url')
        email=request.POST['email']
        TO=Topic.objects.get(topic_name=topic)
        

        WP=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url,email=email)[0]
        WP.save()
    return render(request,'third.html',d)



def access(request):
    LWO=Webpage.objects.all()
    d={'webpage':LWO}
    if request.method=='POST':
        name=request.POST['name']
        author=request.POST.get('author')
        date=request.POST['date']
        WP=Webpage.objects.get(name=name)

        AR=AccessRecords.objects.get_or_create(name=WP,author=author,date=date)[0]
        AR.save()
    return render(request,'access.html',d)