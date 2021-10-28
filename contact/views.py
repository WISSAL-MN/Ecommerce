from django.shortcuts import render

# Create your views here.
from contact.forms import ContactModelForm
from contact.models import Contact


def contact(request):
    form = ContactModelForm(request.POST)
    
    if request.method == "POST":
        form.save()
        form = ContactModelForm()
    else:
        form = ContactModelForm()

    context = {
        'contact_form': form
    }
    return render(request, 'contact/contact-us.html', context)

def contact_list(request):
    context = {
        'contact_list': Contact.objects.all()
    }
    render(request, 'contact/contact_list.html', context)
