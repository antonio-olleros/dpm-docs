# 6 Logical

Logical operators describe operations involving two operands with Boolean data type. To deal with null values, all operations implements Kleene logic for logical operations (also known as Three-valued logic).

## 6.1 Conjunction (and)

### 6.1.1.1 Syntax
```
left and right
```

### 6.1.1.2 Input parameters
- left: rset | scal <boo>
- right: rset | scal <boo>

### 6.1.1.3 Output
rset | scal <boo>

### 6.1.1.4 Semantics
Returns true if both operands are true, otherwise false.

### 6.1.1.5 Additional constraints
None.

### 6.1.1.6 Behaviour
- Binary operators' standard behaviour.

|        | False {#k} | Null {#k} | True {#k} |
|--------|------------|-----------|-----------|
| False {#k}  | False      | False     | False     |
| Null {#k}   | False      | Null      | Null      |
| True {#k}   | False      | Null      | True      |

## 6.2 Disjunction (or)

### 6.2.1.1 Syntax
```
left or right
```

### 6.2.1.2 Input parameters
- left: rset | scal <boo>
- right: rset | scal <boo>

### 6.2.1.3 Output
rset | scal <boo>

### 6.2.1.4 Semantics
Returns true if any operand is true, otherwise false.

### 6.2.1.5 Additional constraints
None.

### 6.2.1.6 Behaviour
- Binary operators' standard behaviour.

|        | False {#k} | Null {#k} | True {#k} |
|--------|------------|-----------|-----------|
| False {#k}  | False      | Null      | True      |
| Null {#k}   | Null       | Null      | True      |
| True {#k}   | True       | True      | True      |

## 6.3 Exclusive disjunction (xor)

### 6.3.1.1 Syntax
```
left xor right
```

### 6.3.1.2 Input parameters
- left: rset | scal <boo>
- right: rset | scal <boo>

### 6.3.1.3 Output
rset | scal <boo>

### 6.3.1.4 Semantics
Returns true if one operand is true and the other is false, otherwise false.

### 6.3.1.5 Additional constraints
None.

### 6.3.1.6 Behaviour
- Binary operators' standard behaviour.

|        | False {#k} | Null {#k} | True {#k} |
|--------|------------|-----------|-----------|
| False {#k}  | False      | Null      | True      |
| Null {#k}   | Null       | Null      | Null      |
| True {#k}   | True       | Null      | False     |

## 6.4 Negation (not)

### 6.4.1.1 Syntax
```
not op
```

### 6.4.1.2 Input parameters
op: rset | scal <boo>

### 6.4.1.3 Output
rset | scal <boo>

### 6.4.1.4 Semantics
Returns true if op is false, and false if op is true.

### 6.4.1.5 Additional constraints
None.

### 6.4.1.6 Behaviour
- Binary operators' standard behaviour.

| Input {#k} | Result {#f} |
|------------|-------------|
| False      | True        |
| Null       | Null        |
| True       | False       |