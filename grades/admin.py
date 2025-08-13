from django.contrib import admin
from django import forms
from .models import Subject, Grade
from django.contrib.auth import get_user_model

User = get_user_model()


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student'].queryset = User.objects.filter(role='user')


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    form = GradeForm
    list_display = ('student', 'subject', 'grade', 'date')
    list_filter = ('subject', 'date')
    search_fields = ('student__username', 'subject__name')

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
