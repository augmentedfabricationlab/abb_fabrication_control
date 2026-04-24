import compas_rrc as rrc
from compas_robots import Configuration
from compas.geometry import Frame, Transformation, Scale


def get_frame(robot, scalefactor=0.001):
    """
    send get frame command to receive robot's frame in mm to m conversation
    """
    frame = robot.abb_client.send_and_wait(rrc.GetFrame(), timeout=1)
    S = Scale.from_factors([scalefactor] * 3)
    frame.transform(S)

    return (frame)

def get_robtarget(robot, scalefactor=0.001):
    """
    send get robtarget command to receive robot's frame and external axes in mm to m conversation
    """
    frame, external_axes = robot.abb_client.send_and_wait(rrc.GetRobtarget(), timeout=1)
    S = Scale.from_factors([scalefactor] * 3) #scale robot frame from mm in m
    frame.transform(S)
    cart = rrc.ExternalAxes(external_axes.values[0]*scalefactor) #store robot cart value in mm to m conversion

    return (frame, cart)

def get_joints(robot, scalefactor=0.001):
    """
    send get joints command to receive robot's joint configuration and external axes in mm to m conversation
    """

    joints, external_axes = robot.abb_client.send_and_wait(rrc.GetJoints(), timeout=1)
    configuration = joints.to_configuration(robot)

    if external_axes.values:
        ext_axes = external_axes.to_configuration(robot)
        return (configuration, ext_axes)

    return (configuration)









