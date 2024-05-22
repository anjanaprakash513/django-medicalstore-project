from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from django.contrib.auth.forms import UserCreationForm
from rest_framework.permissions import AllowAny

from django.views.decorators.csrf import csrf_exempt
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from medicines.forms import medForm

from medicines.models import medList
from .serializers import medSerializer

from django.shortcuts import get_object_or_404

@api_view(['POST'])
@permission_classes((AllowAny,))
def signup(request):
    form = UserCreationForm(data=request.data)
    if form.is_valid():
        user = form.save()
        return Response("account created successfully", status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},status=HTTP_200_OK)



@api_view(['POST'])
@permission_classes((AllowAny,))
def create_product(request):
    form = medForm(request.POST)
    if form.is_valid():
        product = form.save()
        return Response({'id': product.id}, status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((AllowAny,))
def list_products(request):
    products = medList.objects.all()
    serializer = medSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes((AllowAny,))
def update_product(request, pk):
    product = get_object_or_404(medList, pk=pk)
    form = medForm(request.data, instance=product)
    if form.is_valid():
        form.save()
        serializer = medSerializer(product)
        return Response(serializer.data)
    else:
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
@permission_classes((AllowAny,))
def delete_product(request, pk):
    try:
        product = medList.objects.get(pk=pk)
    except medList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    product.delete()
    return Response("deleted successfully")



@api_view(['GET'])
@permission_classes((AllowAny,))
def search_medicine(request):
    search_term = request.GET.get('search')
    if search_term:
        products = medList.objects.filter(Name__icontains=search_term)
    else:
        products = medList.objects.all()

    serializer = medSerializer(products, many=True)
    return Response(serializer.data)