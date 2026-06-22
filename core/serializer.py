from rest_framework import serializers

from .models import Banner,Slider,HomeCategory

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = (
            'title',
            'image',
            'link',
            'is_active',
            'created_at',
        )

        read_only_fields = ('is_active','created_at',)

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = (
            'title',
            'image',
            'order',
            'created_at',
            'is_active',

        )
        read_only_fields = ('is_active','created_at',)

class HomeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeCategory
        fields = (
            'title',
            'slug',
            'is_active',
        )
        read_only_fields = ('is_active',)