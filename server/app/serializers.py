from django.contrib.auth.models import User, Group
from app.models import Team, RoleTeam, UserTeam, RoleTeam, Project
from rest_framework import serializers

from django.shortcuts import render


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'url', 'name')
        read_only_fields = ('id', 'url',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = User
        fields = (
            'id', 'url', 'is_active',
            'first_name', 'last_name', 
            'username', 'email', 'groups',)
        read_only_fields = ('id', 'url', )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # for user registration password
        # don't touch this!!!
        user = User.objects.create_user(**validated_data)
        return user

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name')
        read_only_fields = ('id', )


class UserTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTeam
        fields = ('id', 'user', 'team', 'is_active')
        read_only_fields = ('id', )


class RoleTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleTeam
        fields = ('id', 'user_team', 'role')
        read_only_fields = ('id', )

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'code', 'name', 'client', 'start_date', 'end_date', 'board', 'team')
        read_only_fields = ('id', )
        