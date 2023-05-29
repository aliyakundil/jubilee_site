from django.contrib import admin
from .models import Series, Subject, Clients, Osago, Coefficient_by_type_car, Driver_coefficient, Diagnostic_card, Executor, Natural_legal_person
from django.contrib import admin
from django.contrib.admin import widgets
from django.contrib.admin.sites import site
from django import forms

class BlogRawIdWidget(widgets.ForeignKeyRawIdWidget):
    def url_parameters(self):
        res = super().url_parameters()
        res['type__exact'] = 'PROJ'
        return res

class ProjectAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].queryset = Clients.objects.filter(type='PROJ')
        self.fields['name'].widget = BlogRawIdWidget(rel=Clients._meta.get_field('blog').remote_field, admin_site=site)

    class Meta:
        # Django 1.8 convenience:
        fields = '__all__'
        model = Clients

class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    raw_id_fields = ('name',)

admin.site.register(Subject)
admin.site.register(Series)
admin.site.register(Osago)
admin.site.register(Clients)
admin.site.register(Coefficient_by_type_car)
admin.site.register(Driver_coefficient)
admin.site.register(Diagnostic_card)
admin.site.register(Executor)
admin.site.register(Natural_legal_person)