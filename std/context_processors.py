from .models import Std
from account.models import Teacher


def class_links(request):
    links = Std.objects.all()
    return dict(links=links)
