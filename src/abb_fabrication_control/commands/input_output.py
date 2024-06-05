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
    return set_digital_out(robot, 'Ausgang_100_5', output_state=1, send_and_wait=send_and_wait)


def open_gripper(robot, send_and_wait=False):
    """ Send signal to open the gripper
    """
    set_digital_out(robot, 'Ausgang_100_3', output_state=1, send_and_wait=send_and_wait)
    return set_digital_out(robot, 'Ausgang_100_5', output_state=0, send_and_wait=send_and_wait)

