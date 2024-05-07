from django.urls import path
from .views import RectCreate, SearchRectsIntersectingSegment, RectList, SegmentList

urlpatterns = [
    path('create/', RectCreate.as_view(), name='rect-create'),
    path('search/', SearchRectsIntersectingSegment.as_view(), name='search-rect-by-segments'),
    path('rects/', RectList.as_view(), name='rect-list'),
    path('segments/', SegmentList.as_view(), name='segment-list'),
]