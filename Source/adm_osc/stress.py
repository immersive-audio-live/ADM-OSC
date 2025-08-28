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

from math import *
from time import sleep
from .tests import TestClient

__all__ = ['StressClient']


#   ____  _                        ____ _ _            _
#  / ___|| |_ _ __ ___  ___ ___   / ___| (_) ___ _ __ | |_
#  \___ \| __| '__/ _ \/ __/ __| | |   | | |/ _ \ '_ \| __|
#   ___) | |_| | |  __/\__ \__ \ | |___| | |  __/ | | | |_
#  |____/ \__|_|  \___||___/___/  \____|_|_|\___|_| |_|\__|
class StressClient(TestClient):

    def __init__(self, address: str = '127.0.0.1', out_port: int = 9000, in_port: int = 9001, out_address: str = None) -> None:
        super().__init__(address, out_port, in_port, out_address)

    def stress_polar_position(self, number_of_objects: int = 1, duration_in_second: float = 10.0, interval_in_milliseconds: float = 10.0):

        azimuth = 180
        elevation = 0.0
        elevation_fact = 0.5
        distance = 1.0
        phase = 1.0
        interval = interval_in_milliseconds / 1000.0

        while duration_in_second > 0:
            for obj in range(number_of_objects):
                obj_num = (obj + 1)
                a_ = ((azimuth + 360 * (obj_num / number_of_objects) - 180) % 360) - 180
                e_ = elevation * sin(a_) * elevation_fact
                d_ = distance
                self.send_object_polar_position(obj_num, [a_, e_, d_])

            azimuth += 1.0

            elevation += phase
            if elevation > 90.0 or elevation < 0.0:
                phase = -phase

            distance = 2.0 + sin(duration_in_second)

            duration_in_second -= interval
            sleep(interval)

    def stress_polar_azimuth(self, number_of_objects: int = 1, duration_in_second: float = 10.0, interval_in_milliseconds: float = 10.0):
        azimuth = 180
        elevation = 0.0
        elevation_fact = 0.5
        distance = 0.5
        phase = 1.0
        interval = interval_in_milliseconds / 1000.0

        while duration_in_second > 0:
            for obj in range(number_of_objects):
                obj_num = (obj + 1)
                a_ = azimuth
                e_ = elevation
                d_ = distance
                self.send_object_polar_position(obj_num, [a_, e_, d_])

            azimuth -= 1.0
            if azimuth < -180.0:
                azimuth = 180.0

            duration_in_second -= interval
            sleep(interval)

    def stress_cartesian_position(self, number_of_objects: int = 1, duration_in_second: float = 10.0, interval_in_milliseconds: float = 10.0):

        target_range = 1.0
        target_sin = sin(target_range)
        target_sin_inv = 1.0 / target_sin
        y_fact = 0.5
        z_fact = 0.5
        step = pi * 2.0 / number_of_objects
        interval = interval_in_milliseconds / 1000.0
        iteration = 1

        while duration_in_second > 0:

            wave = -pi

            for obj in range(number_of_objects):
                obj_num = (obj + 1)
                w_ = ((obj_num + iteration) % number_of_objects / number_of_objects)
                x_ = (sin(w_) * target_sin_inv * 2.0) - target_range
                y_ = sin(wave) * y_fact
                z_ = cos(wave) * z_fact

                self.send_object_cartesian_position(obj_num, [x_, y_, z_])

                wave = wave + step

            iteration += 1

            duration_in_second -= interval
            sleep(interval)

    def stress_all(self, number_of_objects: int = 1, duration_in_second: float = 10.0, interval_in_milliseconds: float = 10.0):
        self.stress_polar_position(number_of_objects, duration_in_second / 2, interval_in_milliseconds)
        self.stress_cartesian_position(number_of_objects, duration_in_second / 2, interval_in_milliseconds)
