from django import forms
from .models import Asset, Request, User

class AssetForm(forms.ModelForm):

    class Meta:
        model = Asset

        fields = ['asset_name', 'model', 'serial_no','category', 'asset_tag', 'status']

class RequestForm(forms.ModelForm):

    class Meta:
        model = Request
        fields = ['item', 'qty']


    
