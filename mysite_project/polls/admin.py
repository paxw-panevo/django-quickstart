from django.contrib import admin

from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice

    # This means to provide 3 "Choice" fields by default (i.e. creating);
    # or 3 extra fields when changing a model that has this class "inline"
    # in their form (e.g. editing a question will have 3 "extra" Choice fields
    # on top of itsexisting choices)
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ['question_text', 'pub_date', 'was_published_recently']
    list_filter = ['pub_date']

    # This uses a LIKE query behind the scenes, limiting the number of search
    # fields to a reasonable number will make it easier for your database to
    # do the search.
    # https://docs.djangoproject.com/en/3.2/intro/tutorial07/
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
