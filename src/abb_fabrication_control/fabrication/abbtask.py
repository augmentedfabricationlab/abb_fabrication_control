from fabrication_manager.task import Task
import abb_fabrication_control as abbfc

from compas.geometry import Frame
import compas_rrc as rrc

class ABBTask(Task):
    def __init__(self, robot, *args, **kwargs):
        super(ABBTask, self).__init__(*args, **kwargs)
        self.robot = robot
        self.frame = Frame.WorldXY()

    def content(self):
        ''' Script to execute within the run statement '''
        
        ### Saving the final command to self.future (ensure feedback_level>0)
        future = abbfc.commands.move_to_robtarget(self.robot, frame=self.frame,
                                                  cart=0, speed=250, zone=rrc.Zone.FINE
                                                  feedback_level=1)
        return future

    def run(self, stop_thread):
        future = self.content()
        if future is None:
            raise ValueError("self.future is None, please set a command to wait for")
        while not future.done:
            if stop_thread():
                self.log("Forced to stop...")
                self.robot.abb_client.send(rrc.Stop())
                self.is_running = False
                self.is_completed = False
                break   
        else:
            self.is_completed = True
            return True
        
        
        
    