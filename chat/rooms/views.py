from django.views.generic import ListView, DetailView
from .models import Room
from users.models import Message

class RoomListView(ListView):
    model = Room
    template_name = 'rooms/room_list.html'

class RoomDetailView(DetailView):
    model = Room
    template_name = 'rooms/room_detail.html'
    slug_field = 'name'
    slug_url_kwarg = 'room_name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = Message.objects.filter(room=self.object).order_by('timestamp')
        context['rooms']= Room.objects.all()
        context['current_room_name'] = self.object.name
        return context