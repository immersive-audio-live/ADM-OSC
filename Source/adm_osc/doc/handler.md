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
</style>##handler.**extract_indexes**

<p class="func-header">
    <i>def</i> handler.<b>extract_indexes</b>(<i>idx: str</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/handler.py#L36">[source]</a>
</p>

+ "*" means all objects
+ [n-m] means range from "n" to "m"
+ [n, m, o] means specific object defined by n, m and o index ...
+ single int value == single object

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>



##handler.**adm_handler**

<p class="func-header">
    <i>def</i> handler.<b>adm_handler</b>(<i>address, *args</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/docstr-md/blob/master/handler.py#L84">[source]</a>
</p>

1 - check ADM message header at start of address
2 - extract target : object | setup ...
3 - extract object index:
+ single int value == single object
+ "*" means all objects
+ [n-m] means range from "n" to "m"
+ [n, m, o] means specific object defined by n, m and o index ...
4 - extract and validate command name; It should be in the provided protocol
5 - extract and validate all arguments

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>

