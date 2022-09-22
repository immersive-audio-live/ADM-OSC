<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

<link rel="stylesheet" href="https://assets.readthedocs.org/static/css/readthedocs-doc-embed.css" type="text/css" />

<style>
    a.src-href {
        float: right;
    }
    p.attr {
        margin-top: 0.5em;
        margin-left: 1em;
    }
    p.func-header {
        background-color: gainsboro;
        border-radius: 0.1em;
        padding: 0.5em;
        padding-left: 1em;
    }
    table.field-table {
        border-radius: 0.1em
    }
</style>##protocol.**object_message**

<p class="func-header">
    <i>def</i> protocol.<b>object_message</b>(<i>object_number: Union[int, float, str], command: str</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/protocol.py#L42">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>



##protocol.**object_query_message**

<p class="func-header">
    <i>def</i> protocol.<b>object_query_message</b>(<i>object_number: Union[int, float, str], command: str </i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/protocol.py#L46">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>



##protocol.**SEnum**





<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>





##protocol.**SubElement**





<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>





##protocol.**Units**





<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>





##protocol.**Type**





<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>



####Methods



<p class="func-header">
    <i></i> <b>as_osc_string</b>(<i>self</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/protocol.py#L84">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>



##protocol.**Status**





<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>





##protocol.**Parameter**

<p class="func-header">
    <i>class</i> protocol.<b>Parameter</b>(<i>sub_element: SubElement, attribute: str, osc_command: str, description: str, units: Units=Units.Normalized, type_: Type=Type. Float, min_=0.0, max_=1.0, def_=1.0, status: Status=Status.InProgress, comment: str=''</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/protocol.py#L108">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>



####Methods



<p class="func-header">
    <i></i> <b>osc_format</b>(<i>self</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/protocol.py#L137">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>





<p class="func-header">
    <i></i> <b>osc_example</b>(<i>self, val: Union[int, float, str, None]=None</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/protocol.py#L141">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>





<p class="func-header">
    <i></i> <b>get_number_of_values</b>(<i>self</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/protocol.py#L148">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>





<p class="func-header">
    <i></i> <b>get_parameters</b>(<i>self</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/protocol.py#L151">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>





<p class="func-header">
    <i></i> <b>get_min_value</b>(<i>self</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/protocol.py#L154">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>





<p class="func-header">
    <i></i> <b>get_max_value</b>(<i>self</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/protocol.py#L157">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>





<p class="func-header">
    <i></i> <b>get_default_value</b>(<i>self</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/protocol.py#L160">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>





<p class="func-header">
    <i></i> <b>get_random_value</b>(<i>self</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/protocol.py#L163">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>





<p class="func-header">
    <i></i> <b>get_osc_command</b>(<i>self, object_number: Union[int, float, str]</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/protocol.py#L166">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>





<p class="func-header">
    <i></i> <b>get_osc_query_command</b>(<i>self, object_number: Union[int, float, str]</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/protocol.py#L169">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>





<p class="func-header">
    <i></i> <b>validate_value</b>(<i>self, value: Union[int, float, str]</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/protocol.py#L172">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>





<p class="func-header">
    <i></i> <b>is_stable</b>(<i>self</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/protocol.py#L178">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>





<p class="func-header">
    <i></i> <b>is_in_progress</b>(<i>self</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/protocol.py#L181">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>



##protocol.**PackedParameters**

<p class="func-header">
    <i>class</i> protocol.<b>PackedParameters</b>(<i>sub_element: SubElement, attribute: str, osc_command: str, description: str, params: list[Parameter], status: Status, comment: str=''</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/protocol.py#L190">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>



####Methods



<p class="func-header">
    <i></i> <b>osc_format</b>(<i>self</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/protocol.py#L207">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>





<p class="func-header">
    <i></i> <b>osc_example</b>(<i>self, values: list[Union[int, float, str, None]]=None</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/protocol.py#L214">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>





<p class="func-header">
    <i></i> <b>get_number_of_values</b>(<i>self</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/protocol.py#L226">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>





<p class="func-header">
    <i></i> <b>get_parameters</b>(<i>self</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/protocol.py#L229">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>





<p class="func-header">
    <i></i> <b>get_min_value</b>(<i>self</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/protocol.py#L232">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>





<p class="func-header">
    <i></i> <b>get_max_value</b>(<i>self</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/protocol.py#L235">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>





<p class="func-header">
    <i></i> <b>get_default_value</b>(<i>self</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/protocol.py#L238">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>





<p class="func-header">
    <i></i> <b>get_random_value</b>(<i>self</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/protocol.py#L241">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>





<p class="func-header">
    <i></i> <b>validate_value</b>(<i>self, value: list[Union[int, float, str]]</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/protocol.py#L244">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>



##protocol.**get_all_parameters**

<p class="func-header">
    <i>def</i> protocol.<b>get_all_parameters</b>(<i></i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/protocol.py#L254">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>



##protocol.**get_stable_parameters**

<p class="func-header">
    <i>def</i> protocol.<b>get_stable_parameters</b>(<i></i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/protocol.py#L258">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>



##protocol.**get_in_progress_parameters**

<p class="func-header">
    <i>def</i> protocol.<b>get_in_progress_parameters</b>(<i></i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/protocol.py#L262">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>



##protocol.**find_parameter**

<p class="func-header">
    <i>def</i> protocol.<b>find_parameter</b>(<i>attribute: str</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/protocol.py#L266">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>



##protocol.**dump_protocol**

<p class="func-header">
    <i>def</i> protocol.<b>dump_protocol</b>(<i></i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/protocol.py#L279">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>

