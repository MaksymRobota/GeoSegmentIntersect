from matplotlib.patches import Polygon
import matplotlib.pyplot as plt
from unittest_parametrize import param


def draw_test_case(test_case):
    fig = plt.figure()
    plt.xlim(-2, 5)
    plt.ylim(-2, 5)

    intersecting = test_case["intersecting_rects"]

    currentAxis = plt.gca()
    for idx, rect in enumerate(test_case["rects"]):
        currentAxis.add_patch(Polygon(rect, facecolor='white', edgecolor='red' if idx in intersecting else "grey"))
    currentAxis.add_patch(Polygon(test_case["segment"], facecolor='white', edgecolor='blue'))
    fig.show()
    input()


if __name__ == '__main__':
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
            "intersecting_rects": [0]
            ,
        }, id="Segment_passing_through_rectangle"),
    ]
    for t in test_cases:
        draw_test_case(t.args[0])
