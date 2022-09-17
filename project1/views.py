from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature 
from .models import Slider
from .models import AboutUs, Count_section, Executives, Ppdf
from .models import OfficersA
from .models import OfficersB, FAQ
from django.http import HttpResponse
from django.http import FileResponse
import io 
from .models import Social_link, Advertisements
from .models import GBIRCA, GBIRCB, AccountsA, AccountsB, SectionA, SectionB
from .models import Development 

#from reportlab.pdfgen import canvas
#from reportlab.lib.units import inch 
#from reportlab.lib.pagesizes import letter

# Create your views here.
def portfolio(request):
    executives = Executives.objects.all()
    officer_a = OfficersA.objects.all()
    officer_b = OfficersB.objects.all()
    gbirca = GBIRCA.objects.all()
    gbircab = GBIRCB.objects.all()
    accountsA = AccountsA.objects.all()
    accountsB = AccountsB.objects.all()
    sectiona = SectionA.objects.all()
    sectionb = SectionB.objects.all()
    

    return render(request, 'portfolio.html', {
                            'executives':executives, 
                            'officer_a':officer_a, 'officer_b':officer_b,
                            'gbirca':gbirca, 'gbircab':gbircab, 
                            'accountsA':accountsA, 'accountsB':accountsB, 
                            'sectiona':sectiona, 'sectionb':sectionb , 
                            })

def footer(request):
    social_media = Social_link.objects.all()
    return render(request, 'footer.html', {'social_media':social_media})

def latest(request):
    
    adver = Advertisements.objects.order_by('-uploaded')
    
    return render(request, 'latest.html', {'adver':adver})
    
def budget(request):
    pdf_files = Ppdf.objects.order_by('-uploaded')
    adp_files = Development.objects.order_by('-uploaded')
    
    return render(request, 'budget.html', {'pdf_files':pdf_files, 'adp_files':adp_files})

def navbar(request):
    return render(request, 'navbar.html', {})

def index(request):
    slide = Slider.objects.all()
    features = Feature.objects.all()
    aboutus = AboutUs.objects.all()
    counter = Count_section.objects.all()
    faq = FAQ.objects.all()

    return render(request, 'index.html', {'slide' : slide, 'features': features, 
        'aboutus': aboutus,'counter':counter,'faq':faq})
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used')
                return redirect('register')
            else: 
                user = User.objects.create_user(username= username, email=email, password=password)    
                user.save();
                return redirect('login')
        else: 
            messages.info(request, 'password not the same')
            return redirect('register')
    else:                    
        return render(request, 'register.html')
        

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        
        if user is not None: 
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect ('login')
    else:     
       return render (request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def counter(request):
    posts = [1, 2, 3, 4, 5, 'khan', 'kamal', 'hussain']
    return render(request, 'counter.html', {'posts':posts})  

def post(request, pk):

    return render(request, 'post.html', {'pk':pk})

#def post_pdf(request):
    #create byte stream buffer 
 #   buff = io.BytesIO()
    #create convas 
  #  c = canvas.Canvas(buff, pagesize=letter, bottomup=0)
    #create text object 
   # textob = c.beginText()
    #textob.setTextOrigin(inch, inch)
    #textob.setFont("Helvetica", 14)



     #some lines of text 
    #lines = [
     #  "this is line 1 ",
      #   "this is line 2 ",
       #   "this is line 3 ",
    #]
 #loop
    #for line in lines :
     #   textob.textLine(line)

# finish up 
    #c.drawText(textob)
    #c.showPage()
    #c.save()
    #buff.seek(0)
# return
    #return FileResponse(buff, as_attachment=True, filename='post.pdf')
