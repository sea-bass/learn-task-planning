# Unified Planning - ROS 2 example
#
# First, launch the UP4ROS2 node:
#
#   ros2 launch up4ros2 up4ros2.launch.py
#
# Then, run this example, which acts as a client to the node.

from pathlib import Path

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

from up_msgs.action import PDDLPlanOneShot
from up_msgs.msg import PDDLPlanRequest, PlanGenerationResult


class PlanningClient(Node):
    def __init__(self):
        super().__init__("planning_client")
        self.action_client = ActionClient(
            self,
            PDDLPlanOneShot,
            "/up4ros2/action/planOneShotPDDL"
        )


    def send_goal(self):
        """Sends a task planning goal to the UP4ROS2 node."""
        base_path = Path(__file__).parent
        domain_file_name = base_path / "pddl" / "pick_place_domain.pddl"
        problem_file_name = base_path / "pddl" / "pick_place_problem_01.pddl"

        goal_msg = PDDLPlanOneShot.Goal()
        goal_msg.plan_request = PDDLPlanRequest(
            mode=PDDLPlanRequest.FILE,
            resolution_mode=PDDLPlanRequest.SATISFIABLE,
            domain=domain_file_name.as_posix(),
            problem=problem_file_name.as_posix(),
        )

        self.action_client.wait_for_server()
        self.action_client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback
        )


    def feedback_callback(self, feedback_msg):
        """
        For some reason, the plan result comes in via feedback and not the result...
        I think this has to do with "anytime planners" continuously spitting out plans,
        but it does make the "one shot" planning workflow a little awkward.
        """
        feedback = feedback_msg.feedback
        if feedback.plan_result.status == PlanGenerationResult.SOLVED_SATISFICING:
            print("Received plan:")
            for idx, action in enumerate(feedback.plan_result.plan.actions):
                params = [param.symbol_atom[0] for param in action.parameters]
                print(f"  {idx}. {action.action_name}({','.join(params)})")


if __name__=="__main__":
    rclpy.init()
    node = PlanningClient()
    node.send_goal()
    rclpy.spin(node)
    rclpy.shutdown()
