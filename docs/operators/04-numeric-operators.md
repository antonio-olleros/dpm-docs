# 4 Numeric

Numeric operators describe operations involving operands with data type Number, Integer or Number Interval.

## 4.1 Numeric operators' general behaviour

### 4.1.1 Input parameters

Operands can be of Recordset or Scalar type. Must be defined as _Number interval_, _Number_, or _Integer_.

### 4.1.2 Result type

Recordset or Scalar with type _Number interval_, _Number_, or _Integer_.

### 4.1.3 Behaviour

If any operand is null, then the result is also null.

Numeric operators can be applied to any numeric type (_Number interval_, _Number_, or _Integer_.) and combination of them, in which case casting to the highest type shall apply.

If the type of operands is _Integer_ then the result has type _Integer_. If any of the operands is of type _Number_, and there are no _Number intervals_, then the result has type _Number_. If any operand is of _Number Interval_ type, the result has type Number Interval.

## 4.2 Unary arithmetic operators

### 4.2.1 Plus (+)

#### 4.2.1.1 Syntax

> **+** op


#### 4.2.1.2 Input parameters

> Op: rset | scal <num + interval\>

#### 4.2.1.3 Output

> rset | scal <num\>

#### 4.2.1.4 Semantics
Returns the operand unchanged.

#### 4.2.1.5 Additional constraints
None

#### 4.2.1.6 Behaviour

