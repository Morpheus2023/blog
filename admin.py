from django.contrib import admin
from .models import Post
@admin.register(Post)
class postadmin(admin.ModelAdmin):
    list_display = ('title','author','publish','updated','status') #displays these fields alongwith list title
     
    list_filter = ('status','created','publish','author') #lets filter the posts according to these fields
     
    search_fields = ('title','body') #lets search posts
     
    prepopulated_fields = {'slug':('title',)} #the value of slug field is automatically filled alongwith the title field
    
   #raw_id_fields = ('author',) # let's you input author name wihout a toggle with a search bar instead(useful when you have thousands of user)
    
    date_hierarchy = 'publish' #specifies the default sorting criteria to the field:publish
     
    ordering = ('status','publish') #posts are ordered by status and publish
