import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from django.test import Client
from django.contrib.auth.models import User

client = Client()

# Testa sem login
print("Testando sem login:")
response = client.get('/api/get-address/06825020/')
print(f"Status code: {response.status_code}")
if response.status_code == 302:
    print(f"Redirect para: {response.url}")

# Testa com login
print("\nTestando com login:")
if not User.objects.filter(username='testuser').exists():
    User.objects.create_user(username='testuser', password='password')

client.login(username='testuser', password='password')
response = client.get('/api/get-address/06825020/')
print(f"Status code: {response.status_code}")
print(f"Conteúdo: {response.content.decode('utf-8')}")
