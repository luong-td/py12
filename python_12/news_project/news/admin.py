from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Category)
admin.site.register(New)
admin.site.register(Feedback)
admin.site.register(Comment)
'''class CommentInline(admin.StackedInline):
	model = Comment
class NewAdmin(admin.ModelAdmin):
	list_display = ['title','date']
	list_filter = ['date']
	search_field = ['id']
	inlines = [CommentInline]
admin.site.register(New, NewAdmin)'''