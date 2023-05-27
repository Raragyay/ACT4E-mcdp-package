# Simple unary mathematical operations


::: act4e_mcdp.primitivedps
    options:
      members:
        - M_Ceil_DP
        - M_FloorFun_DP  
        - M_Power_DP
 

## Adding or multiplying by a constant

The next set of DPs implement addition or multiplication by a constant.
The constant is specified by an object of type `ValueFromPoset`.


## Adding a constant

::: act4e_mcdp.primitivedps
    options:
      members:
        - M_Fun_AddConstant_DP
        - M_Res_AddConstant_DP
        

## Multiplying by a constant

::: act4e_mcdp.primitivedps
    options:
      members:
        - M_Fun_MultiplyConstant_DP
        - M_Res_MultiplyConstant_DP
        - M_Res_DivideConstant_DP
