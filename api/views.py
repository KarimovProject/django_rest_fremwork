from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

from rest_framework.request import Request

@api_view(['GET'])
def home(request:Request):
    data = request.query_params

    return Response({'result': data})