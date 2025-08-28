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

from . import stable_params
from .protocol import get_stable_parameters, ValueType
from .client_server import OscClientServer

__all__ = ['TestClient']


#   _____         _      ____ _ _            _
#  |_   _|__  ___| |_   / ___| (_) ___ _ __ | |_
#    | |/ _ \/ __| __| | |   | | |/ _ \ '_ \| __|
#    | |  __/\__ \ |_  | |___| | |  __/ | | | |_
#    |_|\___||___/\__|  \____|_|_|\___|_| |_|\__|
class TestClient(OscClientServer):
    predefined_object = 1
    predefined_value_type = ValueType.Default

    def __init__(self, address: str = '127.0.0.1', out_port: int = 9000, in_port: int = 9001, out_address: str = None) -> None:
        super().__init__(address, out_port, in_port, False, out_address)

    #   _            _      __                  _             _              _     _           _
    #  | |_ ___  ___| |_   / _| ___  _ __   ___(_)_ __   __ _| | ___    ___ | |__ (_) ___  ___| |_
    #  | __/ _ \/ __| __| | |_ / _ \| '__| / __| | '_ \ / _` | |/ _ \  / _ \| '_ \| |/ _ \/ __| __|
    #  | ||  __/\__ \ |_  |  _| (_) | |    \__ \ | | | | (_| | |  __/ | (_) | |_) | |  __/ (__| |_
    #   \__\___||___/\__| |_|  \___/|_|    |___/_|_| |_|\__, |_|\___|  \___/|_.__// |\___|\___|\__|
    #                                                   |___/                   |__/
    def set_object_stable_parameters_predefined_value(self, object_number: Union[int, float, str] = predefined_object, value_type: ValueType = predefined_value_type):
        """test all "stable" parameters of the specified object with minimum value..."""
        for param in get_stable_parameters():
            self.send_object_value_type(object_number, param, value_type)

    def set_object_position_azimuth_predefined_value(self, object_number: Union[int, float, str] = predefined_object, value_type: ValueType = predefined_value_type):
        """test position azimuth of the specified object with minimum value..."""
        self.send_object_value_type(object_number, stable_params.a, value_type)

    def set_object_position_elevation_predefined_value(self, object_number: Union[int, float, str] = predefined_object, value_type: ValueType = predefined_value_type):
        """test position elevation of the specified object with minimum value..."""
        self.send_object_value_type(object_number, stable_params.e, value_type)

    def set_object_position_distance_predefined_value(self, object_number: Union[int, float, str] = predefined_object, value_type: ValueType = predefined_value_type):
        """test position distance of the specified object with minimum value..."""
        self.send_object_value_type(object_number, stable_params.d, value_type)

    def set_object_polar_position_predefined_value(self, object_number: Union[int, float, str] = predefined_object, value_type: ValueType = predefined_value_type):
        """test polar position of the specified object with minimum value..."""
        self.send_object_value_type(object_number, stable_params.aed, value_type)

    def set_object_position_x_predefined_value(self, object_number: Union[int, float, str] = predefined_object, value_type: ValueType = predefined_value_type):
        """test position x of the specified object with minimum value..."""
        self.send_object_value_type(object_number, stable_params.x, value_type)

    def set_object_position_y_predefined_value(self, object_number: Union[int, float, str] = predefined_object, value_type: ValueType = predefined_value_type):
        """test position y of the specified object with minimum value..."""
        self.send_object_value_type(object_number, stable_params.y, value_type)

    def set_object_position_z_predefined_value(self, object_number: Union[int, float, str] = predefined_object, value_type: ValueType = predefined_value_type):
        """test position z of the specified object with minimum value..."""
        self.send_object_value_type(object_number, stable_params.z, value_type)

    def set_object_position_xy_predefined_value(self, object_number: Union[int, float, str] = predefined_object, value_type: ValueType = predefined_value_type):
        """test cartesian xy position of the specified object with minimum value..."""
        self.send_object_value_type(object_number, stable_params.xy, value_type)

    def set_object_cartesian_position_predefined_value(self, object_number: Union[int, float, str] = predefined_object, value_type: ValueType = predefined_value_type):
        """test cartesian position of the specified object with minimum value..."""
        self.send_object_value_type(object_number, stable_params.xyz, value_type)

    def send_object_width_predefined_value(self, object_number: Union[int, float, str] = predefined_object, value_type: ValueType = predefined_value_type):
        """test gain of the specified object with minimum value..."""
        self.send_object_value_type(object_number, stable_params.w, value_type)

    def set_object_gain_predefined_value(self, object_number: Union[int, float, str] = predefined_object, value_type: ValueType = predefined_value_type):
        """test gain of the specified object with minimum value..."""
        self.send_object_value_type(object_number, stable_params.gain, value_type)

    def set_object_mute_predefined_value(self, object_number: Union[int, float, str] = predefined_object, value_type: ValueType = predefined_value_type):
        """test mute of the specified object with minimum value..."""
        self.send_object_value_type(object_number, stable_params.mute, value_type)

    def set_object_dref_predefined_value(self, object_number: Union[int, float, str] = predefined_object, value_type: ValueType = predefined_value_type):
        """test dref of the specified object with minimum value..."""
        self.send_object_value_type(object_number, stable_params.dref, value_type)

    def set_object_dmax_predefined_value(self, object_number: Union[int, float, str] = predefined_object, value_type: ValueType = predefined_value_type):
        """test dmax of the specified object with minimum value..."""
        self.send_object_value_type(object_number, stable_params.dmax, value_type)


    #   _            _      __                              _ _   _       _              _     _           _
    #  | |_ ___  ___| |_   / _| ___  _ __   _ __ ___  _   _| | |_(_)_ __ | | ___    ___ | |__ (_) ___  ___| |_ ___
    #  | __/ _ \/ __| __| | |_ / _ \| '__| | '_ ` _ \| | | | | __| | '_ \| |/ _ \  / _ \| '_ \| |/ _ \/ __| __/ __|
    #  | ||  __/\__ \ |_  |  _| (_) | |    | | | | | | |_| | | |_| | |_) | |  __/ | (_) | |_) | |  __/ (__| |_\__ \
    #   \__\___||___/\__| |_|  \___/|_|    |_| |_| |_|\__,_|_|\__|_| .__/|_|\___|  \___/|_.__// |\___|\___|\__|___/
    #                                                              |_|                      |__/
    def set_objects_stable_parameters_predefined_value(self, objects_range: range = range(1), value_type: ValueType = predefined_value_type):
        """test all "stable" parameters of "number_of_objects" objects with minimum value..."""
        for obj in objects_range:
            self.set_object_stable_parameters_predefined_value(obj + 1, value_type)

    def set_objects_polar_position_predefined_value(self, objects_range: range = range(1), value_type: ValueType = predefined_value_type):
        """test polar position of "number_of_objects" objects with minimum value..."""
        for obj in objects_range:
            self.set_object_polar_position_predefined_value(obj + 1, value_type)

    def set_objects_position_xy_predefined_value(self, objects_range: range = range(1), value_type: ValueType = predefined_value_type):
        """test cartesian position of "number_of_objects" objects with minimum value..."""
        for obj in objects_range:
            self.set_object_position_xy_predefined_value(obj + 1, value_type)

    def set_objects_cartesian_position_predefined_value(self, objects_range: range = range(1), value_type: ValueType = predefined_value_type):
        """test cartesian position of "number_of_objects" objects with minimum value..."""
        for obj in objects_range:
            self.set_object_cartesian_position_predefined_value(obj + 1, value_type)

    def set_objects_width_predefined_value(self, objects_range: range = range(1), value_type: ValueType = predefined_value_type):
        """test width of "number_of_objects" objects with minimum value..."""
        for obj in objects_range:
            self.set_object_width_predefined_value(obj + 1, value_type)

    def set_objects_gain_predefined_value(self, objects_range: range = range(1), value_type: ValueType = predefined_value_type):
        """test gain of "number_of_objects" objects with minimum value..."""
        for obj in objects_range:
            self.set_object_gain_predefined_value(obj + 1, value_type)

    def set_objects_mute_predefined_value(self, objects_range: range = range(1), value_type: ValueType = predefined_value_type):
        """test mute of "number_of_objects" objects with minimum value..."""
        for obj in objects_range:
            self.set_object_mute_predefined_value(obj + 1, value_type)

    def set_objects_dref_predefined_value(self, objects_range: range = range(1), value_type: ValueType = predefined_value_type):
        """test dref of "number_of_objects" objects with minimum value..."""
        for obj in objects_range:
            self.set_object_dref_predefined_value(obj + 1, value_type)

    def set_objects_dmax_predefined_value(self, objects_range: range = range(1), value_type: ValueType = predefined_value_type):
        """test dmax of "number_of_objects" objects with minimum value..."""
        for obj in objects_range:
            self.set_object_dmax_predefined_value(obj + 1, value_type)

    #   _            _        _    _ _         _     _           _
    #  | |_ ___  ___| |_     / \  | | |   ___ | |__ (_) ___  ___| |_ ___
    #  | __/ _ \/ __| __|   / _ \ | | |  / _ \| '_ \| |/ _ \/ __| __/ __|
    #  | ||  __/\__ \ |_   / ___ \| | | | (_) | |_) | |  __/ (__| |_\__ \
    #   \__\___||___/\__| /_/   \_\_|_|  \___/|_.__// |\___|\___|\__|___/
    #                                             |__/
    def set_all_objects_stable_parameters_predefined_value(self, value_type: ValueType = predefined_value_type):
        """test all "stable" parameters of all objects with minimum value..."""
        self.set_object_stable_parameters_predefined_value('*', value_type)

    def set_all_objects_polar_position_predefined_value(self, value_type: ValueType = predefined_value_type):
        """test polar position of all objects with minimum value..."""
        self.set_object_polar_position_predefined_value('*', value_type)

    def set_all_objects_position_xy_predefined_value(self, value_type: ValueType = predefined_value_type):
        """test cartesian position of all objects with minimum value..."""
        self.set_object_position_xy_predefined_value('*', value_type)

    def set_all_objects_cartesian_position_predefined_value(self, value_type: ValueType = predefined_value_type):
        """test cartesian position of all objects with minimum value..."""
        self.set_object_cartesian_position_predefined_value('*', value_type)

    def set_all_objects_width_predefined_value(self, value_type: ValueType = predefined_value_type):
        """test width of all objects with minimum value..."""
        self.set_object_width_predefined_value('*', value_type)

    def set_all_objects_gain_predefined_value(self, value_type: ValueType = predefined_value_type):
        """test gain of all objects with minimum value..."""
        self.set_object_gain_predefined_value('*', value_type)

    def set_all_objects_mute_predefined_value(self, value_type: ValueType = predefined_value_type):
        """test mute of all objects with minimum value..."""
        self.set_object_mute_predefined_value('*', value_type)

    def set_all_objects_dref_predefined_value(self, value_type: ValueType = predefined_value_type):
        """test dref of all objects with minimum value..."""
        self.set_object_dref_predefined_value('*', value_type)

    def set_all_objects_dmax_predefined_value(self, value_type: ValueType = predefined_value_type):
        """test dmax of all objects with minimum value..."""
        self.set_object_dmax_predefined_value('*', value_type)
