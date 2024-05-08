import compas_rrc as rrc

def print_text(robot, text_msg, send_and_wait=False):
    """ Send text to the ABB robot flex pendant for printout.
    """

    if send_and_wait:
        # Send command to the ABB controller and wait for feedback
        return robot.abb_client.send_and_wait(rrc.PrintText(text_msg))
    else:
        # Send command to the ABB controller without waiting for feedback
        return robot.abb_client.send(rrc.PrintText(text_msg))

def set_tool(robot, tool_name="tool0", send_and_wait=False):
    """ Send "set tool" command to the ABB robot controller
    """
    if send_and_wait:
        # Send command to the ABB controller and wait for feedback
        return robot.abb_client.send_and_wait(rrc.SetTool(tool_name))
    else:
        # Send command to the ABB controller without waiting for feedback
        return robot.abb_client.send(rrc.SetTool(tool_name))

def set_tool_attached(robot, send_and_wait=False):
    """ Send "set tool" command to the ABB robot controller
    """
    if robot.attached_tool:
        tool_name = robot.attached_tool.name
    else:
        tool_name = "tool0"

    if send_and_wait:
        # Send command to the ABB controller and wait for feedback
        return robot.abb_client.send_and_wait(rrc.SetTool(tool_name))
    else:
        # Send command to the ABB controller without waiting for feedback
        return robot.abb_client.send(rrc.SetTool(tool_name))