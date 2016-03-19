from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass


class TopicAdmin(admin.TabularInline):
    model = Topic

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    inlines = [TopicAdmin,]

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass
