# import requests

# JSONPLACEHOLDER = "https://jsonplaceholder.typicode.com"
# HTTPBIN = "https://httpbin.org"

# #Query Params

# # Step 1: Buscar todos os comentarios do post 2
# def test_comments_for_post2():
#     # manda o GET com o filtro postId=2
#     response = requests.get(f"{JSONPLACEHOLDER}/comments", params={"postId": 2})
#     assert response.status_code == 200  # tem que responder ok
#     comments = response.json()  # transforma json em lista python
#     # todos os comentarios devem ser do post 2
#     assert all(comment["postId"] == 2 for comment in comments)
#     # e nao pode estar vazio
#     assert len(comments) > 0


# # Step 2: Listar tarefas pendentes do usuario 5
# def test_pending_tasks_user5():
#     # usa "completed=false" pra pegar as pendentes
#     response = requests.get(f"{JSONPLACEHOLDER}/todos", params={"userId": 5, "completed": "false"})
#     assert response.status_code == 200
#     todos = response.json()
#     assert len(todos) > 0  # lista nao pode vir vazia
#     # verifica se todas sao do user 5
#     assert all(todo["userId"] == 5 for todo in todos)
#     # e se todas estao com completed = False
#     assert all(todo["completed"] is False for todo in todos)


# # Step 3: Buscar todos os albuns do usuario 9
# def test_user9_albums_count():
#     response = requests.get(f"{JSONPLACEHOLDER}/albums", params={"userId": 9})
#     assert response.status_code == 200
#     albums = response.json()
#     # confere se todos sao do user 9
#     assert all(album["userId"] == 9 for album in albums)
#     # o user 9 tem que ter 10 albuns
#     assert len(albums) == 10


# # Step 4: Listar todas as tarefas completas do user 1
# def test_completed_todos_user1():
#     response = requests.get(f"{JSONPLACEHOLDER}/todos", params={"userId": 1, "completed": "true"})
#     assert response.status_code == 200  # api respondeu ok
#     todos = response.json()
#     assert len(todos) > 0  # nao veio vazio
#     # todas as tarefas tem que estar completas
#     assert all(todo["completed"] is True for todo in todos)

# # Headers

# # # Step 5: Testar header customizado
# def test_custom_header_echo():
#     headers = {"X-Custom-Header": "MyValue"}  # cria o header
#     response = requests.get(f"{HTTPBIN}/headers", headers=headers)
#     assert response.status_code == 200
#     data = response.json()
#     # verifica se o header chegou igual no servidor
#     assert data["headers"]["X-Custom-Header"] == "MyValue"


# # Step 6: Testar header de resposta
# def test_custom_response_header():
#     params = {"My-Test-Header": "Hello"}  # manda o header como param
#     response = requests.get(f"{HTTPBIN}/response-headers", params=params)
#     assert response.status_code == 200
#     # checa se o header voltou na resposta
#     assert response.headers.get("My-Test-Header") == "Hello"


# # Step 7: Testar User-Agent customizado
# def test_custom_user_agent():
#     headers = {"User-Agent": "My-Test-Agent/1.0"}
#     response = requests.get(f"{HTTPBIN}/headers", headers=headers)
#     assert response.status_code == 200
#     data = response.json()
#     # confere se o user agent foi recebido certo
#     assert data["headers"]["User-Agent"] == "My-Test-Agent/1.0"


# # Step 8: Mandar varios headers de uma vez
# def test_multiple_custom_headers():
#     headers = {"X-Header-1": "Value1", "X-Header-2": "Value2"}
#     response = requests.get(f"{HTTPBIN}/headers", headers=headers)
#     assert response.status_code == 200
#     data = response.json()
#     # checa se os dois headers chegaram certinhos
#     assert data["headers"]["X-Header-1"] == "Value1"
#     assert data["headers"]["X-Header-2"] == "Value2"


# # Step 9: Testar autenticação basica certa
# def test_basic_auth_success():
#     response = requests.get(f"{HTTPBIN}/basic-auth/user/passwd", auth=("user", "passwd"))
#     assert response.status_code == 200
#     data = response.json()
#     # confere se foi autenticado de boa
#     assert data["authenticated"] is True


