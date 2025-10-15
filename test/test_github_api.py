import requests

BASE_URL = "https://api.github.com"

# Step 1
def test_base_request():
    response = requests.get(BASE_URL)
    assert response.status_code == 200

# Step 2
def test_fetch_user_octocat():
    response = requests.get(f"{BASE_URL}/users/octocat")
    assert response.status_code == 200
    data = response.json()
    assert data.get("login") == "octocat"

# Step 3
def test_user_type():
    response = requests.get(f"{BASE_URL}/users/octocat")
    data = response.json()
    assert data.get("type") == "User"

# Step 4
def test_repo_by_id():
    response = requests.get(f"{BASE_URL}/repositories/1296269")
    assert response.status_code == 200
    data = response.json()
    assert data.get("name") == "Hello-World"

# Step 5
def test_nonexistent_user():
    response = requests.get(f"{BASE_URL}/users/nonexistentuser12345")
    assert response.status_code == 404

# Step 6
def test_list_user_repos():
    response = requests.get(f"{BASE_URL}/users/google/repos", params={"per_page": 5})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) <= 5

#Step 7
def test_followers_pagination():
    url = f"{BASE_URL}/users/microsoft/followers?per_page=5"
    response = requests.get(url)
    assert response.status_code == 200
    followers = response.json()
    assert len(followers) <= 5
    # Check if there's a next page
    link_header = response.headers.get("Link")
    if link_header:
        assert 'rel="next"' in link_header

#Step 8
def test_facebook_public_repos_count():
    url = f"{BASE_URL}/users/facebook"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert "public_repos" in data
    assert isinstance(data["public_repos"], int)

# Step 9
def test_facebook_react_languages():
    url = f"{BASE_URL}/repos/facebook/react/languages"
    response = requests.get(url)
    assert response.status_code == 200
    languages = response.json()
    assert "JavaScript" in languages

# Step 10
def test_emoji_endpoint():
    url = f"{BASE_URL}/emojis"
    response = requests.get(url)
    assert response.status_code == 200
    emojis = response.json()
    assert "+1" in emojis

# Step 11
def test_torvalds_linux_json_structure():
    url = f"{BASE_URL}/repos/torvalds/linux"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    for key in ["name", "owner", "language"]:
        assert key in data

# Step 12
def test_compare_stargazers_vscode_atom():
    vscode = requests.get(f"{BASE_URL}/repos/microsoft/vscode").json()
    atom = requests.get(f"{BASE_URL}/repos/atom/atom").json()
    assert vscode["stargazers_count"] > atom["stargazers_count"]

# Step 13
def test_fetch_mit_license():
    url = f"{BASE_URL}/licenses/mit"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data["name"].lower() == "mit license"

# Step 14
def test_list_licenses():
    url = f"{BASE_URL}/licenses"
    response = requests.get(url)
    assert response.status_code == 200
    licenses = response.json()
    assert len(licenses) > 0

# Step 15
def test_search_apache2_license():
    url = f"{BASE_URL}/search/repositories?q=license:apache-2.0&per_page=1"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert "items" in data
    assert len(data["items"]) > 0

# Step 16 
def test_docker_repo_organization():
    url = f"{BASE_URL}/repos/moby/docker"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data["owner"]["login"] == "moby"

# Step 17
def test_last_commit_tensorflow():
    url = f"{BASE_URL}/repos/tensorflow/tensorflow/commits"
    response = requests.get(url)
    assert response.status_code == 200
    commits = response.json()
    assert len(commits) > 0
    assert "commit" in commits[0]
    assert commits[0]["commit"]["message"] != ""

# Step 18: 
def test_apple_is_organization():
    url = f"{BASE_URL}/users/apple"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data["type"] == "Organization"

# Step 19
def test_kubernetes_contributors_count():
    url = f"{BASE_URL}/repos/kubernetes/kubernetes/contributors?per_page=10"
    response = requests.get(url)
    assert response.status_code == 200
    contributors = response.json()
    # Valida se retornou uma lista de contribuidores
    assert isinstance(contributors, list)
    assert len(contributors) > 0  # Ao menos 1 contribuidor

# Step 20: Final 
def fetch_user_info(username):
    url = f"{BASE_URL}/users/{username}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    data = response.json()
    return {
        "login": data.get("login"),
        "name": data.get("name"),
        "public_repos": data.get("public_repos"),
    }

def test_fetch_torvalds_info():
    info = fetch_user_info("torvalds")
    assert info is not None
    assert info["login"].lower() == "torvalds"
    assert isinstance(info["public_repos"], int)
