from django.shortcuts import render, HttpResponse, HttpResponsePermanentRedirect
from .models import Tickers

# Create your views here.
def index(request):
    tickers = Tickers.objects.all()  
    return render(request, "home/index.html", {
        'tickers': tickers 
    })

def under(request):
    return render(request, 'home/under.html')

def submit(request):
    if request.method == "POST":
        try:
            name = request.POST['name']
            mail = request.POST['mail']
            suggestion = request.POST['suggestion']

            name = name.strip().lower()
            mail = mail.strip().lower()
            suggestion = suggestion.strip()

            new_entry = Student(
                name = name,
                mail = mail,
                suggestion = suggestion
            )

            new_entry.save()
            return render(request, "home/thanks.html")
        except():
            return HttpResponse('Please go back and enter valid details..!')
    return HttpResponse('Please go back and enter valid details..!')
        
    
def signin(request):
    return render(request, "home/signin.html")

def signup(request):
    return render(request, "home/signup.html")

def profile(request):
    return render(request, 'home/profile.html')
    
def details(request, id):
    item = Tickers.objects.get(id = id)

    return render(request, 'home/details.html', {
        'item': item
    })