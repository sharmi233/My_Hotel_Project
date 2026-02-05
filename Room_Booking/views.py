from django.shortcuts import render, redirect, get_object_or_404
from .models import Room, Booking

def home(request):
    return render(request, 'home.html')

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'rooms.html', {'rooms': rooms})

def book_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == "POST":
        c_name = request.POST.get('name') 
        c_contact = request.POST.get('contact') 
        c_in = request.POST.get('check_in')
        c_out = request.POST.get('check_out')
        
        # Database logic
        Booking.objects.create(
            room=room, 
            customer_name=c_name, 
            contact_number=c_contact, 
            check_in=c_in, 
            check_out=c_out
        )
        
        room.is_booked = True
        room.save()
        
        # Ippo direct-ah success page-ku redirect aagum
        return redirect('booking_success') 
        
    return render(request, 'book_room.html', {'room': room})

# Success message kaata indha puthu function
def booking_success(request):
    return render(request, 'booking_success.html')