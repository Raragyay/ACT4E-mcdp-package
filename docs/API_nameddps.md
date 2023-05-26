# NamedDPs (Diagrams)

NamedDPs are objects that describe the elements of a co-design diagram; a graph that interconnects
DPs. 

They could be interpreted more as an "operad" built on DP.


## Common NamedDP interface

::: act4e_mcdp.nameddps
    options:
      members:
        - NamedDP




## SimpleWrap

The function of [SimpleWrap][act4e_mcdp.nameddps.SimpleWrap] is to wrap [a PrimiviteDP][act4e_mcdp.primitivedps.PrimitiveDP] in the graph.

::: act4e_mcdp.nameddps
    options:
       members:
        - SimpleWrap


## CompositeNamedDP

The function of [CompositeNamedDP][act4e_mcdp.nameddps.CompositeNamedDP] is to interconnect
a number of [NamedDPs][act4e_mcdp.nameddps.NamedDP] in a graph.

Each node of the graph is a [NamedDP][act4e_mcdp.nameddps.NamedDP] -- either a [SimpleWrap][act4e_mcdp.nameddps.SimpleWrap], which wraps one DP, or another [CompositeNamedDP][act4e_mcdp.nameddps.CompositeNamedDP], thus allowing recursion.



::: act4e_mcdp.nameddps
    options:
       members:
        - CompositeNamedDP


The connections are described by a list of Connection objects.


::: act4e_mcdp.nameddps
    options:
       members:
        - Connection


These are the utility classes that describe the interconnection.


::: act4e_mcdp.nameddps
    options:
       members:
        - ModelResource
        - ModelFunctionality
        - NodeResource
        - NodeFunctionality
