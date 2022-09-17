from django.contrib import admin
from .models import Feature
from .models import Slider
from .models import AboutUs, Count_section, Executives
from .models import OfficersA, OfficersB, Ppdf, FAQ  
from .models import Social_link, Advertisements
from .models import GBIRCA, GBIRCB, AccountsA, AccountsB, SectionA, SectionB
from .models import Development

# Register your models here.

@admin.register(Feature) 
class FeatureAdmin(admin.ModelAdmin):
   list_display = ('name', 'details')
   list_filter = ('name',)
   ordering = ('-name',)
   search_fields = ('name',)

@admin.register(Advertisements)
class AdvertisementsAdmin(admin.ModelAdmin):
   list_display = ('title', 'detail', 'image', 'uploaded', 'pdf_ver')
   list_filter = ('title', 'uploaded')
   ordering = ('-title',)
   search_fields = ('title', 'uploaded')
@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
       
   list_display = ('title', 'created', 'post_image')
   list_filter = ('title', 'created')
   ordering = ('-created',)
   search_fields = ('title', 'created')

@admin.register(AboutUs)
class AboutUs(admin.ModelAdmin):
   list_display = ('title', 'created', 'points_detail1', 'points_detail2', 'points_detail3', 'points_detail4', 'points_detail5', 'points_detail6', 
   'points_detail7', 'points_detail8', 'right_side_paragraph')
  # list_filter = ('created')
   ordering = ('-title',)
   # search_fields = ('title')


@admin.register(Count_section)
class PSDPAdmin(admin.ModelAdmin):
   list_display = ('title', 'FY', 'total_no')
  # list_filter = ('title')
   ordering = ('-title',)
 #  search_fields = ('title') PSDP

@admin.register(Executives)
class PSDPAdmin(admin.ModelAdmin):
   list_display = ('title', 'created', 'image', 'video_url', 'top_paragraph', 'point1', 'point2', 'point3', 'point4', 'point4', 'summary')
  # list_filter = ('title')
   ordering = ('-title',)
 #  search_fields = ('title')
 
@admin.register(OfficersA)
class OfficersAAdmin(admin.ModelAdmin):
   list_display = ('title', 'shortparagraph')
  # list_filter = ('title')
   #ordering = ('-title',)
 #  search_fields = ('title')
 
@admin.register(OfficersB)
class OfficersBAdmin(admin.ModelAdmin):
   list_display = ('oficer_message', 'image', 'name_of_officer', 'designation','facebook', 'phone', 'twitter',)
  # list_filter = ('title')
   #ordering = ('-title',)
 #  search_fields = ('title')
 
@admin.register(Ppdf)
class PpdfAdmin(admin.ModelAdmin):
   list_display = ('title', 'uploaded', 'updated', 'upload_file',)
   list_filter = ('title',)
   ordering = ('-title',)
   search_fields = ('title',)
 
admin.site.register(FAQ)
admin.site.register(Social_link)
admin.site.register(GBIRCA)
admin.site.register(GBIRCB)
admin.site.register(AccountsA)
admin.site.register(AccountsB)
admin.site.register(SectionA)
admin.site.register(SectionB)
admin.site.register(Development)