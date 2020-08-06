from django.contrib import admin

from .models import Question, choice

# admin.site.s

# admin.site.site_titile = "Arms Pollster Admin Area"
# admin.site.index_titile = "Welcome to the Arms Pollster Admin Area"



class ChoiceInline(admin.TabularInline):
    model = choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
    ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),]
    inlines = [ChoiceInline]



# admin.site.register(Question)
# admin.site.register(choice)

admin.site.register(Question, QuestionAdmin)
