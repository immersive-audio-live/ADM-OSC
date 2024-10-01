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

from . import protocol

__all__ = ['extract_indexes', 'adm_handler']


#   _          _
#  | |__   ___| |_ __   ___ _ __ ___
#  | '_ \ / _ \ | '_ \ / _ \ '__/ __|
#  | | | |  __/ | |_) |  __/ |  \__ \
#  |_| |_|\___|_| .__/ \___|_|  |___/
#               |_|
def extract_indexes(idx: str):
    """
    + "*" means all objects
    + [n-m] means range from "n" to "m"
    + [n, m, o] means specific object defined by n, m and o index ...
    + single int value == single object
    """
    if type(idx) is not str:
        return idx

    if idx == '*':
        return 'all'

    # allow brace and parentheses instead of brackets; just replace them
    idx = idx.replace('{', '[').replace('}', ']')
    idx = idx.replace('(', '[').replace(')', ']')

    if idx.startswith('[') and idx.endswith(']'):
        return _extracted_from_extract_indexes_20(idx)
    else:
        # no range or multiple value found !
        # so, consider single object value and just convert it to int
        return int(idx)


# TODO Rename this here and in `extract_indexes`
def _extracted_from_extract_indexes_20(idx):
    # remove brackets
    indexes = idx[1:-1]

    # if 1 "-" founded it should be a range
    if indexes.count('-') == 1:
        indexes = indexes.split('-')
        if len(indexes) == 2:
            return {'from': int(indexes[0]), 'to': int(indexes[1])}

    # if "," founded, it should be multiple index values
    indexes = indexes.replace('-', ',').replace(' ', '').strip()
    if indexes.startswith(','):
        indexes = indexes[1:]
    if indexes.endswith(','):
        indexes = indexes[:-1]

    indexes = indexes.split(',')
    return [int(i) for i in indexes]


#   _                     _ _
#  | |__   __ _ _ __   __| | | ___ _ __ ___
#  | '_ \ / _` | '_ \ / _` | |/ _ \ '__/ __|
#  | | | | (_| | | | | (_| | |  __/ |  \__ \
#  |_| |_|\__,_|_| |_|\__,_|_|\___|_|  |___/
def adm_handler(address, *args):
    """
    1 - check ADM message header at start of address
    2 - extract target : object | setup ...
    3 - extract object index:
        + single int value == single object
        + "*" means all objects
        + [n-m] means range from "n" to "m"
        + [n, m, o] means specific object defined by n, m and o index ...
    4 - extract and validate command name; It should be in the provided protocol
    5 - extract and validate all arguments. If no arguments are provided, command should be considered as a query value command (GET)
    """
    #
    it = address.split('/')

    # 1
    if it[1] != protocol.message_root:
        raise ValueError(f'ERROR: unrecognized ADM address : "{address}" it should start with "/{protocol.message_root}/"')

    # 2
    target = it[2]
    if target not in [ot.msg_name for ot in protocol.object_type_list]:
        raise ValueError(f'ERROR: unrecognized ADM address : "{address}" ! unknown target "/{target}/"')

    # 3
    objects = None
    if target == 'obj':
        objects = extract_indexes(it[3])
        it.pop(3)
    # 4
    command = it[3]
    parameter = protocol.find_parameter(command)
    if parameter is None:
        raise ValueError(f'ERROR: unrecognized ADM address : "{address}" ! unknown command "/{command}/"')

    # filter touch / release messages for now !!!
    # TODO: check with ADM-OSC group how we want to handle this
    is_touch_release = (
        len(args) == 1
        and type(args[0]) is str
        and args[0] in ['touch', 'release']
    )

    if not is_touch_release:
        number_of_arguments = len(args)
        if number_of_arguments == 0:
            return target, objects, parameter, None

        if number_of_arguments != parameter.get_number_of_values():
            raise ValueError(
                    f'ERROR: arguments are malformed for "{address} :: {args} ! '
                    f'bad number of arguments ! provided: {number_of_arguments} - Expected: {parameter.get_number_of_values()}')

        def _type_to_string(val_) -> str:
            return f'{type(val_)}'.replace("<class '", "").replace("'>", "")

        arguments_errors = []
        parameters = parameter.get_parameters()
        for i, param in enumerate(parameters):
            _min = param.get_min_value()
            _max = param.get_max_value()
            _typ = param.type
            val = args[i]

            # else check all values
            if _typ == protocol.Type.Float and type(val) is not float:
                arguments_errors.append(f'argument {i} "{val}" type mismatch ! float is expected but "{_type_to_string(val)}" is provided')
            elif _typ == protocol.Type.Int and type(val) is not int:
                arguments_errors.append(f'argument {i} "{val}" type mismatch ! integer is expected but "{_type_to_string(val)}" is provided')
            elif _typ == protocol.Type.String and type(val) is not str:
                arguments_errors.append(f'argument {i} "{val}" type mismatch ! string is expected but "{_type_to_string(val)}" is provided')
            elif _min is not None and val < _min:
                arguments_errors.append(f'argument {i} "{val}" out of range ! it should be greater or equal than "{_min}"')
            elif _max is not None and val > _max:
                arguments_errors.append(f'argument {i} "{val}" out of range ! it should be less or equal than "{_max}"')

        if arguments_errors:
            errors = f'ERROR: arguments are malformed for "{address} :: {args}":\n'
            for error in arguments_errors:
                errors += f'\t{error}\n'
            raise ValueError(errors)

    return target, objects, parameter, args
