from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(ContactMessage)
admin.site.register(DmAlert)
admin.site.register(DmBefore)
admin.site.register(DmAfter)
admin.site.register(satisfied)