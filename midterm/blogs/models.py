from django.db import models
import requests
import requests
import requests


class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    owner = models.CharField(max_length=255)


url = "http://yourwebsite.com/api/blogs"
response = requests.get(url)

if response.status_code == 200:
    blogs = response.json()
    print(blogs)
else:
    print("Ошибка при получении списка блогов")
    var = [
        {
            "id": 1,
            "title": "Blog 1 1",
            "description": "Blog 2 2",
            "owner": "Blog 3 3"
        },
        {
            "id": 2,
            "title": "Blog 1 1 1",
            "description": "Blog 2 2 2",
            "owner": "Blog 3 3 3"
        },
        {
            "id": 3,
            "title": "Blog 1",
            "description": "Blog 2",
            "owner": "Blog 3"
        }
    ]

url = "http://yourwebsite.com/api/blogs"

new_blog = {
    "title": "Blog 1",
    "description": "Blog 2",
    "owner": "Blog 3"
}

response = requests.post(url, json=new_blog)

if response.status_code == 201:
    created_blog = response.json()
    print(created_blog)
else:
    print("Ошибка")
var = {
    "id": 4,
    "title": "Blog 1",
    "description": "Blog 2",
    "owner": "Blog 3"
}

url = "http://yourwebsite.com/api/blogs/4"

response = requests.get(url)

if response.status_code == 200:
    blog = response.json()
    print(blog)
else:
    print("Ошибка при получении блога")
    var = {
        "id": 4,
        "title": "Blog 1",
        "description": "Blog 2",
        "owner": "Blog 3"
    }