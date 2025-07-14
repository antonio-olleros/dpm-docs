# 11 Clause operators

Clause operators serve to perform operations on the DPM key components of recordsets. Use of clause operators with Standard Key Components are not allowed.

## 11.1 where

### 11.1.1 Syntax
```
op[where condition]
```

### 11.1.2 Input parameters
- op: rset <*>
- condition: expression <boo>

### 11.1.3 Output
rset <*>

### 11.1.4 Semantics
Filters a recordset based on the value of a key component.

### 11.1.5 Additional constraints
Condition must be a Boolean expression using as input key components of op.

### 11.1.6 Behaviour
Returns a recordset with the same data structure as the input operand, and with the records resulting from the evaluation of the filtering condition. When the condition evaluates to true, the record is kept, otherwise (including null), the record is not kept.

### 11.1.7 Examples
Considering the following recordset, generated from the selection {tT1, r010-020}:

| RefDate {#k} | r {#k} | CNT {#k} | f {#f} |
|--------------|--------|----------|--------|
| 2022Q1       |