# 3 Selection operators

## 3.1 Selection operator

### 3.1.1 Syntax

```
{[ttable | vvariable | ooperation]1
[rrow [, rrow]* | rrow_init–rrow_end | r*]*
[ccol [, ccol]*| ccol_init–ccol_end | c* ]*
[ssheet [, ssheet]*| ssheet_init–ssheet_end | s*]*
interval_arithmetics, fallback_value
}
```

### 3.1.2 Input parameters

- **table**: The code of a DPM Report table.
- **variable**: the code of a DPM variable.
- **operation**: The code of a DPM Operation.
- **row, row_init, row_end**: A Reference to the code of a row of a DPM table.
- **col, col_init, col_end**: A Reference to the code of a col of a DPM table.
- **sheet, sheet_init, sheet_end**: A Reference to the code of a sheet of a DPM table.
- **interval_arithmetics**: A Boolean value specifying whether interval arithmetics should apply. The default value, in case the parameter is omitted, is false.
- **default_value**: A scalar value specifying the value to be used in case of nulls.

### 3.1.3 Output

rset<*>

### 3.1.4 Semantics

Serves to select data as defined in the DPM model.

### 3.1.5 Additional constraints

1. Existence of the parameters. The referred table, variable or operation need to be defined in the DPM.
2. Operations need to be defined in the same script.
3. Rows, columns and sheets need to exist in the table or operation on which they are defined.
4. When the selection is done at variable level, row, column and sheet parameters cannot exist.

### 3.1.6 Behaviour

Returns a Recordset with the following structure:

**Key Components:**
- **DPM-XL**
  - Row: If the selected table has ordinate rows and more than one row is present in the selection. The name of the Component is "r".
  - Column: If the selected table has ordinate columns and more than one column is present in the selection. The name of the Component is "c".
  - Sheet: If the selected table has ordinate sheets and more than one sheet is present in the selection. The name of the Component is "s".
- **DPM-ML**
  - X: If there is Column for DPM-XL.
  - Y: If there is Row for DPM-XL.
  - Z: If there is Sheet for DPM-XL.
- A DPM Key Component for each Key Variable belonging to the Key associated to the selected Variable. The name of the Component is the Code of the Property associated to the Key Variable. The Data Type of the component shall be the correspondent Data Type of the Metric or Property associated to the respective Key Variable.

**Fact Component**: With the Data Type corresponding to the selected Variable.

**Attribute Components**: One Component for each Attribute Variable associated to the selected Variable. The name of the Component is the Code of the Property associated to the Attribute Variable. The Data Type of the component shall be the correspondent Data Type of the Metric or Property associated to the respective Attribute Variable.

The Records for the Recordset shall be obtained from the input data according to the selection.

### 3.1.7 DPM-ML metamodel representation

There is no metamodel representation for the selection operator. It is used to select, in last instance, variables. So the result of the selection are processed to get the relevant variables for DPM-ML, as well as the DefaultValue and UseIntervalArithmetics attributes.

## 3.2 With

### 3.2.1 Syntax

```
with partial_selection: expression
```

### 3.2.2 Input parameters

- **partial_selection**: A selection expression (see Selection Operator)
- **expression**: A expression including selection operators

### 3.2.3 Output

Does not generate output; modifies the selections of the expression after the colon.

### 3.2.4 Semantics

Serves to simplify expressions by adding a single context that may apply to all the operands in the expression.

### 3.2.5 Additional constraints

None

### 3.2.6 Behaviour

The selection parameters in the partial selection applies to all the selections in the expression, unless they are overridden by a more specific parameter.

Therefore, in a selection inside the expression, whenever one of the parameters of the selection expression is not present, but that parameter is present on the partial selection, the parameter of the partial selection applies.

### 3.2.7 Examples

```
With {F 01.01 c0010, default:0, interval:false}:
{r0010} = {r0020} + {r0030} + {r0040}
```

The partial selection applies to all the selections in the expression

```
With {F 01.01 c0010, default:0, interval:false}:
{r0010} + {r0040} = {F04.01 r0010, c0010}
```

The partial selection applies to the two selections that do not refer to a table. Regarding the other selection, the default and intervals apply

```
With {F 01.01 c0010, default:0, interval:false}:
{F 01.01 r0010} + {F 01.01 r0040} = {F04.01 r0010, c0010 default:null}
```

The partial selection applies to the two selections that refer to the same table referred to in the partial selection. Regarding the other selection, interval argument in the partial selection applies, but the default is overridden.

```
With {c0010, default:0, interval:false}:
{F 01.01 r0010} + {F 01.01 r0040} = {F04.01 r0010}
```

The partial selection applies to all the selections in the expression.

### 3.2.8 Metamodel representation

See selection operator.