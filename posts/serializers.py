from rest_framework import serializers
from .models import Posts


class PostsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError(
                'Image size too large! Must be under 2MB!'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height too large! Must be under 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width too large! Must be under than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Posts
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'image_filter',
        ]