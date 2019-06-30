# DO NOT EDIT THIS FILE MANUALLY
# THIS FILE IS AUTO-GENERATED
# MANUAL CHANGES WILL BE DISCARDED
# PLEASE READ GARUDA DOCS
from django.contrib.auth.models import Permission  # NOQA
GARUDA_IGNORE_FIELDS = ['created_on', 'updated_on', 'id']  # NOQA


def read_permission(*args, **kwargs):
    try:
        return Permission.objects.get(*args, **kwargs)
    except Permission.DoesNotExist:
        return None


def read_permissions_filter(*args, **kwargs):
    return Permission.objects.filter(*args, **kwargs)


def create_permission(*args, **kwargs):
    for ignore_field in GARUDA_IGNORE_FIELDS:
        if ignore_field in kwargs:
            del kwargs[ignore_field]
    for key in list(kwargs):
        if kwargs[key] in [None, 'None', '']:
            del kwargs[key]
    return Permission.objects.create(*args, **kwargs)


def update_permission(id, *args, **kwargs):
    for ignore_field in GARUDA_IGNORE_FIELDS:
        if ignore_field in kwargs:
            del kwargs[ignore_field]
    for key in list(kwargs):
        if kwargs[key] in [None, 'None', '']:
            del kwargs[key]
    return Permission.objects.filter(id=id).update(*args, **kwargs)


def delete_permission(id):
    return Permission.objects.get(id=id).delete()

from django.contrib.auth.models import Group  # NOQA
GARUDA_IGNORE_FIELDS = ['created_on', 'updated_on', 'id']  # NOQA


def read_group(*args, **kwargs):
    try:
        return Group.objects.get(*args, **kwargs)
    except Group.DoesNotExist:
        return None


def read_groups_filter(*args, **kwargs):
    return Group.objects.filter(*args, **kwargs)


def create_group(*args, **kwargs):
    for ignore_field in GARUDA_IGNORE_FIELDS:
        if ignore_field in kwargs:
            del kwargs[ignore_field]
    for key in list(kwargs):
        if kwargs[key] in [None, 'None', '']:
            del kwargs[key]
    return Group.objects.create(*args, **kwargs)


def update_group(id, *args, **kwargs):
    for ignore_field in GARUDA_IGNORE_FIELDS:
        if ignore_field in kwargs:
            del kwargs[ignore_field]
    for key in list(kwargs):
        if kwargs[key] in [None, 'None', '']:
            del kwargs[key]
    return Group.objects.filter(id=id).update(*args, **kwargs)


def delete_group(id):
    return Group.objects.get(id=id).delete()

from django.contrib.auth.models import User  # NOQA
GARUDA_IGNORE_FIELDS = ['created_on', 'updated_on', 'id']  # NOQA


def read_user(*args, **kwargs):
    try:
        return User.objects.get(*args, **kwargs)
    except User.DoesNotExist:
        return None


def read_users_filter(*args, **kwargs):
    return User.objects.filter(*args, **kwargs)


def create_user(*args, **kwargs):
    for ignore_field in GARUDA_IGNORE_FIELDS:
        if ignore_field in kwargs:
            del kwargs[ignore_field]
    for key in list(kwargs):
        if kwargs[key] in [None, 'None', '']:
            del kwargs[key]
    return User.objects.create(*args, **kwargs)


def update_user(id, *args, **kwargs):
    for ignore_field in GARUDA_IGNORE_FIELDS:
        if ignore_field in kwargs:
            del kwargs[ignore_field]
    for key in list(kwargs):
        if kwargs[key] in [None, 'None', '']:
            del kwargs[key]
    return User.objects.filter(id=id).update(*args, **kwargs)


def delete_user(id):
    return User.objects.get(id=id).delete()