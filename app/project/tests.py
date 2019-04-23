from django.contrib.auth.models import User
from django.test import TestCase, override_settings

# Create your tests here.
from guardian.shortcuts import assign_perm

from project.models import Project


@override_settings(DEBUG=True)
class ProjectViewTest(TestCase):

    @classmethod
    def setTestData(self):
        owner = User.objects.create_user('user', 'user@user.project', 'some password')
        project_1 = Project.objects.create_project(name='project 1')
        project_2 = Project.objects.create_project(name='project 2')
        project_1.owner = owner
        project_2.owner = owner
        project_1.save()
        project_2.save()
        assign_perm("delete_project", owner, project_1)
        assign_perm("delete_project", owner, project_2)
        assign_perm("change_project", owner, project_1)
        assign_perm("change_project", owner, project_2)

    def test_project_create(self):
        self.client.login(username='user', password='some password')
        test_url = '/project/start'
        response = self.client.get(test_url)
        self.assertEquals(response.status_code, 200)
        response = self.client.post(test_url, {'name': 'testt1', 'description': 'test description'})
        self.assertEquals(response.status_code, 302)
        test_project = Project.objects.get(name='testt1')
        self.assertEquals(test_project.owner.username, 'user')

    def test_project_detail(self):
        test_url = '/project/'
        response = self.client.get(test_url + '1/detail')
        self.assertEquals(response.status_code, 200)
        response = self.client.get(test_url + '2/detail')
        self.assertEquals(response.status_code, 200)

    def test_project_update(self):
        self.client.login(username='user', password='some password')
        test_url = '/project/1/update'
        response = self.client.get(test_url)
        self.assertEquals(response.status_code, 200)
        new_name = 'test1 updated'
        response = self.client.post(test_url, {'name': new_name, 'description': 'updated description'})
        test_project = Project.objects.get(pk=1)
        self.assertEquals(test_project.name, new_name)

    def test_project_delete(self):
        self.client.login(username='user', password='some password')
        test_url = '/project/2/delete'
        response = self.client.get(test_url)
        self.assertEquals(response.status_code, 200)
        response = self.client.post(test_url)
        with self.assertRaises(Project.DoesNotExist):
            Project.objects.get(pk=2)

    def test_project_member_add_remove(self):
        test2_user = User.objects.create_user('user2', 'some password2')
        self.client.login(username='user', password='some password')
        test_url = '/project/1/add-member'
        response = self.client.get(test_url)
        self.assertEquals(response.status_code, 200)
        response = self.client.post(test_url, {'username': 'user2'})
        self.assertEquals(response.status_code, 302)
        test_member = User.objects.get(member_of_projects=1, pk=test2_user.id)
        self.assertEquals(test_member, test2_user)

        test_url = '/project/1/remove-member/%d' % test2_user.id
        response = self.client.get(test_url)
        self.assertEquals(response.status_code, 200)
        response = self.client.post(test_url)
        with self.assertRaises(User.DoesNotExist):
            User.objects.filter(member_of_projects=1).get(username=test2_user.username)
