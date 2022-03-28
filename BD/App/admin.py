from django.contrib import admin
from .models import RegistrationData, User, Friends, UserFhoto, UserDialog, Dialog, Message, PhotoInMessage


admin.site.register(RegistrationData)
admin.site.register(User)
admin.site.register(Friends)
admin.site.register(UserFhoto)
admin.site.register(UserDialog)
admin.site.register(Dialog)
admin.site.register(Message)
admin.site.register(PhotoInMessage)


# Register your models here.
