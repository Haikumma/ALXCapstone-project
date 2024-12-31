from rest_framework.routers import DefaultRouter 
from  .views import BookViewSet


router = DefaultRouter()
router.register(r'books', BookViewSet) #defining the urls patterns for the book viewset 
urlpatterns = router.urls

