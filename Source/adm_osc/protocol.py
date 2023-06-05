#  ==============================================================================
# MIT License
#
# Copyright (c) 2022 immersive-audio-live
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

import random
from enum import Enum
from typing import Any, Generator, Union

#                   _
#   ___ _   _ _ __ | |_ __ ___  __
#  / __| | | | '_ \| __/ _` \ \/ /
#  \__ \ |_| | | | | || (_| |>  <
#  |___/\__, |_| |_|\__\__,_/_/\_\
#       |___/
message_root = 'adm'
object_name = 'obj'
query_cmd = 'get'
msg_obj = f'/{message_root}/{object_name}'
object_test_number = 42


def object_message(object_number: Union[int, float, str], command: str) -> str:
    return f'{msg_obj}/{object_number}/{command}'


def object_query_message(object_number: Union[int, float, str], command: str) -> str:
    return f'{msg_obj}/{object_number}/{command}/{query_cmd}'


#   _                               _       __ _       _ _   _
#  | |_ _   _ _ __   ___  ___    __| | ___ / _(_)_ __ (_) |_(_) ___  _ __
#  | __| | | | '_ \ / _ \/ __|  / _` |/ _ \ |_| | '_ \| | __| |/ _ \| '_ \
#  | |_| |_| | |_) |  __/\__ \ | (_| |  __/  _| | | | | | |_| | (_) | | | |
#   \__|\__, | .__/ \___||___/  \__,_|\___|_| |_|_| |_|_|\__|_|\___/|_| |_|
#       |___/|_|
class SEnum(Enum):
    def __str__(self):
        return f"{self._name_}".lower()


class SubElement(SEnum):
    Position = 1
    Width = 2
    Height = 3
    Depth = 4
    Cartesian = 5
    Gain = 6
    Any = 6


class Units(SEnum):
    Degrees = 1
    Normalized = 2
    Ratio = 3
    Boolean = 4
    LinearGain = 5


class Type(SEnum):
    Int = 1
    Float = 2
    String = 3

    def as_osc_string(self) -> str:
        return str(self)[0].lower()


class Status(SEnum):
    Stable = 1
    InProgress = 2


#             _        _
#    ___ __ _| |_ __ _| | ___   __ _
#   / __/ _` | __/ _` | |/ _ \ / _` |
#  | (_| (_| | || (_| | | (_) | (_| |
#   \___\__,_|\__\__,_|_|\___/ \__, |
#                              |___/
value_catalog = {}


#   ____                                _               ___  _     _           _   
#  |  _ \ __ _ _ __ __ _ _ __ ___   ___| |_ ___ _ __   / _ \| |__ (_) ___  ___| |_ 
#  | |_) / _` | '__/ _` | '_ ` _ \ / _ \ __/ _ \ '__| | | | | '_ \| |/ _ \/ __| __|
#  |  __/ (_| | | | (_| | | | | | |  __/ ||  __/ |    | |_| | |_) | |  __/ (__| |_ 
#  |_|   \__,_|_|  \__,_|_| |_| |_|\___|\__\___|_|     \___/|_.__// |\___|\___|\__|
#                                                               |__/
class Parameter(object):

    def __init__(self, sub_element: SubElement, attribute: str, osc_command: str, description: str, units: Units = Units.Normalized, type_: Type = Type.Float, min_=0.0, max_=1.0,
                 def_=1.0, status: Status = Status.InProgress, comment: str = '') -> None:

        super().__init__()

        self.sub_element = sub_element
        self.attribute = attribute
        self.osc_command = osc_command
        self.description = description
        self.units = units
        self.type = type_
        self.min = min_
        self.max = max_
        self.default = def_
        self.status = status
        self.comment = comment

        value_catalog[self.attribute] = self

    def __str__(self) -> str:
        return (f'{self.sub_element} {self.attribute}: \n'
                f'\t* description: {self.description}\n'
                f'\t* osc format: {self.osc_format()} : e.g. {self.osc_example()}"\n'
                f'\t* unit: {self.units} | type: {self.type} | min: {self.min} | max:{self.max} | default:{self.default}\n'
                f'\t* comment: {self.comment}\n'
                )

    def osc_format(self) -> str:
        cmd = object_message(object_number='(k)', command=self.osc_command)
        return f'{cmd} {self.type.as_osc_string()}'

    def osc_example(self, val: Union[int, float, str, None] = None) -> str:
        obj = object_test_number
        cmd = object_message(object_number=obj, command=self.osc_command)
        if val is None:
            val = self.get_random_value()
        return f'{cmd} {val}'

    def get_number_of_values(self) -> int:
        return 1

    def get_parameters(self):
        return [self]

    def get_min_value(self) -> Union[int, float]:
        return self.min

    def get_max_value(self) -> Union[int, float]:
        return self.max

    def get_default_value(self) -> Union[int, float]:
        return self.default

    def get_random_value(self) -> Union[int, float]:
        return float(random.randrange(start=int(self.min * 100.0), stop=int(self.max * 100.0))) / 100.0

    def get_osc_command(self, object_number: Union[int, float, str]) -> str:
        return object_message(object_number, command=self.osc_command)

    def get_osc_query_command(self, object_number: Union[int, float, str]) -> str:
        return object_query_message(object_number, command=self.osc_command)

    def validate_value(self, value: Union[int, float, str]) -> Union[int, float, str]:
        if type(value) is not str:
            return max(min(value, self.get_max_value()), self.get_min_value())
        else:
            return value

    def is_stable(self):
        return self.status == Status.Stable

    def is_in_progress(self):
        return self.status == Status.InProgress


