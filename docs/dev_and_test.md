
## Current development & test tools

+ [**Specifications**](https://github.com/immersive-audio-live/ADM-OSC/blob/main/Source/ADM-OSC%20Specification.xlsx)


+ Tester **Desktop application** (Jose Gaudin / Meyer Sound)
  + [download from resources directory](https://github.com/immersive-audio-live/ADM-OSC/tree/main/Resources)
  

+ Validator, Test and Stress Test **Python Module** (Gael Martinet / FLUX:: SE)
  + adm_osc module is available to install through pip : 
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
     # create a test client, assume default address (local: '127.0.0.1')
     # test client can be used to test how receiver will handle all kind of parameters and parameters value range
     sender = TestClient(out_port=9000)
  
     # all stable parameters for a specific object
     sender.set_object_stable_parameters_to_minimum(object_number=1)
     sender.set_object_stable_parameters_to_maximum(object_number=1)
     sender.set_object_stable_parameters_to_default(object_number=1)
     sender.set_object_stable_parameters_to_random(object_number=1)
  
     # all stable parameters for a range of objects
     sender.set_objects_stable_parameters_minimum(objects_range=range(1, 64))
     sender.set_objects_stable_parameters_maximum(objects_range=range(1, 64))
     sender.set_objects_stable_parameters_default(objects_range=range(1, 64))
     sender.set_objects_stable_parameters_random(objects_range=range(1, 64))
  
     # all stable parameters for all objects
     sender.set_all_objects_stable_parameters_minimum()
     sender.set_all_objects_stable_parameters_maximum()
     sender.set_all_objects_stable_parameters_default()
     sender.set_all_objects_stable_parameters_random()
  
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
  + [full documentation](Source/adm_osc/doc/documentation.md).
  + [Source directory](https://github.com/immersive-audio-live/ADM-OSC/tree/main/Source)




