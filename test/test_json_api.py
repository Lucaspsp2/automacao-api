import requests

# URL base da API fake que vamos usar para treinar os métodos (GET, POST, PUT, PATCH, DELETE)
BASE_URL = "https://jsonplaceholder.typicode.com"


# TESTE 21 - Criar um novo post (método POST)
def test_create_post():
    # Aqui eu monto o corpo (payload) com as informações que quero enviar
    payload = {"title": "foo", "body": "bar", "userId": 1}

    # Envio uma requisição POST para criar o post
    r = requests.post(f"{BASE_URL}/posts", json=payload)

    # A API deve responder com status 201 (criado com sucesso)
    assert r.status_code == 201

    # Converto o retorno da API para JSON pra poder acessar os dados
    data = r.json()

    # Verifico se os dados retornados batem com o que enviei
    assert data.get("title") == payload["title"]
    assert data.get("body") == payload["body"]

    # Comparo o userId convertendo pra int pra evitar erro de tipo
    assert int(data.get("userId")) == payload["userId"]

    # Verifico se a resposta tem um ID (isso indica que o post foi criado)
    assert "id" in data


# TESTE 22 - Validar os dados do post criado
def test_validate_created_post_data():
    payload = {"title": "hello", "body": "world", "userId": 2}
    r = requests.post(f"{BASE_URL}/posts", json=payload)
    assert r.status_code == 201
    data = r.json()

    # Confirmando se a API retornou os mesmos valores
    assert data["title"] == "hello"
    assert data["body"] == "world"
    assert data["userId"] == 2


# TESTE 23 - Atualizar um post existente (método PUT)
def test_update_post_put():
    update_payload = {
        "id": 1,
        "title": "título atualizado",
        "body": "corpo atualizado",
        "userId": 1
    }
    r = requests.put(f"{BASE_URL}/posts/1", json=update_payload)
    assert r.status_code == 200
    data = r.json()

    # O JSONPlaceholder retorna o mesmo payload que a gente enviou
    assert data["title"] == update_payload["title"]
    assert data["body"] == update_payload["body"]


# TESTE 24 - Validar atualização do post
def test_validate_post_update_put():
    update_payload = {"id": 1, "title": "x", "body": "y", "userId": 1}
    r = requests.put(f"{BASE_URL}/posts/1", json=update_payload)
    assert r.status_code == 200
    data = r.json()

    # Conferindo se os dados realmente foram atualizados
    assert data["title"] == "x"
    assert data["body"] == "y"


# TESTE 25 - Deletar um post (método DELETE)
def test_delete_post():
    r = requests.delete(f"{BASE_URL}/posts/1")

    # O JSONPlaceholder geralmente responde com 200 ou 204
    assert r.status_code in [200, 204]


# TESTE 26 - Listar todos os usuários (método GET)
def test_list_all_users():
    r = requests.get(f"{BASE_URL}/users")
    assert r.status_code == 200
    users = r.json()

    # Verifico se o retorno é uma lista e tem 10 usuários
    assert isinstance(users, list)
    assert len(users) == 10


# TESTE 27 - Buscar um usuário específico (id = 5)
def test_fetch_user_5_name():
    r = requests.get(f"{BASE_URL}/users/5")
    assert r.status_code == 200
    user = r.json()

    # Conferindo o nome do usuário 5 no dataset fixo da API
    assert user.get("name") == "Chelsey Dietrich"


# TESTE 28 - Criar um comentário novo no post 1
def test_create_comment_for_post():
    payload = {"postId": 1, "name": "tester", "email": "t@test.com", "body": "nice post"}
    r = requests.post(f"{BASE_URL}/posts/1/comments", json=payload)
    assert r.status_code == 201
    data = r.json()

    # Converto pra int pra garantir o tipo certo
    assert int(data.get("postId")) == 1
    assert data.get("name") == "tester"


# TESTE 29 - Listar os álbuns do usuário 3
def test_list_user_3_albums():
    r = requests.get(f"{BASE_URL}/users/3/albums")
    assert r.status_code == 200
    albums = r.json()

    assert isinstance(albums, list)
    assert len(albums) >= 0  # só uma verificação básica



