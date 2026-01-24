import os
import django
from django.urls import resolve, reverse
from django.urls.exceptions import Resolver404

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

def check_url(url):
    try:
        match = resolve(url)
        print(f"URL '{url}' resolve para: {match.view_name}")
    except Resolver404:
        print(f"URL '{url}' NÃO resolve (404)")

check_url('/api/get-address/06825020/')
try:
    rev = reverse('get_address_by_cep', kwargs={'cep': '06825020'})
    print(f"Reverse 'get_address_by_cep' resolve para: {rev}")
except Exception as e:
    print(f"Reverse falhou: {e}")
