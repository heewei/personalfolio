from django.shortcuts import render

# Create your views here.
def heelloo(request):
    return render(request, "hellohtml.html", {})
