"""
gnstagram middleware catalog.
"""

from django.shortcuts import redirect
from django.urls import reverse

class UserCompletionMiddleware:
    """
    Porfile completion middleware.
    Ensure every user that is interacting with the platform
    have their user picture and biography.
    """

    def __init__(self, get_response):
        """
        Middleware initialization.
        """
        self.get_response = get_response
    
    def __call__(self, request):
        """
        Code to be executed for each request betfore the view is called.
        """
        if not request.user.is_anonymous:
            if not request.user.is_staff:

                # if not request.user.picture or not request.user.biography:
                if not request.user.biography:
                    if request.path not in [reverse('users:update_user'), reverse('users:logout')]:
                        return redirect('users:update_user')
        
        response = self.get_response(request)
        return response