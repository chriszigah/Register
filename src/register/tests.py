from django.test import TestCase, Client

from . models import Record, Department

from django.contrib.auth.models import User

from django.urls import reverse

from . views import home

# Create your tests here.
'''
    1. Set up Code
    2. Logic to Test
    3. Assertions
'''

class TestModels(TestCase):
    def SetUp(self):
        """
        Runs befor each Test Case
        """
      
        user = User.objects.create_user(username='christiano', password='fakepasswod123')
        department = Department.objects.create(name='IT')
        


    def test_record_model(self):
        user = User.objects.create_user(username='christiano', password='fakepasswod123')
        department = Department.objects.create(name='IT')

        record_item = Record.objects.create(
            first_name='Christian',
            last_name='Zigah',
            email='chris@mail.com',
            phone='0248778253',
            city='East Legon',
            country='Ghana',
            department=department,
            user=user
        )
    

        self.assertEquals(str(record_item), 'Christian')
        self.assertTrue(isinstance(record_item, Record))

class TestViews(TestCase):
    def setUp(self):
        pass

    def test_index_GET(self):
        # Mock Response
        index_url = reverse("")
        client = Client()
        response = client.get(index_url)

        #Write Assertions
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'register/index.html')


    def test_dashboard(self):
        client = Client()

        #Set Up User Login Credentials
        User.objects.create_user(username='christiano', password='fakepassword123')
        client.login(username='christiano', password='fakepassword123')
        
        # Mock Response
        dashboard_url = reverse("dashboard")
        response = client.get(dashboard_url)

        #Write Assertions
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'register/dashboard.html')

    def test_dashboard_user_not_logged_in(self):
        client = Client()

        # Mock Response
        dashboard_url = reverse("dashboard")
        response = client.get(dashboard_url)

        #Write Assertions
        self.assertEquals(response.status_code, 302)
        



