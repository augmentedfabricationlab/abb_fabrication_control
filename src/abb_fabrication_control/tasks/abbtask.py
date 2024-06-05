from fabrication_manager import Task
import abb_fabrication_control as abbfc
from compas.geometry import Frame, Translation, Vector
import compas_rrc as rrc

class ABBTask(Task):
    def __init__(self, robot, key):
        super(ABBTask, self).__init__(key)
        self.robot = robot

    def content(self):
        ''' Script to execute within the run statement '''
        
        ### Saving the final command to self.future (ensure feedback_level>0)
        future = abbfc.commands.motion.move_to_robtarget(self.robot, frame=Frame.worldXY(),
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
        
class StartConfigurationTask(ABBTask):
    def __init__(self, robot, configuration, key=None):
        super(StartConfigurationTask, self).__init__(robot, key)
        self.configuration = configuration
        
    def content(self):
        # Moves the robot to start configuration
        abbfc.commands.motion.move_to_joints(self.robot, self.configuration, send_and_wait = True)
        self.log("robot moved to start configuration")  
        future = self.robot.abb_client.send(rrc.PrintText("Moved to startconfiguration done", feedback_level=1))      
        return future
            
class SetToolTask(ABBTask):
    def __init__(self, robot, tool_name, key=None):
        super(SetToolTask, self).__init__(robot, key)
        self.tool_name = tool_name
        
    def content(self):
        # Sets a tool to the robot
        self.robot.abb_client.send(rrc.SetTool(self.tool_name))
        self.log("{} is set".format(self.tool_name))
        future = self.robot.abb_client.send(rrc.PrintText("Setting tool done", feedback_level=1))
        return future        
         
class PickTask(ABBTask):
    def __init__(self, robot, pick_frame, key=None):
        super(PickTask, self).__init__(robot, key)
        self.pick_frame = pick_frame
        
    def content(self):
        T = Translation.from_vector(Vector(0,0,0.2)) 
        
        # Moves to approach frame
        approach_frame = self.pick_frame.transformed(T)
        abbfc.commands.motion.move_to_frame(self.robot, approach_frame)
        self.log("robot moved to approach frame") 

        # Moves to pick frame
        abbfc.commands.motion.move_to_frame(self.robot, self.pick_frame)
        self.log("robot moved to pick frame")  

        # Closes the gripper
        abbfc.commands.input_output.close_gripper(self.robot)
        self.log("gripper closed")

        # Moves to approach frame
        approach_frame = self.pick_frame.transformed(T)
        abbfc.commands.motion.move_to_frame(self.robot, approach_frame)
        self.log("robot moved to approach frame") 

        future = self.robot.abb_client.send(rrc.PrintText("Picking brick done", feedback_level=1))
        return future 
    
class PlaceTask(ABBTask):
    def __init__(self, robot, place_frame, key=None):
        super(PlaceTask, self).__init__(robot, key)
        self.place_frame = place_frame
        
    def content(self):
        T = Translation.from_vector(Vector(0,0,0.2)) 
        
        # Moves to approach frame
        approach_frame = self.place_frame.transformed(T)
        abbfc.commands.motion.move_to_frame(self.robot, approach_frame)
        self.log("robot moved to approach frame") 

        # Moves to place frame
        abbfc.commands.motion.move_to_frame(self.robot, self.place_frame)
        self.log("robot moved to pick frame")  

        # Opens the gripper
        abbfc.commands.input_output.open_gripper(self.robot)
        self.log("gripper closed")

        # Moves to approach frame
        approach_frame = self.pick_frame.transformed(T)
        abbfc.commands.motion.move_to_frame(self.robot, approach_frame)
        self.log("robot moved to approach frame") 

        future = self.robot.abb_client.send(rrc.PrintText("Placing brick done", feedback_level=1))
        return future 