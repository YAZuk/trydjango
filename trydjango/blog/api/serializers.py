from ..models import Article
from rest_framework.serializers import (
                                        Serializer,
                                        ListSerializer,
                                        BaseSerializer,
                                        HyperlinkedModelSerializer,
                                        ModelSerializer
                                        )


class ArticleSerializer(Serializer):

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
