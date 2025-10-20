import pytest

# Marcando o teste como "api_test" para poder rodar só os testes desse grupo
@pytest.mark.api_test
def test_create_post_dinamico(base_url, api_client, post_test_cases):
    """
    Cria posts dinamicamente usando os dados do CSV (via fixture post_test_cases).
    Cada linha do CSV é um caso de teste diferente.
    """

    # Para cada caso de teste no CSV
    for test_case in post_test_cases:
        # Montando o payload que vamos enviar no POST
        payload = {
            "title": test_case["title"],  # pega o título do CSV
            "body": test_case["body"],    # pega o corpo do CSV
            # Se userId estiver vazio, usa 1 como padrão
            "userId": int(test_case["userId"]) if test_case["userId"] else 1
        }

        # Qual status code esperamos receber da API
        expected_status = int(test_case["expected_status"])

        # Fazendo a requisição POST para criar o post
        response = api_client.post(f"{base_url}/posts", json=payload)

        # Print só para sabermos qual caso está rodando
        print(f"\n Rodando caso: {test_case['title']}")

        # Verifica se o status code retornado bate com o esperado
        assert response.status_code == expected_status

        # Se o post foi criado (status 201), validamos os dados retornados
        if expected_status == 201:
            data = response.json()  # Converte JSON da resposta para dicionário
            assert data["title"] == payload["title"]  # título deve bater
            assert data["body"] == payload["body"]    # corpo deve bater
            assert data["userId"] == payload["userId"]  # userId deve bater
