# Learn Task Planning

This is a simple educational repository to introduce automated task planning.

For more information, refer to my blog posts on this topic:
* [Task Planning in Robotics](https://roboticseabass.com/2022/07/19/task-planning-in-robotics/)
* [Integrated Task and Motion Planning in Robotics](https://roboticseabass.com/2022/07/30/integrated-task-and-motion-planning-in-robotics/)

To illustrate these concepts, we will use the [Unified Planning](https://unified-planning.readthedocs.io/en/latest/) library.

By Sebastian Castro, 2025.


## Simple Examples

The basic examples are directly runnable as Jupyter notebooks.

All you need to do is install Unified Planning along with at least one planner.
For example:

```
pip install unified_planning[tamer]
```

will install with the Tamer planner.


## ROS 2 Example

To get the ROS 2 examples running, you should place this repository into a valid ROS 2 workspace.

```
mkdir -p ~/up_ws/src
cd ~/up_ws/src
git clone https://github.com/sea-bass/learn-task-planning.git
```

Then, ensure you also clone the [UP4ROS2](https://github.com/aiplan4eu/UP4ROS2) repo.

```
cd ~/up_ws/src
git clone https://github.com/aiplan4eu/UP4ROS2
```

Finally, you can build this workspace:

```
cd ~/up_ws
source /opt/ros/$ROS_DISTRO/setup.bash
colcon build
source install/setup.bash
```

At this point, you can execute the ROS 2 example.

```
python3 03_intro_up4ros2.py
```
