from django.contrib.auth.models import User
from django.views.generic import DeleteView, ListView
from guardian.shortcuts import remove_perm

from project.models import Project


class DeleteViewWithPermissions(DeleteView):
    permission_required = None

    def delete(self, request, *args, **kwargs):
        remove_perm(self.permission_required, request.user, self.get_object())
        return super().delete(request, *args, **kwargs)


class HomePageView(ListView):
    model = Project
    template_name = 'index.html'
    context_object_name = 'users_projects'

    def get_queryset(self):
        if isinstance(self.request.user, User):
            return Project.objects.filter(owner=self.request.user).order_by('-date_created')[:10]

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['num_projects'] = Project.objects.all().count()
        context['num_users'] = User.objects.all().count()
        return context
