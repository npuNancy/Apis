from django.contrib import admin
from specificApis import models
# Register your models here.


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.StudentData)
admin.site.register(models.Classes)
admin.site.register(models.Grade)
admin.site.register(models.Administrator)
admin.site.register(models.GradeAdmin)
