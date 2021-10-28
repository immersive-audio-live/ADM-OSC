# ADM-OSC
An industry initiative to standardization of Object Based Audio (OBA) positioning data in live production ecosystems, by implementing the Audio Definition Model (ADM) over Open Sound Control (OSC).

## Project Originators

[L-Acoustics](https://www.l-acoustics.com/), [FLUX::SE](https://www.flux.audio/), [Radio-France](https://www.radiofrance.com/innovation-nouveaux-formats)

## Project Contributors
d&b Audiotechnik, DiGiCo, Lawo, Magix, Merging Technologies, Meyer Sound, Steinberg.

## Context
Immersive audio is gaining ground in different industries, from music streaming to gaming, from live sound to broadcast. [ADM](https://adm.ebu.io/) or Audio Definition Model, is becoming a popular standard metadata model in some of these industries, with serialADM used in broadcast or ADM xml files used in the studio.

## Motivation and goals
* To facilitate the sharing of audio objects metadata between a live ecosystem and a broadcast or studio ecosystem.
* To define a basic layer of interoperability between Object Editors and Object renderers while not aiming at replacing more complete manufacturer specific protocols or grammars.
* To define a direct translation of the most relevant ADM Object Properties onto a communication protocol widely used in the live industry, [OSC](http://opensoundcontrol.org/introduction-osc).
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
* Sender
  * Object Editor sending positioning data to one or more receivers.
  * Position data is always normalized 
* Receiver
  * Handles the (optional) local scaling of normalized data: x, y, z, distance
  * The receiver can be a DAW, an ADM renderer, an object editor, a bridge (ADM-OSC <-> sADM)
  
## Current status
Initiative presented to the EBU, and currently being implemented by some Broadcast companies as well. 
Some proofs of concept have been implemented by FLUX:: SE in the SPAT Revolution software, in L-Acoustics L-ISA Controller, in Ovation from Merging Technologies and with Nuendo from Steinberg
OSC Live test tool (talker and listener OSC Live test tool) is now available 

## Current Specification
see repository


## Currently supported in:
SPAT Revolution (FLUX::SE), L-ISA Controller (L-Acoustics), Ovation (Merging Technologies), Nuendo (Steinberg).



