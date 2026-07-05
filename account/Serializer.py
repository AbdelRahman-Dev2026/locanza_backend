from rest_framework import serializers


from .models import User

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, )
    password = serializers.CharField(required=True,write_only=True, )


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'phone_number',
            'role'
        ]

        extra_kwargs = {
            'password': {'write_only': True, }
        }
    # انشاء user استدعائه
    def create(self, validated_data ):
        user = User.objects.create_user(

            email = validated_data['email'],
            password = validated_data['password'],
            phone_number = validated_data['phone_number'],
            role = validated_data['role']

        )
        return user


class ChangePasswordSerializer(serializers.Serializer):

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

























