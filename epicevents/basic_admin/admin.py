from django.contrib.admin import AdminSite

from .forms import BasicAdminAuthenticationForm


class BasicAdminSite(AdminSite):
    """
    BasicAdminSite is the admin site accessible for users that belong to
    the "mangers" group.
    It contains fewer possibilities than normal admin site.
        * only users that belong to manager groups can login
        * logged in users can create and modify Events, Clients, Contracts
        * logged in users can create and modify users and assign them to a group
        but can not see or give them staff or superuser status (reserved for the
        django admin site)
        * logged in users can not list, create, edit or delete Groups
        * logged in users can not list, create, edit or delete Permissions
        * logged in users can not list, create, edit or delete Tokens
    """

    site_header = 'EpicEvents API administration'
    site_title = 'Epicevents API admin'
    index_title = 'API administration'
    site_url = None
    login_form = BasicAdminAuthenticationForm
    enable_nav_sidebar = False

    def has_permission(self, request):
        """
        Return True if the given HttpRequest has permission to view
        *at least one* page in the basic admin site.
        """
        return request.user.is_active and 'managers' in (
            group.name for group in request.user.groups.all())


basic_admin_site = BasicAdminSite(name='basic-admin')
