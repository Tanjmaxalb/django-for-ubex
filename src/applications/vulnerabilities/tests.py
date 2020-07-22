import json

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from applications.vulnerabilities.models import Vulnerability


class ListCreateVulnerabilitiesTestCase(APITestCase):
    fixtures = ["test_sets.yaml"]

    def setUp(self):
        self.url = "/api/vulnerabilities/Vulnerability"

        self.username = "tanjmaxalb"
        self.email = "tanjamxalb@gmail.com"
        self.password = "P@ssw0rd"
        self.user = User.objects.create_user(
            self.username, self.email, self.password)
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_get_all_vulnerabilities(self):
        response = self.client.get(self.url)
        result = response.json()

        self.assertEqual(200, response.status_code)
        self.assertEqual(2, len(result))

    def test_get_python_buf_over(self):
        request_data = {"name": "buffer overflow"}
        response = self.client.get(self.url, request_data)
        result = response.json()

        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(result))
        self.assertEqual("buffer overflow", result[0]["name"])

    def test_get_empty_result(self):
        request_data = {"name": "an undefined vulnerability"}
        response = self.client.get(self.url, request_data)
        result = response.json()

        self.assertEqual(200, response.status_code)
        self.assertEqual(0, len(result))

    def test_get_limited_softwares(self):
        request_data = {"limit": 1}
        response = self.client.get(self.url, request_data)
        result = response.json()

        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(result))

    def test_ordered_softwares(self):
        expected_result = ["buffer overflow", "out of bounds read"]
        expected_result = sorted(expected_result)

        request_data = {"order_by": "name"}
        response = self.client.get(self.url, request_data)
        result = response.json()
        result = [r["name"] for r in result]

        self.assertEqual(200, response.status_code)
        self.assertEqual(expected_result, result)


class CreateVulnerabilityTestCase(APITestCase):
    def setUp(self):
        self.url = "/api/vulnerabilities/Vulnerability"

        self.username = "tanjmaxalb"
        self.email = "tanjamxalb@gmail.com"
        self.password = "P@ssw0rd"
        self.user = User.objects.create_user(
            self.username, self.email, self.password)
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_create_software(self):
        request_data = {
            "name": "a vulnerability",
            "description": "description",
            "created_at": "2020-07-22T22:00:00Z",
            "updated_at": "2020-07-22T22:00:00Z"
        }
        response = self.client.post(self.url, request_data)
        self.assertEqual(201, response.status_code)


class DetailVulnerabilityTestCase(APITestCase):
    def setUp(self):
        self.url = "/api/vulnerabilities/Vulnerability/{id_}"

        self.username = "tanjmaxalb"
        self.email = "tanjamxalb@gmail.com"
        self.password = "P@ssw0rd"
        self.user = User.objects.create_user(
            self.username, self.email, self.password)
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_update_software_name(self):
        my_vulnerabilty = Vulnerability.objects.create(
            name="new vulnerability", description="a description")

        request_data = {
            "name": "new vulnerability",
            "description": "important description",
            "updated_at": "2020-07-22T22:00:10Z"
        }
        response = self.client.put(
            self.url.format(id_=my_vulnerabilty.pk), request_data)
        self.assertEqual(200, response.status_code)

        result = json.loads(response.content)
        self.assertEqual("new vulnerability", result["name"])

    def test_update_not_found(self):
        request_data = {"name": "unknown vulnerability"}
        response = self.client.put(
            self.url.format(id_=10), request_data)
        self.assertEqual(404, response.status_code)

    def test_delete_software_name(self):
        my_vulnerabilty = Vulnerability.objects.create(
            name="new vulnerability", description="a description")

        response = self.client.delete(
            self.url.format(id_=my_vulnerabilty.pk))

        self.assertEqual(204, response.status_code)

    def test_delete_not_found(self):
        response = self.client.delete(self.url.format(id_=10))
        self.assertEqual(404, response.status_code)
