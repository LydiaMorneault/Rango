from django.contrib import admin
from rango.models import Category, Page, Question


# Register your models here.
admin.site.register(Category)

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

class PageAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "url"]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Page, PageAdmin)


