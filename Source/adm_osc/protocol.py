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
#query_cmd = 'get'
query_cmd = '' # now, in final stable 1.0 version of the protocol, query should be the same command but withour arguments
object_test_number = 42


#    ___  _     _           _  _____
#   / _ \| |__ (_) ___  ___| ||_   _|   _ _ __   ___
#  | | | | '_ \| |/ _ \/ __| __|| || | | | '_ \ / _ \
#  | |_| | |_) | |  __/ (__| |_ | || |_| | |_) |  __/
#   \___/|_.__// |\___|\___|\__||_| \__, | .__/ \___|
#            |__/                   |___/|_|
object_type_list = []


class ObjectType(object):
    def __init__(self, name: str, msg_name: str, description: str) -> None:
        super().__init__()
        self.name = name
        self.msg_name = msg_name
        self.description = description
        object_type_list.append(self)

    def __str__(self) -> str:
        return (f'{self.name} - msg_name: {self.msg_name}: \n'
                f'\t* description: {self.description}\n'
                )


obj = ObjectType(name='Object', msg_name='obj', description='used to describe an a object (source) in space')
lis = ObjectType(name='Listener', msg_name='lis', description='used to describe the listener in the space')
env = ObjectType(name='Environment', msg_name='env', description='used to describe global scene or environment')


#                                                                  _                   _   _               _   _      _
#   _ __ ___   ___  ___ ___  __ _  __ _  ___    ___ ___  _ __  ___| |_ _ __ _   _  ___| |_(_) ___  _ __   | | | | ___| |_ __   ___ _ __ ___
#  | '_ ` _ \ / _ \/ __/ __|/ _` |/ _` |/ _ \  / __/ _ \| '_ \/ __| __| '__| | | |/ __| __| |/ _ \| '_ \  | |_| |/ _ \ | '_ \ / _ \ '__/ __|
#  | | | | | |  __/\__ \__ \ (_| | (_| |  __/ | (_| (_) | | | \__ \ |_| |  | |_| | (__| |_| | (_) | | | | |  _  |  __/ | |_) |  __/ |  \__ \
#  |_| |_| |_|\___||___/___/\__,_|\__, |\___|  \___\___/|_| |_|___/\__|_|   \__,_|\___|\__|_|\___/|_| |_| |_| |_|\___|_| .__/ \___|_|  |___/
#                                 |___/                                                                                |_|
def adm_osc_message(object_type: ObjectType, object_number: Union[None, int, float, str], command: str) -> str:

    sub_cmd = f'{object_number}/{command}' if object_number is not None or object_type.name == 'Object' else f'{command}'
    return f'/{message_root}/{object_type.msg_name}/{sub_cmd}'


def adm_osc_query_message(object_type: ObjectType, object_number: Union[None, int, float, str], command: str) -> str:

    sub_cmd = f'{object_number}/{command}' if object_number is not None or object_type.name == 'Object' else f'{command}'
    sub_qry = f'/{query_cmd}' if query_cmd != '' else ''
    return f'/{message_root}/{object_type.msg_name}/{sub_cmd}{sub_qry}'


def object_message(object_number: Union[None, int, float, str], command: str) -> str:
    return adm_osc_message(object_type=obj, object_number=object_number, command=command)


def object_query_message(object_number: Union[None, int, float, str], command: str) -> str:
    return adm_osc_query_message(object_type=obj, object_number=object_number, command=command)


def listener_message(object_number: Union[None, int, float, str], command: str) -> str:
    return adm_osc_message(object_type=lis, object_number=object_number, command=command)


def listener_query_message(object_number: Union[None, int, float, str], command: str) -> str:
    return adm_osc_query_message(object_type=lis, object_number=object_number, command=command)


def environment_message(object_number: Union[None, int, float, str], command: str) -> str:
    return adm_osc_message(object_type=env, object_number=object_number, command=command)


def environment_query_message(object_number: Union[None, int, float, str], command: str) -> str:
    return adm_osc_query_message(object_type=env, object_number=object_number, command=command)


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
    Undefined = 0
    Setup = 1
    Position = 2
    Orientation = 3
    Width = 4
    Depth = 5
    Gain = 6
    Change = 7


class Units(SEnum):
    Undefined = 0
    Degrees = 1
    Normalized = 2
    Ratio = 3
    Boolean = 4
    LinearGain = 5
    Meters = 6


class Type(SEnum):
    Int = 1
    Float = 2
    String = 3

    def as_osc_string(self) -> str:
        return str(self)[0].lower()


