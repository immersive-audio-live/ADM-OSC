# ADM-OSC
### Python module

This module implement ADM-OSC Validator, Test and Stress Test

The module contains:

+ protocol definition and implementation (see [ADM-OSC message specification](https://github.com/immersive-audio-live/ADM-OSC/blob/main/Source/ADM-OSC%20Specification.xlsx))
+ stable parameters (defined in [ADM-OSC message specification](https://github.com/immersive-audio-live/ADM-OSC/blob/main/Source/ADM-OSC%20Specification.xlsx))
+ Client/Server object (Sender/Receiver) which implement command sending and receiving with full analyze/validation
+ TestClient, used to test how receiver will handle all kind of parameters and parameters value range
+ StressClient, used to send huge amount of data to stress test the receivers

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
  
     # see below for full list of available functions
  
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

![myfile](https://github.com/immersive-audio-live/ADM-OSC/tree/main/Source/adm_osc/doc/receiving-command.gif "receiving-command")


  ```python 
     from adm_osc import TestClient
     from adm_osc.protocol import ValueType as vt
     # create a test client, assume default address (local: '127.0.0.1')
     # test client can be used to test how receiver will handle all kind of parameters and parameters value range
     sender = TestClient(out_port=9000)
  
     # all stable parameters for a specific object
     sender.set_object_stable_parameters_predefined_value(object_number=1, value_type=vt.Min)
     sender.set_object_stable_parameters_predefined_value(object_number=1, value_type=vt.Max)
     sender.set_object_stable_parameters_predefined_value(object_number=1, value_type=vt.Default)
     sender.set_object_stable_parameters_predefined_value(object_number=1, value_type=vt.Random)
  
     # all stable parameters for a range of objects
     sender.set_objects_stable_parameters_predefined_value(objects_range=range(1, 64), value_type=vt.Min)
     sender.set_objects_stable_parameters_predefined_value(objects_range=range(1, 64), value_type=vt.Max)
     sender.set_objects_stable_parameters_predefined_value(objects_range=range(1, 64), value_type=vt.Default)
     sender.set_objects_stable_parameters_predefined_value(objects_range=range(1, 64), value_type=vt.Random)
  
     # all stable parameters for all objects
     sender.set_all_objects_stable_parameters_predefined_value(value_type=vt.Min)
     sender.set_all_objects_stable_parameters_predefined_value(value_type=vt.Max)
     sender.set_all_objects_stable_parameters_predefined_value(value_type=vt.Default)
     sender.set_all_objects_stable_parameters_predefined_value(value_type=vt.Random)
  
     # see below for full list of available functions
   ```

![myfile](https://github.com/immersive-audio-live/ADM-OSC/tree/main/Source/adm_osc/doc/testclient.gif "testclient")
    
  ```python 
    from adm_osc import StressClient
    # create a stress client, assume default address (local: '127.0.0.1')
    # stress client will send huge amount of data to stress test the receivers
    sender = StressClient(out_port=9000)
    # do stress test in cartesian coordinates
    sender.stress_cartesian_position(number_of_objects=67, duration_in_second=10.0, interval_in_milliseconds=10.0)
    # do stress test in polar coordinates
    sender.stress_polar_position(number_of_objects=64, duration_in_second=10.0, interval_in_milliseconds=10.0)
   ```

![myfile](https://github.com/immersive-audio-live/ADM-OSC/tree/main/Source/adm_osc/doc/stressclient.gif "stressclient")
