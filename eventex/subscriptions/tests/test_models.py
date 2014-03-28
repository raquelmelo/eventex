#coding : utf-8
from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionTest(TestCase):
	def setUp(self):
		self.obj = Subscription(
		name='Raquel',
		cpf='12356897415',
		email='raquel@mail.com',
		phone='21-36589615')

	def test_create(self):
		self.obj.save()
		self.assertEqual(1, self.obj.id)
		
