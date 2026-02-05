from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Room_Booking.views import home, room_list, book_room, booking_success # Inga booking_success add pannunga

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('rooms/', room_list, name='rooms'),
    path('book/<int:room_id>/', book_room, name='book_room'),
    path('success/', booking_success, name='booking_success'), # Idhu thaan puthu success page URL
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)