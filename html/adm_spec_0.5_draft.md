# ADM-OSC Draft v0.5

All messages can be part of a preset. The preset can be enumerated by adding <code>/preset/n</code>
                before any of the messages below.</p>

            <hr>
            <h2>Object messages</h2>

            <h3>dynamic</h3>

            <table>
                <thead>
                    <tr>
                        <th colspan=2>osc address</th>
                        <th>type</th>
                        <th>units</th>
                        <th>min</th>
                        <th>max</th>
                        <th style="width:100px">default</th>
                        <th style="width:500px">description</th>
                        <th style="width:300px">example</th>
                        <th style="width:300px">status</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td rowspan=11>/adm/obj/<i>n</i></td>
                        <td>/azim</td>
                        <td>float</td>
                        <td>degrees</td>
                        <td>-180.</td>
                        <td>180.</td>
                        <td>-</td>
                        <td><b>azimuth</b> “theta - &#952;” of sound location. -90 is on the Right, 0 is in front.</td>
                        <td>/adm/obj/4/azim -22.5</td>
                        <td bgcolor="LightGreen">stable v0.4</td>
                    </tr>
                    <tr>
                        <td>/elev</td>
                        <td>float</td>
                        <td>degrees</td>
                        <td>-90.</td>
                        <td>90.</td>
                        <td>-</td>
                        <td><b>elevation</b> “phi - &#632;” of sound location</td>
                        <td>/adm/obj/4/elev 12.7</td>
                        <td bgcolor="LightGreen">stable v0.4</td>
                    </tr>
                    <tr>
                        <td>/dist</td>
                        <td>float</td>
                        <td>normalized</td>
                        <td>0.0</td>
                        <td>1.0</td>
                        <td>1.0</td>
                        <td><b>distance</b> “r” from origin</td>
                        <td>/adm/obj/4/dist 0.9</td>
                        <td bgcolor="LightGreen">stable v0.4</td>
                    </tr>
                    <tr>
                        <td>/aed</td>
                        <td>list</td>
                        <td colspan=4>see above</td>
                        <td>compact format enables synchronicity of position changes and also less network traffic</td>
                        <td>/adm/obj/4/aed -22.5 12.7 0.9</td>
                        <td bgcolor="LightGreen">stable v0.4</td>
                    </tr>
                    <tr>
                        <td>/widthDeg</td>
                        <td>float</td>
                        <td>degrees</td>
                        <td>0.0</td>
                        <td>180.0</td>
                        <td>0.0</td>
                        <td>horizontal extent in degrees. See also /w</td>
                        <td>/adm/obj/3/widthDeg 45.2</td>
                        <td bgcolor="Pink"><a href="https://github.com/immersive-audio-live/ADM-OSC/issues/1">in
                                progress</a></td>
                    </tr>
                    <tr>
                        <td>/x</td>
                        <td>float</td>
                        <td>normalized</td>
                        <td>-1.0</td>
                        <td>1.0</td>
                        <td>0.0</td>
                        <td>left/right dimension. -1 is left</td>
                        <td>/adm/obj/4/x -0.9</td>
                        <td bgcolor="LightGreen">stable v0.4</td>
                    </tr>
                    <tr>
                        <td>/y</td>
                        <td>float</td>
                        <td>normalized</td>
                        <td>-1.0</td>
                        <td>1.0</td>
                        <td>0.0</td>
                        <td>front/back dimension</td>
                        <td>/adm/obj/4/y 0.15</td>
                        <td bgcolor="LightGreen">stable v0.4</td>
                    </tr>
                    <tr>
                        <td>/z</td>
                        <td>float</td>
                        <td>normalized</td>
                        <td>-1.0</td>
                        <td>1.0</td>
                        <td>0.0</td>
                        <td>top/bottom dimension</td>
                        <td>/adm/obj/4/z 0.7</td>
                        <td bgcolor="LightGreen">stable v0.4</td>
                    </tr>
                    <tr>
                        <td>/xyz</td>
                        <td>list</td>
                        <td colspan=4>see above</td>
                        <td>compact format enables synchronicity of position changes and also less network traffic</td>
                        <td>/adm/obj/4/xyz -0.9 0.15 0.7</td>
                        <td bgcolor="LightGreen">stable v0.4</td>
                    </tr>
                    </tr>
                    <tr>
                        <td>/w</td>
                        <td>float</td>
                        <td>normalized</td>
                        <td>0.0</td>
                        <td>1.0</td>
                        <td>0.0</td>
                        <td>horizontal extent in normalized units</td>
                        <td>/adm/obj/3/w 0.2</td>
                        <td bgcolor="Pink"><a href="https://github.com/immersive-audio-live/ADM-OSC/issues/1">in
                                progress</a></td>
                    </tr>
                    <tr>
                        <td>/gain</td>
                        <td>float</td>
                        <td>linear</td>
                        <td>0.</td>
                        <td></td>
                        <td>1.0</td>
                        <td>Apply a gain to the audio in the object.</td>
                        <td>/adm/obj/3/gain 0.707</td>
                        <td bgcolor="LightGreen">stable v0.4</td>
                    </tr>
                </tbody>
            </table>

            <h3>static</h3>
            <table>
                <thead>
                    <tr>
                        <th colspan=2>osc address</th>
                        <th>type</th>
                        <th>units</th>
                        <th style="width:100px">default</th>
                        <th style="width:500px">description</th>
                        <th style="width:300px">example</th>
                        <th style="width:300px">status</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td rowspan=10>/adm/config/obj/<i>n</i></td>
                        <td>/chan</td>
                        <td>int</td>
                        <td></td>
                        <td>1</td>
                        <td><b>ADM:</b>ADM mapped to the wavefile chna data chunk. <b>S-ADM:</b> mapped to the listed
                            elements and attributes.</td>
                        <td>/adm/obj/4/azim -22.5</td>
                        <td bgcolor="LightYellow"><b>proposed v0.5</b></td>
                    </tr>
                    <tr>
                        <td>/cartesian</td>
                        <td>int</td>
                        <td>0/1</td>
                        <td>0</td>
                        <td>If the flag is set to 1, Cartesian coordinates are used. Otherwise spherical coordinates are
                            used.</td>
                        <td>/adm/config/obj/1/cartesian 0</td>
                        <td bgcolor="LightGreen">stable v0.4</td>
                    </tr>
                    <tr>
                        <td>/name</td>
                        <td>symbol</td>
                        <td></td>
                        <td>'Content_n'</td>
                        <td>audioContentName, where ‘n’ is the object index value</td>
                        <td></td>
                        <td bgcolor="LightYellow"><b>proposed v0.5</b></td>
                    </tr>
                    <tr>
                        <td>/lang</td>
                        <td>symbol</td>
                        <td>ISO 639-1?</td>
                        <td></td>
                        <td>Used for local language labeling</td>
                        <td>/adm/config/obj/3/lang FR</td>
                        <td bgcolor="LightYellow"><b>proposed v0.5</b></td>
                    </tr>
                    <tr>
                        <td>/type</td>
                        <td>symbol</td>
                        <td></td>
                        <td>'O'</td>
                        <td>dialog content kind</td>
                        <td>/adm/config/obj/3/type AO</td>
                        <td bgcolor="LightYellow"><b>proposed v0.5</b></td>
                    </tr>
                    <tr>
                        <td>/gain</td>
                        <td>float</td>
                        <td>dB</td>
                        <td>0.0</td>
                        <td>Depending upon the template being used, gain is mapped to either an individual audio channel
                            or a higher-level object (which could reference a number of audio channels)</td>
                        <td>/adm/config/obj/3/gain -6.0</td>
                        <td bgcolor="LightYellow"><b>proposed v0.5</b></td>
                    </tr>
                    <tr>
                        <td>/absdistance</td>
                        <td>float</td>
                        <td>meters</td>
                        <td></td>
                        <td>Distance signified by a normalized value of 1</td>
                        <td>/adm/config/obj/1/absdistance 21.3</td>
                        <td bgcolor="LightYellow"><b>proposed v0.5</b></td>
                    </tr>
                    <tr>
                        <td>/refdistance</td>
                        <td>float</td>
                        <td>normalized</td>
                        <td>1.0</td>
                        <td>Distance where dimensionless rendering is replaced with with physics-based rendering.</td>
                        <td>/adm/config/obj/1/refdistance 0.2</td>
                        <td bgcolor="LightYellow"><b>proposed v0.5</b></td>
                    </tr>
                </tbody>
            </table>

            <h3>Object type to ADM dialogue content</h3>
            <table>
                <thead>
                    <tr>
                        <th>type</th>
                        <th>dialogue</th>
                        <th>attribute</th>
                        <th>attribute value</th>
                        <th>notes</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>O</td>
                        <td>2</td>
                        <td>nonDialogueContentKind</td>
                        <td>0</td>
                        <td>Undefined</td>
                    </tr>
                    <tr>
                        <td>D</td>
                        <td>1</td>
                        <td>dialogueContentKind</td>
                        <td>1</td>
                        <td>Dialogue</td>
                    </tr>
                    <tr>
                        <td>AD</td>
                        <td>1</td>
                        <td>dialogueContentKind</td>
                        <td>4</td>
                        <td>Audio description</td>
                    </tr>
                    <tr>
                        <td>SS</td>
                        <td>1</td>
                        <td>dialogueContentKind</td>
                        <td>3</td>
                        <td>SpokenSubtitle</td>
                    </tr>
                    <tr>
                        <td>VO</td>
                        <td>1</td>
                        <td>dialogueContentKind</td>
                        <td>2</td>
                        <td>Voiceover</td>
                    </tr>
                </tbody>
            </table>


            <h3>virtualization</h3>
            <table>
                <thead>
                    <tr>
                        <th colspan=2>osc address</th>
                        <th>type</th>
                        <th>units</th>
                        <th>min</th>
                        <th>max</th>
                        <th style="width:100px">default</th>
                        <th style="width:500px">description</th>
                        <th style="width:300px">example</th>
                        <th style="width:300px">status</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td rowspan=3>/adm/config/obj/<i>n</i>/virt</td>
                        <td>/bypass</td>
                        <td>int</td>
                        <td>true/false</td>
                        <td>0</td>
                        <td>1</td>
                        <td>1</td>
                        <td>Specifies whether the object should be virtualised using a headphone virtualiser or not
                            (1=render to stereo, 0=render with headphone virtualiser)</td>
                        <td></td>
                        <td bgcolor="LightYellow"><b>proposed v0.5</b></td>
                    </tr>
                    <tr>
                        <td>/drr</td>
                        <td>float</td>
                        <td>decibels</td>
                        <td>-130.0</td>
                        <td>130.0</td>
                        <td>130.0</td>
                        <td>Direct to Reverberant Ratio in dB.</td>
                        <td></td>
                        <td bgcolor="LightYellow"><b>proposed v0.5</b></td>
                    </tr>
                    <tr>
                        <td>/hlock</td>
                        <td>int</td>
                        <td>true/false</td>
                        <td>0</td>
                        <td>1</td>
                        <td>1.0</td>
                        <td>Indicates if the perceived
                            location of the audio
                            element is locked to the
                            head (1) or not (0)</td>
                        <td></td>
                        <td bgcolor="LightYellow"><b>proposed v0.5</b></td>
                    </tr>
                </tbody>
            </table>
            <br>

            <hr>
            <h2>Bed messages (static)</h2>

            <table>
                <thead>
                    <tr>
                        <th colspan=2>osc address</th>
                        <th>type</th>
                        <th>units</th>
                        <th>min</th>
                        <th>max</th>
                        <th style="width:100px">default</th>
                        <th style="width:500px">description</th>
                        <th style="width:300px">example</th>
                        <th style="width:300px">status</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td rowspan=4>/adm/config/bed/<i>n</i></td>
                        <td>/chan</td>
                        <td>int</td>
                        <td></td>
                        <td>1</td>
                        <td></td>
                        <td>1</td>
                        <td>Start channel of bed</td>
                        <td>/adm/config/bed/1/chan 1</td>
                        <td bgcolor="LightYellow"><b>proposed v0.5</b></td>
                    </tr>
                    <tr>
                        <td>/name</td>
                        <td>symbol</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td>'Bed_n'</td>
                        <td>Where ‘n’ is the bed index value</td>
                        <td>/adm/prog/2/bed/1/name "name"</td>
                        <td bgcolor="LightYellow"><b>proposed v0.5</b></td>
                    </tr>
                    <td>/layout</td>
                    <td>int</td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td>3</td>
                    <td>Value corresponds to the lower 8 bits of a common definition audioPackFormat.</td>
                    <td>/adm/prog/2/bed/1/layout</td>
                    <td bgcolor="LightYellow"><b>proposed v0.5</b></td>
                    </tr>
                    <td>/gain</td>
                    <td>float</td>
                    <td>dB</td>
                    <td></td>
                    <td></td>
                    <td>0.0</td>
                    <td></td>
                    <td>/adm/config/bed/1/gain -3.2</td>
                    <td bgcolor="LightYellow"><b>proposed v0.5</b></td>
                    </tr>
                </tbody>
            </table>

            <h3>Bed layout values</h3>
            <table>
                <thead>
                    <tr>
                        <th>audioPackFormat</th>
                        <th>value</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>2.0</td>
                        <td>2</td>
                    </tr>
                    <tr>
                        <td>3.0</td>
                        <td>10</td>
                    </tr>
                    <tr>
                        <td>5.0</td>
                        <td>12</td>
                    </tr>
                    <tr>
                        <td>5.1</td>
                        <td>3</td>
                    </tr>
                    <tr>
                        <td>5.1.2</td>
                        <td>19</td>
                    </tr>
                    <tr>
                        <td>5.1.4</td>
                        <td>5</td>
                    </tr>
                    <tr>
                        <td>7.1.4</td>
                        <td>23</td>
                    </tr>
                </tbody>
            </table>
            <br>
            <hr>
            <h2>Template messages (static)</h2>

            <table>
                <thead>
                    <tr>
                        <th colspan=2>osc address</th>
                        <th>type</th>
                        <th>units</th>
                        <th width="500px">description</th>
                        <th width="300px">example</th>
                        <th>status</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td rowspan=3>/adm/config/template</td>
                        <td>/name</td>
                        <td>symbol</td>
                        <td></td>
                        <td rowspan="3">The template applies to all metadata compositions in the current preset path
                        </td>
                        <td>/adm/prog/2/template/name "English AD"</td>
                        <td bgcolor="LightYellow"><b>proposed v0.5</b></td>
                    </tr>
                    <tr>
                        <td>/version</td>
                        <td>symbol</td>
                        <td>x.x.x</td>
                        <td>/adm/prog/2/template/version 3.2.1</td>
                        <td bgcolor="LightYellow"><b>proposed v0.5</b></td>
                    </tr>
                    <td>/level</td>
                    <td>int</td>
                    <td></td>
                    <td>/adm/prog/2/template/format 23</td>
                    <td bgcolor="LightYellow"><b>proposed v0.5</b></td>
                    </tr>
                    <tr>
                </tbody>
            </table>

            <h2>General and Programme <code>/config</code></h2>
            <table>
                <thead>
                    <tr>
                        <th colspan=3>osc address</th>
                        <th>type</th>
                        <th>units</th>
                        <th>default</th>
                        <th width="500px">description</th>
                        <th width="300px">example</th>
                        <th>status</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td rowspan=3>/adm/config/template</td>
                        <td colspan=2>/version</td>
                        <td>symbol</td>
                        <td>x.x.x</td>
                        <td></td>
                        <td>The specification version that the ADM-OSC is compliant with</td>
                        <td>/adm/config/version 0.5.0</td>
                        <td bgcolor="LightYellow"><b>proposed v0.5</b></td>
                    </tr>
                    <tr>
                        <td colspan=2>/dprst</td>
                        <td>int</td>
                        <td></td>
                        <td>1</td>
                        <td>Shorthand mode specifies base preset</td>
                        <td>/adm/config/dprst 1</td>
                        <td bgcolor="LightYellow"><b>proposed v0.5</b></td>
                    </tr>
                    <tr>
                        <td colspan=2>/dprog</td>
                        <td>int</td>
                        <td></td>
                        <td>1</td>
                        <td>Shorthand mode specifies base programme</td>
                        <td>/adm/config/dprog 1</td>
                        <td bgcolor="LightYellow"><b>proposed v0.5</b></td>
                    </tr>
                    <tr>
                        <td rowspan=4>/adm/prog/<i>n</i>/config</td>
                        <td colspan=2>/name</td>
                        <td>symbol</td>
                        <td></td>
                        <td>'Programme_n'</td>
                        <td>Where n is the programme index value</td>
                        <td>/adm/prog/3/config/name 'Programme_3</td>
                        <td bgcolor="LightYellow"><b>proposed v0.5</b></td>
                    </tr>
                    <tr>
                        <td colspan=2>/lang</td>
                        <td>symbol</td>
                        <td>ISO 639-1?</td>
                        <td>'und'</td>
                        <td>audioProgrammeLanguage</td>
                        <td>/adm/prog/3/config/lang FR</td>
                        <td bgcolor="LightYellow"><b>proposed v0.5</b></td>
                    </tr>
                    </tr>
                    <tr>
                        <td rowspan="2">/label/<i>n</i></td>
                        <td>/name</td>
                        <td>symbol</td>
                        <td></td>
                        <td>'und'</td>
                        <td>Used for local language labeling</td>
                        <td>/adm/prog/3/config/label/2/name</td>
                        <td bgcolor="LightYellow"><b>proposed v0.5</b></td>
                    </tr>
                    <tr>
                        <td>/lang</td>
                        <td>symbol</td>
                        <td>ISO 639-1?</td>
                        <td>'und'</td>
                        <td>audioProgrammeLabel</td>
                        <td>/adm/prog/3/config/label/3/lang FR</td>
                        <td bgcolor="LightYellow"><b>proposed v0.5</b></td>
                    </tr>
                </tbody>
            </table>
        </section>
    </div>
</body>

</html>