# 2 Common general behaviours for the operators

## 2.1 Unary operators

This general behaviour is applied to operators taking as an argument one single operand.

Unless explicitly specified differently, the behaviour for the unary operators is as follows:

### 2.1.1 Scalars

The _Operator_ is applied on a _Scalar_ value and returns a _Scalar_ value.

### 2.1.2 Recordsets

The _Operator _ is applied on a _Recordset_ and returns a Recordset.

The _Operator _ is applied to the values of all the facts of the Recordset.

#### 2.1.2.1 Constraints

1. The application of the _Operator_ is only allowed if all the facts of the _Operand_ _Recordset_ are compatible with the _Operator_.

#### 2.1.2.2 Structure

The structure of the resulting _Recordset_ contains the key and fact components of the _Operand_ _Recordset_, the attribute components are not propagated.

#### 2.1.2.3 Records

The operators produce one output _Record_ per each input Record, which have:

- For Key Components, the values unchanged.
- For the Fact values, the _Operator _ is applied to the input value and returns the corresponding value.

## 2.2 Binary operators

This general behaviour is applied whenever an _Operator _ takes as input two operands, which includes the following operators:

- [Arithmetic Binary operators](./04-numeric-operators.md#43-binary-arithmetic-operators)
- [Comparison operators](./05-comparison-operators.md#51-comparison-operators-general-behaviour) 
- [Logical Binary operators](./06-logical-operators.md#6-logical)

Unless explicitly specified differently, the behaviour for the binary Operators is as follows.

### 2.2.1 Scalars

If the two _Operands _of a binary _Operator _ are Scalars, the result shall be the _Scalar_ resulting of applying the _Operator _ to the Operands.

### 2.2.2 Recordset and scalar

A binary _Operator_ applied to a _Recordset_ _Operand_ and a Scalar, will result in a _Recordset_ with the same key and fact components as the input _Recordset_ _Operand_ (attribute components are not propagated). The _Operator_ shall be applied to every _Record_ of the input _Recordset_ and the _Scalar_.

#### 2.2.2.1 Examples

```
0.25*{S.26.01, r0600, cNNN}
```

Supposing that the selection yields the following _Recordset_:

| c {#k} | f {#f} |
|--------|--------|
| 0060   | 100    |
| 0080   | 200    |

The operation results in:

| c {#k} | f {#f} |
|--------|--------|
| 0060   | 25     |
| 0080   | 50     |

### 2.2.3 Recordsets

#### 2.2.3.1 Constraints

Binary Operators can only be applied to two Recordsets _Operands_ if they have:

1. exactly the same Key Components; or
2. the Key Components of one _Recordset_ (Reference Recordset) are a superset of the Key Components of the other _Recordset_.

#### 2.2.3.2 Structure

The _Operator_ yields a _Recordset_ with the common Key Components in case 1, or the Key Components of the Reference _Recordset_ in case 2. The resulting _Recordset_ does not contain any Attribute Component from the _Operand _Recordsets.

#### 2.2.3.3 Records

The _Operator _ applies to the pairs of values resulting from performing an inner join of the input Recordsets on the common Key Components.

#### 2.2.3.4 Examples

##### 2.2.3.4.1 Same identifiers

```
{C 28.00 c040} + {C 28.00 c190}
```

Supposing that the selections yield:

{C 28.00 c040}

| INC {#k} | f {#f} |
|----------|--------|
| 123      | 1000   |
| 456      | 2000   |
| 789      | 3000   |

{C 28.00 c190}

| INC {#k} | f {#f} |
|----------|--------|
| 123      | -100   |
| 456      | -200   |
| 789      | -300   |

The result would be:

| INC {#k} | f {#f} |
|----------|--------|
| 123      | 900    |
| 456      | 1800   |
| 789      | 2700   |

##### 2.2.3.4.2 Subset of identifiers

```
{F 40.01 c0110} >= {F 40.02c0060}
```

Supposing that the selections yield:

{F 40.01 c0110}

| LIN {#k} | TYC {#k} | f {#f} |
|----------|----------|--------|
| 123      | x1       | 1      |
| 456      | x1       | 0.8    |
| 789      | x1       | 0.4    |

{F 40.02 c0060}

| LIN {#k} | TYC {#k} | STC {#k} | LHC {#k} | LHO {#k} | f {#f} |
|----------|----------|----------|----------|----------|--------|
| 123      | x1       | 111      | ABC      | x1       | 0.3    |
| 123      | x1       | 111      | DEF      | x1       | 0.7    |
| 456      | x1       | 222      | ABC      | x1       | 0.85   |

The result would be:

| LIN {#k} | TYC {#k} | STC {#k} | LHC {#k} | LHO {#k} | f {#f} |
|----------|----------|----------|----------|----------|--------|
| 123      | x1       | 111      | ABC      | x1       | true   |
| 123      | x1       | 111      | DEF      | x1       | true   |
| 456      | x1       | 222      | ABC      | x1       | false  |

Note that:

- An inner join on the common _Key Components_ is performed. This means that there is no comparison for the _Record_ in F 40.01 with LIN = 789, because there is no match in F 40.02.
- The result of the operation has the _Structure_ of the _Reference_ _Recordset_, which is the one that has a superset of Key Components.
- For each match in the join the _Operator_ `>=` is applied to the pairs of values for the facts.

### 2.2.4 Intervals treatment

When one of two numeric _Operands _is an interval, and the other is a point, the point is transformed into an interval with centre value equal to the point value, and radius 0.