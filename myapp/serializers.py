from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from .models import *

class AvatarSerializer(serializers.ModelSerializer):
    image = serializers.CharField()

    class Meta:
        model = Avatar
        fields = ('pk', 'image',)


class SiteSerializer(serializers.ModelSerializer):
    url = serializers.CharField()

    class Meta:
        model = Site
        fields = ('pk', 'url',)


class AccessKeySerializer(serializers.ModelSerializer):

    class Meta:
        model = AccessKey
        fields = ('pk', 'key',)


class ProfileSerializer(WritableNestedModelSerializer):
    # Direct ManyToMany relation
    sites = SiteSerializer(many=True)

    # Reverse FK relation
    avatars = AvatarSerializer(many=True)

    # Direct FK relation
    access_key = AccessKeySerializer(allow_null=True)

    class Meta:
        model = Profile
        fields = ('pk', 'sites', 'avatars', 'access_key',)


class UserSerializer(WritableNestedModelSerializer):
    # Reverse OneToOne relation
    profile = ProfileSerializer()

    class Meta:
        model = MyUser
        fields = ('pk', 'profile', 'username',)

class SecurityQuestionSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(required=False)
    class Meta:
        model = SecurityQuestion
        fields=['id','questions']

class DataSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(required=False)
    data=SecurityQuestionSerializer(many=True)
    class Meta:
        model = Data
        fields=['id','email','age','is_merchant','data']

    
class UserDataSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(required=False)
    user_data=DataSerializer()
    class Meta:
        model = MyUser
        fields=['id','username','user_data']

    def create(self, validated_data):
        user_data=validated_data.pop('user_data')
        data=user_data.pop('data')
        user=MyUser.objects.create(**validated_data)
        mydata=Data.objects.create(**user_data,user=user)
        for i in range(len(data)):
            dict_data=dict(data[i])
            SecurityQuestion.objects.create(**dict_data,data=mydata)
        return user
    
    def update(self, instance, validated_data):
        user_data=validated_data.pop('user_data')
        data=user_data.pop('data')
        instance.username=validated_data.get('username',instance.username)
        instance.save()
        data_instance=Data.objects.filter(user=instance).first()
        data_instance.email=user_data.get('email',data_instance.email)
        data_instance.age=user_data.get('age',data_instance.age)
        data_instance.save()
        question_instance=SecurityQuestion.objects.filter(data=data_instance)
        for i in range(len(data)):
            dict_data=dict(data[i])
            q=SecurityQuestion.objects.get(id=question_instance[i].id)
            q.questions=dict_data.get('questions',q.questions)
            q.save()
        return instance



# ManyToMany Practice Serializers

class TagSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(required=False)
    class Meta:
        model = Tag
        fields=['id','name']


class PostSerializer(serializers.ModelSerializer):
    tags=TagSerializer(many=True)

    class Meta:
        model = Post
        fields=['title','description','tags']

    def create(self, validated_data):
        tags=validated_data.pop('tags')
        post=Post.objects.create(**validated_data)
        for tag in tags:
            tag_data=Tag.objects.create(name=tag.get('name'))
            post.tags.add(tag_data)
            post.save()
        return post

    def update(self,instance ,validated_data):
        tags=validated_data.pop('tags')
        instance.title=validated_data.get('title',instance.title)
        instance.description=validated_data.get('description',instance.description)
        instance.save()
        for i in range(len(tags)):
            data=dict(tags[i])
            if data.get('id') is not None:
                tag_id=Tag.objects.filter(id=data.get('id')).first()
                update_tag=Tag.objects.get(id=tag_id.id)
                update_tag.name=data.get('name')
                update_tag.save()
            else:
                tag_data=Tag.objects.create(name=data.get('name'))
                instance.tags.add(tag_data)
                instance.save()
        return instance