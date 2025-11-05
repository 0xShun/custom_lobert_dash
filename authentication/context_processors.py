"""
Context processors for making data available to all templates
"""

def user_preferences(request):
    """Add user preferences to all template contexts"""
    if request.user.is_authenticated:
        from authentication.models import UserPreferences
        preferences, created = UserPreferences.objects.get_or_create(user=request.user)
        return {'user_preferences': preferences}
    return {}
