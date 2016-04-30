from django.contrib import admin
from main.models import Course, Chapter
# Register your models here.

#modelo Hijo
class ChapterChildAdmin(admin.TabularInline):
    model = Chapter

#modelo padre
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    search_fields = ('name', 'price', 'teacher__name')
    list_display = ('name', 'price', 'teacher')
    inlines = (ChapterChildAdmin ,)

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('name', 'course')
