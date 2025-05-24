from rest_framework.routers import DefaultRouter
from expense_tracker.api import category

router = DefaultRouter()
router.register(r'categories', category.CategoryViewSet, basename='category')

urlpatterns = router.urls
