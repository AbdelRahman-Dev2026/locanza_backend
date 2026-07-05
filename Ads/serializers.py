from rest_framework import serializers

from .models import Ad



class AdListSerializer(serializers.ModelSerializer):

    service_name = serializers.CharField(
        source='service.business_name',
        read_only=True
    )

    class Meta:
        model = Ad
        fields =(
            'id',
            'title',
            'service_name',
            'image',
            'description',
        )

#يرجع Api اكتر
class AdDetailSerializer(serializers.ModelSerializer):

    owner_email = serializers.EmailField(
        source='owner.email',
        read_only=True
    )

    class Meta:
        model = Ad
        fields = '__all__'

        read_only_fields = (
           'owner',
           'payment_status',
           'created_at',
           'is_active',
        )