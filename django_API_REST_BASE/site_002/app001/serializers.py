from rest_framework import serializers
from app001.models import App001, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

"""
class App001Serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={"base_template","textarea.html"})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES,default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES,default="friendly")
    
    def create(self, validated_data):
        return App001.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.code = validated_data.get("code", instance.code) 
        instance.linenos = validated_data.get("linenos", instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
"""
"""
class App001Serializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = App001
        fields = ("id", 'owner', 'title', 'code', "linenos", "language", "style")
"""
class App001Serializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='app001-highlight', format='html')
    
    class Meta:
        model = App001
        fields = ("url","id","highlight","owner","title","code","linenos","language",'style')


"""
class UserSerializer(serializers.ModelSerializer):
    app001s = serializers.PrimaryKeyRelatedField(many=True, queryset=App001.objects.all())

    class Meta:
        model = User
        fields = ("id","username","app001s")
"""
class UserSerializer(serializers.HyperlinkedModelSerializer):
    app001s = serializers.HyperlinkedRelatedField(many=True,view_name="app001-detail",read_only=True)
    
    class Meta:
        model = User
        fields = ('url', 'id', 'username', "app001s")
