from django.contrib import admin
from .models import Page, Comment

# set up automated slug creation
class PageAdmin(admin.ModelAdmin):
	model = Page
	list_display = ('author', 'title', 'text',)
	prepopulated_fields = {'slug': ('title',)}


admin.site.register(Page, PageAdmin)
admin.site.register(Comment)


