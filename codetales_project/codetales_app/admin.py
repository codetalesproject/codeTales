from django.contrib import admin
from .models import Registration, Feedback, ListTrial, AdminRegistration
# Register your models here.
admin.site.register(Registration)
admin.site.register(Feedback)
admin.site.register(ListTrial)
admin.site.register(AdminRegistration)