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

import threading
from typing import Any, List, Union

from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer, ThreadingOSCUDPServer
from pythonosc.udp_client import SimpleUDPClient

from . import stable_params
from .handler import adm_handler
from .protocol import message_root, Parameter, PackedParameters, ValueType

__all__ = ['OscClientServer']


#   __  __       _          ___  ____   ____    ____ _ _            _      ______
#  |  \/  | __ _(_)_ __    / _ \/ ___| / ___|  / ___| (_) ___ _ __ | |_   / / ___|  ___ _ ____   _____ _ __
#  | |\/| |/ _` | | '_ \  | | | \___ \| |     | |   | | |/ _ \ '_ \| __| / /\___ \ / _ \ '__\ \ / / _ \ '__|
#  | |  | | (_| | | | | | | |_| |___) | |___  | |___| | |  __/ | | | |_ / /  ___) |  __/ |   \ V /  __/ |
#  |_|  |_|\__,_|_|_| |_|  \___/|____/ \____|  \____|_|_|\___|_| |_|\__/_/  |____/ \___|_|    \_/ \___|_|
class OscClientServer(SimpleUDPClient):
    """Simple ADM OSC client inheriting from SimpleUDPClient"""

    default_object = 1

    def __init__(self, address: str = '127.0.0.1', out_port: int = 9000, in_port: int = 9001,
                 allow_broadcast: bool = False, out_address: str = None) -> None:
        """Initialize client

               As this is UDP it will not actually make any attempt to connect to the
               given server at ip:port until the send() method is called.

               Args:
                   address: IP address of server
                   out_port: Port of server
                   in_port: listening Port
                   allow_broadcast: Allow for broadcast transmissions
                   out_address: IP address of the client (outgoing messages) ; address will be used by default if out_address is not provided
               """

        if out_address is None:
            out_address = address

        super().__init__(out_address, out_port, allow_broadcast)

        self.dispatcher = Dispatcher()
        self.dispatcher.map(f"/{message_root}/*", self.__adm_message_handler)
        self.dispatcher.set_default_handler(self.__default_handler)

        BlockingOSCUDPServer.allow_reuse_address = True
        ThreadingOSCUDPServer.allow_reuse_address = True
        self.server = BlockingOSCUDPServer((address, in_port), self.dispatcher)

        # self.server = ThreadingOSCUDPServer((address, in_port), self.dispatcher)

        def _start_server():
            self.server.serve_forever()

        threading.Thread(target=_start_server, name='_start_server').start()

    #                              _                           _
    #    __ _  ___ _ __   ___ _ __(_) ___   ___  ___ _ __   __| |
    #   / _` |/ _ \ '_ \ / _ \ '__| |/ __| / __|/ _ \ '_ \ / _` |
    #  | (_| |  __/ | | |  __/ |  | | (__  \__ \  __/ | | | (_| |
    #   \__, |\___|_| |_|\___|_|  |_|\___| |___/\___|_| |_|\__,_|
    #   |___/
    def send_object_value(self, object_number: Union[int, float, str], param: Union[Parameter, PackedParameters],
                          v: Union[float, tuple, list]):
        """Send a value to object defined by object_number."""
        if v is None:
            return

        self.send_message(param.get_osc_command(object_number), param.validate_value(v))

    def send_object_value_type(self, object_number: Union[int, float, str], param: Union[Parameter, PackedParameters], value_type: ValueType):
        """Send minimum value to object defined by object_number."""
        self.send_object_value(object_number, param, param.get_value_by_type(value_type=value_type))

    def send_listener_value(self, param: Union[Parameter, PackedParameters], v: Union[None, int, str, float, tuple, list]):
        """Send a value to object defined by object_number."""
        if v is None:
            return

        self.send_message(param.get_osc_command(None), param.validate_value(v))

    def send_environment_value(self, param: Union[Parameter, PackedParameters], v: Union[None, int, str, float, tuple, list]):
        """Send a value to object defined by object_number."""
        if v is None:
            return

        self.send_message(param.get_osc_command(None), param.validate_value(v))

    #                   _ _   _                                  _
    #   _ __   ___  ___(_) |_(_) ___  _ __    ___  ___ _ __   __| |
    #  | '_ \ / _ \/ __| | __| |/ _ \| '_ \  / __|/ _ \ '_ \ / _` |
    #  | |_) | (_) \__ \ | |_| | (_) | | | | \__ \  __/ | | | (_| |
    #  | .__/ \___/|___/_|\__|_|\___/|_| |_| |___/\___|_| |_|\__,_|
    #  |_|
    def send_object_position_x(self, object_number: Union[int, float, str], v: float) -> None:
        """Send position X as a float for object defined by object_number."""
        assert object_number > 0
        self.send_object_value(object_number, stable_params.x, v)

    def send_object_position_y(self, object_number: Union[int, float, str], v: float) -> None:
        """Send position Y as a float for object defined by object_number."""
        assert object_number > 0
        self.send_object_value(object_number, stable_params.y, v)

    def send_object_position_z(self, object_number: Union[int, float, str], v: float) -> None:
        """Send position Z as a float for object defined by object_number."""
        assert object_number > 0
        self.send_object_value(object_number, stable_params.z, v)

    def send_object_position_xy(self, object_number: Union[int, float, str],
                                       pos: Union[float, tuple, list]) -> None:
        """Send XYZ position as a list of double for object defined by object_number."""
        assert object_number > 0
        assert pos is not None
        assert len(pos) == 2
        self.send_object_value(object_number, stable_params.xy, pos)

    def send_object_cartesian_position(self, object_number: Union[int, float, str],
                                       pos: Union[float, tuple, list]) -> None:
        """Send XYZ position as a list of double for object defined by object_number."""
        assert object_number > 0
        assert pos is not None
        assert len(pos) == 3
        self.send_object_value(object_number, stable_params.xyz, pos)

    def send_object_position_azimuth(self, object_number: Union[int, float, str], v: float) -> None:
        """Send position azimuth as a float for object defined by object_number."""
        assert object_number > 0
        self.send_object_value(object_number, stable_params.a, v)

    def send_object_position_elevation(self, object_number: Union[int, float, str], v: float) -> None:
        """Send position elevation as a float for object defined by object_number."""
        assert object_number > 0
        self.send_object_value(object_number, stable_params.e, v)

    def send_object_position_distance(self, object_number: Union[int, float, str], v: float) -> None:
        """Send position distance as a float for object defined by object_number."""
        assert object_number > 0
        self.send_object_value(object_number, stable_params.d, v)

    def send_object_polar_position(self, object_number: Union[int, float, str], pos: Union[float, tuple, list]) -> None:
        """Send AED position as a list of double for object defined by object_number."""
        assert object_number > 0
        assert pos is not None
        assert len(pos) == 3
        self.send_object_value(object_number, stable_params.aed, pos)

    #            _     _ _   _                          _
    #  __      _(_) __| | |_| |__    ___  ___ _ __   __| |
    #  \ \ /\ / / |/ _` | __| '_ \  / __|/ _ \ '_ \ / _` |
    #   \ V  V /| | (_| | |_| | | | \__ \  __/ | | | (_| |
    #    \_/\_/ |_|\__,_|\__|_| |_| |___/\___|_| |_|\__,_|
    def send_object_width(self, object_number: Union[int, float, str], v: float) -> None:
        """Send width as a float for object defined by object_number."""
        assert object_number > 0
        self.send_object_value(object_number, stable_params.w, v)

    #               _                            _
    #    __ _  __ _(_)_ __    ___  ___ _ __   __| |
    #   / _` |/ _` | | '_ \  / __|/ _ \ '_ \ / _` |
    #  | (_| | (_| | | | | | \__ \  __/ | | | (_| |
    #   \__, |\__,_|_|_| |_| |___/\___|_| |_|\__,_|
    #   |___/
    def send_object_gain(self, object_number: Union[int, float, str], v: float) -> None:
        """Send gain as a float for object defined by object_number."""
        assert object_number > 0
        self.send_object_value(object_number, stable_params.gain, v)

    def send_object_mute(self, object_number: Union[int, float, str], v: int) -> None:
        """Send mute as a int for object defined by object_number."""
        assert object_number > 0
        self.send_object_value(object_number, stable_params.mute, v)

    def send_object_dref(self, object_number: Union[int, float, str], v: float) -> None:
        """Send dref as a float for object defined by object_number."""
        assert object_number > 0
        self.send_object_value(object_number, stable_params.dref, v)

    def send_object_dmax(self, object_number: Union[int, float, str], v: float) -> None:
        """Send dmax as a float for object defined by object_number."""
        assert object_number > 0
        self.send_object_value(object_number, stable_params.dmax, v)

    #                    __ _
    #    ___ ___  _ __  / _(_) __ _
    #   / __/ _ \| '_ \| |_| |/ _` |
    #  | (_| (_) | | | |  _| | (_| |
    #   \___\___/|_| |_|_| |_|\__, |
    #                         |___/
    def send_object_name(self, object_number: Union[int, float, str], v: str) -> None:
        """Send gain as a float for object defined by object_number."""
        assert object_number > 0
        self.send_object_value(object_number, stable_params.name, v)

    #   _____            _                                      _
    #  | ____|_ ____   _(_)_ __ ___  _ __  _ __ ___   ___ _ __ | |_
    #  |  _| | '_ \ \ / / | '__/ _ \| '_ \| '_ ` _ \ / _ \ '_ \| __|
    #  | |___| | | \ V /| | | | (_) | | | | | | | | |  __/ | | | |_
    #  |_____|_| |_|\_/ |_|_|  \___/|_| |_|_| |_| |_|\___|_| |_|\__|
    def send_program_change(self, v: str) -> None:
        """Send gain as a float for object defined by object_number."""
        self.send_environment_value(stable_params.program_change, v)

    #   _     _     _
    #  | |   (_)___| |_ ___ _ __   ___ _ __
    #  | |   | / __| __/ _ \ '_ \ / _ \ '__|
    #  | |___| \__ \ ||  __/ | | |  __/ |
    #  |_____|_|___/\__\___|_| |_|\___|_|
    def send_listener_position_x(self, v: float) -> None:
        """Send Listener position X as a float"""
        self.send_listener_value(stable_params.l_x, v)

    def send_listener_position_y(self, v: float) -> None:
        """Send Listener position Y as a float"""
        self.send_listener_value(stable_params.l_y, v)

    def send_listener_position_z(self, v: float) -> None:
        """Send Listener position Z as a float"""
        self.send_listener_value(stable_params.l_z, v)

    def send_listener_position_yaw(self, v: float) -> None:
        """Send Listener position X as a float"""
        self.send_listener_value(stable_params.l_yaw, v)

    def send_listener_position_pitch(self, v: float) -> None:
        """Send Listener position Y as a float"""
        self.send_listener_value(stable_params.l_pitch, v)

    def send_listener_position_roll(self, v: float) -> None:
        """Send Listener position Z as a float"""
        self.send_listener_value(stable_params.l_roll, v)

    def send_listener_cartesian_position(self, pos: Union[float, tuple, list]) -> None:
        """Send Listener XYZ position as a list of double"""
        assert pos is not None
        assert len(pos) == 3
        self.send_listener_value(stable_params.lis_xyz, pos)

    def send_listener_orientation(self, rot: Union[float, tuple, list]) -> None:
        """Send Listener Yaw Pitch Roll orientation as a list of double."""
        assert rot is not None
        assert len(rot) == 3
        self.send_listener_value(stable_params.lis_ypr, rot)


    #                              _
    #    __ _  ___ _ __   ___ _ __(_) ___    __ _ _   _  ___ _ __ _   _
    #   / _` |/ _ \ '_ \ / _ \ '__| |/ __|  / _` | | | |/ _ \ '__| | | |
    #  | (_| |  __/ | | |  __/ |  | | (__  | (_| | |_| |  __/ |  | |_| |
    #   \__, |\___|_| |_|\___|_|  |_|\___|  \__, |\__,_|\___|_|   \__, |
    #   |___/                                  |_|                |___/
    def query_object_value(self, object_number: Union[int, float, str], param: Union[Parameter, PackedParameters]):
        """Send a value to object defined by object_number."""
        self.send_message(param.get_osc_query_command(object_number), None)
        # todo: listen for value from the connected server...

    def query_listener_value(self, param: Union[Parameter, PackedParameters]):
        """Send a value to object defined by object_number."""
        self.send_message(param.get_osc_query_command(None), None)
        # todo: listen for value from the connected server...

    def query_environment_value(self, param: Union[Parameter, PackedParameters]):
        """Send a value to object defined by object_number."""
        self.send_message(param.get_osc_query_command(None), None)
        # todo: listen for value from the connected server...

    #                   _ _   _
    #   _ __   ___  ___(_) |_(_) ___  _ __     __ _ _   _  ___ _ __ _   _
    #  | '_ \ / _ \/ __| | __| |/ _ \| '_ \   / _` | | | |/ _ \ '__| | | |
    #  | |_) | (_) \__ \ | |_| | (_) | | | | | (_| | |_| |  __/ |  | |_| |
    #  | .__/ \___/|___/_|\__|_|\___/|_| |_|  \__, |\__,_|\___|_|   \__, |
    #  |_|                                       |_|                |___/
    def query_object_polar_position(self, object_number: Union[int, float, str]):
        self.query_object_value(object_number, stable_params.aed)

    def query_object_cartesian_position(self, object_number: Union[int, float, str]):
        self.query_object_value(object_number, stable_params.xyz)

    #            _     _ _   _
    #  __      _(_) __| | |_| |__     __ _ _   _  ___ _ __ _   _
    #  \ \ /\ / / |/ _` | __| '_ \   / _` | | | |/ _ \ '__| | | |
    #   \ V  V /| | (_| | |_| | | | | (_| | |_| |  __/ |  | |_| |
    #    \_/\_/ |_|\__,_|\__|_| |_|  \__, |\__,_|\___|_|   \__, |
    #                                   |_|                |___/
    def query_object_width(self, object_number: Union[int, float, str]):
        self.query_object_value(object_number, stable_params.w)

    #               _
    #    __ _  __ _(_)_ __     __ _ _   _  ___ _ __ _   _
    #   / _` |/ _` | | '_ \   / _` | | | |/ _ \ '__| | | |
    #  | (_| | (_| | | | | | | (_| | |_| |  __/ |  | |_| |
    #   \__, |\__,_|_|_| |_|  \__, |\__,_|\___|_|   \__, |
    #   |___/                    |_|                |___/
    def query_object_gain(self, object_number: Union[int, float, str]):
        self.query_object_value(object_number, stable_params.gain)

    def query_object_mute(self, object_number: Union[int, float, str]):
        self.query_object_value(object_number, stable_params.mute)

    def query_object_dref(self, object_number: Union[int, float, str]):
        self.query_object_value(object_number, stable_params.dref)

    def query_object_dmax(self, object_number: Union[int, float, str]):
        self.query_object_value(object_number, stable_params.dmax)

    #                    __ _
    #    ___ ___  _ __  / _(_) __ _    __ _ _   _  ___ _ __ _   _
    #   / __/ _ \| '_ \| |_| |/ _` |  / _` | | | |/ _ \ '__| | | |
    #  | (_| (_) | | | |  _| | (_| | | (_| | |_| |  __/ |  | |_| |
    #   \___\___/|_| |_|_| |_|\__, |  \__, |\__,_|\___|_|   \__, |
    #                         |___/      |_|                |___/
    def query_object_name(self, object_number: Union[int, float, str]):
        self.query_object_value(object_number, stable_params.name)

    def query_object_program_change(self):
        self.query_environment_value(stable_params.program_change)

    #   _     _     _                          ___
    #  | |   (_)___| |_ ___ _ __   ___ _ __   / _ \ _   _  ___ _ __ _   _
    #  | |   | / __| __/ _ \ '_ \ / _ \ '__| | | | | | | |/ _ \ '__| | | |
    #  | |___| \__ \ ||  __/ | | |  __/ |    | |_| | |_| |  __/ |  | |_| |
    #  |_____|_|___/\__\___|_| |_|\___|_|     \__\_\\__,_|\___|_|   \__, |
    #                                                               |___/
    def query_listener_position_x(self) -> None:
        self.query_listener_value(stable_params.l_x)

    def query_listener_position_y(self) -> None:
        self.query_listener_value(stable_params.l_y)

    def query_listener_position_z(self) -> None:
        self.query_listener_value(stable_params.l_z)

    def query_listener_position_yaw(self) -> None:
        self.query_listener_value(stable_params.l_yaw)

    def query_listener_position_pitch(self) -> None:
        self.query_listener_value(stable_params.l_pitch)

    def query_listener_position_roll(self) -> None:
        self.query_listener_value(stable_params.l_roll)

    def query_listener_cartesian_position(self) -> None:
        self.query_listener_value(stable_params.lis_xyz)

    def query_listener_orientation(self) -> None:
        self.query_listener_value(stable_params.lis_ypr)

    #         _ _         _     _           _
    #    __ _| | |   ___ | |__ (_) ___  ___| |_    __ _ _   _  ___ _ __ _   _
    #   / _` | | |  / _ \| '_ \| |/ _ \/ __| __|  / _` | | | |/ _ \ '__| | | |
    #  | (_| | | | | (_) | |_) | |  __/ (__| |_  | (_| | |_| |  __/ |  | |_| |
    #   \__,_|_|_|  \___/|_.__// |\___|\___|\__|  \__, |\__,_|\___|_|   \__, |
    #                        |__/                    |_|                |___/
    def query_all_objects_value(self, param: Union[Parameter, PackedParameters]):
        """Send a value to object defined by object_number."""
        self.send_message(param.get_osc_query_command('*'), None)
        # todo: listen for value from the connected server...

    def query_all_polar_positions(self):
        self.query_all_objects_value(stable_params.aed)

    def query_all_cartesian_positions(self):
        self.query_all_objects_value(stable_params.xyz)

    #   _                           _
    #  (_)_ __   ___ ___  _ __ ___ (_)_ __   __ _   _ __ ___   ___  ___ ___  __ _  __ _  ___
    #  | | '_ \ / __/ _ \| '_ ` _ \| | '_ \ / _` | | '_ ` _ \ / _ \/ __/ __|/ _` |/ _` |/ _ \
    #  | | | | | (_| (_) | | | | | | | | | | (_| | | | | | | |  __/\__ \__ \ (_| | (_| |  __/
    #  |_|_| |_|\___\___/|_| |_| |_|_|_| |_|\__, | |_| |_| |_|\___||___/___/\__,_|\__, |\___|
    #                                       |___/                                 |___/
    @staticmethod
    def __default_handler(address, *args):
        print(f"unhandled incoming message: {address}: {args}")

    def __adm_message_handler(self, address, *args):
        try:
            target, objects, parameter, args = adm_handler(address, *args)

            if args is None:
                self.on_received_query(target, objects, parameter)
            else:
                self.on_received_message(target, objects, parameter, *args)

        except ValueError as e:
            print(e)

    def on_received_query(target: str, objects: Union[int, dict, list[int]],
                          parameter: Union[Parameter, PackedParameters]):
        # unhandled message ! just print it
        name = parameter.attribute
        sub = str(parameter.sub_element)
        if sub.lower() != name.lower():
            name = f'{sub} {name}'

        print(f"received valid adm query for {target} :: {objects} :: {name}")

        if type(objects) is int:
            self.send_object_value(objects, parameter, parameter.get_default_value())
        elif type(objects) is dict:
            for key, o in objects.items():
                self.send_object_value(o, parameter, parameter.get_default_value())
        elif type(objects) is list:
            for o in objects:
                self.send_object_value(o, parameter, parameter.get_default_value())

    @staticmethod
    def on_received_message(target: str, objects: Union[int, dict, list[int]],
                            parameter: Union[Parameter, PackedParameters], *args: Union[Any, List[Any]]):
        # unhandled message ! just print it
        name = parameter.attribute
        sub = str(parameter.sub_element)
        if sub.lower() != name.lower():
            name = f'{sub} {name}'

        arg = f'{args}'.replace(',)', ')')

        print(f"received valid adm message for {target} :: {objects} :: {name} {arg}")
