from django.db import models

class Room(models.Model):
    ROOM_CATEGORIES = (
        ('DELUXE', 'Deluxe Room'),
        ('SUITE', 'Suite Room'),
        ('VILLA', 'Water Villa'),
    )
    room_number = models.IntegerField()
    category = models.CharField(max_length=10, choices=ROOM_CATEGORIES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_booked = models.BooleanField(default=False)
    image = models.ImageField(upload_to='room_images/', null=True, blank=True) 

    def __str__(self):
        return f"Room {self.room_number} - {self.category}"

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15) # Inga 'contact_number' nu iruku
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"{self.customer_name} - Room {self.room.room_number}"