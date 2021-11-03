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

from . import handler, protocol


#   __  __       _            _    ____  __  __        ___  ____   ____    ____ _ _            _
#  |  \/  | __ _(_)_ __      / \  |  _ \|  \/  |      / _ \/ ___| / ___|  / ___| (_) ___ _ __ | |_
#  | |\/| |/ _` | | '_ \    / _ \ | | | | |\/| |_____| | | \___ \| |     | |   | | |/ _ \ '_ \| __|
#  | |  | | (_| | | | | |  / ___ \| |_| | |  | |_____| |_| |___) | |___  | |___| | |  __/ | | | |_
#  |_|  |_|\__,_|_|_| |_| /_/   \_\____/|_|  |_|      \___/|____/ \____|  \____|_|_|\___|_| |_|\__|
class AdmOscClientServer(SimpleUDPClient):
    """Simple ADM OSC client inheriting from SimpleUDPClient"""

    default_object = 1

    def __init__(self, address: str = '127.0.0.1', out_port: int = 9000, in_port: int = 9001, allow_broadcast: bool = False) -> None:
        """Initialize client

               As this is UDP it will not actually make any attempt to connect to the
               given server at ip:port until the send() method is called.

               Args:
                   address: IP address of server
                   out_port: Port of server
                   in_port: listening Port
                   allow_broadcast: Allow for broadcast transmissions
               """

        super().__init__(address, out_port, allow_broadcast)

        self.dispatcher = Dispatcher()
        self.dispatcher.map(f"/{protocol.message_root}/*", self.__adm_message_handler)
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
    def send_object_value(self, object_number: Union[int, float, str], param: Union[protocol.Parameter, protocol.PackedParameters], v: Union[float, tuple, list]):
        """Send a value to object defined by object_number."""
        self.send_message(param.get_osc_command(object_number), param.validate_value(v))

    def send_object_value_min(self, object_number: Union[int, float, str], param: Union[protocol.Parameter, protocol.PackedParameters]):
        """Send minimum value to object defined by object_number."""
        self.send_object_value(object_number, param, param.get_min_value())

    def send_object_value_max(self, object_number: Union[int, float, str], param: Union[protocol.Parameter, protocol.PackedParameters]):
        """Send maximum value to object defined by object_number."""
        self.send_object_value(object_number, param, param.get_max_value())

    def send_object_value_default(self, object_number: Union[int, float, str], param: Union[protocol.Parameter, protocol.PackedParameters]):
        """Send default value to object defined by object_number."""
        self.send_object_value(object_number, param, param.get_default_value())

    def send_object_value_random(self, object_number: Union[int, float, str], param: Union[protocol.Parameter, protocol.PackedParameters]):
        """Send random value to object defined by object_number."""
        self.send_object_value(object_number, param, param.get_random_value())

    #                   _ _   _                                  _
    #   _ __   ___  ___(_) |_(_) ___  _ __    ___  ___ _ __   __| |
    #  | '_ \ / _ \/ __| | __| |/ _ \| '_ \  / __|/ _ \ '_ \ / _` |
    #  | |_) | (_) \__ \ | |_| | (_) | | | | \__ \  __/ | | | (_| |
    #  | .__/ \___/|___/_|\__|_|\___/|_| |_| |___/\___|_| |_|\__,_|
    #  |_|
    def send_object_position_x(self, object_number: Union[int, float, str], v: float) -> None:
        """Send position X as a float for object defined by object_number."""
        assert object_number > 0
        self.send_object_value(object_number, protocol.x, v)

    def send_object_position_y(self, object_number: Union[int, float, str], v: float) -> None:
        """Send position Y as a float for object defined by object_number."""
        assert object_number > 0
        self.send_object_value(object_number, protocol.y, v)

    def send_object_position_z(self, object_number: Union[int, float, str], v: float) -> None:
        """Send position Z as a float for object defined by object_number."""
        assert object_number > 0
        self.send_object_value(object_number, protocol.z, v)

    def send_object_cartesian_position(self, object_number: Union[int, float, str], pos: Union[float, tuple, list]) -> None:
        """Send XYZ position as a list of double for object defined by object_number."""
        assert object_number > 0
        assert pos is not None
        assert len(pos) == 3
        self.send_object_value(object_number, protocol.xyz, pos)

    def send_object_position_azimuth(self, object_number: Union[int, float, str], v: float) -> None:
        """Send position azimuth as a float for object defined by object_number."""
        assert object_number > 0
        self.send_object_value(object_number, protocol.a, v)

    def send_object_position_elevation(self, object_number: Union[int, float, str], v: float) -> None:
        """Send position elevation as a float for object defined by object_number."""
        assert object_number > 0
        self.send_object_value(object_number, protocol.e, v)

    def send_object_position_distance(self, object_number: Union[int, float, str], v: float) -> None:
        """Send position distance as a float for object defined by object_number."""
        assert object_number > 0
        self.send_object_value(object_number, protocol.d, v)

    def send_object_polar_position(self, object_number: Union[int, float, str], pos: Union[float, tuple, list]) -> None:
        """Send AED position as a list of double for object defined by object_number."""
        assert object_number > 0
        assert pos is not None
        assert len(pos) == 3
        self.send_object_value(object_number, protocol.aed, pos)

    #               _                            _
    #    __ _  __ _(_)_ __    ___  ___ _ __   __| |
    #   / _` |/ _` | | '_ \  / __|/ _ \ '_ \ / _` |
    #  | (_| | (_| | | | | | \__ \  __/ | | | (_| |
    #   \__, |\__,_|_|_| |_| |___/\___|_| |_|\__,_|
    #   |___/
    def send_object_gain(self, object_number: Union[int, float, str], v: float) -> None:
        """Send gain as a float for object defined by object_number."""
        assert object_number > 0
        self.send_object_value(object_number, protocol.gain, v)

    #                              _
    #    __ _  ___ _ __   ___ _ __(_) ___    __ _ _   _  ___ _ __ _   _
    #   / _` |/ _ \ '_ \ / _ \ '__| |/ __|  / _` | | | |/ _ \ '__| | | |
    #  | (_| |  __/ | | |  __/ |  | | (__  | (_| | |_| |  __/ |  | |_| |
    #   \__, |\___|_| |_|\___|_|  |_|\___|  \__, |\__,_|\___|_|   \__, |
    #   |___/                                  |_|                |___/
    def query_object_value(self, object_number: Union[int, float, str], param: Union[protocol.Parameter, protocol.PackedParameters]):
        """Send a value to object defined by object_number."""
        self.send_message(param.get_osc_query_command(object_number), None)
        # todo: listen for value from the connected server...

    #                   _ _   _
    #   _ __   ___  ___(_) |_(_) ___  _ __     __ _ _   _  ___ _ __ _   _
    #  | '_ \ / _ \/ __| | __| |/ _ \| '_ \   / _` | | | |/ _ \ '__| | | |
    #  | |_) | (_) \__ \ | |_| | (_) | | | | | (_| | |_| |  __/ |  | |_| |
    #  | .__/ \___/|___/_|\__|_|\___/|_| |_|  \__, |\__,_|\___|_|   \__, |
    #  |_|                                       |_|                |___/
    def query_object_polar_position(self, object_number: Union[int, float, str]):
        self.query_object_value(object_number, protocol.aed)

    def query_object_cartesian_position(self, object_number: Union[int, float, str]):
        self.query_object_value(object_number, protocol.xyz)

    #               _
    #    __ _  __ _(_)_ __     __ _ _   _  ___ _ __ _   _
    #   / _` |/ _` | | '_ \   / _` | | | |/ _ \ '__| | | |
    #  | (_| | (_| | | | | | | (_| | |_| |  __/ |  | |_| |
    #   \__, |\__,_|_|_| |_|  \__, |\__,_|\___|_|   \__, |
    #   |___/                    |_|                |___/
    def query_object_gain(self, object_number: Union[int, float, str]):
        self.query_object_value(object_number, protocol.gain)

    #         _ _         _     _           _
    #    __ _| | |   ___ | |__ (_) ___  ___| |_    __ _ _   _  ___ _ __ _   _
    #   / _` | | |  / _ \| '_ \| |/ _ \/ __| __|  / _` | | | |/ _ \ '__| | | |
    #  | (_| | | | | (_) | |_) | |  __/ (__| |_  | (_| | |_| |  __/ |  | |_| |
    #   \__,_|_|_|  \___/|_.__// |\___|\___|\__|  \__, |\__,_|\___|_|   \__, |
    #                        |__/                    |_|                |___/
    def query_all_objects_value(self, param: Union[protocol.Parameter, protocol.PackedParameters]):
        """Send a value to object defined by object_number."""
        self.send_message(param.get_osc_query_command('*'), None)
        # todo: listen for value from the connected server...

    def query_all_polar_positions(self):
        self.query_all_objects_value(protocol.aed)

    def query_all_cartesian_positions(self):
        self.query_all_objects_value(protocol.xyz)

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
            target, objects, parameter, args = handler.adm_handler(address, *args)
            self.on_received_message(target, objects, parameter, *args)
        except ValueError as e:
            print(e)

    @staticmethod
    def on_received_message(target: str, objects: Union[int, dict, list[int]], parameter: Union[protocol.Parameter, protocol.PackedParameters], *args: Union[Any, List[Any]]):
        # unhandled message ! just print it
        name = parameter.attribute
        sub = str(parameter.sub_element)
        if sub.lower() != name.lower():
            name = f'{sub} {name}'

        arg = f'{args}'.replace(',)', ')')

        print(f"received valid adm message for {target} :: {objects} :: {name} {arg}")
