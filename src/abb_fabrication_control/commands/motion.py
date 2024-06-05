import compas_rrc as rrc
from compas_robots import Configuration
from compas_robots.model import Joint
from compas.geometry import Frame, Transformation, Scale
import math

def move_to_frame(robot, frame, speed=250, zone=rrc.Zone.FINE, motion_type='J',
                  scalefactor=1000, feedback_level=0, send_and_wait=False):
    """ Send "move to frame" command to the ABB robot controller, which moves the robot in cartesian space.
    Converts m to mm.
    """
    # Scale frame from m to mm
    S = Scale.from_factors([scalefactor] * 3)
    frame.transform(S)

    if send_and_wait:
        # Send command to the ABB controller and wait for feedback
        return robot.abb_client.send_and_wait(rrc.MoveToFrame(frame, speed, zone, motion_type, feedback_level=feedback_level))
    else:
        # Send command to the ABB controller without waiting for feedback
        return robot.abb_client.send(rrc.MoveToFrame(frame, speed, zone, motion_type, feedback_level=feedback_level))

def move_to_robtarget(robot, frame, cart, speed=250, zone=rrc.Zone.FINE, motion_type='J',
                      scalefactor=1000, feedback_level=0, send_and_wait=False):
    """ Send "move to robtarget" command to the ABB robot controller, which moves the robot in cartesian space, including explicit external axes values (cart)
    Converts m to mm.
    """

    # Scale target frame from m to mm
    S = Scale.from_factors([scalefactor] * 3)
    frame.transform(S)

    # Scale cart value from m to mm
    cart = cart*scalefactor
    ext_axis = rrc.ExternalAxes([cart])

    if send_and_wait:
        # Send command to the ABB controller and wait for feedback
        return robot.abb_client.send_and_wait(rrc.MoveToRobtarget(frame, ext_axis, speed, zone, motion_type, feedback_level=feedback_level))
    else:
        # Send command to the ABB controller without waiting for feedback Send command to robot
        return robot.abb_client.send(rrc.MoveToRobtarget(frame, ext_axis, speed, zone, motion_type, feedback_level=feedback_level))

def move_to_joints(robot, configuration, speed=250, zone=rrc.Zone.FINE,
                   scalefactor=1000, feedback_level=0, send_and_wait=False):
    """ Send "move to joints" command to the ABB robot controller, which moves the robot in joint space, including explicit external axes values (cart)
    Converts radian to degrees.
    Converts m to mm.
    """
    # get the values from the configuration
    # ext_axes = rrc.ExternalAxes.from_configuration(configuration) #store all robot values from configuration
    # cart = rrc.ExternalAxes(ext_axes.values[0]) #store cart values from robot values as ExternalAxes
    # joints = rrc.RobotJoints(ext_axes.values[1:]) #store joint values from robot values as RobotJoints

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
        return robot.abb_client.send_and_wait(rrc.MoveToJoints(joints, cart, speed, zone, feedback_level=feedback_level))
    else:
        # Send joints and cart values to robot
        return robot.abb_client.send(rrc.MoveToJoints(joints, cart, speed, zone, feedback_level=feedback_level))
