# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Submit, Row, Column
# from .models import Project, Milestone, Issue, Label
# from django import forms

# class ProjectForm(forms.ModelForm):

#     def __init__(self, *args, **kwargs):
#         super(ProjectForm, self).__init__(*args, **kwargs)
#         self.helper=FormHelper()
#         self.helper.form_id = "id-projectForm"
#         self.helper.form_class= "d-table mx-auto justify-content-sm-left"
#         self.helper.label_class = "font-weight-bold"
#         self.helper.field_class="form-control-sm"
#         self.helper.form_group_wrapper_class = 'w-100'
#         self.helper.form_method = 'post'
#         self.helper.form_action = ''

#         self.helper.add_input(Submit('submit', 'Submit'))

#     class Meta:
#         model = Project
#         fields = ['title', 'description',]