# 7 Aggregate operators

## 7.1 Aggregate operators' general behaviour

### 7.1.1 Syntax
```
aggregateOperator (op {group by groupingId {, groupingId}*})
```

### 7.1.2 Input parameters
- op: rset <*>
- groupingId: scal <prop>

### 7.1.3 Output
rset | scal <*>

### 7.1.4 Semantics
Aggregate operators perform operations on the measures of the operand recordset, calculating the required aggregated values for groups of records. The groups of records to be aggregated are specified through the grouping clause. If no grouping clause is used, the operation shall be calculated on all the records, resulting in a scalar.

### 7.1.5 Additional constraints
The allowed data types depend on the specific operator according to the following table:

| Operator {#k} | Operand type {#k} | Result type {#f} |
|---------------|-------------------|------------------|
| Sum           | Number            | Number           |
| Count         | Any               | Integer          |
| Min           | Any               | Any              |
| Max           | Any               | Any              |
| Average       | Number            | Number           |
| Median        | Number            | Number           |

The components in the grouping by clause shall be present in the operand.

### 7.1.6 Behaviour
Aggregate operations generate a recordset or a scalar, depending on the grouping clause.

If the grouping clause exists, the structure of the resulting recordset has as key components the components in the group by

The result may be:
- A recordset, for which the resulting structure contains as key dimensions the components included in the group by clause.
- A scalar, if the grouping clause is omitted.

### 7.1.7 Examples
Supposing the following recordset with name rs1:

| r {#k} | c {#k} | CNT {#k} | f {#f} |
|--------|--------|----------|--------|
| 010    | 010    | PT       | 100    |
| 010    | 020    | PT       | 200    |
| 020    | 010    | PT       | 300    |
| 020    | 020    | PT       | 400    |
| 010    | 010    | DE       | 500    |
| 010    | 020    | DE       | 600    |
| 020    | 010    | DE       | 700    |
| 020    | 020    | DE       | 800    |

sum(rs1 group by r) results in:

| r {#k} | f {#f} |
|--------|--------|
| 010    | 1400   |
| 020    | 2200   |

sum(rs1 group by r, CNT) results in:

| r {#k} | CNT {#k} | f {#f} |
|--------|----------|--------|
| 010    | PT       | 300    |
| 020    | PT       | 700    |
| 010    | DE       | 1100   |
| 020    | DE       | 1500   |

count(rs1) results in: 8 (scalar)

## 7.2 Sum (sum)

### 7.2.1 Syntax
```
sum(op {group by groupingId {, groupingId}*})
```

### 7.2.2 Input parameters
- op: rset <num + interval>
- groupingId: scal <prop>

### 7.2.3 Output
rset | scal <num>

### 7.2.4 Semantics
Returns the sum of the input values. Follows the general semantics of aggregate operators.

For intervals:
- The centre is calculated as the sum of the all the centers of the operands.
- The radius is calculated as the sum of all the radiuses of the operads.

### 7.2.5 Additional constraints
None.

### 7.2.6 Behaviour
Aggregate operators' general behaviour.

## 7.3 Count (count)

### 7.3.1 Syntax
```
count(op {group by groupingId {, groupingId}*})
```

### 7.3.2 Input parameters
- op: rset <*>
- groupingId: scal <prop>

### 7.3.3 Output
rset | scal <num>

### 7.3.4 Semantics
Returns the number of records in the recordset or groups of records. Follows the general semantics of aggregate operators.

### 7.3.5 Additional constraints
None.

### 7.3.6 Behaviour
Aggregate operators' general behaviour.

Note: Aggregate operators generally ignore null values. This behavior can be overridden by using the nvl operator.

## 7.4 Minimum value (min_aggr)

### 7.4.1 Syntax
```
min_aggr(op {group by groupingId {, groupingId}*})
```

### 7.4.2 Input parameters
- op: rset <*>
- groupingId: scal <prop>

### 7.4.3 Output
rset | scal <num>

### 7.4.4 Semantics
Returns the minimum value of the input values. Follows the general semantics of aggregate operators.

For intervals:
- The centre is calculated as the minimum value of the all the centers of the operands.
- The radius is the radius of the operand that has the minimum centre.

### 7.4.5 Additional constraints
None.

### 7.4.6 Behaviour
Aggregate operators' general behaviour.

## 7.5 Maximum value (max_aggr)

### 7.5.1 Syntax
```
max_aggr(op {group by groupingId {, groupingId}*})
```

### 7.5.2 Input parameters
- op: rset <*>
- groupingId: scal <prop>

### 7.5.3 Output
rset | scal <num>

### 7.5.4 Semantics
Returns the maximum value of the input values. Follows the general semantics of aggregate operators.

For intervals:
- The centre is calculated as the maximum value of the all the centers of the operands.
- The radius is the radius of the operand that has the maximum centre.

### 7.5.5 Additional constraints
None.

### 7.5.6 Behaviour
Aggregate operators' general behaviour.

## 7.6 Average (avg)

### 7.6.1 Syntax
```
avg(op {group by groupingId {, groupingId}*})
```

### 7.6.2 Input parameters
- op: rset <num>
- groupingId: scal <prop>

### 7.6.3 Output
rset | scal <num>

### 7.6.4 Semantics
Returns the average of the input values. Follows the general semantics of aggregate operators.

### 7.6.5 Additional constraints
None.

### 7.6.6 Behaviour
Aggregate operators' general behaviour.

## 7.7 Median value (median)

### 7.7.1 Syntax
```
median(op {group by groupingId {, groupingId}*})
```

### 7.7.2 Input parameters
- op: rset <num>
- groupingId: scal <prop>

### 7.7.3 Output
rset | scal <num>

### 7.7.4 Semantics
Returns the median of the input values. Follows the general semantics of aggregate operators.

### 7.7.5 Additional constraints
None.

### 7.7.6 Behaviour
Aggregate operators' general behaviour.