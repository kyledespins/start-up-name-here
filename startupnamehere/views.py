from django.http import HttpResponse


def get_start_up_name(request):
    return HttpResponse("Pooply")
