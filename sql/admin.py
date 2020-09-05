from django.contrib import admin
from .models import Person, Position, Depart, Workers, Image

class BbAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'year')
    list_display_links = ('firstname', 'lastname', 'year')
    search_fields = ('firstname', 'lastname', 'year',)
    
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image',)
    list_display_links = ('image',)
    search_fields = ('image',)


class PositionAdmin(admin.ModelAdmin):
    list_display = ('position', 'age', 'email', 'telephone')
    list_display_links = ('position', 'age', 'email', 'telephone')
    search_fields = ('position', 'age', 'email', 'telephone',)

class DepartAdmin(admin.ModelAdmin):
    list_display = ('name', 'aim')
    list_display_links = ('name', 'aim')
    search_fields = ('name', 'aim',)

class WorkersAdmin(admin.ModelAdmin):
    list_display = ('department', 'corp')
    list_display_links = ('department', 'corp')
    search_fields = ('department',)

admin.site.register(Person,BbAdmin)
admin.site.register(Image,ImageAdmin)
admin.site.register(Position,PositionAdmin)
admin.site.register(Depart,DepartAdmin)
admin.site.register(Workers,WorkersAdmin)