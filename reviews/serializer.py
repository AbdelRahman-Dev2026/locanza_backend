from rest_framework import serializers

from .models import Review

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            'id',
            'user',
            'rating',
            'comment',
            'created_at',
        )

        read_only_fields = (
            'user',
            'created_at',
        )
