from rest_framework import status, permissions

# Admin permission
class AdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        is_superuser = request.user.is_superuser
        if(is_superuser):
            return True
        else:
            return False
        
# Access only the user data
class UserPermission(permissions.BasePermission):
    def has_permission(self,request, view,):
        user_pk = view.kwargs.get('pk', None)
        if(request.user.id  == user_pk):
            return True
        else:
            return False
        
# Access only user recipes
class UserRecipePermission(permissions.BasePermission):
    def has_permission(self,request, view,):
        user_pk = view.kwargs.get('user', None)
        if(request.user.id  == user_pk):
            return True
        else:
            return False