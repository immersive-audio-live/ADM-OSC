# ADM-OSC

An industry initiative to standardization of Object Based Audio (OBA) positioning data in live production ecosystems, by implementing the Audio Definition Model (ADM) over Open Sound Control (OSC).

[https://immersive-audio-live.github.io/ADM-OSC/](https://immersive-audio-live.github.io/ADM-OSC/)

## Project Originators

[L-Acoustics](https://www.l-acoustics.com/), [FLUX::](https://www.flux.audio/), [Radio-France](https://www.radiofrance.com/innovation-nouveaux-formats)

## Project Contributors

Adamson, d&b audiotechnik, DiGiCo, Dolby, Lawo, Magix, Merging Technologies, Meyer Sound, Steinberg

## Context

Immersive audio is gaining ground in different industries, from music streaming to gaming, from live sound to broadcast. [ADM](https://adm.ebu.io/) or Audio Definition Model, is becoming a popular standard metadata model in some of these industries, with serialADM used in broadcast or ADM bwf or xml files used in the studio.

## Motivation and goals

* To facilitate the sharing of audio objects metadata between a live ecosystem and a broadcast or studio ecosystem.
* To define a basic layer of interoperability between Object Editors and Object renderers while not aiming at replacing more complete manufacturer specific protocols or grammars.
* To define a direct translation of the most relevant ADM Object Properties onto a communication protocol widely used in the live industry, [OSC](https://opensoundcontrol.stanford.edu/index.html).
* Keeping the grammar scope aligned with the ADM properties.
* Share this proposal with the EBU so they can become a relay, publish and support this initiative.
* Extend this small grammar to more ADM properties (beds, etc.) in the future.

## Approach

Bijective mapping of the Object subset of ADM with a standard OSC grammar.

## Why OSC ?

* Lightweight network protocol
* Easy to implement
* Human readable
* Supports wildcards and bundles
* Specification: [Open Sound Control website](http://opensoundcontrol.org/)
* Available in a plethora of professional audio hardware and software devices

## General principles

* Sender (client)
  * Object Editor sending positioning data to one or more receivers.
  * Position data is always normalized
* Receiver (server)
  * Handles the (optional) local scaling of normalized data: x, y, z, distance
  * The receiver can be a DAW, an ADM renderer, an object editor, a bridge (ADM-OSC <-> sADM)
  
## Current status

The current dictionary covers most Object properties from the Audio Definition model.
A more complete dictionary is being discussed to cover the remaining parts of the Audio Definition model.
OSC Live test tool (talker and listener OSC Live test tool) is now available.

## Current Specification

See Repository.

## Current Discussions

See Issues.

## Current development & tests tools

* [**Specification v1.0 and implementation guide**](https://aes2.org/publications/elibrary-page/?id=22722)

* [Chataigne module](https://github.com/madees/ADM-OSC-Chataigne-Module) (Mathieu Delquignies / d&b audiotechnik)
  * to retreive parameters or control ADM-OSC object based audio (OBA) software or hardware with OSC protocol.
  * The same repositories also includes some 3D polar<>cartesian converter javascript functions, and
  * An OSCAR ADM-OSC mapping file for https://forum.ircam.fr/projects/detail/oscar/ VST Plug in.
  
* Tester **Desktop application** (Jose Gaudin / Meyer Sound)
  * [download from resources directory](https://github.com/immersive-audio-live/ADM-OSC/tree/main/Resources)

* Validator, Test and Stress Test **Python Module** (Gael Martinet / FLUX:: SE)
  * adm_osc module is available to install through pip :
  
  ```shell
    pip install adm-osc
    ```

  quick examples:

  ```python
     from adm_osc import OscClientServer
  
     # create a basic client/server that implement basic ADM-OSC communication with stable parameters 
     # + command monitoring and analyze
     cs = OscClientServer(address='127.0.0.1', out_port=9000, in_port=9001)

     # send some individual parameters  
     cs.send_object_position_azimuth(object_number=1, v=-30.0)
     cs.send_object_position_elevation(object_number=1, v=0.0)
     cs.send_object_position_distance(object_number=1, v=2.0)

     # or pack them
     cs.send_object_polar_position(object_number=1, pos=[-30.0, 0.0, 2.0])
  
     # in cartesian coordinates
     cs.send_object_cartesian_position(object_number=1, pos=[-5.0, 8.0, 0.0])
  
     # see documentation for full list of available functions
  
     # when receiving an adm osc command its analyze will be printed on the command output window
     #
     # e.g.
     #
     # >> received valid adm message for obj :: 1 :: gain (0.7943282127380371)
     # >> received valid adm message for obj :: 1 :: position aed (20.33701515197754, 0.0, 0.8807612657546997)
     # >> received valid adm message for obj :: 1 :: position xyz (-0.2606865465641022, 0.8273822069168091, 0.0)
     # >>
     # >> ERROR: unrecognized ADM address : "/adm/obj/1/bril" ! unknown command "/bril/"
     # >> ERROR: arguments are malformed for "/adm/obj/1/gain :: (1.4791083335876465,)":
     # >>     argument 0 "1.4791083335876465" out of range ! it should be less or equal than "1.0"
  
     ```
  
  ```python
     from adm_osc import TestClient
     from adm_osc.protocol import ValueType as vt
     # create a test client, assume default address (local: '127.0.0.1')
     # test client can be used to test how receiver will handle all kind of parameters and parameters value range
     sender = TestClient(out_port=9000)
  
     # all stable parameters for a specific object
     sender.set_object_stable_parameters_predefined_value(object_number=1, vt.Min)
     sender.set_object_stable_parameters_predefined_value(object_number=1, vt.Max)
     sender.set_object_stable_parameters_predefined_value(object_number=1, vt.Default)
     sender.set_object_stable_parameters_predefined_value(object_number=1, vt.Random)
  
     # all stable parameters for a range of objects
     sender.set_objects_stable_parameters_predefined_value(objects_range=range(1, 64), vt.Min)
     sender.set_objects_stable_parameters_predefined_value(objects_range=range(1, 64), vt.Max)
     sender.set_objects_stable_parameters_predefined_value(objects_range=range(1, 64), vt.Default)
     sender.set_objects_stable_parameters_predefined_value(objects_range=range(1, 64), vt.Random)
  
     # all stable parameters for all objects
     sender.set_all_objects_stable_parameters_predefined_value(vt.Min)
     sender.set_all_objects_stable_parameters_predefined_value(vt.Max)
     sender.set_all_objects_stable_parameters_predefined_value(vt.Default)
     sender.set_all_objects_stable_parameters_predefined_value(vt.Random)
  
     # see documentation for full list of available functions
     ```

  ```python
    from adm_osc import StressClient
    # create a stress client, assume default address (local: '127.0.0.1')
    # stress client will send huge amount of data to stress test the receivers
    sender = StressClient(out_port=9000)
    # do stress test in cartesian coordinates
    sender.stress_cartesian_position(number_of_objects=64, duration_in_second=60.0, interval_in_milliseconds=10.0)
    # do stress test in polar coordinates
    sender.stress_polar_position(number_of_objects=64, duration_in_second=60.0, interval_in_milliseconds=10.0)
    ```

  * [full documentation](Source/adm_osc/doc/documentation.md).
  * [Source directory](https://github.com/immersive-audio-live/ADM-OSC/tree/main/Source)

## Currently supported in

SPAT Revolution (FLUX::), L-ISA Controller (L-Acoustics), Ovation (Merging Technologies), Nuendo (Steinberg), SpaceMap Go (Meyer Sound), QLAB 5 (Figure 53), Space Controller (Sound Particles), Modulo Kinetic (Modulo Pi), Iosono (Barco). FletcherMAchine (Adamson), En-Bridge (d&b audiotechnik), Fulcrum One (Fulcrum Acoustic)

