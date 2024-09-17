from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.
CATEGORY = (
    ('Desktops', 'Desktops'),
    ('Laptops','Laptops'),
    ('Servers', 'Servers'),
    ('Network','Network'),
    ('UPS','UPS'),
    ('Audio/Visual', 'Audio/Visual'),

)
STATUS = (
    ('Working','Working'),
    ('Faulty','Faulty'),
    ('Obsolete','Obsolete'),
    ('Lost','Lost'),
    ('Disposed','Disposed'),
)
class Asset(models.Model):
    asset_name = models.CharField(max_length=100)
    model = models.CharField(max_length=50)
    serial_no = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=CATEGORY)
    asset_tag = models.CharField(max_length=50, null=True, blank=True)
    created_by = models.ForeignKey(User, models.CASCADE, null=True)
    status = models.CharField(max_length=50, choices=STATUS)
    issued = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.asset_name} {self.model} {self.serial_no}'

class Staff(models.Model):
     first_name = models.CharField(max_length=50)
     last_name = models.CharField(max_length=50)
     staff_no = models.CharField(max_length=50)

     def __str__(self):
        return f'{self.first_name} {self.last_name} '
     
class Request(models.Model):
    item = models.CharField(max_length=100)
    qty = models.IntegerField()
    order_by = models.ForeignKey(User, models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.item} - {self.qty} - {self.order_by}'


class Issue_Assets(models.Model):
    asset =  models.ForeignKey(Asset, on_delete=models.CASCADE, blank=True)
    issued_to = models.ForeignKey(Staff,on_delete=models.CASCADE,related_name='assets' )
    # issued_to = models.OneToOneField(Staff, on_delete=models.SET_NULL, null=True, blank=True, related_name='asset')
    issued_by = models.ForeignKey(User, models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    issued = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        issued_asset = Issue_Assets.objects.get(pk=self.pk)
        if issued_asset.issued_to.staff_no != self.issued_to.staff_no:
             raise ValidationError(f"The {self.asset} has already been issued to {self.issued_to}")
        super(Issue_Assets, self).save(*args, **kwargs)

    

    class Meta:
        verbose_name_plural = 'Issue an Asset'

    def __str__(self):
        return f'{self.asset} issued to {self.issued_to} '
    

