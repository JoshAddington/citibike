# Create your views here.
import json
import os

from django.conf import settings
from django.db.models import Prefetch
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Station, UpdateTime, Bike
from .serializers import StationSerializer, StationBikeSerializer, StationMapSerializer


# Create your views here.
def boroughs(request):
    """
        Returns the JSON used for creating the NYC map in D3.
    """
    return JsonResponse(
        json.loads(open(
            os.path.join(settings.STATIC_ROOT, 'citibike', 'nyc.json')).read()
            )
        )


@api_view(['GET'])
def citibike_map(request):
    """
        Returns citibike information formatted for use in the D3 visualization.
        The updates and bikes indexes correspond to each other.
        {
        "updates":
            [
                "2015-10-04T22:50:00.102Z",
                "2015-10-04T23:00:00.079Z",
                ...
            ],
        "stations":
            {
                "station_number": 79,
                "name": "Franklin St & W Broadway",
                "available_docks": 32,
                "latitude": "40.719115520",
                "longitude": "-74.006666610",
                "bikes": [
                    28,
                    27,
                    ...
            }
        }
    """
    if request.method == 'GET':
        stations = Station.objects.all().prefetch_related(Prefetch('bikes', queryset=Bike.objects.order_by('update')))
        station_serializer = StationMapSerializer(stations, many=True)
        updates = UpdateTime.objects.values_list('datetime', flat=True)
        return Response({'stations': station_serializer.data,
                         'updates': updates})


@api_view(['GET'])
def station_collection(request):
    """
        Returns station information for all stations
    """
    if request.method == 'GET':
        stations = Station.objects.all()
        serializer = StationSerializer(stations, many=True)
        return Response({'stations': serializer.data})


@api_view(['GET'])
def station_detail(request, pk):
    """
        Returns station information for a specific station.
    """
    if request.method == 'GET':
        station = get_object_or_404(Station, station_number=pk)
        serializer = StationSerializer(station)
        return Response({'station': serializer.data})


@api_view(['GET'])
def station_bikes(request, pk):
    """
        Returns station information, update times, and bike count for a specific station.
    """
    if request.method == 'GET':
        station = get_object_or_404(Station.objects.all().prefetch_related(Prefetch('bikes', queryset=Bike.objects.order_by('update'))), station_number=pk)
        serializer = StationBikeSerializer(station)
        return Response({'station': serializer.data})


@api_view(['GET'])
def updates(request):
    """
        Returns date and time information for when update script was run.
    """
    if request.method == 'GET':
        updates = UpdateTime.objects.values_list('datetime', flat=True)
        return Response({'updates': updates})
