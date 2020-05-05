from rest_framework.serializers import ModelSerializer
from .models import Tag, Category, Article
from authentication.serializers import UserSerializer


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'slug']


class ArticleSerializer(ModelSerializer):
    tags = TagSerializer(read_only=True)
    author = UserSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ['title', 'slug', 'body_html', 'summary_html', 'created_at', 'updated_at','author','tags']
