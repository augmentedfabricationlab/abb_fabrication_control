import compas_rrc as rrc
from compas.robots import Configuration
from compas.geometry import Scale

def get_frame(robot, scalefactor=0.001):
    """
    send get frame command to receive robot's frame in mm to m conversation
    """
    frame = robot.abb_client.send_and_wait(rrc.GetFrame())
    S = Scale.from_factors([scalefactor] * 3)
    frame.transform(S)
    return (frame)

def get_robtarget(robot, scalefactor=0.001):
    """
    send get robtarget command to receive robot's frame and external axes in mm to m conversation
    """
    frame, external_axes = robot.abb_client.send_and_wait(rrc.GetRobtarget())
    S = Scale.from_factors([scalefactor] * 3) #scale robot frame from mm in m
    frame.transform(S)
    cart = rrc.ExternalAxes(external_axes.values[0]*scalefactor) #store robot cart value in mm to m conversion
    return (frame, cart)

def get_joints(robot):
    """
    send get joints command to receive robot's joint configuration
    """

    joints, external_axes = robot.abb_client.send_and_wait(rrc.GetJoints())
    ext_val = external_axes.values + joints.values
    axes = rrc.ExternalAxes(ext_val)
    configuration = axes.to_configuration(robot)
    return (configuration)

    # robot_joints, external_axes = robot.abb_client.send_and_wait(rrc.GetJoints())
    # joint_values = external_axes.values + joints.values
    # configuration = joint_values.to_configuration(robot)
    # return (configuration)







