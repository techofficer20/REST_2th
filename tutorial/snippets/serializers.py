from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


"""
class SnippetSerializer(serializers.Serializer):

    # id (pk 값) 정수. read_only true로 값 변할 수 없도록 설정
    id = serializers.IntegerField(read_only=True)
    # title (allow_blank: 공백 허용. required: 굳이 입력을 하지 않아도 된다.)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    # code
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    # linenos (required: 굳이 입력을 하지 않아도 된다.)
    linenos = serializers.BooleanField(required=False)
    # language
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    # style
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):

        # Create and return a new `Snippet` instance, given the validated data.

        return Snippet.objects.create(**validated_data) # validated_data를 unpacking 해서 객체를 생성

    def update(self, instance, validated_data):

        # Update and return an existing `Snippet` instance, given the validated data.

        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
"""

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']