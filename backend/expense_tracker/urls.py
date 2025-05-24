from rest_framework.routers import DefaultRouter
from expense_tracker.api import category, expenses

router = DefaultRouter()
router.register(r'categories', category.CategoryViewSet, basename='category')
router.register(r'expenses', expenses.ExpenseViewSet, basename='expense')
urlpatterns = router.urls
