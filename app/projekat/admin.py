from django.contrib import admin
from .models import Project, Milestone, Issue, Label

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display=['title', 'pk', 'owner', 'description', 'date_created',]
    def get_changeform_initial_data(self, request):
        get_data = super(ProjectAdmin, self).get_changeform_initial_data(request)
        get_data['owner'] = request.user.pk
        return get_data

admin.site.register(Project, admin_class=ProjectAdmin)
admin.site.register(Milestone)
admin.site.register(Issue)
admin.site.register(Label)
