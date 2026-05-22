"""
save_image_pose.py -- Save the robot camera image-acquisition pose for reuse.

Workflow:
  1. Use Dobot Studio and jog manually to the desired camera snapshot pose.
  2. Keep the robot at that pose.
  3. Run this script to save the current pose into JSON.

Later in Session 4, load and use the same pose before taking each picture.

Usage:
  python save_image_pose.py
  python save_image_pose.py --output image_acquisition_pose.json
  python save_image_pose.py --robot-ip 192.168.201.1
"""

import argparse
import os

from dobot_pick import DobotE6, save_image_acquisition_pose


def main():
    parser = argparse.ArgumentParser(
        description="Save the current Dobot pose as image-acquisition pose"
    )
    parser.add_argument(
        "--robot-ip",
        type=str,
        default="192.168.201.1",
        help="Dobot dashboard IP",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="image_acquisition_pose.json",
        help="Path to output JSON file",
    )
    parser.add_argument(
        "--user",
        type=int,
        default=0,
        help="User coordinate system index to store with pose",
    )
    parser.add_argument(
        "--tool",
        type=int,
        default=0,
        help="Tool coordinate system index to store with pose",
    )
    args = parser.parse_args()

    robot = DobotE6(ip=args.robot_ip)
    try:
        robot.connect()
        save_image_acquisition_pose(
            robot,
            file_path=args.output,
            user=args.user,
            tool=args.tool,
        )
        print("Saved successfully.")
        print(f"File: {os.path.abspath(args.output)}")
    finally:
        robot.disconnect()


if __name__ == "__main__":
    main()
