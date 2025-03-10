from datetime import datetime, timezone


def set_audit_values(obj_dict: dict, user_id: str):
    obj_dict["created_at"] = datetime.now(timezone.utc)
    obj_dict["created_by"] = user_id
    obj_dict["updated_at"] = datetime.now(timezone.utc)
    obj_dict["updated_by"] = user_id
    obj_dict["deleted_at"] = None
    obj_dict["deleted_by"] = None
    obj_dict["deleted"]: False
