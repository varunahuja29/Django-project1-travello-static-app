from django.shortcuts import render
from .models import Destination

# Create your views here.
def indexFun(request):
    dest1 = Destination(1, 'Boston', 'Its the financial capital', 'destination_1.jpg', 200, False)
    dest2 = Destination(2, 'Florida', 'Place of aligators', 'destination_2.jpg', 300, True)
    dest3 = Destination(3, 'Vegas', 'Land of casinos', 'destination_3.jpg', 400, False)

    dests = [dest1, dest2, dest3]
    return render(request, "index.html", {'dests': dests})