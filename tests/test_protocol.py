# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from adm_osc.protocol import *


class TestProtocol(unittest.TestCase):

    def test_object_message(self):
        self.assertEqual(object_message(object_test_number, 'xyz'), '/adm/obj/42/xyz')

    def test_object_query_message(self):

        if query_cmd != '':
            self.assertEqual(object_query_message(object_test_number, 'xyz'), '/adm/obj/42/xyz/get')
        else:
            self.assertEqual(object_query_message(object_test_number, 'xyz'), '/adm/obj/42/xyz')

    def test_Type_OSC_string(self):
        self.assertEqual(Type.Int.as_osc_string(), 'i')
        self.assertEqual(Type.Float.as_osc_string(), 'f')
        self.assertEqual(Type.String.as_osc_string(), 's')

    def test_dump_protocol(self):
        print(f'ADM-OSC PROTOCOL:\n-----------------\n\n{dump_protocol()}')


class TestParameter(unittest.TestCase):

    def test_Parameter(self):
        p = Parameter(object_type=obj, sub_element=SubElement.Position, attribute='test', osc_command='test',
                      description='test desc', units=Units.Normalized, type_=Type.Float, min_=-1.0, max_=1.0,
                      def_=0.0, status=Status.Stable, comment='')

        self.assertEqual(p.sub_element, SubElement.Position)
        self.assertEqual(p.attribute, 'test')
        self.assertEqual(p.osc_command, 'test')
        self.assertEqual(p.description, 'test desc')
        self.assertEqual(p.units, Units.Normalized)
        self.assertEqual(p.type, Type.Float)
        self.assertEqual(p.get_min_value(), -1.0)
        self.assertEqual(p.get_max_value(), 1.0)
        self.assertEqual(p.get_default_value(), 0.0)
        self.assertEqual(p.is_stable(), True)
        self.assertEqual(p.is_in_progress(), False)
        self.assertEqual(p.comment, '')

        self.assertEqual(p.get_osc_command(42), '/adm/obj/42/test')

        if query_cmd != '':
            self.assertEqual(p.get_osc_query_command(42), '/adm/obj/42/test/get')
        else:
            self.assertEqual(p.get_osc_query_command(42), '/adm/obj/42/test')

        self.assertEqual(p.osc_format(), '/adm/obj/(k)/test f')
        self.assertEqual(p.osc_example(0.42), '/adm/obj/42/test 0.42')

        self.assertEqual(p.get_number_of_values(), 1)

        self.assertEqual(p.validate_value(-2.0), -1.0)
        self.assertEqual(p.validate_value(-1.0), -1.0)
        self.assertEqual(p.validate_value(0.0), 0.0)
        self.assertEqual(p.validate_value(1.0), 1.0)
        self.assertEqual(p.validate_value(2.0), 1.0)

    def test_PackedParameters(self):
        p = Parameter(object_type=obj, sub_element=SubElement.Position, attribute='p', osc_command='p', description='p desc', units=Units.Normalized, type_=Type.Float, min_=-1.0, max_=1.0, def_=0.0, status=Status.Stable)
        t = Parameter(object_type=obj, sub_element=SubElement.Position, attribute='t', osc_command='t', description='t desc', units=Units.Normalized, type_=Type.Float, min_=-1.0, max_=1.0, def_=0.0, status=Status.Stable)
        v = Parameter(object_type=obj, sub_element=SubElement.Position, attribute='v', osc_command='v', description='v desc', units=Units.Normalized, type_=Type.Float, min_=-1.0, max_=1.0, def_=0.0, status=Status.Stable)
        ptv = PackedParameters(object_type=obj, sub_element=SubElement.Position, attribute='ptv', osc_command='ptv', description='ptv desc', params=[p, t, v], status=Status.Stable, comment='')

        self.assertEqual(ptv.sub_element, SubElement.Position)
        self.assertEqual(ptv.attribute, 'ptv')
        self.assertEqual(ptv.osc_command, 'ptv')
        self.assertEqual(ptv.description, 'ptv desc')
        self.assertEqual(ptv.is_stable(), True)
        self.assertEqual(ptv.is_in_progress(), False)
        self.assertEqual(ptv.comment, '')

        self.assertEqual(ptv.get_osc_command(42), '/adm/obj/42/ptv')
        if query_cmd != '':
            self.assertEqual(ptv.get_osc_query_command(42), '/adm/obj/42/ptv/get')
        else:
            self.assertEqual(ptv.get_osc_query_command(42), '/adm/obj/42/ptv')

        self.assertEqual(ptv.osc_format(), '/adm/obj/(k)/ptv fff')
        self.assertEqual(ptv.osc_example([0.42, 0.42, 0.42]), '/adm/obj/42/ptv 0.42 0.42 0.42')

        self.assertEqual(ptv.get_number_of_values(), 3)

        self.assertEqual(ptv.validate_value([-2.0, -2.0, -2.0]), [-1.0, -1.0, -1.0])
        self.assertEqual(ptv.validate_value([-1.0, -1.0, -1.0]), [-1.0, -1.0, -1.0])
        self.assertEqual(ptv.validate_value([0.0, 0.0, 0.0]), [0.0, 0.0, 0.0])
        self.assertEqual(ptv.validate_value([1.0, 1.0, 1.0]), [1.0, 1.0, 1.0])
        self.assertEqual(ptv.validate_value([2.0, 2.0, 2.0]), [1.0, 1.0, 1.0])


if __name__ == '__main__':
    unittest.main()
