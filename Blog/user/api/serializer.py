from django.contrib.auth.models import User

from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from user.utils import normalise_email


# Serializers define the API representation.
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

    def validate(self, data):
        email = normalise_email(data["email"])
        if User._default_manager.filter(email__iexact=email).exists():
            raise serializers.ValidationError(_("A user with that email address already exists"))
        return data

    def create(self, validated_data):
        user = super(RegisterSerializer, self).create(validated_data)
        user.username = validated_data['email']
        user.set_password(validated_data['password'])
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, data):
        user = authenticate(username=data['email'], password=data['password'])
        if user is None:
            raise serializers.ValidationError(_('invalid login'))
        elif not user.is_active:
            raise serializers.ValidationError(
                _('Can not log in as inactive user'))
        self.instance = user
        return data
