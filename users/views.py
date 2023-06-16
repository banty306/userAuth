from unittest import result
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.db import transaction
import json


class TemplateView(APIView):
    def get(self, request, *args, **kwargs):
        return Response("response", status=status.HTTP_400_BAD_REQUEST)
