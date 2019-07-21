from django.shortcuts import render
from django.http import HttpResponse, JsonResponse # response 체크
from django.views.decorators.csrf import csrf_exempt # csrf_token 체크
# from rest_framework.parsers import JSONParser # json import
from snippets.models import Snippet # snippet import
from snippets.serializers import SnippetSerializer # serializers import
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def snippet_list(request, format=None):
    if request.method == 'GET':
        snippets= Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SnippetSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = status.HTTP_201_CREATED) # 생성이 잘 되었다는 http의 응답 코드
        return JsonResponse(serializer.errors, status = status.HTTP_400_BAD_REQUEST) 

@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format = None):
    snippet = Snippet.objects.get(pk = pk)
    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# Create your views here.
# @csrf_exempt # csrf_token을 쓰지 않아도 요청을 보낼 수 있게 됨.
"""def snippet_list(request):
    # GET: 조회(List)
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many = True)
        return JsonResponse(serializer.data, safe = False)

    # POST: Create
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201) # 생성이 잘 되었다는 http의 응답 코드
        return JsonResponse(serializer.errors, status = 400)
    """
 # 127.0.0.1/snippets/3   
# @csrf_exempt
"""
def snippet_detail(request, pk):
    snippet = Snippet.objects.get(pk = pk)
    # GET: Read
    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)
    # PUT: Update
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    # DELETE: Delete(Destroy)
    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204) #204: no content
"""