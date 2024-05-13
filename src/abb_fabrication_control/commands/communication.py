import compas_rrc as rrc

def close(robot):
    robot.abb_client.send(rrc.WaitTime(1))
    robot.abb_client.send(rrc.SetDigital('Ausgang_100_3', 1))
    robot.abb_client.send(rrc.SetDigital('Ausgang_100_5', 0))
    robot.abb_client.send(rrc.WaitTime(0.5))


def open(robot):
    robot.abb_client.send(rrc.WaitTime(1))
    robot.abb_client.send(rrc.SetDigital('Ausgang_100_3', 0))
    robot.abb_client.send(rrc.SetDigital('Ausgang_100_5', 1))
    robot.abb_client.send(rrc.WaitTime(0.5))

def extrude(robot):
    robot.abb_client.send(rrc.WaitTime(1))
    robot.abb_client.send(rrc.SetDigital('Ausgang_100_1', 1))
    robot.abb_client.send(rrc.WaitTime(3))
    robot.abb_client.send(rrc.SetDigital('Ausgang_100_1', 0))
    robot.abb_client.send(rrc.WaitTime(1))

def valve_open(robot):
    robot.abb_client.send(rrc.WaitTime(1))
    robot.abb_client.send(rrc.SetDigital('Ausgang_100_1', 1))
    robot.abb_client.send(rrc.WaitTime(0.5))

def valve_close(robot):
    robot.abb_client.send(rrc.WaitTime(1))
    robot.abb_client.send(rrc.SetDigital('Ausgang_100_1', 0))
    robot.abb_client.send(rrc.WaitTime(0.5))
