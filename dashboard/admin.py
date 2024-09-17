from django.contrib import admin
from .models import Asset, Staff, Issue_Assets, Request


admin.site.site_header = "ICT Assets Management Dashboard"
class AssetAdmin(admin.ModelAdmin):
    list_display = ('asset_name', 'model','serial_no','category','asset_tag', 'created_by')
    list_filter = ['category']
# Register your models here.

admin.site.register(Asset,AssetAdmin)

class StaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','staff_no')
   

admin.site.register(Staff,StaffAdmin)

class IssueAdmin(admin.ModelAdmin):
    list_display = ('asset', 'issued_to', 'issued_by','date')
    list_filter = ['issued_to']

admin.site.register(Issue_Assets,IssueAdmin)

admin.site.register(Request)

