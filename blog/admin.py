from django.contrib import admin

#Hérnaer ég að sækja Blog Class úr models og skrá hann inn í admin
from .models import Blog

#Hérna er ég að registera þetta inn í admin
admin.site.register(Blog)
# Register your models here.
# Register your models here.
