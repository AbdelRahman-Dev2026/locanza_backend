from rest_framework import serializers

from .models import Category, Serviceprofile, Product

class CategorySerializer(serializers.ModelSerializer):

        class Meta:
            model = Category
            fields = '__all__'
            read_only_fields = ('id','name')


class ServiceProfileSerializer(serializers.ModelSerializer):

    # ليعرض إيميل صاحب النشاط.
    # owner_email = serializers.EmailField(
    #     source='owner.email',
    #     read_only=True
    # )

    business_name = serializers.CharField(
        source='business_name',
        read_only=True
    )

    category_name = serializers.CharField(
        source='category.name',
        read_only=True
    )

    class Meta:
        model = Serviceprofile
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


