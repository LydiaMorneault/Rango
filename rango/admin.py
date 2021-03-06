from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

class PageAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "url"]

# Customizes the admin interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

# Update registration to include this customised interface
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)


