from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from .models import Flight, Review, Attendance, Queue, Inventory
from .serializers import FlightSerializer, QueueSerializer, InventorySerializer
from django.db.models import F
from django.views.generic import TemplateView



# Create your views here.

@api_view(['GET'])
def getFlights(request):
    flights = Flight.objects.all()
    serializers = FlightSerializer(flights, many=True)
    return Response(serializers.data)



@api_view(['POST'])
def updateReview(request):
 
    post_data = json.loads(request.body.decode("utf-8"))
    review = post_data['review']
    Review.objects.filter(name=review).update(rating=F('rating') + 1)

    return JsonResponse({'foo':'bar'})




class dataPage(TemplateView):

    template_name = 'data-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Review.objects.all()
        return context



@api_view(['POST'])
def updateAttendance(request):
 
    post_data = json.loads(request.body.decode("utf-8"))
    name = post_data['name']
    Attendance.objects.filter(name=name).update(attendance=True)

    return JsonResponse({'foo':'bar'})



def attendancePage(request):

    qs = Attendance.objects.all()
    print(qs)
    context = {'qs':qs}

    return render(request, 'attendance_page.html', context)



@api_view(['POST'])
def addQueue(request):
 
    post_data = json.loads(request.body.decode("utf-8"))
    name = post_data['name']
    Queue.objects.create(name=name)

    return JsonResponse({'foo':'bar'})


@api_view(['GET'])
def getQueue(request):
    queue = Queue.objects.all()
    serializers = QueueSerializer(queue, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def getInventory(request):

    inventory = Inventory.objects.all()
    serializers = InventorySerializer(inventory, many=True)
    return Response(serializers.data)