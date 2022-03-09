from django.contrib import admin

from .models import Choice, Question

class ChoiceInline(admin.StackedInline):
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

admin.site.register(Question, QuestionAdmin)
