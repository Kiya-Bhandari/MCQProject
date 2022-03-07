'''
 display questions app  models in the Django admin panel
'''
from django.contrib import admin
from django.forms import forms
from django.urls import path
from django.shortcuts import render
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponseRedirect
import pandas as pd
from api.quizes.models import Quiz
from .models import Question, Answer


# Register your models here.


class CsvImportForm(forms.Form):
    """
        A class to represent Csv file.

        ...

        Attributes
        ----------
        csv_upload : File
            used to upload csv file

    """
    csv_upload = forms.FileField()


class AnswerInLine(admin.TabularInline):
    """
        A class to represent Answer in tabular form

    """
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    """
        A class to represent Questions in admin panel.

        ...

        inlines : displays options in tabular form below question

        Methods
        -------
        upload_csv(self, request):
            stores the result in respective tables.
    """
    inlines = [AnswerInLine]

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv), ]
        return new_urls + urls

    def upload_csv(self, request):
        """
        stores the result in respective tables.

        Parameters
        ----------
        request : request object which contains csv file uploaded by admin

        """
        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]

            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)

            data = pd.read_csv(csv_file)
            for index, row in data.iterrows():
                correct_answer = row['correct answer']

                Question.objects.update_or_create(
                    text=row['questions'],
                    quiz=Quiz.objects.get(Q(topic=row['topic']) & Q(
                        difficulty=row['difficulty level'])),
                    marks=row['marks']
                )

                if row['A'] is not None:

                    Answer.objects.update_or_create(
                        text=row['A'],
                        correct=True if (r"row['A']".replace(
                            "row['", "").replace("']", "") == correct_answer) else False,
                        question=Question.objects.get(text=row['questions']),

                    )

                if row['B'] is not None:

                    Answer.objects.update_or_create(
                        text=row['B'],
                        correct=True if (r"row['B']".replace(
                            "row['", "").replace("']", "") == correct_answer) else False,
                        question=Question.objects.get(text=row['questions']),

                    )

                if row['C'] is not None:

                    Answer.objects.update_or_create(
                        text=row['C'],
                        correct=True if (r"row['C']".replace(
                            "row['", "").replace("']", "") == correct_answer) else False,
                        question=Question.objects.get(text=row['questions']),

                    )

                if row['D'] is not None:

                    Answer.objects.update_or_create(
                        text=row['D'],
                        correct=True if (r"row['A']".replace(
                            "row['", "").replace("']", "") == correct_answer) else False,
                        question=Question.objects.get(text=row['questions']),

                    )

        form = CsvImportForm()
        data = {"form": form}

        return render(request, "admin/csv_upload.html", data)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
