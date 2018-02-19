from django.contrib import admin
from .models import Post
from mce_filebrowser.admin import MCEFilebrowserAdmin
# Register your models here.

class MyModelAdmin(MCEFilebrowserAdmin):
    pass

admin.site.register(Post, MyModelAdmin)
