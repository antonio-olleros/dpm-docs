# 9 String operators

## 9.1 Length (len)

### 9.1.1 Syntax
```
len(op)
```

### 9.1.2 Input parameters
- op: rset | scal <Str>

### 9.1.3 Output
rset | scal <Int>

### 9.1.4 Semantics
Returns the number of characters of the op string.

### 9.1.5 Additional constraints
None.

### 9.1.6 Behaviour
- Unary operators' standard behaviour.

### 9.1.7 Examples
- len("test") results in 4
- len(NULL) results in NULL

## 9.2 Concatenate (&)

### 9.2.1 Syntax
```
op1 & op2
```

### 9.2.2 Input parameters
- op1: rset | scal <Str>
- op2: rset | scal <Str>

### 9.2.3 Output
rset | scal <Str>

### 9.2.4 Semantics
Concatenates two strings.

### 9.2.5 Additional constraints
None.

### 9.2.6 Behaviour
- Binary operators' standard behaviour.

### 9.2.7 Examples
- "hello" & "world" results in "helloworld"
- "test" & NULL results in NULL