#   ____            _            _   ____                                _            
#  |  _ \ __ _  ___| | _____  __| | |  _ \ __ _ _ __ __ _ _ __ ___   ___| |_ ___ _ __ 
#  | |_) / _` |/ __| |/ / _ \/ _` | | |_) / _` | '__/ _` | '_ ` _ \ / _ \ __/ _ \ '__|
#  |  __/ (_| | (__|   <  __/ (_| | |  __/ (_| | | | (_| | | | | | |  __/ ||  __/ |   
#  |_|   \__,_|\___|_|\_\___|\__,_| |_|   \__,_|_|  \__,_|_| |_| |_|\___|\__\___|_|   
class PackedParameters(Parameter):

    def __init__(self, sub_element: SubElement, attribute: str, osc_command: str, description: str, params: list[Parameter], status: Status, comment: str = '') -> None:

        super().__init__(sub_element=sub_element, attribute=attribute, osc_command=osc_command, description=description, status=status, comment=comment)
        self.params = params

    def __str__(self) -> str:
        text = (f'{self.sub_element} {self.attribute}:\n'
                f'\t* description: {self.description}\n'
                f'\t* osc format: {self.osc_format()} : e.g. {self.osc_example()}\n'
                f'\t* comment: {self.comment}\n'
                f'\t* parameters: \n')
        for param in self.params:
            text += f'\t\t- {param.attribute} (unit: {param.units} | type: {param.type} | min: {param.min} | max:{param.max} | default:{param.default})\n'
        return text

    def osc_format(self) -> str:
        cmd = object_message(object_number='(k)', command=self.osc_command)
        param_types = ''.join(f'{param.type.as_osc_string()}' for param in self.params)
        return f'{cmd} {param_types}'

    def osc_example(self, values: list[Union[int, float, str, None]] = None) -> str:
        obj = object_test_number
        cmd = object_message(object_number=obj, command=self.osc_command)
        params = ''
        if values is not None:
            for val in values:
                params += f'{val} '
        else:
            for val in self.params:
                params += f'{val.get_random_value()} '
        return f'{cmd} {params}'.strip()

    def get_number_of_values(self) -> int:
        return len(self.params)

    def get_parameters(self) -> list[Parameter]:
        return self.params

    def get_min_value(self) -> list[Union[int, float]]:
        return [param.get_min_value() for param in self.params]

    def get_max_value(self) -> list[Union[int, float]]:
        return [param.get_max_value() for param in self.params]

    def get_default_value(self) -> list[Union[int, float]]:
        return [param.get_default_value() for param in self.params]

    def get_random_value(self) -> list[Union[int, float]]:
        return [param.get_random_value() for param in self.params]

    def validate_value(self, value: list[Union[int, float, str]]) -> list[Union[int, float, str]]:
        return [param.validate_value(value[i]) for i, param in enumerate(self.params)]


#   _          _
#  | |__   ___| |_ __   ___ _ __ ___
#  | '_ \ / _ \ | '_ \ / _ \ '__/ __|
#  | | | |  __/ | |_) |  __/ |  \__ \
#  |_| |_|\___|_| .__/ \___|_|  |___/
#               |_|
def get_all_parameters() -> Generator[Any, Any, None]:
    return (val for key, val in value_catalog.items())


def get_stable_parameters() -> Generator[Any, Any, None]:
    return (val for key, val in value_catalog.items() if val.is_stable())


def get_in_progress_parameters() -> Generator[Any, Any, None]:
    return (val for key, val in value_catalog.items() if val.is_in_progress())


def find_parameter(attribute: str) -> Union[Parameter, PackedParameters, None]:
    return next(
        (
            param
            for param in get_all_parameters()
            if param.attribute == attribute
        ),
        None,
    )


#              _       _               _        _
#   _ __  _ __(_)_ __ | |_    ___ __ _| |_ __ _| | ___   __ _
#  | '_ \| '__| | '_ \| __|  / __/ _` | __/ _` | |/ _ \ / _` |
#  | |_) | |  | | | | | |_  | (_| (_| | || (_| | | (_) | (_| |
#  | .__/|_|  |_|_| |_|\__|  \___\__,_|\__\__,_|_|\___/ \__, |
#  |_|                                                  |___/
def dump_protocol() -> str:
    return ''.join(f'{param}\n\n' for param in get_all_parameters())

