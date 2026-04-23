from app.services.profile_service import ProfileService
from app.utils.response import success_response


def get_profile():
    profile = ProfileService.get_profile()
    return success_response(profile, "Profile fetched successfully")
