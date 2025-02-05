from rest_framework.test import APITestCase
from rest_framework import status
from .models import Policy
from datetime import date


class PolicyTests(APITestCase):
    def setUp(self):
        self.valid_policy = Policy.objects.create(
            customer_name="Yuri", policy_type="home", expiry_date=date.today()
        )

    def test_create_policy(self):
        url = "/api/policies/"
        data = {
            "customer_name": "Yuri",
            "policy_type": "home",
            "expiry_date": str(date.today()),
        }

        response = self.client.post(url, data, format="json")
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["customer_name"], data["customer_name"])

    def test_create_policy_with_expiry_in_past(self):
        url = "/api/policies/"
        data = {
            "customer_name": "Yuri",
            "policy_type": "home",
            "expiry_date": str(date(2020, 1, 1)),
        }

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("expiry_date", response.data)

    def test_list_policies(self):
        url = "/api/policies/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_policy(self):
        url = f"/api/policies/{self.valid_policy.policy_id}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["customer_name"], self.valid_policy.customer_name
        )

    def test_retrieve_policy_not_found(self):
        url = "/api/policies/99999/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_policy(self):
        url = f"/api/policies/{self.valid_policy.policy_id}/"
        data = {
            "customer_name": "Yuri",
            "policy_type": "home",
            "expiry_date": str(date.today()),
        }

        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(response.data["customer_name"], data["customer_name"])

    def test_update_policy_not_found(self):
        url = "/api/policies/99999/"
        data = {
            "customer_name": "Yuri",
            "policy_type": "home",
            "expiry_date": str(date.today()),
        }

        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_policy(self):
        url = f"/api/policies/{self.valid_policy.policy_id}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Policy.objects.count(), 0)

    def test_delete_policy_not_found(self):
        url = "/api/policies/99999/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
