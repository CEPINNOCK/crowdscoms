#Import only the datetime module
from datetime import datetime

from django.utils import timezone

from rest_framework.response import Response
from rest_framework.views import APIView

#The class base view 
class HelloWorld(APIView):
    """
    Basic 'Hello World' view. Show our current API version, the current time, the number of recent visitors
    in the last 1 hour, and the total number of visitors and page visits
    """

    def get(self, request, format=None):
        # Initialize data dictionary with default values
        data = {
            'version': 1.0,
            'time': timezone.now(),
            'recent_visitors': 0,
            'all_visitors': 0,
            'all_visits': 0,
        }

        # TODO: Retrieve recent_visitors, all_visitors, and all_visits data from database

        return Response(data)
