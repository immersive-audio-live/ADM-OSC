# ADM-OSC Draft v0.5
All messages can be part of a preset. The preset can be enumerated by adding `/preset/n` before any of the messages below.

## Dynamic messages

<table>
    <thead>
        <tr>
            <th>Address</th>
            <th></th>
            <th></th>
            <th></th>
            <th>type</th>
            <th>units</th>
            <th>min</th>
            <th>max</th>
            <th width="400px">description</th>
            <th width="200px">example</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=810/adm</td>
            <td rowspan=3>/obj</td>
            <td rowspan=3>/(object number)</td>
            <td>/azim</td>
            <td>float</td>
            <td>degrees</td>
            <td>-180.</td>
            <td>180.</td>
            <td>azimuth “theta” of sound location. -90 is on the Right, 0 is in front.</td>
            <td>/adm/obj/4/azim -22.5</td>
        </tr>
        <tr>
            <td>/elev</td>
            <td>float</td>
            <td>degrees</td>
            <td>-90.</td>
            <td>90.</td>
            <td>elevation “phi” of sound location</td>
            <td>/adm/obj/4/elev 12.7</td>
        </tr>
        <tr>
            <td>/dist</td>
            <td>float</td>
            <td>normalized</td>
            <td>0.</td>
            <td>1.</td>
            <td>distance “r” from origin</td>
            <td>/adm/obj/4/dist 0.9</td>
        </tr>
        <tr>
            <td rowspan=2>/prog</td>
            <td rowspan=2>/(program number)</td>
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
