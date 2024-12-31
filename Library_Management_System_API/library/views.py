from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BookSerializer 
from rest_framework.permissions import IsAuthenticated 



# Create your views here.

class BookViewSet(ModelViewSet):  
    queryset = Book.objects.all()
    serializer_class = BookSerializer        
    permission_classes = [IsAuthenticated] #the user must be logged in to access this viewset
    lookup_field = 'title'