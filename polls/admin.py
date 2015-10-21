from django.contrib import admin

from .models import Question, Choice
# Register your models here.


class ChoiceInline(admin.TabularInline):
	#TabularInline or StackedInline
	model = Choice
	extra = 3






class QuestionAdmin(admin.ModelAdmin):
	list_display = ['question_text','pub_date', 'was_published_recently' ]
	#fields = ['pub_date', 'question_text']  # change to fieldsets
	fieldsets = [
	    (None, {'fields':['question_text']}),
	    ('Date Information', {'fields':['pub_date'], 'classes':['collapse']}),
	]

	inlines = [ChoiceInline]





admin.site.register( Question, QuestionAdmin )
#admin.site.register( Choice )