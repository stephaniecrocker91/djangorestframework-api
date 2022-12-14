from rest_framework import serializers
from posts.models import Post
from likes.models import Like
from bookmarks.models import Bookmark


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")
    like_id = serializers.SerializerMethodField()
    bookmark_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    bookmarks_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError(
                "Image size too large! Must be under 2MB!"
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                "Image height too large! Must be under 4096px!"
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                "Image width too large! Must be under than 4096px!"
            )
        return value

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context["request"].user
        if user.is_authenticated:
            liked = Like.objects.filter(owner=user, post=obj).first()
            return liked.id if liked else None
        return None

    def get_bookmark_id(self, obj):
        user = self.context["request"].user
        if user.is_authenticated:
            bookmarked = Bookmark.objects.filter(owner=user, post=obj).first()
            return bookmarked.id if bookmarked else None
        return None

    class Meta:
        model = Post
        fields = [
            "id",
            "owner",
            "is_owner",
            "profile_id",
            "profile_image",
            "created_at",
            "updated_at",
            "title",
            "content",
            "image",
            "image_filter",
            "like_id",
            "bookmark_id",
            "likes_count",
            "comments_count",
            "bookmarks_count",
        ]
