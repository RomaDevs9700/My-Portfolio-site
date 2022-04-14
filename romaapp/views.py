from django.shortcuts import render, redirect

from .forms import ContactForm
from .models import Contact, Home, About, Category, Portfolio, Profile

# Create your views here.
def index(request):
    if request.method == "GET":
        # HOME
        home = Home.objects.latest('updated')

        # ABOUT
        about = About.objects.latest('updated')
        profiles = Profile.objects.filter(about=about)

        # SKILLS
        categories = Category.objects.all()

        # PORTFOLIO
        portfolios = Portfolio.objects.all()

        # CONTACT
        form = ContactForm() 

        context = {
            'home': home,
            'about': about,
            'profiles': profiles,
            'categories': categories,
            'portfolios': portfolios,
            'form': form
        }

        return render(request, 'index.html', context)
    
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Contact.objects.create(
                name=data["name"],
                email=data["email"],
                review=data["review"]
            )
            return redirect("index")

    return render(request, "index.html", form)

        # def post(self, request):
        #     form = ContactForm(request.POST)
        #     print(type(form))
        #     print(form)

        #     if form.is_valid():
        #         data = form.cleaned_data
        #         print(data)
        #         print(type(data))
        #         Contact.objects.create(
        #             name=data["name"],
        #             email=data["email"],
        #             review=data["review"]
        #         )
        #         return redirect("main")
        #     else:
        #         print("error: Invalid")
        #     return render(request, "index.html", {
        #         'form': form,
        #     })


# from django.shortcuts import render, redirect

# from django.views.generic import View
# from django.urls import reverse_lazy

# from .models import Contact, Home, About, Category, Portfolio, Profile
# from .forms import ContactForm

# # Create your views here.
# class MainView(View):
#     def get(self, request):

#         # HOME
#         home = Home.objects.get('updated')

#         # ABOUT
#         about = About.objects.get('updated')
#         profiles = Profile.objects.filter(about=about)

#         # SKILLS
#         categories = Category.objects.all()

#         # PORTFOLIO
#         portfolios = Portfolio.objects.all()

#         # CONTACT
#         contact = Contact.objects.filter(check_display='False') 

#         return render(request, 'index.html', {
#             'home': home, 'about': about, 'profiles': profiles, 'categories': categories,
#             'portfolios': portfolios, 'contact': contact})
            

#         def post(self, request):
#             form = ContactForm(request.POST)
#             print(type(form))
#             print(form)

#             if form.is_valid():
#                 data = form.cleaned_data
#                 print(data)
#                 print(type(data))
#                 Contact.objects.create(
#                     name=data["name"],
#                     email=data["email"],
#                     review=data["review"]
#                 )
#                 return redirect("main")
#             else:
#                 print("error: Invalid")
#             return render(request, "index.html", {
#                 'form': form,
#             })

#         # context = {
#         #     'home': home,
#         #     'about': about,
#         #     'profiles': profiles,
#         #     'categories': categories,
#         #     'portfolios': portfolios
#         # }

        # return render(request, 'index.html', context)
       