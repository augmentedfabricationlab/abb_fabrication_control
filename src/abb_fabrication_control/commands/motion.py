from compas.geometry import Scale
from compas.robots import Joint
import compas_rrc as rrc
import math

__all__ = ["move_to_frame",
           "move_to_robtarget",
           "move_to_joints"]

def move_to_frame(robot, frame, speed=250, zone=rrc.Zone.FINE,
                  scalefactor=1000, send_and_wait=False):
    """
    Move to frame is a function that moves the robot in cartesian space.
    Converts m to mm.
    """
    # Scale frame from m to mm
    S = Scale.from_factors([scalefactor] * 3)
    frame.transform(S)
    if send_and_wait:
        # Send command to robot
        robot.abb_client.send_and_wait(rrc.MoveToFrame(frame, speed, zone))
    else:
        # Send command to robot
        robot.abb_client.send(rrc.MoveToFrame(frame, speed, zone))

def move_to_robtarget(robot, frame, cart, speed=250, zone=rrc.Zone.FINE,
                      scalefactor=1000, send_and_wait=False):
    """
    Move to robtarget is a call that moves the robot in cartesian space with explicit external axes values, which in this case are the cart values.
    Converts m to mm.
    """
    # Scale frame from m to mm
    S = Scale.from_factors([scalefactor] * 3)
    frame.transform(S)
    # Scale cart
    cart = cart*scalefactor
    ext_axes = rrc.ExternalAxes([cart])
    if send_and_wait:
        # Send command to robot
        robot.abb_client.send_and_wait(rrc.MoveToRobtarget(frame, ext_axes, speed, zone))
    else:
        # Send command to robot
        robot.abb_client.send(rrc.MoveToRobtarget(frame, ext_axes, speed, zone))

def move_to_joints(robot, configuration, speed=250, zone=rrc.Zone.FINE,
                   scalefactor=1000, send_and_wait=False):
    """
    Move to joints is a function that moves the robot and the external axes with axes values.
    """
    # Store joint values in degree from configuration
    joints = []
    for i, joint_type in enumerate(configuration.joint_types):
        if joint_type == Joint.REVOLUTE:
            joints.append(math.degrees(configuration.joint_values[i]))
    joints = rrc.RobotJoints(joints)
    
    # If there are more than the robot joint axes, add them as the external axes.
    if (len(configuration.joint_values) > 6): 
        # Store cart values from configuration in m
        cart = (configuration.joint_values[0])
        # Scale cart value in mm
        cart = cart*scalefactor
        cart = rrc.ExternalAxes(cart)
    else:
        cart = []

    if send_and_wait:
        # Send joints and cart values to robot
        robot.abb_client.send_and_wait(rrc.MoveToJoints(joints, cart, speed, zone))
    else:
        # Send joints and cart values to robot
        robot.abb_client.send(rrc.MoveToJoints(joints, cart, speed, zone))