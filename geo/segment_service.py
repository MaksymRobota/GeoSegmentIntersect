from typing import Set

from geo.models import Rect, Segment


def find_rects_intersecting_with_segment(x1: float, y1: float, x2: float, y2: float) -> Set[Rect]:
    intersecting_rects = set()
    for s in Segment.objects.all():
        if s.rect in intersecting_rects:
            continue
        if do_segments_intersect(s.x1, s.y1, s.x2, s.y2, x1, y1, x2, y2):
            intersecting_rects.add(s.rect)
    return intersecting_rects


def do_segments_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    denom = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
    if denom == 0:
        return False
    ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denom
    if ua < 0 or ua > 1:
        return False
    ub = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / denom
    if ub < 0 or ub > 1:
        return False
    return True
