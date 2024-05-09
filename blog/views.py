from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from .forms import ContactForm
from .bot import send_message
from django.urls import reverse  # new

from .models import Article,Contact

# -----------------------------------------------------------------------------------------------------------------

# def home_view(request):
    
#     if request.method == "GET":
#         form  = ContactForm()
#     else:
#         contact = Contact.objects.all()
#         form = ContactForm(request.POST)
#     if form.is_valid():
#         name = form.cleaned_data["name"]
#         email = form.cleaned_data["email"]
        
#         phone_number = form.cleaned_data["phone_number"]
#         description = form.cleaned_data["description"]
#         contact=contact

#         send_message(name,email,phone_number,description)
        
#         form.save()
#         form = ContactForm()
        
#     context = {"form":form}


#     return render(request, "theme-particle.html",context)










def contact_view(request):

    if request.method == "GET":
        form = ContactForm()
    else:
        # contact = Contact.objects.all()
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            phone_number = form.cleaned_data["phone_number"]
            description = form.cleaned_data["description"]

            send_message(name,email,phone_number,description)
            form.save()
            form = ContactForm()
            messages.success(request, '🥳 Murojatingiz adminga yuborildi...')
            return HttpResponseRedirect(reverse('home-page'))
        else:
            messages.error(request, 'Formani qaytadan to\'ldiring')

    context = {"forms":form}

    return render(request, "theme-particle.html",context)

# # # --------------------------------------------------------------------------------------------------------------------



def home_view(request):
    articles = Article.objects.all().order_by("-id")
    context = {"articles":articles}
    return render(request,"theme-particle.html",context)
