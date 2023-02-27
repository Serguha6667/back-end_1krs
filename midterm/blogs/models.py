from django.db import models
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
    print("Ошибка")
    var = [
        {
            "id": 1,
            "title": "Новый блог",
            "description": "еще новый блог",
            "owner": "Tobyl Sanat"
        },
        {
            "id": 2,
            "title": "Новый блог",
            "description": "еще новый блог",
            "owner": "Tobyl Sanat"
        },
        {
            "id": 3,
            "title": "Новый блог",
            "description": "еще новый блог",
            "owner": "Tobyl Sanat"
        }
    ]

url = "http://yourwebsite.com/api/blogs"

new_blog = {
    "title": "Новый блог",
    "description": "еще новый блог",
    "owner": "Tobyl Sanat"
}

response = requests.post(url, json=new_blog)

if response.status_code == 201:
    created_blog = response.json()
    print(created_blog)
else:
    print("Ошибка при создании блога")
var = {
    "id": 4,
    "title": "Новый блог",
    "description": "еще новый блог",
    "owner": "Tobyl Sanat"
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
        "title": "Новый блог",
        "description": "еще новый блог",
        "owner": "Tobyl Sanat"
    }