from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session


def get_authenticated_users(include=[], exclude=[]):
    """
    Gets a lit of all the authenticated user who are in the include list and not in the exclude list.
    For example, assuming your user profile has a "friends" property to get all authenticated friends you would use:

    >>> get_authenticated_users(include=user.friends, exclude=[user])

    :param include: A list of users to include, if False no include filter is applied
    :param exclude: A list of users to exclude

    :return: A query set containing all authenticate uses in
    """
    # get the ids of the authenticated sessions
    sessions = Session.objects.filter(expire_date__gte=datetime.now())
    uid_list = []
    for session in sessions:
        data = session.get_decoded()
        uid_list.append(data.get('_auth_user_id', None))


    #find all the users
    if include:
        return User.objects.filter(
            id__in=uid_list
        ).filter(
            id__in=[u.id for u in include],
        ).exclude(
            id__in=[u.id for u in exclude]
        )
    else:
        return User.objects.filter(
            id__in=uid_list,
        ).exclude(
            id__in=[u.id for u in exclude]
        )