- [Unary operators'standard behaviour](./02-general-behaviour.md#21-unary-operators).
- [Numeric operators' standard behaviour](./04-numeric-operators.md#41-numeric-operators-general-behaviour).

#### 4.2.1.7 Examples
- `+ 1` results in `1`
- `+ (-3)` results in `-3`

### 4.2.2 Minus (-)

#### 4.2.2.1 Syntax


> **-** op


#### 4.2.2.2 Input parameters

> Op: rset | scal <num + interval\>

#### 4.2.2.3 Output

> rset | scal <num\>

#### 4.2.2.4 Semantics
Inverts the sign of the operand.

For intervals, inverts the sign of the centre, leaving the radius unchanged.

#### 4.2.2.5 Additional constraints
None

#### 4.2.2.6 Behaviour

- [Unary operators'standard behaviour](./02-general-behaviour.md#21-unary-operators).
- [Numeric operators' standard behaviour](./04-numeric-operators.md#41-numeric-operators-general-behaviour).

#### 4.2.2.7 Examples
- `- 1` results in `-1`
- `- (-3)` results in `3`

### 4.2.3 Absolute value (abs)

#### 4.2.3.1 Syntax

> **abs(** op **)**


#### 4.2.3.2 Input parameters

> Op: rset | scal <num + interval\>

#### 4.2.3.3 Output

> rset | scal <num\>

#### 4.2.3.4 Semantics
Calculates the absolute value of a number.

For intervals, return the absolute value of the centre, leaving the radius unchanged

#### 4.2.3.5 Additional constraints
None

#### 4.2.3.6 Behaviour

- [Unary operators'standard behaviour](./02-general-behaviour.md#21-unary-operators).
- [Numeric operators' standard behaviour](./04-numeric-operators.md#41-numeric-operators-general-behaviour).

#### 4.2.3.7 Examples
- `Abs(-1)` results in `1`
- `Abs(3)` results in `3`

### 4.2.4 Exponential (exp)

#### 4.2.4.1 Syntax

> **exp(** op **)** 


#### 4.2.4.2 Input parameters

> Op: rset | scal <num\>

#### 4.2.4.3 Output

> rset | scal <num>

#### 4.2.4.4 Semantics
Returns `e` (base of the natural logarithm) raised to the op power.

#### 4.2.4.5 Additional constraints
None

#### 4.2.4.6 Behaviour

- [Unary operators'standard behaviour](./02-general-behaviour.md#21-unary-operators).
- [Numeric operators' standard behaviour](./04-numeric-operators.md#41-numeric-operators-general-behaviour).

#### 4.2.4.7 Examples

- `exp(2)` results in `7.38905`
- `exp(1)` results in `2.71828` (the `e` number)

### 4.2.5 Natural logarithm (ln)

#### 4.2.5.1 Syntax

> **ln(** op **)**


#### 4.2.5.2 Input parameters

> Op: rset | scal <num\>

#### 4.2.5.3 Output

> rset | scal <num\>

#### 4.2.5.4 Semantics
Calculates the natural logarithm of a number.

#### 4.2.5.5 Additional constraints
The numeric values must be greater than 0.

#### 4.2.5.6 Behaviour

- [Unary operators'standard behaviour](./02-general-behaviour.md#21-unary-operators).
- [Numeric operators' standard behaviour](./04-numeric-operators.md#41-numeric-operators-general-behaviour).
- If any value is smaller than or equal to 0, generates a run-time error.

#### 4.2.5.7 Examples

- `ln(1)` results in `0`
- `ln(148)` results in `4.997`

### 4.2.6 Square root (sqrt)

#### 4.2.6.1 Syntax

> **sqrt(** op **)**


#### 4.2.6.2 Input parameters

> Op: rset | scal <num\>

#### 4.2.6.3 Output

> rset | scal <num\>

#### 4.2.6.4 Semantics
Calculates the square root of a number.

#### 4.2.6.5 Additional constraints
The numeric values must be greater than or equal to 0.

#### 4.2.6.6 Behaviour

- [Unary operators'standard behaviour](./02-general-behaviour.md#21-unary-operators).
- [Numeric operators' standard behaviour](./04-numeric-operators.md#41-numeric-operators-general-behaviour).
- If any value is smaller than 0, generates a run-time error.

#### 4.2.6.7 Examples

- `sqrt(4)` results in `2`
- `sqrt(25)` results in `5`

### 4.2.7 Logarithm (log)

#### 4.2.7.1 Syntax

> **log(** op, base **)**


#### 4.2.7.2 Input parameters

> op: rset | scal <num\>

> base: scal <num\>

#### 4.2.7.3 Output

> rset | scal <num\>

#### 4.2.7.4 Semantics
Calculates the logarithm of base op.

#### 4.2.7.5 Additional constraints
op numeric values must be greater than 1. base numeric values must be greater than 0.

#### 4.2.7.6 Behaviour

- [Unary operators'standard behaviour](./02-general-behaviour.md#21-unary-operators).
- [Numeric operators' standard behaviour](./04-numeric-operators.md#41-numeric-operators-general-behaviour).
- If the base is 1 or smaller, generates a run-time error.
- If the number is 0 or smaller, generates a run-time error.

#### 4.2.7.7 Examples

- `log(512, 2)` results in `9`
- `log(100, 10)` results in `2`

## 4.3 Binary arithmetic operators

This operators group follows the [General behavior for binary operators](./02-general-behaviour.md#22-binary-operators).

### 4.3.1 Addition (+)

#### 4.3.1.1 Syntax

> left **+** right


#### 4.3.1.2 Input parameters

> left: rset | scal <num + interval\>

> right: rset | scal <num + interval\>

#### 4.3.1.3 Output

> rset | scal <num + interval\>

#### 4.3.1.4 Semantics
Returns the sum of two numbers.

For intervals:

- Centre is calculated as `centre(left) + centre(right)`
- Radius is calculated `radius(left) + radius(right)`

#### 4.3.1.5 Additional constraints
None.

#### 4.3.1.6 Behaviour

- [Binary operators' standard behaviour](./02-general-behaviour.md#22-binary-operators)
- [Numeric operators' standard behaviour](./04-numeric-operators.md#41-numeric-operators-general-behaviour).

#### 4.3.1.7 Examples

- `3 + 2` results in `5`
- `-7 + 3` results in `-4`

### 4.3.2 Subtraction (-)

#### 4.3.2.1 Syntax

> left **-** right


#### 4.3.2.2 Input parameters

> left: rset | scal <num + interval\>

> right: rset | scal <num + interval\>

#### 4.3.2.3 Output

> rset | scal <num + interval\>

#### 4.3.2.4 Semantics
Returns the difference of two numbers.

For intervals:

- Centre is calculated as `centre(left) - centre(right)`
- Radius is calculated `radius(left) + radius(right)`

#### 4.3.2.5 Additional constraints
None.

#### 4.3.2.6 Behaviour

- [Binary operators' standard behaviour](./02-general-behaviour.md#22-binary-operators)
- [Numeric operators' standard behaviour](./04-numeric-operators.md#41-numeric-operators-general-behaviour).

#### 4.3.2.7 Examples

- `3 - 2` results in `1`
- `-7 - 3` results in `-10`

### 4.3.3 Multiplication (*)

#### 4.3.3.1 Syntax

> left **\*** right


#### 4.3.3.2 Input parameters

> left: rset | scal <num + interval\>

> right: rset | scal <num + interval\>

#### 4.3.3.3 Output

> rset | scal <num + interval\>

#### 4.3.3.4 Semantics
Returns the product of two numbers.

For intervals:

- Centre is calculated as `centre(left) * centre(right)`
- Radius is calculated as `(centre(left) * radius(right)) + abs(radius(left) * centre(right)) + (radius(left) * radius(right))`



#### 4.3.3.5 Additional constraints
None.

#### 4.3.3.6 Behaviour

- [Binary operators' standard behaviour](./02-general-behaviour.md#22-binary-operators)
- [Numeric operators' standard behaviour](./04-numeric-operators.md#41-numeric-operators-general-behaviour).

#### 4.3.3.7 Examples

- `4 * 6` results in `24`
- `-9 * 2` results in `-18`

### 4.3.4 Division (/)

#### 4.3.4.1 Syntax

> num **/** den


#### 4.3.4.2 Input parameters

> num: rset | scal <num\>

> den: rset | scal <num\>

#### 4.3.4.3 Output

> rset | scal <num\>

#### 4.3.4.4 Semantics
Divides two numbers.

For intervals:
- Centre is calculated as `centre(left) / centre(right)`
- Radius is calculated as `max((centre(left) + radius(left)) / (centre(right) + radius(right)), (centre(left) + radius(left)) / (centre(right) - radius(right)), (centre(left) - radius(left)) / (centre(right) + radius(right)), (centre(left) - radius(left)) / (centre(right) - radius(right)))`

#### 4.3.4.5 Additional constraints
The denominator must be different to zero.

#### 4.3.4.6 Behaviour

- [Binary operators' standard behaviour](./02-general-behaviour.md#22-binary-operators)
- [Numeric operators' standard behaviour](./04-numeric-operators.md#41-numeric-operators-general-behaviour).
- If the denominator is 0, generates a run-time error.

#### 4.3.4.7 Examples
- `24 / 6` results in `4`
- `-18 / 2` results in `-9`

### 4.3.5 Maximum (max)

#### 4.3.5.1 Syntax

> **max(** op1, op2 {, op}* **)**


#### 4.3.5.2 Input parameters

> op1: rset | scal <num + interval\>

> op2: rset | scal <num + interval\>

#### 4.3.5.3 Output

> rset | scal <num + interval\>

#### 4.3.5.4 Semantics
Calculates the maximum value from a set of operands.

For intervals:
- Centre is calculated as the maximum centre value from all the intervals.
- Radius is the radius of the interval with maximum centre.

#### 4.3.5.5 Additional constraints
None.

#### 4.3.5.6 Behaviour
- For each pair of operands, the [standard behaviour for binary operators](./02-general-behaviour.md#22-binary-operators) applies.

#### 4.3.5.7 Examples

- `Max(1, 3, -5)` results in `3`
- `Max(1, 3, null)` results in `null`

### 4.3.6 Minimum (min)

#### 4.3.6.1 Syntax

> **min(** op1, op2 {, op}* **)**


#### 4.3.6.2 Input parameters

> op1: rset | scal <num + interval\>

> op2: rset | scal <num + interval\>

#### 4.3.6.3 Output

> rset | scal <num + interval\>

#### 4.3.6.4 Semantics
Calculates the minimum value from a set of operands.

For intervals:

- Centre is calculated as the minimum centre value from all the intervals.
- Radius is the radius of the interval with minimum centre.

#### 4.3.6.5 Additional constraints
None.

#### 4.3.6.6 Behaviour

- For each pair of operands, the [standard behaviour for binary operators](./02-general-behaviour.md#22-binary-operators) applies.

#### 4.3.6.7 Examples

- `Min(1, 3, -5)` results in `-5`
- `Min(1, 3, null)` results in `null`

### 4.3.7 Power

#### 4.3.7.1 Syntax

> **power(** base, exponent **)**


#### 4.3.7.2 Input parameters

> num: rset | scal <num\>

> den: rset | scal <num\>

#### 4.3.7.3 Output

> rset | scal <num\>

#### 4.3.7.4 Semantics
Raises the power to the exponent.

#### 4.3.7.5 Additional constraints
None.

#### 4.3.7.6 Behaviour

- [Binary operators' standard behaviour](./02-general-behaviour.md#22-binary-operators)
- [Numeric operators' standard behaviour](./04-numeric-operators.md#41-numeric-operators-general-behaviour).

#### 4.3.7.7 Examples
- `power(5,2)` results in `25`
- `power(5,-1)` results in `0.2`
- `power(-5, 3)` results in `-125`