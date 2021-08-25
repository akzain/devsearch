from rest_framework import serializers
from projects.models import *
from users.models import *


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    owner = ProfileSerializers(many=False)
    tags = TagSerializers(many=True)
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = "__all__"

    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return serializer.data
