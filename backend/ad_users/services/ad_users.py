from core.services.active_directory import get_ad_domain_session


def get_user_by_samaccountname(sam: str):
    session = get_ad_domain_session()

    user = session.find_user_by_sam_name(
        sam,
        [
            "mail",
            "displayName",
            "givenName",
            "sAMAccountName",
            "userAccountControl",
        ],
    )

    return user if user else None


def is_ad_user_enabled(user) -> bool:
    uac = int(user.get("userAccountControl", 0))
    return not (uac & 2)
