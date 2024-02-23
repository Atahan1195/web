from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from home.models import Reservation


def is_manager(user):
    return user.has_perm('auth.is_staff') or user.groups.filter(name='manager').exists()


@login_required(login_url='login')
@user_passes_test(is_manager)
def manager_page(request):
    context = {'reservations': Reservation.objects.all()}
    return render(request, 'layouts/manager.html', context=context)


