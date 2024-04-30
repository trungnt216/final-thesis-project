from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from metter.models import Metter
from metter.serializers import MetterSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def metter_list(request):
    if request.method == 'GET':
        metters = Metter.objects.all()
        print('List metters: ', metters)
        
        # title = request.query_params.get('title', None)
        # if title is not None:
        #     tutorials = tutorials.filter(title__icontains=title)
        
        metter_serializer = MetterSerializer(metters, many=True)
        return JsonResponse({"data": metter_serializer.data}, safe=False)
        # 'safe=False' for objects serialization
 
    # elif request.method == 'POST':
    #     tutorial_data = JSONParser().parse(request)
    #     tutorial_serializer = TutorialSerializer(data=tutorial_data)
    #     if tutorial_serializer.is_valid():
    #         tutorial_serializer.save()
    #         return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
    #     return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Metter.objects.all().delete()
        return JsonResponse({'message': '{} Metter were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def metter_detail(request, pk):
    try: 
        metter = Metter.objects.get(pk=pk) 
    except Metter.DoesNotExist: 
        return JsonResponse({'message': 'The Metter does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        metter_serializer = MetterSerializer(metter) 
        return JsonResponse(metter_serializer.data) 
 
    # elif request.method == 'PUT': 
    #     tutorial_data = JSONParser().parse(request) 
    #     tutorial_serializer = TutorialSerializer(tutorial, data=tutorial_data) 
    #     if tutorial_serializer.is_valid(): 
    #         tutorial_serializer.save() 
    #         return JsonResponse(tutorial_serializer.data) 
    #     return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        metter.delete() 
        return JsonResponse({'message': 'Metter was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
# @api_view(['GET'])
# def tutorial_list_published(request):
#     tutorials = Tutorial.objects.filter(published=True)
        
#     if request.method == 'GET': 
#         tutorials_serializer = TutorialSerializer(tutorials, many=True)
#         return JsonResponse(tutorials_serializer.data, safe=False)
    
