from datetime import datetime

from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Users, Resources, ResourceScheduling

class ResourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resources
        fields = ['id', 'description', 'available']

    def create(self):
        return Resources.objects.create(**self.validated_data)

    def update(self, instance):
        instance.description = self.validated_data.get('description', instance.description)
        instance.available = self.validated_data.get('available', instance.available)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        return instance

class ResourceSchedulingSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    description = serializers.CharField(source='resource.description', read_only=True)

    class Meta:
        model = ResourceScheduling
        fields = ['id', 'resource', 'description', 'user', 'username', 'initial_date', 'final_date']

    def validate(self, data):
        resource_id = data.get('resource')
        date_ini = data.get('initial_date')
        date_now = datetime.now()
        if date_ini < date_now:
            raise serializers.ValidationError({'msg': 'The date must be greater than the current date'})
        if data['initial_date'] > data['final_date']:
            raise serializers.ValidationError({'msg': 'Start date must be less than end date'})
        get_resource = ResourceScheduling.objects.filter(resource_id=resource_id, final_date__gte=date_ini, is_deleted=False)
        if get_resource:
            for resource in get_resource:
                if resource.initial_date <= date_ini <= resource.final_date:
                    raise serializers.ValidationError({'msg': 'Resource already scheduled in this period'})
        return data

    def create(self):
        return ResourceScheduling.objects.create(**self.validated_data)

    def delete(self, instance, user):
        if instance.user == user or user.is_staff:
            instance.is_deleted = True
            instance.save()
            return instance
        else:
            raise serializers.ValidationError({'msg': 'You can only delete your own reservations'})
        return instance
