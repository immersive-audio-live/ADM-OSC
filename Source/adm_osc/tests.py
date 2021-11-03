#  ==============================================================================
# MIT License
#
# Copyright (c) 2021 immersive-audio-live
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#  ==============================================================================

from typing import Union

from . import protocol
from .client_server import AdmOscClientServer


#   _____         _      ____ _ _            _
#  |_   _|__  ___| |_   / ___| (_) ___ _ __ | |_
#    | |/ _ \/ __| __| | |   | | |/ _ \ '_ \| __|
#    | |  __/\__ \ |_  | |___| | |  __/ | | | |_
#    |_|\___||___/\__|  \____|_|_|\___|_| |_|\__|
class TestClient(AdmOscClientServer):
    default_object = 1

    def __init__(self, address: str = '127.0.0.1', out_port: int = 9000, in_port: int = 9001) -> None:
        super().__init__(address, out_port, in_port)

    #   _            _      __                  _             _              _     _           _
    #  | |_ ___  ___| |_   / _| ___  _ __   ___(_)_ __   __ _| | ___    ___ | |__ (_) ___  ___| |_
    #  | __/ _ \/ __| __| | |_ / _ \| '__| / __| | '_ \ / _` | |/ _ \  / _ \| '_ \| |/ _ \/ __| __|
    #  | ||  __/\__ \ |_  |  _| (_) | |    \__ \ | | | | (_| | |  __/ | (_) | |_) | |  __/ (__| |_
    #   \__\___||___/\__| |_|  \___/|_|    |___/_|_| |_|\__, |_|\___|  \___/|_.__// |\___|\___|\__|
    #                                                   |___/                   |__/
    def set_object_stable_parameters_to_minimum(self, object_number: Union[int, float, str] = default_object):
        """test all "stable" parameters of the specified object with minimum value..."""
        for val in protocol.get_stable_parameters():
            self.send_object_value_min(object_number, val)

    def set_object_stable_parameters_to_maximum(self, object_number: Union[int, float, str] = default_object):
        """test all "stable" parameters of the specified object with maximum value..."""
        for val in protocol.get_stable_parameters():
            self.send_object_value_max(object_number, val)

    def set_object_stable_parameters_to_default(self, object_number: Union[int, float, str] = default_object):
        """test all "stable" parameters of the specified object with default value..."""
        for val in protocol.get_stable_parameters():
            self.send_object_value_default(object_number, val)

    def set_object_stable_parameters_to_random(self, object_number: Union[int, float, str] = default_object):
        """test all "stable" parameters of the specified object with random value..."""
        for val in protocol.get_stable_parameters():
            self.send_object_value_random(object_number, val)

    def set_object_position_azimuth_minimum(self, object_number: Union[int, float, str] = default_object):
        """test position azimuth of the specified object with minimum value..."""
        self.send_object_value_min(object_number, protocol.a)

    def set_object_position_azimuth_maximum(self, object_number: Union[int, float, str] = default_object):
        """test position azimuth of the specified object with maximum value..."""
        self.send_object_value_max(object_number, protocol.a)

    def set_object_position_azimuth_default(self, object_number: Union[int, float, str] = default_object):
        """test position azimuth of the specified object with default value..."""
        self.send_object_value_default(object_number, protocol.a)

    def set_object_position_azimuth_random(self, object_number: Union[int, float, str] = default_object):
        """test position azimuth of the specified object with random value..."""
        self.send_object_value_random(object_number, protocol.a)

    def set_object_position_elevation_minimum(self, object_number: Union[int, float, str] = default_object):
        """test position elevation of the specified object with minimum value..."""
        self.send_object_value_min(object_number, protocol.e)

    def set_object_position_elevation_maximum(self, object_number: Union[int, float, str] = default_object):
        """test position elevation of the specified object with maximum value..."""
        self.send_object_value_max(object_number, protocol.e)

    def set_object_position_elevation_default(self, object_number: Union[int, float, str] = default_object):
        """test position elevation of the specified object with default value..."""
        self.send_object_value_default(object_number, protocol.e)

    def set_object_position_elevation_random(self, object_number: Union[int, float, str] = default_object):
        """test position elevation of the specified object with random value..."""
        self.send_object_value_random(object_number, protocol.e)

    def set_object_position_distance_minimum(self, object_number: Union[int, float, str] = default_object):
        """test position distance of the specified object with minimum value..."""
        self.send_object_value_min(object_number, protocol.d)

    def set_object_position_distance_maximum(self, object_number: Union[int, float, str] = default_object):
        """test position distance of the specified object with maximum value..."""
        self.send_object_value_max(object_number, protocol.d)

    def set_object_position_distance_default(self, object_number: Union[int, float, str] = default_object):
        """test position distance of the specified object with default value..."""
        self.send_object_value_default(object_number, protocol.d)

    def set_object_position_distance_random(self, object_number: Union[int, float, str] = default_object):
        """test position distance of the specified object with random value..."""
        self.send_object_value_random(object_number, protocol.d)

    def set_object_polar_position_minimum(self, object_number: Union[int, float, str] = default_object):
        """test polar position of the specified object with minimum value..."""
        self.send_object_value_min(object_number, protocol.aed)

    def set_object_polar_position_maximum(self, object_number: Union[int, float, str] = default_object):
        """test polar position of the specified object with maximum value..."""
        self.send_object_value_max(object_number, protocol.aed)

    def set_object_polar_position_default(self, object_number: Union[int, float, str] = default_object):
        """test polar position of the specified object with default value..."""
        self.send_object_value_default(object_number, protocol.aed)

    def set_object_polar_position_random(self, object_number: Union[int, float, str] = default_object):
        """test polar position of the specified object with random value..."""
        self.send_object_value_random(object_number, protocol.aed)

    def set_object_position_x_minimum(self, object_number: Union[int, float, str] = default_object):
        """test position x of the specified object with minimum value..."""
        self.send_object_value_min(object_number, protocol.x)

    def set_object_position_x_maximum(self, object_number: Union[int, float, str] = default_object):
        """test position x of the specified object with maximum value..."""
        self.send_object_value_max(object_number, protocol.x)

    def set_object_position_x_default(self, object_number: Union[int, float, str] = default_object):
        """test position x of the specified object with default value..."""
        self.send_object_value_default(object_number, protocol.x)

    def set_object_position_x_random(self, object_number: Union[int, float, str] = default_object):
        """test position x of the specified object with random value..."""
        self.send_object_value_random(object_number, protocol.x)

    def set_object_position_y_minimum(self, object_number: Union[int, float, str] = default_object):
        """test position y of the specified object with minimum value..."""
        self.send_object_value_min(object_number, protocol.y)

    def set_object_position_y_maximum(self, object_number: Union[int, float, str] = default_object):
        """test position y of the specified object with maximum value..."""
        self.send_object_value_max(object_number, protocol.y)

    def set_object_position_y_default(self, object_number: Union[int, float, str] = default_object):
        """test position y of the specified object with default value..."""
        self.send_object_value_default(object_number, protocol.y)

    def set_object_position_y_random(self, object_number: Union[int, float, str] = default_object):
        """test position y of the specified object with random value..."""
        self.send_object_value_random(object_number, protocol.y)

    def set_object_position_z_minimum(self, object_number: Union[int, float, str] = default_object):
        """test position z of the specified object with minimum value..."""
        self.send_object_value_min(object_number, protocol.z)

    def set_object_position_z_maximum(self, object_number: Union[int, float, str] = default_object):
        """test position z of the specified object with maximum value..."""
        self.send_object_value_max(object_number, protocol.z)

    def set_object_position_z_default(self, object_number: Union[int, float, str] = default_object):
        """test position z of the specified object with default value..."""
        self.send_object_value_default(object_number, protocol.z)

    def set_object_position_z_random(self, object_number: Union[int, float, str] = default_object):
        """test position z of the specified object with random value..."""
        self.send_object_value_random(object_number, protocol.z)

    def set_object_cartesian_position_minimum(self, object_number: Union[int, float, str] = default_object):
        """test cartesian position of the specified object with minimum value..."""
        self.send_object_value_min(object_number, protocol.xyz)

    def set_object_cartesian_position_maximum(self, object_number: Union[int, float, str] = default_object):
        """test cartesian position of the specified object with maximum value..."""
        self.send_object_value_max(object_number, protocol.xyz)

    def set_object_cartesian_position_default(self, object_number: Union[int, float, str] = default_object):
        """test cartesian position of the specified object with default value..."""
        self.send_object_value_default(object_number, protocol.xyz)

    def set_object_cartesian_position_random(self, object_number: Union[int, float, str] = default_object):
        """test cartesian position of the specified object with random value..."""
        self.send_object_value_random(object_number, protocol.xyz)

    def set_object_gain_minimum(self, object_number: Union[int, float, str] = default_object):
        """test gain of the specified object with minimum value..."""
        self.send_object_value_min(object_number, protocol.gain)

    def set_object_gain_maximum(self, object_number: Union[int, float, str] = default_object):
        """test gain of the specified object with maximum value..."""
        self.send_object_value_max(object_number, protocol.gain)

    def set_object_gain_default(self, object_number: Union[int, float, str] = default_object):
        """test gain of the specified object with default value..."""
        self.send_object_value_default(object_number, protocol.gain)

    def set_object_gain_random(self, object_number: Union[int, float, str] = default_object):
        """test gain of the specified object with random value..."""
        self.send_object_value_random(object_number, protocol.gain)

    #   _            _      __                              _ _   _       _              _     _           _
    #  | |_ ___  ___| |_   / _| ___  _ __   _ __ ___  _   _| | |_(_)_ __ | | ___    ___ | |__ (_) ___  ___| |_ ___
    #  | __/ _ \/ __| __| | |_ / _ \| '__| | '_ ` _ \| | | | | __| | '_ \| |/ _ \  / _ \| '_ \| |/ _ \/ __| __/ __|
    #  | ||  __/\__ \ |_  |  _| (_) | |    | | | | | | |_| | | |_| | |_) | |  __/ | (_) | |_) | |  __/ (__| |_\__ \
    #   \__\___||___/\__| |_|  \___/|_|    |_| |_| |_|\__,_|_|\__|_| .__/|_|\___|  \___/|_.__// |\___|\___|\__|___/
    #                                                              |_|                      |__/
    def set_objects_stable_parameters_minimum(self, objects_range: range = range(1)):
        """test all "stable" parameters of "number_of_objects" objects with minimum value..."""
        for obj in objects_range:
            self.set_object_stable_parameters_to_minimum(obj + 1)

    def set_objects_stable_parameters_maximum(self, objects_range: range = range(1)):
        """test all "stable" parameters of "number_of_objects" objects with maximum value..."""
        for obj in objects_range:
            self.set_object_stable_parameters_to_maximum(obj + 1)

    def set_objects_stable_parameters_default(self, objects_range: range = range(1)):
        """test all "stable" parameters of "number_of_objects" objects with default value..."""
        for obj in objects_range:
            self.set_object_stable_parameters_to_default(obj + 1)

    def set_objects_stable_parameters_random(self, objects_range: range = range(1)):
        """test all "stable" parameters of "number_of_objects" objects with random value..."""
        for obj in objects_range:
            self.set_object_stable_parameters_to_random(obj + 1)

    def set_objects_polar_position_minimum(self, objects_range: range = range(1)):
        """test polar position of "number_of_objects" objects with minimum value..."""
        for obj in objects_range:
            self.set_object_polar_position_minimum(obj + 1)

    def set_objects_polar_position_maximum(self, objects_range: range = range(1)):
        """test polar position of "number_of_objects" objects with maximum value..."""
        for obj in objects_range:
            self.set_object_polar_position_maximum(obj + 1)

    def set_objects_polar_position_default(self, objects_range: range = range(1)):
        """test polar position of "number_of_objects" objects with default value..."""
        for obj in objects_range:
            self.set_object_polar_position_default(obj + 1)

    def set_objects_polar_position_random(self, objects_range: range = range(1)):
        """test polar position of "number_of_objects" objects with random value..."""
        for obj in objects_range:
            self.set_object_polar_position_random(obj + 1)

    def set_objects_cartesian_position_minimum(self, objects_range: range = range(1)):
        """test cartesian position of "number_of_objects" objects with minimum value..."""
        for obj in objects_range:
            self.set_object_cartesian_position_minimum(obj + 1)

    def set_objects_cartesian_position_maximum(self, objects_range: range = range(1)):
        """test cartesian position of "number_of_objects" objects with maximum value..."""
        for obj in objects_range:
            self.set_object_cartesian_position_maximum(obj + 1)

    def set_objects_cartesian_position_default(self, objects_range: range = range(1)):
        """test cartesian position of "number_of_objects" objects with default value..."""
        for obj in objects_range:
            self.set_object_cartesian_position_default(obj + 1)

    def set_objects_cartesian_position_random(self, objects_range: range = range(1)):
        """test cartesian position of "number_of_objects" objects with random value..."""
        for obj in objects_range:
            self.set_object_cartesian_position_random(obj + 1)

    def set_objects_gain_minimum(self, objects_range: range = range(1)):
        """test gain of "number_of_objects" objects with minimum value..."""
        for obj in objects_range:
            self.set_object_gain_minimum(obj + 1)

    def set_objects_gain_maximum(self, objects_range: range = range(1)):
        """test gain of "number_of_objects" objects with maximum value..."""
        for obj in objects_range:
            self.set_object_gain_maximum(obj + 1)

    def set_objects_gain_default(self, objects_range: range = range(1)):
        """test gain of "number_of_objects" objects with default value..."""
        for obj in objects_range:
            self.set_object_gain_default(obj + 1)

    def set_objects_gain_random(self, objects_range: range = range(1)):
        """test gain of "number_of_objects" objects with random value..."""
        for obj in objects_range:
            self.set_object_gain_random(obj + 1)

    #   _            _        _    _ _         _     _           _
    #  | |_ ___  ___| |_     / \  | | |   ___ | |__ (_) ___  ___| |_ ___
    #  | __/ _ \/ __| __|   / _ \ | | |  / _ \| '_ \| |/ _ \/ __| __/ __|
    #  | ||  __/\__ \ |_   / ___ \| | | | (_) | |_) | |  __/ (__| |_\__ \
    #   \__\___||___/\__| /_/   \_\_|_|  \___/|_.__// |\___|\___|\__|___/
    #                                             |__/
    def set_all_objects_stable_parameters_minimum(self):
        """test all "stable" parameters of all objects with minimum value..."""
        self.set_object_stable_parameters_to_minimum('*')

    def set_all_objects_stable_parameters_maximum(self):
        """test all "stable" parameters of all objects with maximum value..."""
        self.set_object_stable_parameters_to_maximum('*')

    def set_all_objects_stable_parameters_default(self):
        """test all "stable" parameters of all objects with default value..."""
        self.set_object_stable_parameters_to_default('*')

    def set_all_objects_stable_parameters_random(self):
        """test all "stable" parameters of all objects with random value..."""
        self.set_object_stable_parameters_to_random('*')

    def set_all_objects_polar_position_minimum(self):
        """test polar position of all objects with minimum value..."""
        self.set_object_polar_position_minimum('*')

    def set_all_objects_polar_position_maximum(self):
        """test polar position of all objects with maximum value..."""
        self.set_object_polar_position_maximum('*')

    def set_all_objects_polar_position_default(self):
        """test polar position of all objects with default value..."""
        self.set_object_polar_position_default('*')

    def set_all_objects_polar_position_random(self):
        """test polar position of all objects with random value..."""
        self.set_object_polar_position_random('*')

    def set_all_objects_cartesian_position_minimum(self):
        """test cartesian position of all objects with minimum value..."""
        self.set_object_cartesian_position_minimum('*')

    def set_all_objects_cartesian_position_maximum(self):
        """test cartesian position of all objects with maximum value..."""
        self.set_object_cartesian_position_maximum('*')

    def set_all_objects_cartesian_position_default(self):
        """test cartesian position of all objects with default value..."""
        self.set_object_cartesian_position_default('*')

    def set_all_objects_gain_minimum(self):
        """test gain of all objects with minimum value..."""
        self.set_object_gain_minimum('*')

    def set_all_objects_gain_maximum(self):
        """test gain of all objects with maximum value..."""
        self.set_object_gain_maximum('*')

    def set_all_objects_gain_default(self):
        """test gain of all objects with default value..."""
        self.set_object_gain_default('*')
