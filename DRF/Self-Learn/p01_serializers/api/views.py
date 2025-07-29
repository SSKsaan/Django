from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse, HttpResponse
from rest_framework.renderers import JSONRenderer
from .models import Book
from .serializers import *

# View to return books using Response (standard DRF)
class BookListCreate(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

# Return books using JsonResponse (mid-level)
class BookJsonResponse(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False)

# Return books using JSONRenderer + HttpResponse (lowest-level)
class BookHttpJsonRenderer(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

# Handle book creation (POST) with full validation flow
class BookCreateManual(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            book = serializer.save()  # Calls create()
            return Response(BookSerializer(book).data, status=201)
        return Response(serializer.errors, status=400)

# Test nested book + author creation
class BookNestedCreate(APIView):
    def post(self, request):
        serializer = BookNestedCreateSerializer(data=request.data)
        if serializer.is_valid():
            book = serializer.save()
            return Response(BookSerializer(book).data)
        return Response(serializer.errors, status=400)

# Test dynamic serializer output (optional)
class BookDynamicFields(APIView):
    def get(self, request):
        book = Book.objects.first()
        serializer = DynamicBookSerializer(book, fields=['title', 'is_recent'])
        return Response(serializer.data)
