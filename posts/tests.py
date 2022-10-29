from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username="adam", password="pass")

    def test_can_list_posts(self):
        adam = User.objects.get(username="adam")
        Post.objects.create(owner=adam, title="a title")
        response = self.client.get("/posts/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_post(self):
        self.client.login(username="adam", password="pass")
        response = self.client.post("/posts/", {"title": "a title"})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_post(self):
        response = self.client.post("/posts/", {"title": "a title"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PostDetailViewTests(APITestCase):
    def setUp(self):
        steph = User.objects.create_user(username="steph", password="123")
        flavio = User.objects.create_user(username="flavio", password="123")
        Post.objects.create(
            owner=steph, title="title 1", content="stephs content"
        )
        Post.objects.create(
            owner=flavio, title="title 2", content="flavios content"
        )

    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get("/posts/1/")
        self.assertEqual(response.data["title"], "title 1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_post_using_invalid_id(self):
        response = self.client.get("/posts/999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_post(self):
        self.client.login(username="steph", password="123")
        response = self.client.put("/posts/1/", {"title": "new title"})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, "new title")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_post(self):
        self.client.login(username="steph", password="123")
        response = self.client.put("/posts/2/", {"title": "new title"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
