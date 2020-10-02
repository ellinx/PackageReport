from django.contrib import admin

from .models import PackageInfo, MailGroup, UserRight

admin.site.register(PackageInfo)
admin.site.register(MailGroup)
admin.site.register(UserRight)
