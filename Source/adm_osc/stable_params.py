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

from .protocol import *

#               _                              _ _   _
#   _ __   ___ | | __ _ _ __   _ __   ___  ___(_) |_(_) ___  _ __
#  | '_ \ / _ \| |/ _` | '__| | '_ \ / _ \/ __| | __| |/ _ \| '_ \
#  | |_) | (_) | | (_| | |    | |_) | (_) \__ \ | |_| | (_) | | | |
#  | .__/ \___/|_|\__,_|_|    | .__/ \___/|___/_|\__|_|\___/|_| |_|
#  |_|                        |_|
a = Parameter(object_type=obj
              , sub_element=SubElement.Position
              , attribute='azimuth'
              , osc_command='azim'
              , description='azimuth “theta” of sound location. -90 is on the Right, 0 is in front.'
              , units=Units.Degrees
              , type_=Type.Float
              , min_=-180.0
              , max_=180.0
              , def_=0.0
              , status=Status.Stable
              , comment='')

e = Parameter(object_type=obj
              , sub_element=SubElement.Position
              , attribute='elevation'
              , osc_command='elev'
              , description='elevation “phi” of sound location'
              , units=Units.Degrees
              , type_=Type.Float
              , min_=-90.0
              , max_=90.0
              , def_=0.0
              , status=Status.Stable
              , comment='')

d = Parameter(object_type=obj
              , sub_element=SubElement.Position
              , attribute='distance'
              , osc_command='dist'
              , description='distance “r” from origin'
              , units=Units.Normalized
              , type_=Type.Float
              , min_=0.0
              , max_=1.0
              , def_=1.0
              , status=Status.Stable
              , comment='In most renderers, the distance parameter has no impact on the object Gain')

aed = PackedParameters(object_type=obj
                       , sub_element=SubElement.Position
                       , attribute='aed'
                       , osc_command='aed'
                       , description='compact command for azimuth, elevation, distance'
                       , params=[a, e, d]
                       , status=Status.Stable
                       , comment='')

#  __        ___     _ _   _
#  \ \      / (_) __| | |_| |__
#   \ \ /\ / /| |/ _` | __| '_ \
#    \ V  V / | | (_| | |_| | | |
#     \_/\_/  |_|\__,_|\__|_| |_|

w = Parameter(object_type=obj
              , sub_element=SubElement.Width
              , attribute='width'
              , osc_command='w'
              , description='object width'
              , units=Units.Normalized
              , type_=Type.Float
              , min_=0.0
              , max_=1.0
              , def_=0.0
              , status=Status.Stable
              , comment='“Width” describes the perceived size of a sound object')

#                  _            _                               _ _   _
#    ___ __ _ _ __| |_ ___  ___(_) __ _ _ __    _ __   ___  ___(_) |_(_) ___  _ __
#   / __/ _` | '__| __/ _ \/ __| |/ _` | '_ \  | '_ \ / _ \/ __| | __| |/ _ \| '_ \
#  | (_| (_| | |  | ||  __/\__ \ | (_| | | | | | |_) | (_) \__ \ | |_| | (_) | | | |
#   \___\__,_|_|   \__\___||___/_|\__,_|_| |_| | .__/ \___/|___/_|\__|_|\___/|_| |_|
#                                              |_|
x = Parameter(object_type=obj
              , sub_element=SubElement.Position
              , attribute='x'
              , osc_command='x'
              , description='left/right dimension'
              , units=Units.Normalized
              , type_=Type.Float
              , min_=-1.0
              , max_=1.0
              , def_=0.0
              , status=Status.Stable
              , comment='The receiver can scale this normalized value into meters')

y = Parameter(object_type=obj
              , sub_element=SubElement.Position
              , attribute='y'
              , osc_command='y'
              , description='back/front dimension'
              , units=Units.Normalized
              , type_=Type.Float
              , min_=-1.0
              , max_=1.0
              , def_=0.0
              , status=Status.Stable
              , comment='The receiver can scale this normalized value into meters')

z = Parameter(object_type=obj
              , sub_element=SubElement.Position
              , attribute='z'
              , osc_command='z'
              , description='bottom/top dimension'
              , units=Units.Normalized
              , type_=Type.Float
              , min_=-1.0
              , max_=1.0
              , def_=0.0
              , status=Status.Stable
              , comment='The receiver can scale this normalized value into meters')

xyz = PackedParameters(object_type=obj
                       , sub_element=SubElement.Position
                       , attribute='xyz'
                       , osc_command='xyz'
                       , description='compact command for x, y and z'
                       , params=[x, y, z]
                       , status=Status.Stable
                       , comment='')

xy = PackedParameters(object_type=obj
                      , sub_element=SubElement.Position
                      , attribute='xy'
                      , osc_command='xy'
                      , description='compact command for x and y'
                      , params=[x, y]
                      , status=Status.Stable
                      , comment='')

#               _
#    __ _  __ _(_)_ __
#   / _` |/ _` | | '_ \
#  | (_| | (_| | | | | |
#   \__, |\__,_|_|_| |_|
#   |___/
gain = Parameter(object_type=obj
                 , sub_element=SubElement.Gain
                 , attribute='gain'
                 , osc_command='gain'
                 , description='Apply a gain to the audio in the object.'
                 , units=Units.LinearGain
                 , type_=Type.Float
                 , min_=0.0
                 , max_=1.0
                 , def_=1.0
                 , status=Status.Stable
                 ,
                 comment='In some Renderers (Spat, L-ISA), the Gain of an object can be optionally computed from the distance parameter.')

