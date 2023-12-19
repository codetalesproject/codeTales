from django.contrib import admin
from .models import Registration, Feedback, AdminRegistration
from .models import CChallenge, CPuzzle, CStory,PyChallenge,PyPuzzle,PyStory
# Register your models here.
admin.site.register(Registration)
admin.site.register(Feedback)
admin.site.register(AdminRegistration)
admin.site.register(CChallenge)
admin.site.register(CStory)
admin.site.register(CPuzzle)
admin.site.register(PyChallenge)
admin.site.register(PyStory)
admin.site.register(PyPuzzle)