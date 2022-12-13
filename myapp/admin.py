from django.contrib import admin

from .models import *

admin.site.register(Site)
admin.site.register(MyUser)
admin.site.register(AccessKey)
admin.site.register(Avatar)
admin.site.register(Profile)
admin.site.register(Data)
admin.site.register(SecurityQuestion)
admin.site.register(Tag)
admin.site.register(Post)
