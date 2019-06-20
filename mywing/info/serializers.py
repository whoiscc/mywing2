#

from rest_framework import serializers
from mywing.info.models import News, BoardSnapshot, BoardSnapshotItem, Board


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class BoardSnapshotItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardSnapshotItem
        fields = '__all__'


class BoardSnapshotSerializer(serializers.ModelSerializer):
    items = BoardSnapshotItemSerializer(many=True, read_only=True)
    class Meta:
        model = BoardSnapshot
        fields = '__all__'


class LatestSnapshotField(serializers.RelatedField):
    def to_representation(self, snapshots):
        return BoardSnapshotSerializer(snapshots.all()[0]).data


class BoardSerializer(serializers.ModelSerializer):
    latest_snapshot = LatestSnapshotField(source='snapshots', read_only=True)
    class Meta:
        model = Board
        fields = '__all__'
