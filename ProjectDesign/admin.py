from django.contrib import admin
from .models import (Home,
                     About,
                     Intrest,
                     Project,
                     Certificate
                     )


admin.site.register(Home)
admin.site.register(About)
admin.site.register(Intrest)
admin.site.register(Project)
admin.site.register(Certificate)
