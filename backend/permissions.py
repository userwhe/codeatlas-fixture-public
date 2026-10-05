"""Read-only repository access rules used by the demo service."""


def check_repository_access(user_id: str, allowed_users: set[str]) -> bool:
    """Allow access only when the user appears in the repository allowlist."""
    return user_id in allowed_users


def require_external_processing_consent(is_private: bool, accepted: bool) -> None:
    """Private repository excerpts require explicit external-processing consent."""
    if is_private and not accepted:
        raise PermissionError("external_processing_not_accepted")
