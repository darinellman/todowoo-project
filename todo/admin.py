from django.contrib import admin
from .models import Todo

#this is so that the created field in the Todo model shows up in the admin interface
#but does not allow for editing - the "TodoAdmin()" name is not special and it can
#be anythng - however the class name must also be included in the registration below

class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


# Register your models here.
admin.site.register(Todo, TodoAdmin)
