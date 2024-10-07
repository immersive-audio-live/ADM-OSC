# Implementation Matrix

## v1.0

<table>
    <tr>
        <th>&#x2713; = transmit and receive<br>
            tx = transmit only<br>
            rx = receive only</th>
        <th style="writing-mode:vertical-lr;">Spat Revolution (Flux::)</th>
        <th style="writing-mode:vertical-lr;">
            <a href="https://l-isa.l-acoustics.com/">L-ISA Controller (L-Acoustics)</a>
        </th>
        <th style="writing-mode:vertical-lr;">
            <a href="https://l-isa.l-acoustics.com/">mc<sup>2</sup> (Lawo)</a>
        </th>
        <th style="writing-mode:vertical-lr;">
        <a href="https://meyersound.com/product/spacemap-go/">SpaceMap Go (Meyer Sound Laboratories)</a>
        <th style="writing-mode:vertical-lr;">
    </tr>
    <tr>
        <td>/adm/obj/(k)/azim </td>
        <td>&#x2713;</td> <!-- spat -->
        <td>&#x2713;</td> <!-- l-isa -->
        <td>&#x2713;</td> <!-- lawo -->
        <td>rx</td>
    </tr>
    <tr>
        <td>/adm/obj/(k)/elev </td>
        <td>&#x2713;</td> <!-- spat -->
        <td>&#x2713;</td>
        <td>&#x2713;</td>
        <td>rx</td>
    </tr>
    <tr>
        <td>/adm/obj/(k)/dist </td>
        <td>&#x2713;</td> <!-- spat -->
        <td>&#x2713;</td>
        <td>&#x2713;</td>
        <td>rx</td>
    </tr>
    <tr>
        <td>/adm/obj/(k)/aed </td>
        <td>&#x2713;</td> <!-- spat -->
        <td>&#x2713;</td>
        <td>&#x2713;</td>
        <td>rx</td>
    </tr>
    <tr>
        <td>/adm/obj/(k)/x </td>
        <td>&#x2713;</td> <!-- spat -->
        <td>&#x2713;</td>
        <td>&#x2713;</td>
        <td>rx</td>
    </tr>
    <tr>
        <td>/adm/obj/(k)/y </td>
        <td>&#x2713;</td> <!-- spat -->
        <td>&#x2713;</td>
        <td>&#x2713;</td>
        <td>rx</td>
    </tr>
    <tr>
        <td>/adm/obj/(k)/xy </td>
        <td>-</td> <!-- spat -->
        <td>-</td>
        <td>-</td>
        <td>-</td>
    </tr>
    <tr>
        <td>/adm/obj/(k)/z </td>
        <td>&#x2713;</td> <!-- spat -->
        <td>&#x2713;</td>
        <td>&#x2713;</td>
        <td>rx</td>
    </tr>
    <tr>
        <td>/adm/obj/(k)/xyz </td>
        <td>&#x2713;</td> <!-- spat -->
        <td>&#x2713;</td>
        <td>&#x2713;</td>
        <td>rx</td>
    </tr>
    <tr>
        <td>/adm/obj/(k)/w </td>
        <td>&#x2713;</td> <!-- spat -->
        <td>&#x2713;</td>
        <td>&#x2713;</td>
        <td>rx</td>
    </tr>
    <tr>
        <td>/adm/obj/(k)/dref</td>
        <td>-</td>
        <td>-</td>
        <td>rx</td>
    </tr>
    <tr>
        <td>/adm/obj/(k)/dmax</td>
        <td>-</td>
        <td>-</td>
    </tr>
    <tr>
        <td>/adm/obj/(k)/gain</td>
        <td>&#x2713;</td> <!-- spat -->
        <td>&#x2713;</td>
        <td>-</td>
        <td>rx</td>
    </tr>
    <tr>
        <td>/adm/obj/(k)/mute</td>
        <td>&#x2713;</td> <!-- spat -->
        <td>&#x2713;</td>
        <td>&#x2713;</td> <!-- spat -->
        <td>-</td>
        <td>rx</td>
    </tr>
    <tr>
        <td>/adm/obj/(k)/name</td>
        <td>&#x2713;</td>
        <td>-</td>
        <td>rx</td>
    </tr>
    <tr>
        <td>/adm/env/change</td>
        <td>&#x2713;</td>
    </tr>
    <tr>
        <td>/adm/lis/xyz</td>
        <td>rx</td>
    </tr>
    <tr>
        <td>/adm/lis/xyz/ypr</td>
        <td>rx</td>
    </tr>
</table>
