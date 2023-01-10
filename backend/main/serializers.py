from rest_framework import serializers

from .models import News


class NewsInfo(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
