# ADM-OSC Draft v0.5
All messages can be part of a preset. The preset can be enumerated by adding `/preset/n` before any of the messages below.

## Dynamic messages
Dynamic messages, such as object postions, have the potential to change rapidly over the course of a program. They exist in a separate namespace so they can be prioritized for maximum temporal accuracy.

### Dynamic messages for objects &mdash; polar coordinates

<table>
    <thead>
        <tr>
            <th colspan=4>osc address</th>
            <th>type</th>
            <th>units</th>
            <th>min</th>
            <th>max</th>
            <th width="500px">description</th>
            <th width="300px">example</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=8>/adm</td>
            <td rowspan=4>/obj</td>
            <td rowspan=4>/<i>(object number)</i></td>
            <td>/azim</td>
            <td>float</td>
            <td>degrees</td>
            <td>-180.</td>
            <td>180.</td>
            <td><b>azimuth</b> “theta - &#952;” of sound location. -90 is on the Right, 0 is in front.</td>
            <td>/adm/obj/4/azim -22.5</td>
        </tr>
        <tr>
            <td>/elev</td>
            <td>float</td>
            <td>degrees</td>
            <td>-90.</td>
            <td>90.</td>
            <td><b>elevation</b> “phi - &#632;” of sound location</td>
            <td>/adm/obj/4/elev 12.7</td>
        </tr>
        <tr>
            <td>/dist</td>
            <td>float</td>
            <td>normalized</td>
            <td>0.</td>
            <td>1.</td>
            <td><b>distance</b> “r” from origin</td>
            <td>/adm/obj/4/dist 0.9</td>
        </tr>
         <tr>
            <td>/aed</td>
            <td>list</td>
            <td>see above</td>
            <td></td>
            <td></td>
            <td>compact format enables synchronicity of position changes and also less network traffic</td>
            <td>/adm/obj/4/aed -22.5 12.7 0.9</td>
        </tr>
        <tr>
            <td rowspan=2>/prog</td>
            <td rowspan=2>/<i>(program number)</i></td>
            <td>more</td>
            <td>more</td>
            <td>more</td>
            <td>more</td>
        </tr>
        <tr>
            <td>more</td>
        </tr>
    </tbody>
</table>

### Dynamic messages for objects &mdash; cartesian coordinates

<table>
    <thead>
        <tr>
            <th colspan=4>osc address</th>
            <th>type</th>
            <th>units</th>
            <th>min</th>
            <th>max</th>
            <th width="500px">description</th>
            <th width="300px">example</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=8>/adm</td>
            <td rowspan=4>/obj</td>
            <td rowspan=4>/<i>(object number)</i></td>
            <td>/x</td>
            <td>float</td>
            <td>normalized</td>
            <td>-1.</td>
            <td>1.</td>
            <td>left/right dimension. -1 is left</td>
            <td>/adm/obj/4/x -0.9</td>
        </tr>
        <tr>
            <td>/y</td>
            <td>float</td>
            <td>normalized</td>
            <td>-1.</td>
            <td>1.</td>
            <td>front/back dimension</td>
            <td>/adm/obj/4/y 0.15</td>
        </tr>
        <tr>
            <td>/z</td>
            <td>float</td>
            <td>normalized</td>
            <td>-1.</td>
            <td>1.</td>
            <td>top/bottom dimension</td>
            <td>/adm/obj/4/z 0.7</td>
        </tr>
         <tr>
            <td>/xyz</td>
            <td>list</td>
            <td>see above</td>
            <td></td>
            <td></td>
            <td>compact format enables synchronicity of position changes and also less network traffic</td>
            <td>/adm/obj/4/xyz -0.9 0.15 0.7</td>
        </tr>
        <tr>
            <td rowspan=2>/prog</td>
            <td rowspan=2>/<i>(program number)</i></td>
            <td>more</td>
            <td>more</td>
            <td>more</td>
            <td>more</td>
        </tr>
        <tr>
            <td>more</td>
        </tr>
    </tbody>
</table>

## Static messages