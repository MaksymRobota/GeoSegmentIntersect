from django.test import TestCase
from unittest_parametrize import ParametrizedTestCase, parametrize, param

from geo.models import Segment, Rect
from geo.segment_service import find_rects_intersecting_with_segment


test_cases = [
    param({
        "rects": [((0, 0), (1, 0), (1, 1), (0, 1))],
        "segment": ((-1, 1), (-2, 2)),
        "intersecting_rects": [],
    }, id="Non_intersecting_segment"),
    param({
        "rects": [((0, 0), (1, 0), (1, 1), (0, 1)), ((2, 2), (3, 2), (3, 3), (2, 3))],
        "segment": ((0.5, 0.5), (2.5, 2.5)),
        "intersecting_rects": [0, 1],
    }, id="Segment_intersecting_multiple_rectangles"),
    param({
        "rects": [((0, 0), (1, 0), (1, 1), (0, 1))],
        "segment": ((0.5, 1.5), (2.5, 1.5)),
        "intersecting_rects": [],
    }, id="Segment_intersecting_horizontal_edge_of_rectangle"),
    param({
        "rects": [((0, 0), (1, 0), (1, 1), (0, 1))],
        "segment": ((0, 0.5), (0, 2)),
        "intersecting_rects": [0],
    }, id="Segment_intersecting_vertical_edge_of_rectangle"),
    param({
        "rects": [((0, 0), (1, 0), (1, 1), (0, 1))],
        "segment": ((-1, -1), (0, 0)),
        "intersecting_rects": [0],
    }, id="Segment_intersecting_corner_of_rectangle"),
    param({
        "rects": [((0, 0), (1, 0), (1, 1), (0, 1)), ((2, 2), (3, 2), (3, 3), (2, 3))],
        "segment": ((-1, 0.5), (3, 0.5)),
        "intersecting_rects": [0],
    }, id="Horizontal_segment_intersecting_multiple_rectangles"),
    param({
        "rects": [((0, 0), (1, 0), (1, 1), (0, 1)), ((2, 2), (3, 2), (3, 3), (2, 3))],
        "segment": ((0.5, -1), (0.5, 3)),
        "intersecting_rects": [0],
    }, id="Vertical_segment_intersecting_multiple_rectangles"),
    param({
        "rects": [((0, 0), (2, 0), (2, 2), (0, 2)), ((1, 1), (3, 1), (3, 3), (1, 3))],
        "segment": ((0.5, 0.5), (2.5, 2.5)),
        "intersecting_rects": [0, 1],
    }, id="Overlapping_rectangles"),
    param({
        "rects": [((0, 0), (1, 0), (1, 1), (0, 1))],
        "segment": ((0.25, 0.25), (0.75, 0.75)),
        "intersecting_rects": [],
    }, id="Segment_inside_rectangle"),
    param({
        "rects": [((0, 0), (1, 0), (1, 1), (0, 1))],
        "segment": ((-1, 0.5), (2, 0.5)),
        "intersecting_rects": [0],
    }, id="Segment_passing_through_rectangle"),
]


class IntegrationTestCase(ParametrizedTestCase, TestCase):

    @parametrize("test_case", test_cases)
    def test_rectangle_search(self, test_case):
        intersecting_rects = set()
        intersecting_rects_indexes = test_case["intersecting_rects"]
        for idx, rect in enumerate(test_case["rects"]):
            (x1, y1), (x2, y2), (x3, y3), (x4, y4) = rect
            s1 = Segment(x1=x1, y1=y1, x2=x2, y2=y2)
            s2 = Segment(x1=x2, y1=y2, x2=x3, y2=y3)
            s3 = Segment(x1=x3, y1=y3, x2=x4, y2=y4)
            s4 = Segment(x1=x4, y1=y4, x2=x1, y2=y1)
            rect = Rect(name=f"Rect-{idx}")
            s1.rect = rect
            s2.rect = rect
            s3.rect = rect
            s4.rect = rect
            rect.save()
            s1.save()
            s2.save()
            s3.save()
            s4.save()
            if idx in intersecting_rects_indexes:
                intersecting_rects.add(rect)

        ((seg_x1, seg_y1), (seg_x2, seg_y2)) = test_case["segment"]

        rects_search_result = set(find_rects_intersecting_with_segment(seg_x1, seg_y1, seg_x2, seg_y2))
        self.assertSetEqual(rects_search_result, intersecting_rects)


