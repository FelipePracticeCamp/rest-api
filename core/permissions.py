from rest_framework.permissions import BasePermission


class GlobalPermission(BasePermission):
    def has_permission(self, request, view):
        permission_codename = self.get_model_permission_codename(request.method, view)
        if permission_codename:
            return request.user.has_perm(permission_codename)
        else:
            return False
    

    def get_model_permission_codename(self, method, view):
        try:
            app = view.queryset.model._meta.app_label
            model = view.queryset.model._meta.model_name
            action = self.get_actionsufix(method)
            return f'{app}_{action}.{model}'
        except:
            return None

    def get_action_sufix(self, method):
        METHOD_ACTIONS = {
            "GET":"view",
            "OPTION":"view",
            "HEAD":"view",
            "POST":"add",
            "PUT":"change",
            "PATCH":"change",
            "DELETE":"delete",
        }

        action = METHOD_ACTIONS.get(method, '')
        return action