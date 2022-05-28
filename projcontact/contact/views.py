from django.shortcuts import redirect, render

from contact.models import Contact

def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        message = request.POST["desc"]
        cntct = Contact(name=name,phone=phone,email=email,message=message)
        cntct.save()
        return redirect("/")
    return render(request,"contact/contact.html")
    
