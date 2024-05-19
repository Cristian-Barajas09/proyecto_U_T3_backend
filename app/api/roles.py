from rolepermissions.roles import AbstractUserRole

class AdminRole(AbstractUserRole):
    available_permissions = {
        'view_event': True,
        'view_plate': True,
        'view_order': True,
        'create_order': True,
        'update_order': True,
        'delete_order': True,
        'create_event': True,
        'update_event': True,
        'delete_event': True,
        'create_plate': True,
        'update_plate': True,
        'delete_plate': True,
    }

class SalesPersonRole(AbstractUserRole):
    available_permissions = {
        'view_event': True,
        'view_plate': True,
        'view_order': True,
        'create_order': True,
        'update_order': True,
        'delete_order': True,
        'create_event': True,
        'update_event': True,
        'delete_event': True,
    }

class ClientRole(AbstractUserRole):
    available_permissions = {
        'view_event': True,
        'view_plate': True,
        'view_order': True,
    }