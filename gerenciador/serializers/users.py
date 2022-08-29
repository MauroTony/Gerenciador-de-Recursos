from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Users


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = Users
        fields = ["username", "password", "password2"]
        extra_kwargs = {"password": {"write_only": True}}

    def create_user(self):
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]
        if password != password2:
            raise serializers.ValidationError({"password": "Passwords must match."})
        user = get_user_model().objects.create_user(
            username=self.validated_data["username"], password=password
        )
        return user

    def create_superuser(self):
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]
        if password != password2:
            raise serializers.ValidationError({"password": "Passwords must match."})
        user = get_user_model().objects.create_superuser(
            username=self.validated_data["username"], password=password
        )

        return user


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(
        style={"input_type": "password"}, required=True
    )
    new_password = serializers.CharField(
        style={"input_type": "password"}, required=True
    )

    def validate_current_password(self, value):
        if not self.context["request"].user.check_password(value):
            raise serializers.ValidationError({"current_password": "Does not match"})
        return value


class DeleteUserSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)

    def validate_username(self, value):
        if value == self.context["request"].user.username:
            raise serializers.ValidationError({"msg": "You cannot delete yourself"})
        return value

    def delete_user(self):
        try:
            user = get_user_model().objects.get(
                username=self.validated_data["username"]
            )
        except get_user_model().DoesNotExist:
            raise serializers.ValidationError({"msg": "User does not exist"})
        user.delete()
        return user
