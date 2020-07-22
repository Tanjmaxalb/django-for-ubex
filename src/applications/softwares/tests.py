import json

from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from applications.softwares.models import Software


class GetSoftwareTestCase(APITestCase):
    fixtures = ["test_sets.yaml"]

    def setUp(self):
        self.url = "/api/softwares/Software"

        self.username = "tanjmaxalb"
        self.email = "tanjamxalb@gmail.com"
        self.password = "P@ssw0rd"
        self.user = User.objects.create_user(
            self.username, self.email, self.password)
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        
    def test_get_all_softwares(self):
        response = self.client.get(self.url)
        result = response.json()
        
        self.assertEqual(200, response.status_code)
        self.assertEqual(3, len(result))

    def test_get_softwares_with_1st_vulnerability(self):
        request_data = {"vulnerability": 1}
        response = self.client.get(self.url, request_data)
        result = response.json()
        
        self.assertEqual(200, response.status_code)
        self.assertEqual(2, len(result))

    def test_get_empty_result(self):
        request_data = {"vulnerability": 100}
        response = self.client.get(self.url, request_data)
        result = response.json()
        
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, len(result))

    def test_get_python_software(self):
        request_data = {"name": "python"}
        response = self.client.get(self.url, request_data)
        result = response.json()
        
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(result))
        self.assertEqual("python", result[0]["name"])

    def test_get_limited_softwares(self):
        request_data = {"limit": 2}
        response = self.client.get(self.url, request_data)
        result = response.json()

        self.assertEqual(200, response.status_code)
        self.assertEqual(2, len(result))

    def test_ordered_softwares(self):
        expected_result = ["python", "pytest", "django"]
        expected_result = sorted(expected_result)

        request_data = {"order_by": "name"}
        response = self.client.get(self.url, request_data)
        result = response.json()
        result = [r["name"] for r in result]

        self.assertEqual(200, response.status_code)
        self.assertEqual(expected_result, result)


class CreateSoftwareTestCase(APITestCase):
    def setUp(self):
        self.url = "/api/softwares/Software"

        self.username = "tanjmaxalb"
        self.email = "tanjamxalb@gmail.com"
        self.password = "P@ssw0rd"
        self.user = User.objects.create_user(
            self.username, self.email, self.password)
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_create_software(self):
        request_data = {
            "name": "pandas",
            "description": "description",
            "vulnerabilities": 1,
            "created_at": "2020-07-22T22:00:00Z",
            "updated_at": "2020-07-22T22:00:00Z"
        }
        response = self.client.post(self.url, request_data)
        self.assertEqual(201, response.status_code)


class DetailSoftwareTestCase(APITestCase):
    def setUp(self):
        self.url = "/api/softwares/Software/{id_}"

        self.username = "tanjmaxalb"
        self.email = "tanjamxalb@gmail.com"
        self.password = "P@ssw0rd"
        self.user = User.objects.create_user(
            self.username, self.email, self.password)
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_update_software_name(self):
        my_software = Software.objects.create(
            name="python 2", description="too old python")

        request_data = {
            "name": "python 3",
            "description": "python 3.7",
            "updated_at": "2020-07-22T22:00:10Z"
        }
        response = self.client.put(
            self.url.format(id_=my_software.pk), request_data)
        self.assertEqual(200, response.status_code)

        result = json.loads(response.content)
        self.assertEqual("python 3", result["name"])

    def test_update_not_found(self):
        request_data = {"name": "linux"}
        response = self.client.put(
            self.url.format(id_=10), request_data)
        self.assertEqual(404, response.status_code)

    def test_delete_software_name(self):
        my_software = Software.objects.create(
            name="python 2", description="too old python")

        response = self.client.delete(
            self.url.format(id_=my_software.pk))
        
        self.assertEqual(204, response.status_code)

    def test_delete_not_found(self):
        response = self.client.delete(self.url.format(id_=10))
        self.assertEqual(404, response.status_code)
