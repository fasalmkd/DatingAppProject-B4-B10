from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from.models import User,Interest,Habbit,Hobbies,Qualification,Location


admin.site.register(User,UserAdmin)

admin.site.register(Interest)
admin.site.register(Habbit)
admin.site.register(Hobbies)
admin.site.register(Qualification)
admin.site.register(Location)



