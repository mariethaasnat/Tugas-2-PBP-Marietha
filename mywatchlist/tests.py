from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.

class UnitTest (TestCase):
    def setting_up (x):
        x.client = Client()
        x.mywatchlist_html = reverse ('mywatchlist:show_mywatchlist')
        x.mywatchlist_xml = reverse ('mywatchlist:show_xml')
        x.mywatchlist_json = reverse ('mywatchlist:show_json')

    def test_html (x):
        response = x.client.get(x.mywatchlist_html)
        x.assertEqual(response.status_code, 200)

    def show_xml (x):
        response = x.client.get(x.mywatchlist_xml)
        x.assertEqual(response.status_code, 200)
    
    def show_json (x):
        response = x.client.get(x.mywatchlist_json)
        x.assertEqual(response.status_code, 200)