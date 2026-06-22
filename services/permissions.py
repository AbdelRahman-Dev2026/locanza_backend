from rest_framework.permissions import BasePermission

#  صلاحية خاصة بالخدمات:
#  تسمح لصاحب الخدمة أو الأدمن فقط بتعديل أو حذف الخدمة.
class IsOwnerOrAdmin(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True

        return obj.owner == request.user


# صلاحية خاصة بالمنتجات:
# تسمح لصاحب الخدمة المرتبط بها المنتج أو الأدمن فقط
# بتعديل أو حذف المنتج.

class IsProductOwnerOrAdmin(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True

        return obj.service.owner == request.user

