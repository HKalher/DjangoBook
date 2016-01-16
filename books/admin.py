from django.contrib import admin
from books.models import Publisher, Author, Book

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email')
    search_fields = ('first_name','last_name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','edition','publisher','ISBN','publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    #fields maintains the order of the header of the tables,and the header which is not mentioned here will not be editable by the users in the administration page
    #these things work to enter new items or to change values of the attributes of these items not to show the items or their details
    fields = ('title','authors','edition','publisher','ISBN','publication_date')
    filter_horizontal = ('authors',)
    raw_id_fields = ('publisher',)

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name','address','website')

admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)

