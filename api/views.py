from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Policy
from .serializers import PolicySerializer
from rest_framework import status


@api_view(["GET"])
def getPolicies(request):
    policies = Policy.objects.all()
    serializer = PolicySerializer(policies, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getPolicy(request, id):
    try:
        policy = Policy.objects.get(pk=id)
        serializer = PolicySerializer(policy, many=True)
        return Response(serializer.data)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def addPolicy(request):
    serializer = PolicySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def updatePolicy(request, id):
    try:
        policy = Policy.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PolicySerializer(policy, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def deletePolicy(request, id):
    try:
        policy = Policy.objects.get(pk=id)
        policy.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)