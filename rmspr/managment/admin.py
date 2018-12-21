from django.contrib import admin

# Register your models here.
from .models import User, property, visitor, owner, review


class UserAdmin(admin.ModelAdmin):
    last_display = ['id', 'username']

    class Meta:
        model = User


class propertyadmin(admin.ModelAdmin):
    last_display = ["id", "description", "price", "location", "num_views"]

    class Meta:
        model = property


class visitoradmin(admin.ModelAdmin):
    last_display = ["id", "profile", "num_views", "pref_location"]

    class Meta:
        model = visitor


class owneradmin(admin.ModelAdmin):
    last_display = ["id", "owner_name", "num_properties","email","phone_no"]

    class Meta:
        model = owner


class reviewadmin(admin.ModelAdmin):
    last_display = ["property_id", "visitor_id", "visitor_name", "rating", "comment"]

    class Meta:
        model = review


admin.site.register(User, UserAdmin)
admin.site.register(property, propertyadmin)
admin.site.register(visitor, visitoradmin)
admin.site.register(owner, owneradmin)
admin.site.register(review, reviewadmin)
