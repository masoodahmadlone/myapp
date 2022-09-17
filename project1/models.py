from django.db import models
from datetime import datetime


# Create your models here.
class FAQ(models.Model):
    title_q = models.CharField(max_length=300)
    ans_q = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)

class Slider(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, null=True)
    post_image = models.FileField(blank=True, upload_to="images/")


class Feature (models.Model):
    name = models.CharField(max_length=250) 
    details = models.TextField(max_length=500)

class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)

class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, null=True)
    detial = models.CharField(max_length=1000000, null=True)
    points_detail1 = models.TextField(max_length=300, blank=True)
    points_detail2 = models.TextField(max_length=300, blank=True)
    points_detail3 = models.TextField(max_length=300, blank=True)
    points_detail4 = models.TextField(max_length=300, blank=True)
    points_detail5 = models.TextField(max_length=300, blank=True)
    points_detail6 = models.TextField(max_length=300, blank=True)
    points_detail7 = models.TextField(max_length=300, blank=True)
    points_detail8 = models.TextField(max_length=300, blank=True)
    right_side_paragraph = models.TextField(max_length=10000, blank=True)
    
class Count_section(models.Model):
    title = models.CharField(max_length=100, blank=True)
    FY =  models.CharField(max_length=100)
    total_no = models.CharField(max_length=100)

class Executives(models.Model):
    title = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    image = models.FileField(upload_to='images/', blank=True)
    video_url = models.URLField(blank=True,null=True)
    top_paragraph = models.TextField(blank=True)
    point1 = models.CharField(max_length=300, blank=True)
    point2 = models.CharField(max_length=300, blank=True)
    point3 = models.CharField(max_length=300, blank=True)
    point4 = models.CharField(max_length=300, blank=True) 
    point5 = models.CharField(max_length=300, blank=True)
    summary = models.CharField(max_length=1000, blank=True)

class OfficersA(models.Model):
    title = models.CharField(max_length=250, blank=True)
    shortparagraph = models.TextField(max_length=1000, blank=True)

class OfficersB(models.Model):
    oficer_message = models.TextField(max_length=300, blank=True)
    image = models.ImageField(upload_to='images/')
    name_of_officer = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    facebook = models.URLField(max_length=250, blank=True)
    phone = models.CharField(max_length=150, blank=True )
    twitter = models.URLField(blank=True)
    models.URLField(blank=True)

class GBIRCA(models.Model):
    title = models.CharField(max_length=250, blank=True)
    shortparagraph = models.TextField(max_length=1000, blank=True)

class GBIRCB(models.Model):
    oficer_message = models.TextField(max_length = 300, blank=True)
    image = models.ImageField(upload_to='images/')
    name_of_officer = models.CharField(max_length = 50)
    designation = models.CharField(max_length = 50)
    facebook = models.URLField(max_length=250)
    phone = models.CharField(max_length=100)
    twitter = models.URLField(blank=True)

class AccountsA(models.Model):
    title = models.CharField(max_length=250, blank=True)
    shortparagraph = models.TextField(max_length=1000, blank=True)

class AccountsB(models.Model):
    oficer_message = models.TextField(max_length = 300, blank=True)
    image = models.ImageField(upload_to='images/')
    name_of_officer = models.CharField(max_length = 50)
    designation = models.CharField(max_length = 50)
    facebook = models.URLField(max_length=250)
    phone = models.CharField(max_length=100)
    twitter = models.URLField(blank=True)    

class SectionA(models.Model):
    title = models.CharField(max_length=250, blank=True)
    shortparagraph = models.TextField(max_length=1000, blank=True)

class SectionB(models.Model):
    oficer_message = models.TextField(max_length = 300, blank=True)
    image = models.ImageField(upload_to='images/')
    name_of_officer = models.CharField(max_length = 50)
    designation = models.CharField(max_length = 50)
    facebook = models.URLField(max_length=250)
    phone = models.CharField(max_length=100)
    twitter = models.URLField(blank=True)
    
class Ppdf(models.Model):
    title = models.CharField(max_length=200)
    uploaded = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    upload_file = models.FileField(blank=True, upload_to="pdf/")

class Social_link(models.Model):
    facebook = models.URLField(blank=True, help_text="facebook link")
    twitter = models.URLField(blank=True, help_text="twitter link")
    phone = models.CharField(max_length=100, blank=True, help_text='Contact phone number')
    instagram = models.URLField(blank=True, help_text="Intagram link")
    skype = models.URLField(blank=True, help_text="skype number")

class Advertisements(models.Model):
    title = models.CharField(max_length=250)
    detail = models.CharField(max_length=250)
    image = models.ImageField(blank=True, upload_to="images/")
    uploaded = models.DateTimeField(auto_now_add=True, null=True)
    pdf_ver = models.FileField(blank=True, upload_to="pdf/")    

class Development(models.Model):
    title = models.CharField(max_length=250)
    detail = models.CharField(max_length=250, blank=True)
    image = models.ImageField(blank=True, upload_to="images/")
    uploaded = models.DateTimeField(auto_now_add=True, null=True)
    pdf_file = models.FileField(blank=True, upload_to="pdf/")    


