# ADM-OSC Quick Reference (v1.0)

> **ADM-OSC** is an open industry protocol for real-time Object-Based Audio (OBA) positioning in live and broadcast production, mapping the [Audio Definition Model (ADM)](https://adm.ebu.io/) onto [Open Sound Control (OSC)](https://ccrma.stanford.edu/groups/osc/index.html).
>
> Full specification: <https://immersive-audio-live.github.io/ADM-OSC/>  
> Machine-readable schema: [`adm-osc-schema.json`](adm-osc-schema.json)  
> AES paper: [Implementation of ADM-OSC v1.0](https://aes2.org/publications/elibrary-page/?id=22722)

---

## 1. Protocol Overview

| Property | Value |
|---|---|
| Transport | **UDP** (connectionless) |
| Default send port | **4001** |
| Default receive port (queries/return) | **4002** |
| Encoding | OSC 1.0 |
| Message direction | Typically sender → receiver (unidirectional) |
| Query mechanism | Send message without arguments; receiver replies with current value |

### OSC Type Tags

| Tag | Type | Notes |
|---|---|---|
| `f` | float32 | IEEE 754 single-precision floating point |
| `i` | int32 | 32-bit signed integer |
| `s` | string | Null-terminated, padded to 4-byte boundary |

---

## 2. Address Pattern

All ADM-OSC addresses follow this pattern:

```
/adm/{object_type}/{object_number}/{parameter}
```

- **`/adm`** — root namespace, always present
- **`{object_type}`** — `obj`, `lis`, or `env` (see §3)
- **`{object_number}`** — positive integer starting from **1** (for `obj` only)
- **`{parameter}`** — the specific command (see §4–§6)

> **Wildcards:** OSC wildcards (`*`, `?`) are supported.  
> Example: `/adm/obj/*/gain 1.0` sets gain on **all** objects at once.
>
> **Bundles:** Multiple messages can be grouped in an OSC bundle with a shared timestamp for atomic/synchronous delivery.

---

## 3. Object Types

| Type | Prefix | Description |
|---|---|---|
| `obj` | `/adm/obj/{n}/` | An audio object (source) positioned in 3D space |
| `lis` | `/adm/lis/` | Listener position/orientation (binaural / 6DOF) |
| `env` | `/adm/env/` | Global scene or environment events |

---

## 4. Object Messages — `/adm/obj/{n}/…`

Replace `{n}` with a positive integer (1, 2, 3, …).

### 4.1 Polar Position (spherical coordinates)

| Address | Type | Units | Min | Max | Default | Description |
|---|---|---|---|---|---|---|
| `/adm/obj/{n}/azim` | `f` | degrees | −180.0 | 180.0 | — | **Azimuth**: 0° = front, positive = left, −90° = right |
| `/adm/obj/{n}/elev` | `f` | degrees | −90.0 | 90.0 | — | **Elevation**: 0° = horizontal, +90° = directly above |
| `/adm/obj/{n}/dist` | `f` | normalized | 0.0 | 1.0 | 1.0 | **Distance** from origin; 1.0 = on reference sphere |
| `/adm/obj/{n}/aed` | `f f f` | see above | — | — | — | **Packed**: azimuth, elevation, distance (recommended for atomicity) |

**Examples:**
```
/adm/obj/4/azim -22.5
/adm/obj/4/elev 12.7
/adm/obj/4/dist 0.9
/adm/obj/4/aed -22.5 12.7 0.9
```

### 4.2 Cartesian Position (normalized)

| Address | Type | Units | Min | Max | Default | Description |
|---|---|---|---|---|---|---|
| `/adm/obj/{n}/x` | `f` | normalized | −1.0 | 1.0 | 0.0 | Left/right: −1.0 = full left, +1.0 = full right |
| `/adm/obj/{n}/y` | `f` | normalized | −1.0 | 1.0 | 0.0 | Back/front: −1.0 = full back, +1.0 = full front |
| `/adm/obj/{n}/z` | `f` | normalized | −1.0 | 1.0 | 0.0 | Bottom/top: −1.0 = bottom, +1.0 = top |
| `/adm/obj/{n}/xy` | `f f` | normalized | −1.0 | 1.0 | 0.0 | **Packed**: x, y (horizontal plane only) |
| `/adm/obj/{n}/xyz` | `f f f` | normalized | −1.0 | 1.0 | 0.0 | **Packed**: x, y, z (recommended for atomicity) |

**Cartesian diagram (top view):**
```
          y=1 (front)
            |
 x=-1 ------+------ x=1
(left)      |      (right)
            |
          y=-1 (back)
```

**Examples:**
```
/adm/obj/4/x -0.9
/adm/obj/4/y  0.15
/adm/obj/4/z  0.7
/adm/obj/4/xyz -0.9 0.15 0.7
```

### 4.3 Extent

| Address | Type | Units | Min | Max | Default | Description |
|---|---|---|---|---|---|---|
| `/adm/obj/{n}/w` | `f` | normalized | 0.0 | 1.0 | 0.0 | Horizontal extent (width): 0.0 = point source, 1.0 = maximum spread |

**Example:**
```
/adm/obj/3/w 0.2
```

### 4.4 Gain and Attenuation

| Address | Type | Units | Min | Max | Default | Description |
|---|---|---|---|---|---|---|
| `/adm/obj/{n}/gain` | `f` | linear | 0.0 | *(no max)* | 1.0 | Linear gain. 1.0 = unity (0 dB). Receiver clamps to its capabilities. |
| `/adm/obj/{n}/dref` | `f` | normalized | 0.0 | 1.0 | 1.0 | Reference distance: below this normalized distance, dimensionless rendering applies (no physics-based attenuation). |
| `/adm/obj/{n}/dmax` | `f` | meters | 0.0 | *(no max)* | — | Physical distance (meters) corresponding to normalized value 1.0. Maps ADM `absoluteDistance`. |
| `/adm/obj/{n}/mute` | `i` | boolean | 0 | 1 | 0 | 1 = muted, 0 = active |

> **dB conversion:** `dB = 20 × log10(gain_linear)`  
> Common values: 1.0 = 0 dB, 0.707 ≈ −3 dB, 0.501 ≈ −6 dB, 0.0 = −∞ dB (silence)

**Examples:**
```
/adm/obj/3/gain 0.707
/adm/obj/1/dref 0.2
/adm/obj/1/dmax 21.3
/adm/obj/2/mute 1
```

### 4.5 Metadata

| Address | Type | Units | Min | Max | Default | Description |
|---|---|---|---|---|---|---|
| `/adm/obj/{n}/name` | `s` | string | — | 128 chars | — | Human-readable label for the object |

**Example:**
```
/adm/obj/1/name kickdrum
```

---

## 5. Listener Messages — `/adm/lis/…`

Used for binaural rendering and 6DOF (Six Degrees of Freedom) applications. No object number.

| Address | Type | Units | Min | Max | Default | Description |
|---|---|---|---|---|---|---|
| `/adm/lis/xyz` | `f f f` | normalized | −1.0 | 1.0 | 0.0 | Listener 3D position (x, y, z) |
| `/adm/lis/ypr` | `f f f` | degrees | −180.0 | 180.0 | 0.0 | Listener orientation: yaw, pitch, roll |

**Orientation axes:**
- **Yaw** — rotation around Z (vertical) axis. Positive = left.
- **Pitch** — rotation around X axis. Positive = up.
- **Roll** — rotation around Y axis. Positive = tilt right.

**Examples:**
```
/adm/lis/xyz 0.0 0.5 -0.2
/adm/lis/ypr -45.0 30.0 5.0
```

---

## 6. Environment Messages — `/adm/env/…`

Global messages not tied to a specific object.

| Address | Type | Units | Min | Max | Default | Description |
|---|---|---|---|---|---|---|
| `/adm/env/change` | `s` | string | — | 128 chars | — | Scene / program change event |

**Example:**
```
/adm/env/change verse
```

---

## 7. Queries (Bi-directional Communication)

To **GET** the current value of any parameter, send the OSC address without arguments.  
The receiver replies to the sender's IP on port 4002 with the current value.

```
→ send:   /adm/obj/4/xyz            (no arguments)
← reply:  /adm/obj/4/xyz -0.9 0.15 0.0
```

Any message listed above can be queried this way.

---

## 8. Coordinate System Conversions

### Polar → Cartesian

```
x = -d · sin(π/2 - e·2π/360) · sin(a·2π/360)
y =  d · sin(π/2 - e·2π/360) · cos(a·2π/360)
z =  d · cos(π/2 - e·2π/360)
```

### Cartesian → Polar

```
a = (360/(2π)) · atan2(x, y)
e = (360/(2π)) · asin(z / d)
d = sqrt(x² + y² + z²)
```

Reference: ITU-R BS.2127 §6.8.  
Code examples: [C++](https://github.com/ChristianAhrens/RemoteProtocolBridgeCore/blob/master/Source/ProcessingEngine/ProtocolProcessor/OSCProtocolProcessor/ADMOSCProtocolProcessor.cpp) · [Swift](https://github.com/Daniel-Higgott/ADMCoordinateConversion) · [JavaScript](https://github.com/madees/ADM-OSC-Chataigne-Module)

---

## 9. Implementation Checklist

### Minimum Viable Sender
- [ ] Send UDP packets to port **4001**
- [ ] Implement `/adm/obj/{n}/xyz` (Cartesian) **or** `/adm/obj/{n}/aed` (polar)
- [ ] Use object numbers starting at **1**
- [ ] Use packed messages (`xyz` / `aed`) for atomic position updates

### Minimum Viable Receiver
- [ ] Listen for UDP on port **4001**
- [ ] Parse `/adm/obj/{n}/xyz` and/or `/adm/obj/{n}/aed`
- [ ] Parse `/adm/obj/{n}/gain`
- [ ] Clamp out-of-range values to valid range (do not error)
- [ ] Reply to queries (messages with no arguments) on port **4002**

### Recommended Additions
- [ ] Support all polar parameters: `azim`, `elev`, `dist`
- [ ] Support all Cartesian parameters: `x`, `y`, `z`, `xy`
- [ ] Support `w` (object width)
- [ ] Support `mute` and `name`
- [ ] Support `/adm/env/change`
- [ ] Support OSC wildcards (`/adm/obj/*/…`)
- [ ] Support `/adm/lis/xyz` and `/adm/lis/ypr` for 6DOF

---

## 10. Complete Message Summary

| Address | Type | Description |
|---|---|---|
| `/adm/obj/{n}/azim` | `f` | Polar azimuth, degrees, −180 to 180 |
| `/adm/obj/{n}/elev` | `f` | Polar elevation, degrees, −90 to 90 |
| `/adm/obj/{n}/dist` | `f` | Polar distance, normalized 0–1 |
| `/adm/obj/{n}/aed` | `f f f` | Packed polar: azim, elev, dist |
| `/adm/obj/{n}/x` | `f` | Cartesian X (L/R), normalized −1 to 1 |
| `/adm/obj/{n}/y` | `f` | Cartesian Y (B/F), normalized −1 to 1 |
| `/adm/obj/{n}/z` | `f` | Cartesian Z (B/T), normalized −1 to 1 |
| `/adm/obj/{n}/xy` | `f f` | Packed Cartesian: x, y |
| `/adm/obj/{n}/xyz` | `f f f` | Packed Cartesian: x, y, z |
| `/adm/obj/{n}/w` | `f` | Width/extent, normalized 0–1 |
| `/adm/obj/{n}/gain` | `f` | Linear gain, 0 to ∞, default 1.0 |
| `/adm/obj/{n}/dref` | `f` | Reference distance, normalized 0–1, default 1.0 |
| `/adm/obj/{n}/dmax` | `f` | Max distance in meters |
| `/adm/obj/{n}/mute` | `i` | Mute: 0=off, 1=on |
| `/adm/obj/{n}/name` | `s` | Object label, max 128 chars |
| `/adm/lis/xyz` | `f f f` | Listener position: x, y, z |
| `/adm/lis/ypr` | `f f f` | Listener orientation: yaw, pitch, roll |
| `/adm/env/change` | `s` | Scene/program change label |

---

## 11. Code Examples

### Python (using `adm-osc` module)

```python
pip install adm-osc
```

```python
from adm_osc import OscClientServer

# Create client/server with monitoring
cs = OscClientServer(address='127.0.0.1', out_port=4001, in_port=4002)

# Send individual polar parameters
cs.send_object_position_azimuth(object_number=1, v=-30.0)
cs.send_object_position_elevation(object_number=1, v=0.0)
cs.send_object_position_distance(object_number=1, v=0.8)

# Send packed polar position (atomic update)
cs.send_object_polar_position(object_number=1, pos=[-30.0, 0.0, 0.8])

# Send packed Cartesian position (atomic update)
cs.send_object_cartesian_position(object_number=1, pos=[-0.5, 0.8, 0.0])
```

### Raw OSC (pseudocode)

```
# Set object 1 front-left at ground level
send_osc("/adm/obj/1/xyz", [-0.5, 0.8, 0.0])   # Cartesian

# Set object 2 overhead right
send_osc("/adm/obj/2/aed", [-45.0, 45.0, 0.9])  # Polar

# Fade out object 3
send_osc("/adm/obj/3/gain", [0.0])

# Mute object 4
send_osc("/adm/obj/4/mute", [1])

# Set all objects to unity gain
send_osc("/adm/obj/*/gain", [1.0])

# Query object 1 position (receiver replies)
send_osc("/adm/obj/1/xyz", [])
```

---

## 12. Resources

| Resource | Link |
|---|---|
| Specification website | <https://immersive-audio-live.github.io/ADM-OSC/> |
| GitHub repository | <https://github.com/immersive-audio-live/ADM-OSC> |
| Machine-readable schema | [`docs/adm-osc-schema.json`](adm-osc-schema.json) |
| Python module (`adm-osc`) | `pip install adm-osc` |
| AES paper (v1.0) | <https://aes2.org/publications/elibrary-page/?id=22722> |
| Chataigne module | <https://github.com/madees/ADM-OSC-Chataigne-Module> |
| Desktop test tool | [Resources directory](https://github.com/immersive-audio-live/ADM-OSC/tree/main/Resources) |
