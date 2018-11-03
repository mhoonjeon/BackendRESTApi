from rest_framework import serializers

from profiles.serializers import ProfileSerializer

from .models import Article, Comment, Tag
from .relations import TagRelatedField


class ArticleSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(read_only=True)
    description = serializers.CharField(required=False)
    slug = serializers.SlugField(required=False)

    favorited = serializers.SerializerMethodField()
    favoritesCount = serializers.SerializerMethodField(
        method_name='get_favorites_count'
    )

    tagList = TagRelatedField(many=True, required=False, source='tags')

    created = serializers.SerializerMethodField(method_name='get_created')
    modified = serializers.SerializerMethodField(method_name='get_modified')

    class Meta:
        model = Article
        fields = (
            'author',
            'body',
            'created',
            'description',
            'favorited',
            'favoritesCount',
            'slug',
            'tagList',
            'title',
            'modified',
        )

    def create(self, validated_data):
        author = self.context.get('author', None)

        tags = validated_data.pop('tags', [])

        article = Article.objects.create(author=author, **validated_data)

        for tag in tags:
            article.tags.add(tag)

        return article

    def get_created(self, instance):
        return instance.created.isoformat()

    def get_favorited(self, instance):
        request = self.context.get('request', None)

        if request is None:
            return False

        if not request.user.is_authenticated():
            return False

        return request.user.profile.has_favorited(instance)

    def get_favorites_count(self, instance):
        return instance.favorited_by.count()

    def get_modified(self, instance):
        return instance.modified.isoformat()


class CommentSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(required=False)

    created = serializers.SerializerMethodField(method_name='get_created')
    modified = serializers.SerializerMethodField(method_name='get_modified')

    class Meta:
        model = Comment
        fields = (
            'id',
            'author',
            'body',
            'created',
            'modified',
        )

    def create(self, validated_data):
        article = self.context['article']
        author = self.context['author']

        return Comment.objects.create(
            author=author, article=article, **validated_data
        )

    def get_created(self, instance):
        return instance.created.isoformat()

    def get_modified(self, instance):
        return instance.modified.isoformat()


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('tag',)

    def to_representation(self, obj):
        return obj.tag
