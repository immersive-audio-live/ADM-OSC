All messages can be part of a preset. The preset can be enumerated by adding `/preset/n` before and of the messages below.

| Address      |   |  | type |
| ----------- | ----------- | ----------- | ----------- |
| /obj      | /\<object number\>       | /azim | float
|           |         | 
| /prog | /\<program number\> |

<table>
    <thead>
        <tr>
            <th>Address</th>
            <th></th>
            <th></th>
            <th>type</th>
            <th>units</th>
            <th>description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=4>/adm</td>
            <td rowspan=2>/obj</td>
            <td>/azim</td>
            <td>float</td>
            <td>degrees</td>
            <td>azimuth “theta” of sound location. -90 is on the Right, 0 is in front.</td>
        </tr>
        <tr>
            <td>/elevation</td>
            <td>float</td>
            <td>degrees</td>
            <td>elevation “phi” of sound location</td>
        </tr>
        <tr>
            <td rowspan=2>/prog</td>
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