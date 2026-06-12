def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    """

    left_a, top_a, right_a, bottom_a = box_a
    left_b, top_b, right_b, bottom_b = box_b

    ## check overlap 
    # if not overlap, returns 0 
    if (right_a < left_b or left_a > right_b or top_a > bottom_b or bottom_a < top_b ):
        return 0
    else:
        # normal case 
        height = abs(bottom_b - top_a) if bottom_a > bottom_b else (bottom_a - top_b)
        width = abs(right_b - left_a) if  right_a > right_b else (right_a - left_b)
        # special case: overlapping: 
        intersection = height * width
        area_1 = abs(right_a - left_a) * abs(top_a - bottom_a)
        area_2 = abs(right_b - left_b) * abs(top_b - bottom_b)
        if left_a > left_b and top_a > top_b and bottom_a < bottom_b and right_a < right_b:
            intersection = area_1
        if left_b > left_a and top_b > top_a and bottom_b < bottom_a and right_b < right_a:
            intersection = area_2 
        union =  area_1 + area_2 - intersection
        return intersection / union