from ninja import NinjaAPI
from core.utils.auth import GlobalAuth
from core.utils.version import get_version

# Import routers from apps
from ad_users.api.routers.user import ad_user_router

api = NinjaAPI(auth=GlobalAuth())
api.title = "LenoreAD"
api.version = get_version()
api.description = "API documetation for LenoreAD"

# Add routers to the API
api.add_router("/users", ad_user_router)
