from django.contrib import admin
from .models import Room, Booking  # Models-ah anga irundhu import panrom

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    # Models.py-la enna field names irukko adhai thaan inga tharanum
    # Oru velai room_number-ku badhila 'name' nu models.py-la irundha, 'name' nu mathunga
    list_display = ('room_number', 'category', 'price', 'is_booked')
    list_filter = ('category', 'is_booked')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'room', 'check_in', 'check_out', 'contact_number')
    search_fields = ('customer_name', 'contact_number')