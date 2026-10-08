import requests

def test_get_posts_one():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == 1
    print(f"\nУспех! Заголовок поста: {response_data['title']}")