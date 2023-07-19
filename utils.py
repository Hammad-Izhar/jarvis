import os
import pyttsx3 as tts

from typing import Union

CRAZYFLIE_DIR = os.path.exists(f"{os.getenv('HOME')}/ros2_ws/src/Brown-crazyswarm2")

CRAZYFLIE_SCRIPT_DIRECTORIES = {
    f"{os.getenv('HOME')}/ros2_ws/src/Brown-crazyswarm2/crazyflie_examples/crazyflie_examples": "crazyflie_examples",
    f"{os.getenv('HOME')}/ros2_ws/src/Brown-crazyswarm2/crazyswarm_demos/crazyswarm_demos": "crazyswarm_demos",
    f"{os.getenv('HOME')}/ros2_ws/src/crazyswarm2/crazyswarm_demos/crazyswarm_demos": "crazyswarm_demos",
    f"{os.getenv('HOME')}/ros2_ws/src/crazyswarm2/crazyswarm_demos/crazyswarm_demos": "crazyswarm_demos",
}

ROBOT_DETAILS = {
    "cf1": {"uri": "radio://0/80/2M/E7E7E7E701", "type": "cf21_m1"},
    "cf2": {"uri": "radio://1/100/2M/E7E7E7E702", "type": "cf21_m2"},
    "cf3": {"uri": "radio://2/120/2M/E7E7E7E703", "type": "cf21_m3"},
    "cf4": {"uri": "radio://0/80/2M/E7E7E7E704", "type": "cf21_m4"},
    "cf5": {"uri": "radio://1/100/2M/E7E7E7E705", "type": "cf21_m1"},
    "cf6": {"uri": "radio://2/120/2M/E7E7E7E706", "type": "cf21_m2"},
    "cf7": {"uri": "radio://0/80/2M/E7E7E7E707", "type": "cf_big"},
    "cf8": {"uri": "radio://0/80/2M/E7E7E7E708", "type": "cf21_m3"},
    "cf9": {"uri": "radio://0/80/2M/E7E7E7E709", "type": "cf21_m1"},
    "cf10": {"uri": "radio://1/100/2M/E7E7E7E709", "type": "cf21_m2"},
    "cf11": {"uri": "radio://1/100/2M/E7E7E7E70B", "type": "cf21_m3"},
    "cf12": {"uri": "radio://2/120/2M/E7E7E7E70C", "type": "cf21_m4"},
    "cf14": {"uri": "radio://2/120/2M/E7E7E7E70E", "type": "cf21_m2"},
    "cf15": {"uri": "radio://0/80/2M/E7E7E7E70F", "type": "cf21_m3"},
    "cf16": {"uri": "radio://1/100/2M/E7E7E7E710", "type": "cf21_m4"},
    "cf17": {"uri": "radio://2/120/2M/E7E7E7E711", "type": "cf21_m1"},
    "cf18": {"uri": "radio://1/100/2M/E7E7E7E712", "type": "cf21_m2"},
    "cf19": {"uri": "radio://0/80/2M/E7E7E7E713", "type": "cf21_m3"},
    "cf20": {"uri": "radio://1/100/2M/E7E7E7E71", "type": "cf21_m4"},
    "cf21": {"uri": "radio://2/120/2M/E7E7E7E715", "type": "cf21_m1"},
    "cf23": {"uri": "radio://0/80/2M/E7E7E7E717", "type": "cf21_m3"},
    "cf24": {"uri": "radio://1/100/2M/E7E7E7E718", "type": "cf21_m4"},
    "cf25": {"uri": "radio://2/120/2M/E7E7E7E719", "type": "cf21_m1"},
    "cf27": {"uri": "radio://0/80/2M/E7E7E7E71B", "type": "cf21_m3"},
    "cf28": {"uri": "radio://1/100/2M/E7E7E7E71C", "type": "cf21_m4"},
    "cf30": {"uri": "radio://2/120/2M/E7E7E7E71E", "type": "cf21_m2"},
    "cf31": {"uri": "radio://0/80/2M/E7E7E7E71F", "type": "cf21_m3"},
    "cf33": {"uri": "radio://0/100/2M/E7E7E7E721", "type": "cf21_m1"},
    "cf34": {"uri": "radio://2/120/2M/E7E7E7E722", "type": "cf21_m2"},
    "cf35": {"uri": "radio://0/80/2M/E7E7E7E723", "type": "cf21_m3"},
    "cf36": {"uri": "radio://1/100/2M/E7E7E7E724", "type": "cf21_m4"},
    "cf38": {"uri": "radio://2/120/2M/E7E7E7E726", "type": "cf21_m2"},
    "cf40": {"uri": "radio://0/80/2M/E7E7E7E728", "type": "cf21_m4"},
    "cf41": {"uri": "radio://1/100/2M/E7E7E7E729", "type": "cf21_m1"},
    "cf43": {"uri": "radio://2/120/2M/E7E7E7E72B", "type": "cf21_m3"},
    "cf44": {"uri": "radio://0/80/2M/E7E7E7E72C", "type": "cf21_m4"},
    "cf45": {"uri": "radio://1/100/2M/E7E7E7E72D", "type": "cf21_m3"},
    "cf47": {"uri": "radio://1/100/2M/E7E7E7E72F", "type": "cf21_m3"},
    "cf50": {"uri": "radio://2/120/2M/E7E7E7E732", "type": "cf21_m2"},
    "cf13": {"uri": "radio://0/80/2M/E7E7E7E70D", "type": "cf21_m1"},
    "cf29": {"uri": "radio://1/120/2M/E7E7E7E71D", "type": "cf21_m3"},
    "cf65": {"uri": "radio://0/80/2M/E7E7E7E741", "type": "cf21_m1"},
    "cf67": {"uri": "radio://0/80/2M/E7E7E7E743", "type": "cf21_m3"},
    "cf61": {"uri": "radio://0/80/2M/E7E7E7E73D", "type": "cf21_m1"},
    "cf72": {"uri": "radio://0/80/2M/E7E7E7E748", "type": "cf21_m4"},
    "cf66": {"uri": "radio://0/80/2M/E7E7E7E742", "type": "cf21_m2"},
    "cf62": {"uri": "radio://0/80/2M/E7E7E7E73E", "type": "cf21_m2"},
    "cf60": {"uri": "radio://0/80/2M/E7E7E7E73C", "type": "cf21_m4"},
    "cf29": {"uri": "radio://1/120/2M/E7E7E7E71D", "type": "cf21_m3"},
}

