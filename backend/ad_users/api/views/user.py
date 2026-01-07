from ninja import Router
from ninja.errors import HttpError
from ad_users.api.schemas.user import ADUserOut
from ad_users.services import get_user_by_samaccountname, is_ad_user_enabled
import logging

api_logger = logging.getLogger("api")
db_logger = logging.getLogger("db")
error_logger = logging.getLogger("error")
task_logger = logging.getLogger("task")

ad_user_router = Router(tags=["Users"])


@ad_user_router.get("/get/{user_sam}", response=ADUserOut)
def get_ad_user(request, user_sam: str):
    """
    get_ad_user _summary_

    _extended_summary_

    Args:
        request (_type_): _description_
        user_sam (str): _description_

    Returns:
        _type_: _description_
    """

    user = get_user_by_samaccountname(user_sam)

    if not user:
        api_logger.error("AD User not found")
        raise HttpError(404, "User not found")

    api_logger.info(f"AD User {user_sam} found")
    return ADUserOut(
        username=user.get("sAMAccountName"),
        email=user.get("mail"),
        display_name=user.get("displayName"),
        enabled=is_ad_user_enabled(user),
    )
