from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import DishCategory, Dish, FooterItem, Gallery, Reservation, Chef, Event, Contact


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date', 'time', 'people_number', 'message')
    list_filter = ('date', 'time')


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_visible')


@admin.register(FooterItem)
class FooterItemAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email',)


@admin.register(DishCategory)
class DishCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position', 'is_visible')
    list_editable = ('name', 'position', 'is_visible')


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('photo_src_tag', 'name', 'slug', 'ingredients', 'description', 'price', 'is_visible', 'position', 'category')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('ingredients', 'price', 'is_visible', 'position')
    list_filter = ('category', 'is_visible')
    search_fields = ('name', 'ingredients', 'description')

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50 height=50>")

    photo_src_tag.short_description = 'Dish photo'


@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo_src_tag', 'name', 'position', 'is_visible')
    list_editable = ('name', 'position', 'is_visible')

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50 height=50>")

    photo_src_tag.short_description = 'Chef photo'


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_visible')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_visible', 'phone')








