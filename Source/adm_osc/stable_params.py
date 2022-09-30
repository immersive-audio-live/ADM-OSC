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
a = Parameter(sub_element=SubElement.Position
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

e = Parameter(sub_element=SubElement.Position
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

d = Parameter(sub_element=SubElement.Position
              , attribute='distance'
              , osc_command='dist'
              , description='distance “r” from origin'
              , units=Units.Degrees
              , type_=Type.Float
              , min_=0.0
              , max_=1.0
              , def_=1.0
              , status=Status.Stable
              , comment='In most renderers, the distance parameter has no impact on the object Gain')

aed = PackedParameters(sub_element=SubElement.Position
                       , attribute='aed'
                       , osc_command='aed'
                       , description='compact command for azimuth, elevation, distance'
                       , params=[a, e, d]
                       , status=Status.Stable
                       , comment='')

#                  _            _                               _ _   _
#    ___ __ _ _ __| |_ ___  ___(_) __ _ _ __    _ __   ___  ___(_) |_(_) ___  _ __
#   / __/ _` | '__| __/ _ \/ __| |/ _` | '_ \  | '_ \ / _ \/ __| | __| |/ _ \| '_ \
#  | (_| (_| | |  | ||  __/\__ \ | (_| | | | | | |_) | (_) \__ \ | |_| | (_) | | | |
#   \___\__,_|_|   \__\___||___/_|\__,_|_| |_| | .__/ \___/|___/_|\__|_|\___/|_| |_|
#                                              |_|
x = Parameter(sub_element=SubElement.Position
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

y = Parameter(sub_element=SubElement.Position
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

z = Parameter(sub_element=SubElement.Position
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

xyz = PackedParameters(sub_element=SubElement.Position
                       , attribute='xyz'
                       , osc_command='xyz'
                       , description='compact command for x, y and z'
                       , params=[x, y, z]
                       , status=Status.Stable
                       , comment='')

#               _
#    __ _  __ _(_)_ __
#   / _` |/ _` | | '_ \
#  | (_| | (_| | | | | |
#   \__, |\__,_|_|_| |_|
#   |___/
gain = Parameter(sub_element=SubElement.Gain
                 , attribute='gain'
                 , osc_command='gain'
                 , description='Apply a gain to the audio in the object.'
                 , units=Units.LinearGain
                 , type_=Type.Float
                 , min_=0.0
                 , max_=1.0
                 , def_=1.0
                 , status=Status.Stable
                 , comment='In some Renderers (Spat, L-ISA), the Gain of an object can be optionally computed from the distance parameter.')
