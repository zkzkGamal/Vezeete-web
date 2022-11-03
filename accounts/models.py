from secrets import choice
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

gender = (
    ('M',"Male") , 
    ('F',"Female")
)

class Profile(models.Model):
    doctor_in = {
        ('tooth',"tooth") , 
        ('skin',"skin"),
        ('heart',"hreat") , 
        ('nose and ear',"nose and ear")
    }
    
    user = models.OneToOneField(User,verbose_name = _("user"),on_delete = models.CASCADE, blank = True , null = True)
    name = models.CharField(_("name"),max_length = 35)
    subtitle = models.CharField(_("about you"),max_length = 50,blank = True , null = True)
    address = models.CharField(_("adress"),max_length = 50)
    phone = models.CharField(_("phone number"),max_length = 11,default = '01*********')
    working_hour = models.CharField(_("working hour"),max_length = 2 , default = '6')
    who_I = models.TextField(_("about-me"),max_length = 250 , blank = True , null = True)
    specialist = models.CharField(_("doctor at"),choices = doctor_in,max_length = 20, blank = True , null = True)
    price = models.IntegerField(_("price"),default = 100)
    image = models.ImageField(_("photo"),upload_to = 'profile' , blank = True , null = True)
    slug = models.SlugField(_("slug"),null = True , blank = True)
    facebook = models.CharField(max_length = 100 , blank = True , null = True)
    google = models.CharField(max_length = 100 , blank = True , null = True)
    twitter = models.CharField(max_length = 100 , blank = True , null = True)
    active = models.BooleanField(default = True)
    created = models.DateTimeField(default = datetime.now, blank = True , null = True)
    Type = models.CharField(_("gender"),choices =gender,max_length = 10)
    
        
    def __str__(self): 
        return '%s' %(self.user.username)
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Profile,self).save(*args,**kwargs)
    
    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'
        
def createPorfile(sender , **kwargs):
    if kwargs['created']:
        Profile.objects.create(user = kwargs['instance'])

post_save.connect(createPorfile,sender = User)
