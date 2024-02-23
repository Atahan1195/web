from django.shortcuts import render
from .models import DishCategory, Gallery, Chef, Event, Contact
from django.views.generic import TemplateView
from .forms import ReservationForm


class MainPageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = DishCategory.objects.filter(is_visible=True)
        gallery = Gallery.objects.filter(is_visible=True)
        chef = Chef.objects.filter(is_visible=True)
        reservation_form = ReservationForm()
        events = Event.objects.filter(is_visible=True)
        contacts = Contact.objects.filter(is_visible=True)

        context['categories'] = categories
        context['gallery'] = gallery
        context['reservation_form'] = reservation_form
        context['chef'] = chef
        context['events'] = events
        context['contacts'] = contacts
        return context

    def post(self, request, *args, **kwargs):
        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid():
            reservation_form.save()
            return render(request, self.template_name, {'reservation_form': reservation_form})
        else:
            return render(request, self.template_name, {'reservation_form': reservation_form})




