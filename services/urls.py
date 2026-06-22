from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import(

CategoryViewSet,
ServiceProfileViewSet,
ProductViewSet

)
# = إنشاء نظام تلقائي لإدارة الروابط (URLs) الخاصة بالـ ViewSets
router = DefaultRouter()

router.register('category', CategoryViewSet)
router.register('serviceprofile', ServiceProfileViewSet)
router.register('product', ProductViewSet)

# ل الـ URLs اللي الـ router أنشأها تلقائيًا
urlpatterns = router.urls