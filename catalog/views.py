from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'catalog/home.html')

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        context = {
            'message_sent': True,
            'name': name,
        }
        return render(request, 'catalog/contacts.html', context)
    return render(request, 'catalog/contacts.html')