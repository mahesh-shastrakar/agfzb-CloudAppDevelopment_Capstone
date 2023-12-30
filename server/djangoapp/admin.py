from django.contrib import admin
# from .models import related models
from .models import CarMake, CarModel


# Register your models here.

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
@admin.register(CarMake)
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Display fields in the admin list view

@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('car_make', 'name', 'dealer_id', 'type', 'year')  # Display fields in the admin list view
    list_filter = ('car_make', 'type', 'year')  # Add filters on the right side
    search_fields = ('car_make__name', 'name', 'dealer_id')  # Add search functionality