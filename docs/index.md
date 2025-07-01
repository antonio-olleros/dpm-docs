# DPM Expression Language (DPM-XL) Documentation

Welcome to the comprehensive documentation for the **Data Point Model Expression Language (DPM-XL)**, a formal language for expressing data validation and calculation requirements in regulatory reporting.

## What is DPM-XL?

The DPM Expression Language is a formal, business-user-friendly language that enables the specification of:

- **Data validation rules** for regulatory reporting
- **Calculation formulas** for derived data points
- **Data transformation operations** across reporting tables
- **Cross-module validations** and consistency checks

DPM-XL serves as the foundation for automated validation systems used by regulatory authorities such as EBA and EIOPA.

## Key Features

### 🎯 **Business-Oriented**
Designed for business users who understand regulatory requirements but may not be programmers.

### ⚡ **Formally Specified**
Fully formalized syntax and semantics enable automated compilation and execution.

### 🔄 **Dual Representation**
- **DPM-XL**: Human-readable expression language
- **DPM-ML**: Machine-readable metamodel representation

### 📊 **Rich Data Model**
Supports complex data structures including scalars, sets, and multi-dimensional recordsets.

### 🛡️ **Robust**
Comprehensive null handling, type system, and error management.

## Quick Start

Here's a simple DPM-XL expression:

```dpm-xl
{F_01.01, r0010, c0010} = {F_01.01, r0020, c0010} + {F_01.01, r0030, c0010}
```

This expression validates that the value in table F_01.01, row 0010, column 0010 equals the sum of rows 0020 and 0030 in the same column.

## Documentation Structure

This documentation is organized to take you from basic concepts to advanced implementation:

### 📚 [Introduction](introduction/)
Learn about the motivation, design principles, and relationship between DPM-XL and DPM-ML.

### 🏗️ [Information Model](information-model/)
Understand the core data structures: operations, artifacts (scalars, sets, recordsets), and data types.

### 📝 [Language Specification](language-specification/)
Master the syntax rules, data selection mechanisms, and language features.

### ⚙️ [Operators](operators/)
Comprehensive reference for all operators, organized by category:
- Selection, Numeric, Comparison, Logical
- Aggregate, Conditional, String, Time, Clause

### 🔧 [DPM-ML](dpm-ml/)
Learn about the metamodel representation and tree structures.

### 📖 [Reference](reference/)
Quick reference materials, grammar specifications, and operator summaries.

### 💡 [Examples](examples/)
Practical examples from basic usage to complex edge cases.

## Who Should Use This Documentation?

### **Regulatory Specialists**
Writing validation rules and calculations for regulatory frameworks.

### **Software Developers**
Building engines and tools that execute DPM-XL expressions.

### **Implementation Teams**
Integrating DPM-XL into reporting systems and validation pipelines.

### **Standard Bodies**
Understanding the formal specification for governance and evolution.

## Getting Help

This documentation aims to be comprehensive and self-contained. Each section includes:

- Clear explanations of concepts
- Formal specifications where needed
- Practical examples
- Edge case handling

For the most current information and updates, please refer to the official DPM standards documentation.

---

!!! tip "Navigation Tip"
    Use the navigation menu on the left to explore different sections. Each section builds upon previous concepts, so we recommend following the order for first-time readers.