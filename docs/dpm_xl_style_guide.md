# DPM-XL Documentation Style Guide

## Purpose

This style guide ensures consistency across all DPM-XL documentation by establishing clear rules for capitalization, italics usage, and terminology.

## Core Principles

1. **Model classes and concepts should be clearly distinguished from general usage**
2. **Consistency across all documentation files is mandatory**
3. **Technical precision should not compromise readability**

## Capitalization Rules

### Model Classes (Always Capitalized + Italics)

Use capitalization and italics for all formal model classes and their instances:

✅ **Correct:**
- *Operation*
- *Recordset*
- *Scalar*
- *Variable*
- *Component*
- *Key Component*
- *Fact Component*
- *Attribute Component*
- *Operator*
- *Operand*
- *Record*
- *Structure*
- *Artifact*
- *Key*
- *Key Variable*
- *Attribute Variable*

❌ **Incorrect:**
- operation (when referring to the model class)
- recordset
- scalar
- variable
- component

### Data Types (Always Capitalized)

Use capitalization for formal data types:

✅ **Correct:**
- String
- Number
- Integer
- Boolean
- Date
- Time
- Time Period
- Time Interval

❌ **Incorrect:**
- string (when referring to the data type)
- number
- boolean

### Technical Concepts (Capitalize when referring to the formal concept)

✅ **Correct:**
- "The Selection *Operator* is used..." (formal concept)
- "this selection operation..." (general usage)
- "DPM *Operations* are expressions..." (formal concept)
- "the operation fails..." (general usage)

## Italics Usage Rules

### Always Use Italics For:

1. **Model Classes**: *Operation*, *Recordset*, *Scalar*
2. **Formal Concepts**: *Key*, *Fact*, *Attribute*
3. **Language Elements**: *Operator*, *Operand*, *Variable*

### Never Use Italics For:

1. **Data Types**: String, Number, Boolean (capitalized but not italicized)
2. **Technical terms in general usage**: "this operation", "the result"
3. **Code examples**: `{tF_01.01, r0010, c0010}`

## Specific Terminology

### Operator vs Operation
- **Operation**: The entire expression or calculation
- **Operator**: The specific symbol or function (e.g., +, sum, max)

✅ **Correct:**
- "An *Operation* uses several *Operators*"
- "The addition *Operator* (+) is binary"

### Recordset vs Record
- **Recordset**: The entire collection/table
- **Record**: Individual row within a *Recordset*

✅ **Correct:**
- "The *Recordset* contains multiple *Records*"
- "Each *Record* has *Key Components*"

### Variable vs variable
- **Variable**: DPM model concept (capitalized + italics)
- **variable**: General programming concept (lowercase)

✅ **Correct:**
- "The DPM *Variable* represents..."
- "Set this variable to null"

## Examples

### Before (Inconsistent):
```
The recordset contains records that have key components and a fact component. 
Each operation uses operators to process variables and produce results.
The scalar values are defined on data types like string or number.
```

### After (Consistent):
```
The *Recordset* contains *Records* that have *Key Components* and a *Fact Component*.
Each *Operation* uses *Operators* to process *Variables* and produce results.
The *Scalar* values are defined on *Data Types* like String or Number.
```

## Section Headers

Use consistent capitalization for section headers:

✅ **Correct:**
- "Key Components"
- "Fact Component" 
- "Data Types"
- "Binary Operators"

❌ **Incorrect:**
- "key components"
- "fact component"
- "data types"

## Table Headers and Content

In tables, maintain consistency with the style guide:

✅ **Correct:**
| *Component* Type | *Data Type* | Description |
|------------------|-------------|-------------|
| *Key Component*  | String      | Identifies the *Record* |
| *Fact Component* | Number      | Contains the measured value |

## Quality Checklist

Before publishing any documentation:

- [ ] All model classes use capitalization + italics
- [ ] Data types are capitalized but not italicized  
- [ ] Terminology is consistent throughout the document
- [ ] Section headers follow capitalization rules
- [ ] Tables maintain style consistency
- [ ] Code examples are properly formatted

## Automated Checks

Consider implementing these automated checks:

1. **Search for lowercase model terms**: recordset, operation, variable, component
2. **Check for inconsistent italics**: *recordset* vs Recordset
3. **Verify data type capitalization**: string → String, number → Number

## Common Mistakes to Avoid

1. **Mixed capitalization**: "The recordset contains Records" 
2. **Missing italics**: "The Operation uses operators"
3. **Inconsistent data types**: "string values" instead of "String values"
4. **General vs specific usage**: Using *Operation* when meaning general operation

## File-by-File Application

This style guide should be applied consistently across:

- Information Model documents
- Operator specifications  
- Grammar documentation
- Examples and tutorials
- API documentation
- Error messages and logs

## Version Control

- Document version: 1.0
- Last updated: [Current Date]
- Review cycle: With each major documentation update

This style guide serves as the definitive reference for maintaining consistency in DPM-XL documentation.