# # Step 10: Testar auth basica com senha errada
# def test_basic_auth_failure():
#     response = requests.get(f"{HTTPBIN}/basic-auth/user/passwd", auth=("user", "wrong"))
#     assert response.status_code == 401  # deve dar nao autorizado


# # Step 11: Testar token Bearer valido
# def test_bearer_token_valid():
#     token = "my-mock-token"
#     headers = {"Authorization": f"Bearer {token}"}
#     response = requests.get(f"{HTTPBIN}/bearer", headers=headers)
#     assert response.status_code == 200
#     data = response.json()
#     # confere se autenticou e se o token bate
#     assert data["authenticated"] is True
#     assert data["token"] == token


# # Step 12: Testar Bearer sem token
# def test_bearer_token_missing():
#     response = requests.get(f"{HTTPBIN}/bearer")
#     assert response.status_code == 401  # sem token nao passa


# # Step 13: Validar estrutura do user 1
# def test_user1_schema_types():
#     response = requests.get(f"{JSONPLACEHOLDER}/users/1")
#     assert response.status_code == 200
#     data = response.json()
#     # checa os tipos dos dados principais
#     assert isinstance(data["id"], int)
#     assert isinstance(data["name"], str)
#     assert isinstance(data["address"], dict)
#     assert isinstance(data["company"], dict)


# # Step 14: Ver se o address tem as chaves certas
# def test_user1_address_fields():
#     response = requests.get(f"{JSONPLACEHOLDER}/users/1")
#     data = response.json()
#     address = data["address"]
#     # precisa ter essas 3 chaves no endereco
#     for key in ["street", "city", "zipcode"]:
#         assert key in address


# # Step 15: Validar o post 10
# def test_post10_fields():
#     response = requests.get(f"{JSONPLACEHOLDER}/posts/10")
#     assert response.status_code == 200
#     data = response.json()
#     # checa tipos e se os textos nao tao vazios
#     assert isinstance(data["userId"], int)
#     assert isinstance(data["id"], int)
#     assert isinstance(data["title"], str) and len(data["title"]) > 0
#     assert isinstance(data["body"], str) and len(data["body"]) > 0


# # Step 16: Ver estrutura das fotos do album 1
# def test_album1_photos_structure():
#     response = requests.get(f"{JSONPLACEHOLDER}/albums/1/photos")
#     assert response.status_code == 200
#     photos = response.json()
#     # cada foto precisa ter essas chaves
#     for photo in photos:
#         for key in ["albumId", "id", "title", "url", "thumbnailUrl"]:
#             assert key in photo


# # Step 17: Validar formato do email do user 3
# def test_user3_email_format():
#     response = requests.get(f"{JSONPLACEHOLDER}/users/3")
#     data = response.json()
#     email = data["email"]
#     # so checa se tem @ e . no email
#     assert "@" in email and "." in email.split("@")[-1]


# # Step 18: Comentarios do post 5 nao podem estar vazios
# def test_post5_comments_not_empty():
#     response = requests.get(f"{JSONPLACEHOLDER}/posts/5/comments")
#     assert response.status_code == 200
#     comments = response.json()
#     assert len(comments) > 0


# # Step 19: Validar estrutura do primeiro comentario
# def test_first_comment_structure():
#     response = requests.get(f"{JSONPLACEHOLDER}/posts/5/comments")
#     comments = response.json()
#     first = comments[0]
#     # confere tipos basicos dos campos
#     assert isinstance(first["postId"], int)
#     assert isinstance(first["id"], int)
#     assert isinstance(first["name"], str)
#     assert isinstance(first["email"], str)
#     assert isinstance(first["body"], str)


# # Step 20: Validar se o campo completed é bool
# def test_todo199_completed_boolean():
#     response = requests.get(f"{JSONPLACEHOLDER}/todos/199")
#     assert response.status_code == 200
#     data = response.json()
#     # completed tem que ser booleano
#     assert isinstance(data["completed"], bool)

