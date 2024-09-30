# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from adm_osc.handler import *
from adm_osc.protocol import *


class TestADMHandler(unittest.TestCase):

    def test_indexes(self):

        self.assertEqual(extract_indexes('*'), 'all')
        self.assertEqual(extract_indexes('42'), 42)
        self.assertEqual(extract_indexes('[12-42]'), {'from': 12, 'to': 42})
        self.assertEqual(extract_indexes('(12-42)'), {'from': 12, 'to': 42})
        self.assertEqual(extract_indexes('{12-42}'), {'from': 12, 'to': 42})
        self.assertEqual(extract_indexes('[1, 3, 5, 7, 9]'), [1, 3, 5, 7, 9])
        self.assertEqual(extract_indexes('(1, 3, 5, 7, 9)'), [1, 3, 5, 7, 9])
        self.assertEqual(extract_indexes('{1, 3, 5, 7, 9}'), [1, 3, 5, 7, 9])

    def test_handler(self):

        try:
            address = '/adm/obj/42/x'
            values = 0.0
            target, objects, parameter, args = adm_handler(address, values)
            self.assertEqual(target, 'obj')
            self.assertEqual(objects, 42)
            self.assertEqual(parameter.attribute, 'x')
            self.assertEqual(len(args), 1)
            self.assertEqual(args[0], 0.0)
        except ValueError as e_:
            print(e_)

        try:
            address = '/adm/obj/[12-42]/xyz'
            values = (1.0, 0.0, -1.0)
            target, objects, parameter, args = adm_handler(address, *values)
            self.assertEqual(target, 'obj')
            self.assertEqual(objects, {'from': 12, 'to': 42})
            self.assertEqual(parameter.attribute, 'xyz')
            self.assertEqual(len(args), 3)
            self.assertEqual(args[0], 1.0)
            self.assertEqual(args[1], 0.0)
            self.assertEqual(args[2], -1.0)
        except ValueError as e_:
            print(e_)

    def test_error_messages(self):

        self.assertEqual(message_root, 'adm')
        self.assertEqual(obj.msg_name, 'obj')
        self.assertEqual(lis.msg_name, 'lis')
        self.assertEqual(env.msg_name, 'env')

        if query_cmd != '':
            self.assertEqual(query_cmd, 'get')

        try:
            adm_handler('/xxx/obj/42/x', 0.0)
        except ValueError as e_:
            self.assertEqual(str(e_), str(ValueError(
                'ERROR: unrecognized ADM address : "/xxx/obj/42/x" it should start with "/adm/"')))
        try:
            adm_handler('/adm/xxx/42/x', 0.0)
        except ValueError as e_:
            self.assertEqual(str(e_), str(ValueError(
                'ERROR: unrecognized ADM address : "/adm/xxx/42/x" ! unknown target "/xxx/"')))
        try:
            adm_handler('/adm/obj/42/xxx', 0.0)
        except ValueError as e_:
            self.assertEqual(str(e_), str(ValueError(
                'ERROR: unrecognized ADM address : "/adm/obj/42/xxx" ! unknown command "/xxx/"')))
        try:
            adm_handler('/adm/obj/42/xyz', 0.0)
        except ValueError as e_:
            self.assertEqual(str(e_), str(ValueError(
                'ERROR: arguments are malformed for "/adm/obj/42/xyz :: (0.0,) ! bad number of arguments ! provided: 1 - Expected: 3')))
        try:
            adm_handler('/adm/obj/42/x', 1)
        except ValueError as e_:
            arg_error = str(e_).split('\n')[1]
            self.assertEqual(arg_error, '\targument 0 "1" type mismatch ! float is expected but "int" is provided')
        Parameter(object_type=obj, sub_element=SubElement.Position, attribute='test_float', osc_command='test_float',
                  description='test_float desc', units=Units.Normalized, type_=Type.Float,
                  min_=-1.0, max_=1.0, def_=0.0, status=Status.Stable, comment='for testing purposes')

        Parameter(object_type=obj, sub_element=SubElement.Position, attribute='test_int', osc_command='test_int',
                  description='test_int desc', units=Units.Normalized, type_=Type.Int,
                  min_=-1, max_=1, def_=0, status=Status.Stable, comment='for testing purposes')

        Parameter(object_type=obj, sub_element=SubElement.Position, attribute='test_str', osc_command='test_str',
                  description='test_str desc', units=Units.Normalized, type_=Type.String,
                  status=Status.Stable, comment='for testing purposes')

        try:
            adm_handler('/adm/obj/42/test_float', 1)
        except ValueError as e_:
            arg_error = str(e_).split('\n')[1][1:]
            self.assertEqual(arg_error, 'argument 0 "1" type mismatch ! float is expected but "int" is provided')
        try:
            adm_handler('/adm/obj/42/test_int', 1.0)
        except ValueError as e_:
            arg_error = str(e_).split('\n')[1][1:]
            self.assertEqual(arg_error, 'argument 0 "1.0" type mismatch ! integer is expected but "float" is provided')
        try:
            adm_handler('/adm/obj/42/test_str', 1.0)
        except ValueError as e_:
            arg_error = str(e_).split('\n')[1][1:]
            self.assertEqual(arg_error, 'argument 0 "1.0" type mismatch ! string is expected but "float" is provided')
        try:
            adm_handler('/adm/obj/42/test_float', (-10))
        except ValueError as e_:
            arg_error = str(e_).split('\n')[1][1:]
            self.assertEqual(arg_error, 'argument 0 "-10" type mismatch ! float is expected but "int" is provided')
        try:
            adm_handler('/adm/obj/42/test_float', 10)
        except ValueError as e_:
            arg_error = str(e_).split('\n')[1][1:]
            self.assertEqual(arg_error, 'argument 0 "10" type mismatch ! float is expected but "int" is provided')


if __name__ == '__main__':
    unittest.main()
