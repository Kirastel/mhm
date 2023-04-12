from rest_framework import serializers

from main.models import Property, Entity


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'


class EntitySerializer(serializers.ModelSerializer):
    properties = PropertySerializer(many=True)

    class Meta:
        model = Entity
        fields = ('id', 'modified_by', 'value', 'properties')
        read_only_fields = ('id',)

    def create(self, validated_data):
        # properties_data = validated_data.pop('properties')
        user = self.context['request'].user
        validated_data['modified_by'] = user
        entity = Entity.objects.create(value=validated_data['data']['value'], modified_by=user)
        # entity = Entity.objects.create(**validated_data)
        # for property_data in properties_data:
        #     Property.objects.create(entity=entity, **property_data)
        return entity