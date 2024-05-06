from fabrication_manager.task import Task
import abb_fabrication_control as abbfc

from compas.geometry import Frame
import compas_rrc as rrc


class ABBTask(Task):
    def __init__(self, robot, key):
        super(ABBTask, self).__init__(key)
        self.robot = robot

    def content(self):
        ''' Script to execute within the run statement '''
        
        ### Saving the final command to self.future (ensure feedback_level>0)
        future = abbfc.commands.move_to_robtarget(self.robot, frame=Frame.worldXY(),
                                                  cart=0, speed=250, zone=rrc.Zone.FINE,
                                                  feedback_level=1)
        return future

    def run(self, stop_thread):
        future = self.content()
        if future is None:
            raise ValueError("future is None, please set a command to wait for")
        while not future.done:
            if stop_thread():
                self.log("Forced to stop...")
                #self.robot.abb_client.send(rrc.Stop())
                self.is_running = False
                self.is_completed = False
                break   
        else:
            self.is_completed = True
            return True
        
        
        
# class ABBTask2(Task):
#     def __init__(self, robot, *args, **kwargs):
#         super(ABBTask, self).__init__(*args, **kwargs)
#         self.robot = robot
#         self.frame = Frame.WorldXY()

#     def run(self, stop_thread, future=None):
#         '''overwrite and set variable future'''
#         if future is None:
#             raise ValueError("self.future is None, please set a command to wait for")
#         while not future.done:
#             if stop_thread():
#                 self.log("Forced to stop...")
#                 self.robot.abb_client.send(rrc.Stop())
#                 self.is_running = False
#                 self.is_completed = False
#                 break   
#         else:
#             self.is_completed = True
#             return True
        
# class SetToolTask(ABBTask):
#     def __init__(self, robot, tool_name, key=None):
#         super(SetToolTask, self).__init__(key)
#         self.robot = robot
#         self.tool_name = tool_name
        
#     def run(self, stop_thread):
#         # Sets a tool to the robot
#         future = self.robot.abb_client.send(rrc.SetTool(self.tool_name), feedback_level=1)
#         self.log("{} is set".format(self.tool_name))
#         return super(SetToolTask, self).run(stop_thread, future)