# TESTE 30 - Listar fotos do álbum 2 e checar o título da primeira
def test_list_photos_album_2_first_title():
    r = requests.get(f"{BASE_URL}/albums/2/photos")
    assert r.status_code == 200
    photos = r.json()
    assert isinstance(photos, list)
    assert len(photos) > 0

    first_title = photos[0].get("title", "")
    expected_start = "non sunt voluptatem"
    assert first_title.startswith(expected_start)


# TESTE 31 - Criar uma nova tarefa
def test_create_todo_for_user_1():
    payload = {"userId": 1, "title": "Aprender Pytest", "completed": False}
    r = requests.post(f"{BASE_URL}/todos", json=payload)
    assert r.status_code == 201
    data = r.json()
    assert data.get("title") == "Aprender Pytest"
    assert data.get("userId") == 1


# TESTE 32 - Atualizar uma tarefa (PATCH)
def test_patch_todo_set_completed():
    payload = {"completed": True}
    r = requests.patch(f"{BASE_URL}/todos/5", json=payload)
    assert r.status_code == 200
    data = r.json()

    # A API retorna o campo atualizado (simulação)
    assert data.get("completed") is True


# TESTE 33 - Listar tarefas concluídas do usuário 1
def test_list_user_1_completed_tasks():
    r = requests.get(f"{BASE_URL}/todos", params={"userId": 1, "completed": "true"})
    assert r.status_code == 200
    todos = r.json()

    assert isinstance(todos, list)
    for t in todos:
        assert t.get("completed") is True


# TESTE 34 - Validar a estrutura de um comentário
def test_comment_10_structure():
    r = requests.get(f"{BASE_URL}/comments/10")
    assert r.status_code == 200
    c = r.json()
    for key in ["postId", "id", "name", "email", "body"]:
        assert key in c


# TESTE 35 - Deletar um comentário (id = 3)
def test_delete_comment_3():
    r = requests.delete(f"{BASE_URL}/comments/3")
    assert r.status_code in [200, 204]


# TESTE 36 - Criar um post com corpo vazio (dados inválidos)
def test_create_post_with_empty_body():
    r = requests.post(f"{BASE_URL}/posts", json={})
    assert r.status_code == 201
    data = r.json()
    assert "id" in data


# TESTE 37 - Buscar posts do usuário 7 e contar
def test_fetch_posts_user_7_count():
    r = requests.get(f"{BASE_URL}/posts", params={"userId": 7})
    assert r.status_code == 200
    posts = r.json()
    assert isinstance(posts, list)
    assert len(posts) >= 0


# TESTE 38 - Atualizar o email do usuário 2 (método PUT)
def test_update_user_2_email_put():
    payload = {
        "id": 2,
        "name": "Ervin Howell",
        "username": "Antonette",
        "email": "novo.email@example.com"
    }
    r = requests.put(f"{BASE_URL}/users/2", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert data.get("email") == "novo.email@example.com"



# TESTE 39 - Deletar um álbum (id = 4)
def test_delete_album_4():
    r = requests.delete(f"{BASE_URL}/albums/4")
    assert r.status_code in [200, 204]


# TESTE 40 - Fluxo completo: criar post → comentar → deletar post
def create_post_for_user(user_id, title="auto post", body="auto body"):
    payload = {"title": title, "body": body, "userId": user_id}
    r = requests.post(f"{BASE_URL}/posts", json=payload)
    return r

def add_comment_to_post(post_id, name="auto", email="auto@example.com", body="ok"):
    payload = {"postId": post_id, "name": name, "email": email, "body": body}
    r = requests.post(f"{BASE_URL}/posts/{post_id}/comments", json=payload)
    return r

def delete_post(post_id):
    r = requests.delete(f"{BASE_URL}/posts/{post_id}")
    return r

def test_full_flow_create_comment_delete_post():
    # 1️⃣ Crio um post
    r_post = create_post_for_user(9, title="fluxo completo", body="testando o fluxo")
    assert r_post.status_code == 201
    post_data = r_post.json()
    post_id = int(post_data.get("id"))
    assert post_id is not None

    # 2️⃣ Adiciono um comentário no post criado
    r_comment = add_comment_to_post(post_id, name="flow", email="f@e.com", body="nice")
    assert r_comment.status_code == 201
    comment_data = r_comment.json()
    assert int(comment_data.get("postId")) == post_id

    # 3️⃣ Finalmente deleto o post
    r_del = delete_post(post_id)
    assert r_del.status_code in [200, 204]
