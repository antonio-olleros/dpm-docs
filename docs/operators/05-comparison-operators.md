# 5 Comparison operators

## 5.1 Comparison operators' general behaviour

Comparison operators describe operations that compare the values of operands.

This operator group is based upon the General behavior for binary operators.

### 5.1.1 Input parameters

Operands that can be of Recordset or Scalar type. Must have the same data type. For all operators that accept numeric operands, intervals are allowed.

### 5.1.2 Result type

Recordset or Scalar with type Boolean.

### 5.1.3 Constraints

The operands for the comparison operations must be of the same type (considering implicit casting).

### 5.1.4 Behaviour

If any operand is null, then the result is also null.

For comparison operators implying an order (`>`, `>=`, `<`, `<=`), the following rules apply:

- Boolean values: `true` is considered greater than `false`.
- Strings: Alphabetic order is followed.

## 5.2 Equal (=)

### 5.2.1.1 Syntax

> left **=** right


### 5.2.1.2 Input parameters

> left: rset | scal <*>

> right: rset | scal <*>

### 5.2.1.3 Output

> rset | scal <boo\>

### 5.2.1.4 Semantics
Returns `true` if left is equal to right and `false` otherwise.

For intervals: `abs(centre(left) – centre(right)) <= radius(left) + radius(right)`.

### 5.2.1.5 Additional constraints
None.

### 5.2.1.6 Behaviour

