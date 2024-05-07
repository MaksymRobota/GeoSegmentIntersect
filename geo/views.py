from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Rect, Segment
from .segment_service import find_rects_intersecting_with_segment
from .serializers import RectSerializer, SegmentSerializer


class RectList(generics.ListAPIView):
    queryset = Rect.objects.all()
    serializer_class = RectSerializer


class SegmentList(generics.ListAPIView):
    queryset = Segment.objects.all()
    serializer_class = SegmentSerializer


class RectCreate(generics.CreateAPIView):
    queryset = Rect.objects.all()
    serializer_class = RectSerializer


class SearchRectsIntersectingSegment(APIView):
    def post(self, request):
        data = request.data
        x1 = data.get('x1')
        y1 = data.get('y1')
        x2 = data.get('x2')
        y2 = data.get('y2')

        if x1 is None or y1 is None or x2 is None or y2 is None:
            return Response("Segment coordinates missing", status=status.HTTP_400_BAD_REQUEST)

        intersecting_rects = find_rects_intersecting_with_segment(x1, y1, x2, y2)

        intersecting_rect_names = [rect.name for rect in intersecting_rects]

        return Response({"intersecting_rect_names": intersecting_rect_names}, status=status.HTTP_200_OK)
