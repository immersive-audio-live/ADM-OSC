# ADM-OSC principals

### Sender (client)

- Object Editor sending positioning data to one or more receivers.
- Position data is always normalized

### Receiver (server)

- Handles the (optional) local scaling of normalized data: x, y, z, distance
- The receiver can be a DAW, an ADM renderer, an object editor, a bridge (ADM-OSC <-> sADM)

## Relationship to ADM

ADM-OSC messages are designed to be translatable to (S-)ADM if needed. Messages that don't translate into one (or more) ADM tag should not be in the `/adm` namespace.

## Coordinates

For Cartesian coordinates, values are normalized between -1 and 1. $x = 1$ is right, $y = 1$ is forward, $z = 1$ is up.

    (-1, 1) --------- (1, 1)  
       |                |  
       |                |  
       |                |  
       |                |  
    (-1, -1) ---------(1, -1)  

For polar coordinates, 0&deg; azimuth is straight ahead. Positive azimuth is on the left, so a front-left speaker is +30&deg;. +90&deg; elevation is straight up.

### pol <--> car

The ADM relationship between polar and Cartesian coordinates is specified in [section 10.1 of this document](https://www.itu.int/dms_pubrec/itu-r/rec/bs/R-REC-BS.2127-0-201906-I!!PDF-E.pdf). This has [some limitations](https://github.com/immersive-audio-live/ADM-OSC/issues/25) and could be extended to include more AR, VR, and game engine use cases.