class ValueType(SEnum):
    Undefined = 0
    Min = 1
    Max = 2
    Default = 3
    Random = 4


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

    def __init__(self, object_type: ObjectType, sub_element: SubElement, attribute: str, osc_command: str,
                 description: str, units: Units = Units.Undefined, type_: Type = Type.Float,
                 min_: Union[int, float, None] = None, max_: Union[int, float, None] = None,
                 def_: Union[int, float, None] = None, status: Status = Status.InProgress, comment: str = '') -> None:

        super().__init__()

        self.object_type: ObjectType = object_type
        self.sub_element: SubElement = sub_element
        self.attribute: str = attribute
        self.osc_command: str = osc_command
        self.description: str = description
        self.units: Units = units
        self.type: Type = type_
        self.min: Union[int, float, None] = min_
        self.max: Union[int, float, None] = max_
        self.default: Union[int, float, None] = def_
        self.status: Status = status
        self.comment: str = comment

        value_catalog[self.attribute] = self

    def __str__(self) -> str:
        return (f'{self.object_type.name} {self.sub_element} {self.attribute}: \n'
                f'\t* description: {self.description}\n'
                f'\t* osc format: {self.osc_format()} : e.g. {self.osc_example()}\n'
                f'\t* unit: {self.units} | type: {self.type} | min: {self.min} | max:{self.max} | default:{self.default}\n'
                f'\t* comment: {self.comment}\n'
                )

    def osc_format(self) -> str:
        cmd = adm_osc_message(object_type=self.object_type, object_number='(k)', command=self.osc_command)
        return f'{cmd} {self.type.as_osc_string()}'

    def osc_example(self, val: Union[int, float, str, None] = None) -> str:
        num = object_test_number
        cmd = adm_osc_message(object_type=self.object_type, object_number=num, command=self.osc_command)
        if val is None:
            val = self.get_random_value()
        return f'{cmd} {val}'

    def get_number_of_values(self) -> int:
        return 1

    def get_parameters(self):
        return [self]

    def get_value_by_type(self, value_type: ValueType) -> Union[int, float, None]:
        if value_type == ValueType.Min:
            return self.get_min_value()
        elif value_type == ValueType.Max:
            return self.get_max_value()
        elif value_type == ValueType.Default:
            return self.get_default_value()
        elif value_type == ValueType.Random:
            return self.get_random_value()
        return None

    def get_min_value(self) -> Union[int, float, None]:
        return self.min

    def get_max_value(self) -> Union[int, float, None]:
        return self.max

    def get_default_value(self) -> Union[int, float, None]:
        return self.default

    def get_random_value(self) -> Union[int, float, None]:
        if self.min is not None and self.max is not None:
            return float(random.randrange(start=int(self.min * 100.0), stop=int(self.max * 100.0))) / 100.0
        if self.type == Type.String:
            def generate_random_word_string(num_words=2, word_list=None):
                if word_list is None:
                    word_list = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon']

                return ' '.join(random.choices(word_list, k=num_words))

            return generate_random_word_string()
        return None

    def get_osc_command(self, object_number: Union[None, int, float, str]) -> str:
        return adm_osc_message(object_type=self.object_type, object_number=object_number, command=self.osc_command)

    def get_osc_query_command(self, object_number: Union[None, int, float, str]) -> str:
        return adm_osc_query_message(object_type=self.object_type, object_number=object_number,
                                     command=self.osc_command)

    def validate_value(self, value: Union[int, float, str]) -> Union[int, float, str]:

        if type(value) is not str:
            if self.get_min_value() is not None and self.get_max_value() is not None:
                return max(min(value, self.get_max_value()), self.get_min_value())
            elif self.get_min_value() is not None:
                return max(value, self.get_min_value())
            elif self.get_max_value() is not None:
                return min(value, self.get_max_value())
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

    def __init__(self, object_type: ObjectType, sub_element: SubElement, attribute: str, osc_command: str,
                 description: str, params: list[Parameter], status: Status, comment: str = '') -> None:

        super().__init__(object_type=object_type, sub_element=sub_element, attribute=attribute, osc_command=osc_command,
                         description=description, status=status, comment=comment)

        self.params = params

    def __str__(self) -> str:
        text = (f'{self.object_type.name} {self.sub_element} {self.attribute}:\n'
                f'\t* description: {self.description}\n'
                f'\t* osc format: {self.osc_format()} : e.g. {self.osc_example()}\n'
                f'\t* comment: {self.comment}\n'
                f'\t* parameters: \n')
        for param in self.params:
            text += f'\t\t- {param.attribute} (unit: {param.units} | type: {param.type} | min: {param.min} | max:{param.max} | default:{param.default})\n'
        return text

    def osc_format(self) -> str:
        cmd = adm_osc_message(object_type=self.object_type, object_number='(k)', command=self.osc_command)
        param_types = ''.join(f'{param.type.as_osc_string()}' for param in self.params)
        return f'{cmd} {param_types}'

    def osc_example(self, values: list[Union[int, float, str, None]] = None) -> str:
        num = object_test_number
        cmd = adm_osc_message(object_type=self.object_type, object_number=num, command=self.osc_command)
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


def find_parameter(address: str) -> Union[Parameter, PackedParameters, None]:
    return next(
        (
            param
            for param in get_all_parameters()
            if param.osc_command == address
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


def dump_stable_protocol() -> str:
    return ''.join(f'{param}\n\n' for param in get_stable_parameters())
