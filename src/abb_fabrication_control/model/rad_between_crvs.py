
from compas.geometry import Line




def radius_between_frames(from_frame, via_frame, to_frame, max_radius):
        in_line = Line(from_frame.point, via_frame.point)
        out_line = Line(via_frame.point, to_frame.point)
        radius_between_frames = min(max_radius, in_line.length/2, out_line.length/2)
        return radius_between_frames