SPAWN_TERMINAL = f"gnome-terminal --"

with open("prompt.txt", "r") as f:
    PROMPT = "\n".join(f.readlines())


TTS_ENGINE = tts.init()
TTS_ENGINE.setProperty("volume", 1)
def jarvis_say(str):
    TTS_ENGINE.say(str)
    TTS_ENGINE.runAndWait()


def find_file(file_name: "str") -> Union["str", None]:
    # TODO: account for the case where a file name is repeated in multiple directories
    for crazyflie_script_dir, package_name in CRAZYFLIE_SCRIPT_DIRECTORIES.items():
        for _, _, files in os.walk(crazyflie_script_dir):
            if file_name in files:
                return package_name
    return


YAML_DICT_TEMPLATE = {
    "robot_types": {
        "cf21": {
            "motion_capture": {
                "enabled": True,
                "marker": "default",
                "dynamics": "default",
            },
            "big_quad": False,
            "battery": {"voltage_warning": 3.8, "voltage_critical": 3.7},
        },
        "cf21_single_marker": {
            "motion_capture": {
                "enabled": True,
                "marker": "default_single_marker",
                "dynamics": "default",
            },
            "big_quad": False,
            "battery": {"voltage_warning": 3.8, "voltage_critical": 3.7},
        },
        "cf21_m4": {
            "motion_capture": {"enabled": True, "marker": "m4", "dynamics": "default"},
            "big_quad": False,
            "battery": {"voltage_warning": 3.8, "voltage_critical": 3.7},
        },
        "cf21_m3": {
            "motion_capture": {"enabled": True, "marker": "m3", "dynamics": "default"},
            "big_quad": False,
            "battery": {"voltage_warning": 3.8, "voltage_critical": 3.7},
        },
        "cf21_m2": {
            "motion_capture": {"enabled": True, "marker": "m2", "dynamics": "default"},
            "big_quad": False,
            "battery": {"voltage_warning": 3.8, "voltage_critical": 3.7},
        },
        "cf21_m1": {
            "motion_capture": {"enabled": True, "marker": "m1", "dynamics": "default"},
            "big_quad": False,
            "battery": {"voltage_warning": 3.8, "voltage_critical": 3.7},
        },
        "cf21_mocap_deck": {
            "motion_capture": {
                "enabled": True,
                "marker": "mocap_deck",
                "dynamics": "default",
            },
            "big_quad": False,
            "battery": {"voltage_warning": 3.8, "voltage_critical": 3.7},
        },
        "cf_big": {
            "motion_capture": {
                "enabled": True,
                "marker": "big_frame",
                "dynamics": "default",
            },
            "big_quad": True,
        },
    },
    "all": {
        "firmware_logging": {"enabled": False},
        "firmware_params": {
            "commander": {"enHighLevel": 1},
            "stabilizer": {"estimator": 2, "controller": 1},
            "ring": {"effect": 7, "solidBlue": 255, "solidGreen": 0, "solidRed": 0},
            "locSrv": {"extPosStdDev": "1e-3", "extQuatStdDev": 0.05},
        },
        "broadcasts": {"num_repeats": 15, "delay_between_repeats_ms": 1},
        "unicasts": {"num_repeats": 2},
    },
}
