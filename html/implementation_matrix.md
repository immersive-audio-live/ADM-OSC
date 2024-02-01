# ADM-OSC Implementations

## Matrix?

<table>
    <tr>
        <th style="writing-mode:vertical-lr;"></th>
        <th style="writing-mode:vertical-lr;">SPAT Revolution (FLUX::SE)</th>
        <th style="writing-mode:vertical-lr;">L-ISA Controller (L-Acoustics)</th>
        <th style="writing-mode:vertical-lr;">Implementation 3</th>
        <th style="writing-mode:vertical-lr;">Implementation 4</th>
  </tr>
  <tr>
    <td>/adm/obj/(k)/azim </td>
    <td>tx</td>
    <td></td>
    <td></td>
    <td>&#x2713;</td>
  </tr>
  <tr>
   <td>/adm/obj/(k)/elev</td>
    <td></td>
    <td>rx</td>
    <td></td>
    <td>&#x2713;</td>
  </tr>
  <tr>
    <td>/adm/obj/(k)/x</td>
    <td>&#x2713;</td>
    <td>&#x2713;</td>
    <td></td>
    <td>&#x2713;</td>
  </tr>
  <tr>
   <td>/adm/obj/(k)/y</td>
    <td>&#x2713;</td>
    <td>&#x2713;</td>
    <td></td>
    <td>&#x2713;</td>
  </tr>
</table>

- Tx = transmit only
- Rx = receive only
- &#x2713; = transmit and receive

## or...

## SPAT Revolution (FLUX::SE)

|  message | rx | tx  | notes  |
|---|---|---|---|
| /adm/obj/(k)/azim | | |   |
| /adm/obj/(k)/elev | | |   |
| /adm/obj/(k)/dist | | |   |
| /adm/obj/(k)/aed  | | |   |
| /adm/obj/(k)/gain | | | |
| /adm/obj/(k)/x    | | |  |
| /adm/obj/(k)/y    | | |  |
| /adm/obj/(k)/z    | | |  |
| /adm/obj/(k)/xyz  | | |  |
| /adm/obj/(k)/config/cartesian | | | |

## [L-ISA Controller (L-Acoustics)](https://www.l-acoustics.com/products/l-isa-studio/)

|  message | rx | tx  | notes  |
|---|---|---|---|
| /adm/obj/(k)/azim | &#x2713; | &#x2713;  |   |
| /adm/obj/(k)/elev | &#x2713; | &#x2713;  |   |
| /adm/obj/(k)/dist | &#x2713; | &#x2713; |   |
| /adm/obj/(k)/aed  | &#x2713;  |   |   |
| /adm/obj/(k)/gain |  | &#x2713; | |
| /adm/obj/(k)/w    | &#x2713;  |   |  _not in spec_ |
| /adm/obj/(k)/s    | &#x2713; | &#x2713; | _not in spec_ |
| /adm/obj/(k)/x    | &#x2713; | &#x2713; |  |
| /adm/obj/(k)/y    | &#x2713; | &#x2713; |  |
| /adm/obj/(k)/z    | &#x2713; | &#x2713; |  |
| /adm/obj/(k)/xyz  | &#x2713; | &#x2713; |  |
| /adm/obj/(k)/config/cartesian | | | |

## Next implementation

|  message | rx | tx  | notes  |
|---|---|---|---|
| /adm/obj/(k)/azim | | |   |
| /adm/obj/(k)/elev | | |   |
| /adm/obj/(k)/dist | | |   |
| /adm/obj/(k)/aed  | | |   |
| /adm/obj/(k)/gain | | | |
| /adm/obj/(k)/x    | | |  |
| /adm/obj/(k)/y    | | |  |
| /adm/obj/(k)/z    | | |  |
| /adm/obj/(k)/xyz  | | |  |
| /adm/obj/(k)/config/cartesian | | | |

