from api_base.permission import MyBasePermission
from api_account.constants import RoleData


class UserPermission(MyBasePermission):
    match_any_roles = [RoleData.USER]


class DoctorPermission(MyBasePermission):
    match_any_roles = [RoleData.DOCTOR]


class AdminPermission(MyBasePermission):
    match_any_roles = [RoleData.ADMIN]


class DoctorOrAdminPermission(MyBasePermission):
    match_any_roles = [RoleData.ADMIN, RoleData.DOCTOR]