dref = Parameter(object_type=obj
                 , sub_element=SubElement.Gain
                 , attribute='dref'
                 , osc_command='dref'
                 , description='distance where start gain attenuation'
                 , units=Units.Normalized
                 , type_=Type.Float
                 , min_=0.0
                 , max_=1.0
                 , def_=1.0
                 , status=Status.Stable
                 , comment='')

dmax = Parameter(object_type=obj
                 , sub_element=SubElement.Gain
                 , attribute='dmax'
                 , osc_command='dmax'
                 , description='distance in meters that correspond to 1.0'
                 , units=Units.Meters
                 , type_=Type.Float
                 , min_=0.0
                 , max_=100.0
                 , def_=1.0
                 , status=Status.Stable
                 , comment='')

mute = Parameter(object_type=obj
                 , sub_element=SubElement.Gain
                 , attribute='mute'
                 , osc_command='mute'
                 , description='1 means “true” so muted'
                 , units=Units.Boolean
                 , type_=Type.Int
                 , min_=0.0
                 , max_=1.0
                 , def_=0.0
                 , status=Status.Stable
                 , comment='')

#            _
#   ___  ___| |_ _   _ _ __
#  / __|/ _ \ __| | | | '_ \
#  \__ \  __/ |_| |_| | |_) |
#  |___/\___|\__|\__,_| .__/
#                     |_|
name = Parameter(object_type=obj
                 , sub_element=SubElement.Setup
                 , attribute='name'
                 , osc_command='name'
                 , description='object nice name'
                 , units=Units.Undefined
                 , type_=Type.String
                 , status=Status.Stable
                 , comment='')

program_change = Parameter(object_type=env
                           , sub_element=SubElement.Change
                           , attribute='change'
                           , osc_command='change'
                           , description='This is a user interaction or show control event that describes a change in the global scene or environment.'
                           , units=Units.Undefined
                           , type_=Type.String
                           , status=Status.Stable
                           , comment='')

#   _ _     _
#  | (_)___| |_ ___ _ __   ___ _ __
#  | | / __| __/ _ \ '_ \ / _ \ '__|
#  | | \__ \ ||  __/ | | |  __/ |
#  |_|_|___/\__\___|_| |_|\___|_|

l_x = Parameter(object_type=lis
                , sub_element=SubElement.Position
                , attribute='x'
                , osc_command='x'
                , description='listener left/right dimension'
                , units=Units.Normalized
                , type_=Type.Float
                , min_=-1.0
                , max_=1.0
                , def_=0.0
                , status=Status.Stable
                , comment='')

l_y = Parameter(object_type=lis
                , sub_element=SubElement.Position
                , attribute='y'
                , osc_command='y'
                , description='listener back/front dimension'
                , units=Units.Normalized
                , type_=Type.Float
                , min_=-1.0
                , max_=1.0
                , def_=0.0
                , status=Status.Stable
                , comment='')

l_z = Parameter(object_type=lis
                , sub_element=SubElement.Position
                , attribute='z'
                , osc_command='z'
                , description='listener bottom/top dimension'
                , units=Units.Normalized
                , type_=Type.Float
                , min_=-1.0
                , max_=1.0
                , def_=0.0
                , status=Status.Stable
                , comment='')

l_yaw = Parameter(object_type=lis
                  , sub_element=SubElement.Orientation
                  , attribute='yaw'
                  , osc_command='yaw'
                  , description='listener yaw'
                  , units=Units.Degrees
                  , type_=Type.Float
                  , min_=-180.0
                  , max_=180.0
                  , def_=0.0
                  , status=Status.Stable
                  , comment='')

l_pitch = Parameter(object_type=lis
                    , sub_element=SubElement.Orientation
                    , attribute='pitch'
                    , osc_command='pitch'
                    , description='listener pitch'
                    , units=Units.Degrees
                    , type_=Type.Float
                    , min_=-180.0
                    , max_=180.0
                    , def_=0.0
                    , status=Status.Stable
                    , comment='')

l_roll = Parameter(object_type=lis
                   , sub_element=SubElement.Orientation
                   , attribute='roll'
                   , osc_command='roll'
                   , description='listener roll'
                   , units=Units.Degrees
                   , type_=Type.Float
                   , min_=-180.0
                   , max_=180.0
                   , def_=0.0
                   , status=Status.Stable
                   , comment='')

lis_xyz = PackedParameters(object_type=lis
                           , sub_element=SubElement.Position
                           , attribute='xyz'
                           , osc_command='xyz'
                           , description='listener compact command for x, y and z'
                           , params=[l_x, l_y, l_z]
                           , status=Status.Stable
                           , comment='')

lis_ypr = PackedParameters(object_type=lis
                           , sub_element=SubElement.Orientation
                           , attribute='ypr'
                           , osc_command='ypr'
                           , description='listener compact command for yaw, pitch and roll'
                           , params=[l_yaw, l_pitch, l_roll]
                           , status=Status.Stable
                           , comment='')
