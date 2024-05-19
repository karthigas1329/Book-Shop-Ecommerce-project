from django.contrib import admin
from sampleapp.models import Book
from sampleapp.models import Order

class BookAdmin(admin.ModelAdmin):
	list_display=['title','author','description','price','image_url','follow_author','book_available']
admin.site.register(Book,BookAdmin)


class OrderAdmin(admin.ModelAdmin):
	list_display=['product','created']
admin.site.register(Order,OrderAdmin)