- [Binary operators' standard behaviour](./02-general-behaviour.md#22-binary-operators).
- [Comparison operators' standard behaviour](#51-comparison-operators-general-behaviour).

### 5.2.1.7 Examples

- `1 = 2` results in `false`
- `3 = null` results in `null`
- `"4" = "4"` results in `true`

## 5.3 Not Equal (!=)

### 5.3.1.1 Syntax

> left **!=** right


### 5.3.1.2 Input parameters

> left: rset | scal <*>

> right: rset | scal <*>

### 5.3.1.3 Output

rset | scal <boo\>

### 5.3.1.4 Semantics
Returns `false` if left is equal to right and `true` otherwise.

For intervals: `abs(centre(left) – centre(right)) > radius(left) + radius(right)`.

### 5.3.1.5 Additional constraints
None.

### 5.3.1.6 Behaviour

- [Binary operators' standard behaviour](./02-general-behaviour.md#22-binary-operators).
- [Comparison operators' standard behaviour](#51-comparison-operators-general-behaviour).

### 5.3.1.7 Examples

- `1 != 2` results in `true`
- `3 != null` results in `null`
- `"4" != "4"` results in `false`

## 5.4 Greater than (>)

### 5.4.1.1 Syntax

> left **\>** right


### 5.4.1.2 Input parameters

> left: rset | scal <*>

> right: rset | scal <*>

### 5.4.1.3 Output

> rset | scal <boo\>

### 5.4.1.4 Semantics

Returns `true` if left is greater than right and `false` otherwise.

For intervals: `centre(left) > centre(right) - (radius(left) + radius(right))`.

### 5.4.1.5 Additional constraints
None.

### 5.4.1.6 Behaviour

- [Binary operators' standard behaviour](./02-general-behaviour.md#22-binary-operators).
- [Comparison operators' standard behaviour](#51-comparison-operators-general-behaviour).

### 5.4.1.7 Examples

- `12 > 2` results in `true`
- `3 > null` results in `null`
- `true` > `false` results in `true`
- `"tez" > "test"` results in `true`

## 5.5 Greater Equal than (>=)

### 5.5.1.1 Syntax

> left **>=** right


### 5.5.1.2 Input parameters

> left: rset | scal <*>

> right: rset | scal <*>

### 5.5.1.3 Output

> rset | scal <boo\>

### 5.5.1.4 Semantics
Returns `true` if left is greater than or equal to right and `false` otherwise.

For intervals: `centre(left) >= centre(right) - (radius(left) + radius(right))`.

### 5.5.1.5 Additional constraints
None.

### 5.5.1.6 Behaviour

- [Binary operators' standard behaviour](./02-general-behaviour.md#22-binary-operators).
- [Comparison operators' standard behaviour](#51-comparison-operators-general-behaviour).

### 5.5.1.7 Examples
- `1 >= 2` results in `false`
- `3 >= null` results in `null`
- `"tez" >= "test"` results in `true`

## 5.6 Less than (<)

### 5.6.1.1 Syntax

> left **<** right

### 5.6.1.2 Input parameters

> left: rset | scal <*>

> right: rset | scal <*>

### 5.6.1.3 Output

> rset | scal <boo\>

### 5.6.1.4 Semantics
Returns `true` if left is smaller than right and `false` otherwise.

For intervals: `centre(left) – centre(right) < radius(left) + radius(right)`.

### 5.6.1.5 Additional constraints
None.

### 5.6.1.6 Behaviour

- [Binary operators' standard behaviour](./02-general-behaviour.md#22-binary-operators).
- [Comparison operators' standard behaviour](#51-comparison-operators-general-behaviour).

### 5.6.1.7 Examples

- `1 < 2` results in `true`
- `3 < null` results in `null`
- `"tea" < "test"` results in `true`

## 5.7 Less Equal than (<=)

### 5.7.1.1 Syntax

> left **<=** right


### 5.7.1.2 Input parameters

> left: rset | scal <*>

> right: rset | scal <*>

### 5.7.1.3 Output
rset | scal <boo\>

### 5.7.1.4 Semantics
Returns `true` if left is smaller than or equal to right and `false` otherwise.

For intervals: `centre(left) – centre(right) <= radius(left) + radius(right)`.

### 5.7.1.5 Additional constraints
None.

### 5.7.1.6 Behaviour

- [Binary operators' standard behaviour](./02-general-behaviour.md#22-binary-operators).
- [Comparison operators' standard behaviour](#51-comparison-operators-general-behaviour).

### 5.7.1.7 Examples

- `3 <= 2` results in `false`
- `3 <= null` results in `null`
- `"tea" <= "test"` results in `true`

## 5.8 Element of (in)

### 5.8.1.1 Syntax

> op **in** set


### 5.8.1.2 Input parameters

> op: rset | scal <num\>

> set: scalar_set <*> | subcategory

### 5.8.1.3 Output

> rset | scal <boo\>

### 5.8.1.4 Semantics
Returns `true` if op belongs to the set and `false` otherwise.

### 5.8.1.5 Additional constraints
op must be of the same data type as the values in the set (considering implicit casting)

### 5.8.1.6 Behaviour

- [Binary operators' standard behaviour](./02-general-behaviour.md#22-binary-operators).
- [Comparison operators' standard behaviour](#51-comparison-operators-general-behaviour).

### 5.8.1.7 Examples

- `5 in {1,3, 5}` results in `true`
- `"abc" in {"def", "ghi"}` results in `false`

## 5.9 Match characters (match)

### 5.9.1.1 Syntax

> **match(** op, pattern **)**


### 5.9.1.2 Input parameters

> op: rset | scal <str\>

> pattern: scal <str\>

### 5.9.1.3 Output
> rset | scal <boo\>

### 5.9.1.4 Semantics
Returns true if op matches the pattern, false otherwise.

### 5.9.1.5 Additional constraints
pattern is a regex expression following the Python definition.

### 5.9.1.6 Behaviour

- [Binary operators' standard behaviour](./02-general-behaviour.md#22-binary-operators).
- [Comparison operators' standard behaviour](#51-comparison-operators-general-behaviour).

### 5.9.1.7 Examples
- `match("test", "[0-9]+")` results in `false`
- `match("1234", "[0-9]+")` results in `true`
- `match("hello", "[a-z]+")` results in `true`

## 5.10 Is null (isnull)

### 5.10.1.1 Syntax

> **isnull(** op **)**


### 5.10.1.2 Input parameters

> op: rset | scal <*>

### 5.10.1.3 Output

> rset | scal <boo\>

### 5.10.1.4 Semantics
Returns `true` if the value of op is `null`, `false` otherwise.

### 5.10.1.5 Additional constraints
None.

### 5.10.1.6 Behaviour

- [Binary operators' standard behaviour](./02-general-behaviour.md#22-binary-operators).
- [Comparison operators' standard behaviour](#51-comparison-operators-general-behaviour).