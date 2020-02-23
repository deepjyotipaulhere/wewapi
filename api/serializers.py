from rest_framework import serializers
from .models import Blog, Users



class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('fullname','email',)
        # fields='__all__'


class BlogSerializer(serializers.ModelSerializer):
    users=UsersSerializer( read_only=True)
    class Meta:
        model = Blog
        fields = '__all__'
