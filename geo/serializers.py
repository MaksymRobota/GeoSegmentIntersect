from rest_framework import serializers
from .models import Rect, Segment


class SegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Segment
        fields = ['x1', 'y1', 'x2', 'y2']


class RectSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=30)
    segments = SegmentSerializer(many=True, write_only=True)

    class Meta:
        model = Rect
        fields = ['name', 'segments']

    def create(self, validated_data):
        segments_data = validated_data.pop('segments', [])
        name = validated_data.pop('name')
        rect = Rect.objects.create(name=name)

        for segment_data in segments_data:
            Segment.objects.create(rect=rect, **segment_data)

        return rect
