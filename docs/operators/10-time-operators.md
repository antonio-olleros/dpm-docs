# 10 Time operators

## 10.1 Time shift

### 10.1.1 Syntax
```
time_shift(op, period, numberPeriods, {var})
```

### 10.1.2 Input parameters
- op: rset <*> | scal <date>
- period: scal <Str>
- numberPeriods: scal <int>
- var: scal <prop>

### 10.1.3 Output
rset <*>

### 10.1.4 Semantics
Changes the dates of the var component of the recordset op by adding (or subtracting) the numberPeriods of the period type.

### 10.1.5 Additional constraints
The component var must belong to the recordset op, and has to be of Time interval type.

The period must have one of the following values:
- A for year
- S for semester
- Q for quarter
- M for month
- W for week
- D for day

### 10.1.6 Behaviour
Returns a recordset with the same data structure and number of records as the input op. The dates for the component var are modified by adding the numberPeriods (subtracting, if negative) of the period type.

### 10.1.7 Examples
Considering the following recordset, generated from the selection {tT1, r010-020, c010-020}:

| RefDate {#k} | r {#k} | c {#k} | f {#f} |
|--------------|--------|--------|--------|
| 2022Q1       | 010    | 010    | 100    |
| 2022Q1       | 010    | 020    | 200    |
| 2022Q1       | 010    | 010    | 300    |
| 2022Q1       | 010    | 020    | 400    |
| 2022Q2       | 020    | 010    | 500    |
| 2022Q2       | 020    | 020    | 600    |
| 2022Q2       | 020    | 010    | 700    |
| 2022Q2       | 020    | 020    | 800    |

time_shift({tT1, r010-020, c010-020}, RefDate, Q, 1) returns:

| RefDate {#k} | R {#k} | c {#k} | f {#f} |
|--------------|--------|--------|--------|
| 2022Q2       | 010    | 010    | 100    |
| 2022Q2       | 010    | 020    | 200    |
| 2022Q2       | 010    | 010    | 300    |
| 2022Q2       | 010    | 020    | 400    |
| 2022Q3       | 020    | 010    | 500    |
| 2022Q3       | 020    | 020    | 600    |
| 2022Q3       | 020    | 010    | 700    |
| 2022Q3       | 020    | 020    | 800    |

time_shift({tT1, r010-020, c010-020}, RefDate, Q, -1) returns:

| RefDate {#k} | r {#k} | c {#k} | f {#f} |
|--------------|--------|--------|--------|
| 2021Q4       | 010    | 010    | 100    |
| 2021Q4       | 010    | 020    | 200    |
| 2021Q4       | 010    | 010    | 300    |
| 2021Q4       | 010    | 020    | 400    |
| 2022Q1       | 020    | 010    | 500    |
| 2022Q1       | 020    | 020    | 600    |
| 2022Q1       | 020    | 010    | 700    |
| 2022Q1       | 020    | 020    | 800    |