import pytest
import requests

JSONPLACEHOLDER = "https://jsonplaceholder.typicode.com"
HTTPBIN = "https://httpbin.org"

# Função utilitária para requests que ignora 503
# Se a API HTTPBIN estiver fora do ar, o teste será pulado em vez de falhar
def safe_request(method, url, **kwargs):
    response = requests.request(method, url, **kwargs)
    if response.status_code == 503:
        pytest.skip(f"HTTPBIN indisponível (503) ao acessar {url}")
    return response


# Query Params

# Step 1: Buscar todos os comentarios do post 2
def test_comments_for_post2():
    response = requests.get(f"{JSONPLACEHOLDER}/comments", params={"postId": 2})
    assert response.status_code == 200  # tem que responder ok
    comments = response.json()  # transforma json em lista python
    # todos os comentarios devem ser do post 2
    assert all(comment["postId"] == 2 for comment in comments)
    # e nao pode estar vazio
    assert len(comments) > 0


# Step 2: Listar tarefas pendentes do usuario 5
def test_pending_tasks_user5():
    # usa "completed=false" pra pegar as pendentes
    response = requests.get(f"{JSONPLACEHOLDER}/todos", params={"userId": 5, "completed": "false"})
    assert response.status_code == 200
    todos = response.json()
    assert len(todos) > 0  # lista nao pode vir vazia
    # verifica se todas sao do user 5
    assert all(todo["userId"] == 5 for todo in todos)
    # e se todas estao com completed = False
    assert all(todo["completed"] is False for todo in todos)


# Step 3: Buscar todos os albuns do usuario 9
def test_user9_albums_count():
    response = requests.get(f"{JSONPLACEHOLDER}/albums", params={"userId": 9})
    assert response.status_code == 200
    albums = response.json()
    # confere se todos sao do user 9
    assert all(album["userId"] == 9 for album in albums)
    # o user 9 tem que ter 10 albuns
    assert len(albums) == 10


# Step 4: Listar todas as tarefas completas do user 1
def test_completed_todos_user1():
    response = requests.get(f"{JSONPLACEHOLDER}/todos", params={"userId": 1, "completed": "true"})
    assert response.status_code == 200  # api respondeu ok
    todos = response.json()
    assert len(todos) > 0  # nao veio vazio
    # todas as tarefas tem que estar completas
    assert all(todo["completed"] is True for todo in todos)


# Headers

# Step 5: Testar header customizado
def test_custom_header_echo():
    headers = {"X-Custom-Header": "MyValue"}  # cria o header
    response = safe_request("GET", f"{HTTPBIN}/headers", headers=headers)
    assert response.status_code == 200
    data = response.json()
    # verifica se o header chegou igual no servidor
    assert data["headers"]["X-Custom-Header"] == "MyValue"


# Step 6: Testar header de resposta
def test_custom_response_header():
    params = {"My-Test-Header": "Hello"}  # manda o header como param
    response = safe_request("GET", f"{HTTPBIN}/response-headers", params=params)
    assert response.status_code == 200
    # checa se o header voltou na resposta
    assert response.headers.get("My-Test-Header") == "Hello"


# Step 7: Testar User-Agent customizado
def test_custom_user_agent():
    headers = {"User-Agent": "My-Test-Agent/1.0"}
    response = safe_request("GET", f"{HTTPBIN}/headers", headers=headers)
    assert response.status_code == 200
    data = response.json()
    # confere se o user agent foi recebido certo
    assert data["headers"]["User-Agent"] == "My-Test-Agent/1.0"


# Step 8: Mandar varios headers de uma vez
def test_multiple_custom_headers():
    headers = {"X-Header-1": "Value1", "X-Header-2": "Value2"}
    response = safe_request("GET", f"{HTTPBIN}/headers", headers=headers)
    assert response.status_code == 200
    data = response.json()
    # checa se os dois headers chegaram certinhos
    assert data["headers"]["X-Header-1"] == "Value1"
    assert data["headers"]["X-Header-2"] == "Value2"


