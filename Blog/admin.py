from django.contrib import admin
from .models import Posts
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','content','dated_post','auther')


admin.site.register(Posts,PostAdmin)