from rest_framework import serializers

from users.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ["email", "user_name", "first_name", "password", "about"]

    def validate(self, attrs):
        email = attrs.get("email", "")
        user_name = attrs.get("user_name", "")
        if not user_name.isalnum():
            raise serializers.ValidationError("Username can only contain alphanumeric characters")
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
