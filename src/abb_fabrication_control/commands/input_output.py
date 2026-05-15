import compas_rrc as rrc

def set_digital_out(abb_client, output_name, output_state=0, send_and_wait=False):
    """ Send Digital Output signal
    """

    if send_and_wait:
        # Send command to the ABB controller and wait for feedback
        return abb_client.send_and_wait(rrc.SetDigital(output_name,output_state))
    else:
        # Send command to the ABB controller without waiting for feedback
        return abb_client.send(rrc.SetDigital(output_name,output_state))







