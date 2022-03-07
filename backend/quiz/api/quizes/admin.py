'''
 display quiz app  models in the Django admin panel
'''
import datetime
from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext
from api.quizes.models import Quiz, AssignDeassignQuiz
# Register your models here.
admin.site.register(Quiz)


class AssignDeassignAdmin(admin.ModelAdmin):
    """
        A class to represent assign and deassign test in admin panel.

        ...

        actions : add option in action section of Assign Deassign Quiz

        list_display : contains fields which are displayed on the change list page of the admin.

        Methods
        -------
        assign_quiz(self, request, queryset):
            used to update the field when admin clicks on 'Assign Test' in admin panel.

        deassign_quiz(self, request, queryset):
            used to update the field when admin clicks on 'Deassign Test' in admin panel.
    """
    actions = ['assign_quiz', 'deassign_quiz']

    list_display = ('assign_deassign', 'topic', 'user',
                    'created', 'expired', 'is_attempted')

    # @admin.action(description='Assign Test')
    def assign_quiz(self, request, queryset):
        """
        update the field when admin clicks on 'Assign Test' in admin panel.

        Parameters
        ----------
        request : request object

        queryset : contains the objects

        """
        updated = queryset.update(assign_deassign=True, created=datetime.date.today(
        ), expired=datetime.date.today()+datetime.timedelta(days=10))
        self.message_user(request, ngettext(
            '%d assigned',
            '%d assigned',
            updated,
        ) % updated, messages.SUCCESS)

    # @admin.action(description='Deassign Test')
    def deassign_quiz(self, request, queryset):
        """
        update the field when admin clicks on 'Deassign Test' in admin panel.

        Parameters
        ----------
        request : request object

        queryset : contains the objects

        """
        updated = queryset.update(assign_deassign=False)
        self.message_user(request, ngettext(
            '%d deassign',
            '%d deassigned',
            updated,
        ) % updated, messages.SUCCESS)


admin.site.register(AssignDeassignQuiz, AssignDeassignAdmin)