# Step 9: Testar autenticação basica certa
def test_basic_auth_success():
    response = safe_request("GET", f"{HTTPBIN}/basic-auth/user/passwd", auth=("user", "passwd"))
    assert response.status_code == 200
    data = response.json()
    # confere se foi autenticado de boa
    assert data["authenticated"] is True


# Step 10: Testar auth basica com senha errada
def test_basic_auth_failure():
    response = safe_request("GET", f"{HTTPBIN}/basic-auth/user/passwd", auth=("user", "wrong"))
    assert response.status_code == 401  # deve dar nao autorizado


# Step 11: Testar token Bearer valido
def test_bearer_token_valid():
    token = "my-mock-token"
    headers = {"Authorization": f"Bearer {token}"}
    response = safe_request("GET", f"{HTTPBIN}/bearer", headers=headers)
    assert response.status_code == 200
    data = response.json()
    # confere se autenticou e se o token bate
    assert data["authenticated"] is True
    assert data["token"] == token


# Step 12: Testar Bearer sem token
def test_bearer_token_missing():
    response = safe_request("GET", f"{HTTPBIN}/bearer")
    assert response.status_code == 401  # sem token nao passa


# Step 13: Validar estrutura do user 1
def test_user1_schema_types():
    response = requests.get(f"{JSONPLACEHOLDER}/users/1")
    assert response.status_code == 200
    data = response.json()
    # checa os tipos dos dados principais
    assert isinstance(data["id"], int)
    assert isinstance(data["name"], str)
    assert isinstance(data["address"], dict)
    assert isinstance(data["company"], dict)


# Step 14: Ver se o address tem as chaves certas
def test_user1_address_fields():
    response = requests.get(f"{JSONPLACEHOLDER}/users/1")
    data = response.json()
    address = data["address"]
    # precisa ter essas 3 chaves no endereco
    for key in ["street", "city", "zipcode"]:
        assert key in address


# Step 15: Validar o post 10
def test_post10_fields():
    response = requests.get(f"{JSONPLACEHOLDER}/posts/10")
    assert response.status_code == 200
    data = response.json()
    # checa tipos e se os textos nao tao vazios
    assert isinstance(data["userId"], int)
    assert isinstance(data["id"], int)
    assert isinstance(data["title"], str) and len(data["title"]) > 0
    assert isinstance(data["body"], str) and len(data["body"]) > 0


# Step 16: Ver estrutura das fotos do album 1
def test_album1_photos_structure():
    response = requests.get(f"{JSONPLACEHOLDER}/albums/1/photos")
    assert response.status_code == 200
    photos = response.json()
    # cada foto precisa ter essas chaves
    for photo in photos:
        for key in ["albumId", "id", "title", "url", "thumbnailUrl"]:
            assert key in photo


# Step 17: Validar formato do email do user 3
def test_user3_email_format():
    response = requests.get(f"{JSONPLACEHOLDER}/users/3")
    data = response.json()
    email = data["email"]
    # so checa se tem @ e . no email
    assert "@" in email and "." in email.split("@")[-1]


# Step 18: Comentarios do post 5 nao podem estar vazios
def test_post5_comments_not_empty():
    response = requests.get(f"{JSONPLACEHOLDER}/posts/5/comments")
    assert response.status_code == 200
    comments = response.json()
    assert len(comments) > 0


# Step 19: Validar estrutura do primeiro comentario
def test_first_comment_structure():
    response = requests.get(f"{JSONPLACEHOLDER}/posts/5/comments")
    comments = response.json()
    first = comments[0]
    # confere tipos basicos dos campos
    assert isinstance(first["postId"], int)
    assert isinstance(first["id"], int)
    assert isinstance(first["name"], str)
    assert isinstance(first["email"], str)
    assert isinstance(first["body"], str)


# Step 20: Validar se o campo completed é bool
def test_todo199_completed_boolean():
    response = requests.get(f"{JSONPLACEHOLDER}/todos/199")
    assert response.status_code == 200
    data = response.json()
    # completed tem que ser booleano
    assert isinstance(data["completed"], bool)
