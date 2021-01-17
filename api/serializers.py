from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
    
    class Meta:
        model = Snippet
        fields = ['url', 'id', 'title', 'code', 'highlight','owner','linenos', 'language', 'style']
    

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)


    class Meta:
        model = get_user_model()
        fields = ['url', 'id', 'username', 'snippets']