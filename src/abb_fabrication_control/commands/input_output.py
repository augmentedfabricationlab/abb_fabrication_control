import compas_rrc as rrc

def set_digital_out(robot, output_name, output_state=0, send_and_wait=False):
    """ Send Digital Output signal
    """

    if send_and_wait:
        # Send command to the ABB controller and wait for feedback
        return robot.abb_client.send_and_wait(rrc.SetDigital(output_name,output_state))
    else:
        # Send command to the ABB controller without waiting for feedback
        return robot.abb_client.send(rrc.SetDigital(output_name,output_state))

def close_gripper(robot, send_and_wait=False):
    """ Send signal to open the gripper
    """
    set_digital_out(robot, 'Ausgang_100_3', output_state=0, send_and_wait=send_and_wait)
    set_digital_out(robot, 'Ausgang_100_5', output_state=1, send_and_wait=send_and_wait)
    return robot.abb_client.send(rrc.WaitTime(0.5))


def open_gripper(robot, send_and_wait=False):
    """ Send signal to open the gripper
    """
    set_digital_out(robot, 'Ausgang_100_3', output_state=1, send_and_wait=send_and_wait)
    set_digital_out(robot, 'Ausgang_100_5', output_state=0, send_and_wait=send_and_wait)
    return robot.abb_client.send(rrc.WaitTime(0.5))

def enable_gun(robot, send_and_wait=False):
    """ Send signal to enable the gun
    """
    set_digital_out(robot, 'Ausgang_100_0', output_state=1, send_and_wait=send_and_wait)
    return robot.abb_client.send(rrc.WaitTime(0.5))

def disable_gun(robot, send_and_wait=False):
    """ Send signal to disable the gun
    """
    set_digital_out(robot, 'Ausgang_100_0', output_state=0, send_and_wait=send_and_wait)
    return robot.abb_client.send(rrc.WaitTime(0.5))

def trigger_gun(robot, send_and_wait=False):
    """ Send signal to trigger the gun
    """
    set_digital_out(robot, 'Ausgang_100_6', output_state=1, send_and_wait=send_and_wait)
    robot.abb_client.send(rrc.WaitTime(1))
    set_digital_out(robot, 'Ausgang_100_6', output_state=0, send_and_wait=send_and_wait)
    return robot.abb_client.send(rrc.WaitTime(0.5))