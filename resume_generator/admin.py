from django.contrib import admin

from resume_generator.models import *


from .forms import *


# Register your models here.
admin.site.register(Header)
admin.site.register(Body)
