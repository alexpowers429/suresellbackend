from rest_framework import serializers
from .models import Car, SellingFeatures



class CarSerializer(serializers.HyperlinkedModelSerializer):
    features = serializers.HyperlinkedRelatedField(
        view_name='feature_detail',
        many=True,
        read_only=True
    )
    car_url = serializers.ModelSerializer.serializer_url_field(
        view_name='car_detail'
    )

    class Meta:
        model = Car
        fields = ['id', 'year', 'make', 'model', 'trim', 'features', 'car_url']


class FeatureSerializer(serializers.HyperlinkedModelSerializer):
    car = serializers.HyperlinkedRelatedField(
        view_name='car_detail',
        read_only=True
    )

    car_id = serializers.PrimaryKeyRelatedField(
        queryset=Car.objects.all(),
        source='car'

    )

    class Meta:
        model = SellingFeatures
        fields = ['id', 'car', 'car_id', 'feat1', 'feat2',
                  'feat3', 'feat4', 'feat5', 'feat6', 'feat7', 'feat8', 'feat9', 'feat10']

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     car = serializers.HyperlinkedRelatedField(
#         view_name='car_list',
#         read_only=True
#     )

    # car_id = serializers.PrimaryKeyRelatedField(
    #     queryset=Car.objects.all(),
    #     source='car'
    # )

    # class Meta:
    #     model = User
    #     fields = ['id', 'car', 'car_id', 'username', 'email', 'password']