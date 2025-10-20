import pytest
import requests
import logging
import csv
import os
from datetime import datetime

# Setup de logging (console + arquivo)
def setup_logging():
    """
    Configura o log para mostrar no console e salvar em um arquivo.
    Assim conseguimos ver o que aconteceu em cada execução de teste.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.StreamHandler(),  # mostra no console
            logging.FileHandler("test_run.log", mode="w", encoding="utf-8")  # salva em arquivo
        ]
    )

# Hook que roda antes da sessão de testes começar
def pytest_sessionstart(session):
    setup_logging()
    logging.info("=== Iniciando sessão de testes ===")

# Classe personalizada de cliente API
class ApiClient(requests.Session):
    """
    Cliente de API que herda de requests.Session.
    Guarda a última resposta recebida para facilitar debug em caso de falha.
    """
    def __init__(self):
        super().__init__()
        self.last_response = None

    def request(self, *args, **kwargs):
        response = super().request(*args, **kwargs)
        self.last_response = response  # guarda a última resposta
        return response

# Fixture global: cliente API
@pytest.fixture(scope="session")
def api_client():
    """
    Retorna uma instância compartilhada de ApiClient para todos os testes.
    Isso evita recriar a sessão HTTP toda hora.
    """
    return ApiClient()

# Fixture base_url
@pytest.fixture(scope="session")
def base_url():
    """
    Retorna a URL base da API usada nos testes.
    Facilita em caso de troca do endpoint depois.
    """
    return "https://jsonplaceholder.typicode.com"

# Hook: adiciona corpo da resposta no relatório HTML em caso de falha
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Esse hook intercepta os resultados de cada teste.
    Se o teste falhar, ele anexa o corpo da última resposta HTTP no relatório.
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        api_client = item.funcargs.get("api_client", None)
        if api_client and api_client.last_response is not None:
            response_text = api_client.last_response.text
            rep.longrepr = f"{rep.longrepr}\n\nAPI Response Body:\n{response_text}"

# Fixture para ler casos de teste de um arquivo CSV
@pytest.fixture(scope="session")
def post_test_cases():
    """
    Lê os casos de teste do arquivo 'casos_de_teste.csv' (que deve estar na raiz do projeto).
    Cada linha do CSV vira um dicionário com:
      - title
      - body
      - userId
      - expected_status
    Retorna uma lista de casos que podem ser usados nos testes dinâmicos.
    """
    file_path = os.path.join(os.getcwd(), "casos_de_teste.csv")
    cases = []
    try:
        with open(file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cases.append(row)
        logging.info(f"{len(cases)} casos de teste carregados de {file_path}")
    except FileNotFoundError:
        logging.error(f"Arquivo {file_path} não encontrado!")
    return cases
