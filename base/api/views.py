from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.models import Room
from .serializers import RoomSerializer

# view that shows all the routes in our api
@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms', # for viewing rooms
        'GET /api/rooms/:id', # for info. about single room

    ]
    return Response(routes)


@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True) # many = True, bcz there are many objects
    return Response(serializer.data)
    
    
    
@api_view(['GET'])
def getRoom(request, pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False) # many = True, bcz there are many objects
    return Response(serializer.data)