# Scalar Sets

Scalar Sets are collections of scalar values that share the same data type. They are primarily used for membership operations and set-based comparisons in DPM-XL expressions.

## Definition

**Scalar Sets** are sets of *Scalar* values defined on the same *Data Type*.

Key characteristics:
- **Homogeneous**: All values must be of the same data type
- **Unordered**: No inherent ordering (though may be sorted for efficiency)
- **Unique**: Typically contain unique values (set semantics)
- **Finite**: Always contain a finite number of elements

## Primary Usage

Scalar Sets are **typically used with the *in* operator** for membership testing:

```dpm-xl
{F_40.01, c0015}[where TYC in {"LEI", "ISIN", "MIC"}]
#                              ^^^^^^^^^^^^^^^^^^^^ Scalar set
```

## Syntax and Creation

### **Literal Sets**
Created using curly brace syntax with comma-separated values:

```dpm-xl
{1, 2, 3, 4, 5}              # Integer set
{"ES", "PT", "DE", "FR"}     # String set
{true, false}                # Boolean set
{#2023Q1#, #2023Q2#}         # Time period set
```

### **Type Consistency**
All elements must be of the same type:
```dpm-xl
{1, 2, 3}           # ✓ Valid: all integers
{"A", "B", "C"}     # ✓ Valid: all strings
{1, "A", true}      # ✗ Invalid: mixed types
```

### **Empty Sets**
Empty sets are valid and type-neutral:
```dpm-xl
{}                  # Empty set (type determined by context)
```

## Data Type Support

Scalar Sets can be created for any DPM data type:

### **Numeric Sets**
```dpm-xl
{100, 200, 300}                    # Integer set
{1.5, 2.7, 3.14159}               # Number set
{-10, 0, 10}                      # Mixed positive/negative integers
```

### **String Sets**
```dmp-xl
{"Active", "Inactive", "Pending"}  # Status codes
{"EUR", "USD", "GBP"}             # Currency codes
{"High", "Medium", "Low"}         # Risk categories
```

### **Temporal Sets**
```dpm-xl
{#2023Q1#, #2023Q2#, #2023Q3#, #2023Q4#}    # Quarterly periods
{#2023-01-01#, #2023-06-30#, #2023-12-31#}  # Specific dates
```

### **Category Item Sets**
```dpm-xl
{[item, "code1"], [item, "code2"], [item, "code3"]}  # Category items
```

## Operations with Scalar Sets

### **Membership Testing**
The primary operation is membership testing with `in`:
```dpm-xl
"EUR" in {"EUR", "USD", "GBP"}     # true
100 in {200, 300, 400}             # false
```

### **Negated Membership**
Test for non-membership:
```dpm-xl
not ("JPY" in {"EUR", "USD", "GBP"})  # true
```

### **With Recordsets**
Most commonly used to filter recordsets:
```dmp-xl
{F_20.05, r0020-0030, c0010}[where CNT in {"ES", "PT", "DE"}]
```

## Advanced Usage Patterns

### **Dynamic Filtering**
```dpm-xl
# Filter records based on predefined country set
with {F_20.05}:
    {r0020-0030, c0010}[where CNT in {"ES", "PT", "IT", "FR"}]
```

### **Multi-Condition Filtering**
```dpm-xl
# Multiple set-based conditions
{F_40.01, c0031}[where 
    TYC in {"LEI", "ISIN"} and 
    STC in {"Active", "Inactive"}
]
```

### **Exclusion Patterns**
```dpm-xl
# Select records NOT in specified set
{F_20.05, r0020-0030, c0010}[where not (CNT in {"EX1", "EX2"})]
```

## Null Handling

Scalar Sets can contain null values:

```dpm-xl
{null, "A", "B"}     # Set containing null
null in {null, 1, 2} # true
```

### **Null Propagation**
```dpm-xl
null in {"A", "B"}   # null (three-valued logic)
```

## Performance Considerations

### **Set Size**
- Small sets (< 10 elements): Linear search is efficient
- Large sets: May require hash-based implementation
- Very large sets: Consider alternative approaches

### **Type Optimization**
Different data types may have different optimal implementations:
- **Integers**: Bit sets for small ranges
- **Strings**: Hash sets or tries
- **Temporal**: Range-based optimizations

