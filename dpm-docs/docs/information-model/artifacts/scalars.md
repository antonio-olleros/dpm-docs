# Scalars

Scalars are the simplest and most fundamental language artifacts in DPM-XL, representing individual values of a specific data type. They serve as the building blocks for more complex data structures and operations.

## Definition

**Scalars** are individual values of a certain *Data Type*.

Key characteristics:
- **Single value**: Represents exactly one data point
- **Typed**: Every scalar has a specific, well-defined data type
- **Atomic**: Cannot be decomposed into smaller parts within the language
- **Immutable**: Value and type are fixed once created

## Scalar Types

Scalars can be of any data type supported by DPM-XL:

### Numeric Scalars
```dpm-xl
100        # Integer scalar
3.14159    # Number scalar  
-42        # Negative integer scalar
0.5        # Decimal number scalar
```

### String Scalars
```dpm-xl
"Hello"           # String scalar
'World'           # String scalar (alternative quotes)
"Asset Class A"   # String with spaces
""                # Empty string scalar
```

### Boolean Scalars
```dpm-xl
true     # Boolean true scalar
false    # Boolean false scalar
```

### Temporal Scalars
```dpm-xl
#2023-12-31#     # Date scalar
#2023Q4#         # Time period scalar
#P1Y#            # Duration scalar (1 year)
```

### DPM Object Scalars
```dpm-xl
[item, eba_RT:x11]                    # Category item scalar
[subcategory, eba_CU:iso_currencies]  # Subcategory scalar
```

## Usage in Expressions

Scalars appear in expressions in several ways:

### **Literals**
Direct scalar values written in expressions:
```dpm-xl
{F_01.01, r0010, c0010} > 1000
#                         ^^^^ Scalar literal
```

### **Operation Results**
Many operations produce scalar results:
```dpm-xl
sum({F_20.05, r0020-0030, c0010})  # Produces a scalar sum
```

### **Extracted from Recordsets**
Scalars can be extracted from single-record recordsets:
```dpm-xl
{F_01.01, r0010, c0010}  # Single cell selection → scalar-like behavior
```

## Scalar Operations

### **Arithmetic Operations**
Scalars participate in standard arithmetic:
```dpm-xl
100 + 50           # Addition: produces 150
3.14 * 2           # Multiplication: produces 6.28
-5                 # Unary minus: produces -5
abs(-10)          # Absolute value: produces 10
```

### **Comparison Operations**
Scalars can be compared:
```dpm-xl
100 > 50          # Greater than: produces true
"abc" = "abc"     # String equality: produces true
#2023Q1# < #2023Q2#  # Date comparison: produces true
```

### **Logical Operations**
Boolean scalars support logical operations:
```dpm-xl
true and false    # Conjunction: produces false
not true          # Negation: produces false
```

### **Type Conversion**
Scalars can be cast between compatible types:
```dpm-xl
cast(100, "string")    # Integer to string: produces "100"
cast("3.14", number)   # String to number: produces 3.14
```

## Special Scalar Values

### **Null Values**
Every data type includes the special value `null`:
- Represents "no value" or "missing value"
- Behaves according to three-valued logic in boolean operations
- Propagates through most arithmetic operations

```dpm-xl
100 + null        # Produces null
null > 50         # Produces null
null and true     # Produces null
```

### **Empty String**
For string types, `null` is equivalent to the empty string:
```dpm-xl
null = ""         # true for string context
```

## Scalar Validation

Scalars must satisfy data type constraints:

### **Numeric Constraints**
```dpm-xl
sqrt(-1)          # Runtime error: negative square root
10 / 0            # Runtime error: division by zero
```

### **Temporal Constraints**
```dpm-xl
#2023-02-30#      # Invalid date
#2023Q5#          # Invalid quarter
```

### **Reference Constraints**
```dpm-xl
[item, invalid_code]  # Error: item does not exist
```

## Performance Characteristics

Scalars offer optimal performance characteristics:

### **Memory Efficiency**
- Minimal memory footprint
- Direct value storage without overhead
- Efficient copying and passing

### **Computational Speed**
- Direct CPU operations
- No indirection or lookup costs
- Optimal for mathematical calculations

### **Cache Friendliness**
- Small size enables efficient caching
- Good CPU cache utilization
- Fast access patterns

## Implementation Guidelines

### **Value Storage**
Implement scalars as direct value storage:
```pseudo
class Scalar {
    DataType type;
    Value value;        // Union of all possible value types
    boolean isNull;
}
```

### **Type Safety**
Enforce type constraints at runtime:
- Validate operations match type requirements
- Perform explicit casting where allowed
- Fail fast on type errors

### **Null Handling**
Implement consistent null propagation:
- Most operations return null if any operand is null
- Comparison operations handle null according to three-valued logic
- Aggregation operations typically ignore nulls

## Examples in Context

### **Simple Validation**
```dpm-xl
{F_01.01, r0010, c0010} = 100
#                         ^^^ Scalar literal for comparison
```

### **Calculation with Constants**
```dmp-xl
{F_01.01, r0010, c0010} * 0.8 + 1000
#                         ^^^   ^^^^ Scalar constants
```

### **Conditional Logic**
```dpm-xl
if {F_01.01, r0010, c0010} > 0 then 1 else 0
#                             ^        ^    ^ Scalar values
```

---

!!! note "Scalar Behavior with Recordsets"
    When scalars are used with recordsets in binary operations, the scalar is conceptually "broadcast" to match each record in the recordset. This enables operations like:
    
    ```dpm-xl
    {F_01.01, r0010-0020, c0010} * 1.1  # Multiply each record by 1.1
    ```