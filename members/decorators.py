# decorators.py
import jwt
from functools import wraps
from django.conf import settings
from django.http import JsonResponse

def branch_admin_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        token = request.COOKIES.get("jwt") 

        if not token:
            return JsonResponse({"status": "failed", "message": "Missing token"}, status=401)

        try:
            payload = jwt.decode(token, settings.JWT_SECRET, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return JsonResponse({"status": "failed", "message": "Token expired"}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({"status": "failed", "message": "Invalid token"}, status=401)

        request.user_id = payload.get("user_id")
        request.role = payload.get("role")
        request.branch_id = payload.get("branch_id")

        if request.role not in ["branch_admin", "superuser"]:
            return JsonResponse({"status": "failed", "message": "Not authorized"}, status=403)

        return view_func(request, *args, **kwargs)
    return wrapper
