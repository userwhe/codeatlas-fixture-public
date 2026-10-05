"""Small service illustrating access checks and private-code consent."""

from .permissions import check_repository_access, require_external_processing_consent


def connect_repository(user_id: str, allowed_users: set[str], *, is_private: bool,
                       external_processing_accepted: bool = False) -> dict[str, str]:
    if not check_repository_access(user_id, allowed_users):
        raise PermissionError("not_found")
    require_external_processing_consent(is_private, external_processing_accepted)
    return {"status": "queued"}