### **Membership Testing**
Frequent membership testing benefits from:
- Hash-based lookup structures
- Sorted arrays with binary search
- Bloom filters for very large sets

## Implementation Guidelines

### **Storage Strategy**
```pseudo
class ScalarSet {
    DataType elementType;
    Set<Value> values;      // Hash set for O(1) lookup
    
    boolean contains(Value v) {
        return values.contains(v);
    }
}
```

### **Type Validation**
Enforce type homogeneity:
```pseudo
void addValue(Value v) {
    if (elementType == null) {
        elementType = v.getType();
    } else if (!v.getType().isCompatibleWith(elementType)) {
        throw new TypeError("Incompatible type in scalar set");
    }
    values.add(v);
}
```

### **Optimization Opportunities**
- **Immutable sets**: Can be pre-optimized and cached
- **Static sets**: Compile-time optimization for literal sets
- **Set intersection**: Optimize multiple membership tests
- **Range sets**: Special handling for numeric ranges

## Common Patterns

### **Regulatory Code Lists**
```dpm-xl
# Country codes for EU member states
{"AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR", 
 "DE", "GR", "HU", "IE", "IT", "LV", "LT", "LU", "MT", "NL", 
 "PL", "PT", "RO", "SK", "SI", "ES", "SE"}
```

### **Asset Class Categories**
```dpm-xl
# High-risk asset classes
{"Derivatives", "Structured Products", "Commodities", "Alternative Investments"}
```

### **Reporting Periods**
```dpm-xl
# Quarterly reporting periods for current year
{#2023Q1#, #2023Q2#, #2023Q3#, #2023Q4#}
```

### **Status Codes**
```dpm-xl
# Valid loan statuses
{"Performing", "Non-performing", "Defaulted", "Written-off"}
```

## Error Conditions

### **Type Mismatch**
```dpm-xl
{1, 2, "three"}     # Error: mixed integer and string types
```

### **Invalid Values**
```dpm-xl
{#2023-02-30#}      # Error: invalid date in set
```

### **Malformed Syntax**
```dpm-xl
{1, 2, 3,}          # Error: trailing comma (depending on implementation)
```

## Interaction with Subcategories

Scalar Sets can reference DPM subcategories for predefined sets:
```dpm-xl
[subcategory, eba_CU:iso_currencies]  # References predefined currency codes
```

This provides:
- **Standardization**: Use official code lists
- **Maintenance**: Centrally managed sets
- **Validation**: Automatic validation against official values

## Best Practices

### **Readability**
Use meaningful groupings and formatting:
```dpm-xl
# Good: Clearly grouped and formatted
{
    "High Risk Asset Classes": {"Derivatives", "Commodities", "Alternatives"},
    "Medium Risk": {"Equities", "Corporate Bonds"},
    "Low Risk": {"Government Bonds", "Cash"}
}

# Better: Use sets for membership testing
where AssetClass in {"Derivatives", "Commodities", "Alternatives"}
```

### **Maintainability**
For frequently used sets, consider referencing subcategories:
```dpm-xl
# Instead of hardcoding:
where Country in {"ES", "PT", "IT", "FR"}

# Use subcategory reference:
where Country in [subcategory, eu_southern_countries]
```

### **Performance**
For large sets used frequently, consider implementation optimizations:
- Use hash-based lookups for string sets
- Use bit vectors for small integer ranges
- Cache compiled sets for repeated use

## Examples in Context

### **Multi-Table Validation**
```dpm-xl
# Ensure consistent currency usage across tables
with {c0010}:
    {F_01.01, r0010}[where CUR in {"EUR", "USD"}] = 
    {F_02.01, r0010}[where CUR in {"EUR", "USD"}]
```

### **Conditional Aggregation**
```dpm-xl
# Sum only for specific countries
sum({F_20.05, r0020-0030, c0010}[where CNT in {"ES", "PT", "IT"}])
```

### **Complex Filtering**
```dpm-xl
# Multiple set-based conditions
{F_40.01, c0031}[where 
    LIN in {"123456", "789012"} and
    TYC in {"LEI", "ISIN"} and
    not (STC in {"Inactive", "Suspended"})
]
```

---

!!! tip "Performance Tip"
    For sets used in multiple expressions, consider:
    
    1. **Subcategory references** for standardized code lists
    2. **Compilation optimization** for frequently used literal sets  
    3. **Indexing strategies** in the underlying data for common membership tests