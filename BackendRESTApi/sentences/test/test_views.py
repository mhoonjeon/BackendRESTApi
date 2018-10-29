import json

from django.urls import reverse
from django.forms.models import model_to_dict
from nose.tools import ok_, eq_
from rest_framework.test import APITestCase
from rest_framework import status
from faker import Faker
from ..models import Sentence
from .factories import SentenceFactory
from BackendRESTApi.users.test.factories import UserFactory
from BackendRESTApi.charts.test.factories import ChartFactory

fake = Faker()


class TestSentenceListTestCase(APITestCase):
    """
    Tests /sentences list operations.
    """

    def setUp(self):
        self.url = reverse('sentence-list')
        self.sentence_data = model_to_dict(SentenceFactory.create())
        self.client.force_authenticate(user=UserFactory.build())

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        response = self.client.post(self.url, self.sentence_data)
        eq_(response.status_code, status.HTTP_201_CREATED)

        sentence = Sentence.objects.get(pk=response.data.get('id'))
        eq_(sentence.raw, self.sentence_data.get('raw'))

    def test_post_request_with_multiple_data_succeeds(self):
        sentence_count_before = Sentence.objects.count()
        chart = ChartFactory.create()

        sentence_list = []
        for _ in range(3):
            sentence_list.append(model_to_dict(SentenceFactory.build(chart=chart)))
        response = self.client.post(self.url, sentence_list, format='json')
        sentence_count_after = Sentence.objects.count()

        eq_(response.status_code, status.HTTP_201_CREATED)
        eq_(sentence_count_before + 3, sentence_count_after)

    def test_get_list_request_filtered_with_chart_id_succeeds(self):
        chart = ChartFactory.create()
        SentenceFactory.create_batch(size=3, chart=chart)
        response = self.client.get(self.url, {'chart': chart.id} )
        eq_(len(response.json()['results']), 3)

    def test_list_create_sentences_succeeds(self):
        chart = ChartFactory.create()
        payload = [
            {
                "chart": chart.id,
                "raw": "머리가 아파요",
                "category": "CC"
            },
            {
                "chart": chart.id,
                "raw": "기침이 나요",
                "category": "PI"
            },
            {
                "chart": chart.id,
                "raw": "10년전부터 당뇨가 있어요",
                "category": "PMH"
            }
        ]
        response = self.client.post(self.url, json.dumps(payload), content_type='application/json')
        eq_(response.status_code, status.HTTP_201_CREATED)
        eq_(len(response.json()), 3)
