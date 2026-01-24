import requests
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


@login_required
def get_address_by_cep(request, cep):
    try:
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        response.raise_for_status()
        data = response.json()

        if data.get("erro"):
            return JsonResponse({"error": "CEP não encontrado."}, status=404)

        return JsonResponse(
            {
                "address": data.get("logradouro", ""),
                "bairro": data.get("bairro", ""),
                "city": data.get("localidade", ""),
                "state": data.get("uf", ""),
            }
        )

    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": str(e)}, status=500)