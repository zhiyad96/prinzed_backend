from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import (MarketingSolution, Portfolio, Service, Coomessage, Teammembers, Creative, Desinglist, Reviews )




class Marketingsolutionserializer(ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = MarketingSolution
        fields = "__all__"
       
    def get_image(self, obj):
        request = self.context.get("request")
        if obj.image:
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        if obj.image_url:
            return obj.image_url
        return None


class Portfolioserializer(ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = Portfolio
        fields = "__all__"
        
    
    def get_image(self, obj):
        request = self.context.get("request")
        if obj.image:
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        if obj.image_url:
            return obj.image_url
        return None


class Serviceserializer(ModelSerializer):
    
    image = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = "__all__"
        
    def get_image(self, obj):
        request = self.context.get("request")
        if obj.image:
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        if obj.image_url:
            return obj.image_url
        return None


class CooMessageserializer(ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = Coomessage
        fields = "__all__"
        
    def get_image(self, obj):
        request = self.context.get("request")
        if obj.image:
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        if obj.image_url:
            return obj.image_url
        return None


class TeamMembersserializer(ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Teammembers
        fields = "__all__"
    
    def get_image(self, obj):
        request = self.context.get("request")
        if obj.image:
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        if obj.image_url:
            return obj.image_url
        return None


class Creativeserializer(ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Creative
        fields = "__all__"
        
    def get_image(self, obj):
        request = self.context.get("request")
        if obj.image:
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        if obj.image_url:
            return obj.image_url
        return None
        
class Desinglistserializer(ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model=Desinglist
        fields='__all__'
        
    def get_image(self, obj):
        request = self.context.get("request")
        if obj.image:
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        if obj.image_url:
            return obj.image_url
        return None
    
    
class Reviewserializer(ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Reviews
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get("request")
        if obj.image:
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        if obj.image_url:
            return obj.image_url
        return None
    
class coreserviceserializer(ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Reviews
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get("request")
        if obj.image:
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        if obj.image_url:
            return obj.image_url
        return None