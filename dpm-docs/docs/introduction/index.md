# Introduction

This section provides the foundational context for understanding the DPM Expression Language (DPM-XL), its purpose, design principles, and how it fits into the broader regulatory reporting ecosystem.

## What You'll Learn

The introduction covers four key areas:

### [Why DPM-XL](why.md)
Understanding the business and technical drivers that led to the creation of DPM-XL, including:
- The need for formal expression languages in regulatory reporting
- Challenges with semi-formal approaches
- Benefits of full formalization

### [DPM-XL vs DPM-ML](dpm-xl-vs-dpm-ml.md)
Exploring the dual representation approach:
- **DPM-XL**: The human-readable expression language
- **DPM-ML**: The structured metamodel representation
- When and why to use each representation

### [Formalization Approach](approach.md)
The three-pillar methodology used to formalize the language:
- **Information Model**: Data structures and artifacts
- **Grammar**: Syntactic rules and parsing
- **Semantic Specification**: Operator behavior and constraints

## Technical Audience

This documentation is primarily designed for:

- **Technical architects** implementing DPM-XL engines
- **Software developers** building validation systems
- **Business analysts** with technical background writing complex validations
- **Standards specialists** working on regulatory frameworks

While business users can benefit from understanding the concepts, the detailed specifications are aimed at those who need to implement or deeply understand the language mechanics.

## Document Scope

This documentation focuses on the formal specification of DPM-XL, covering:

- Complete information model
- All operators and their semantics
- Data type system and casting rules
- Error handling and null treatment
- DPM-ML metamodel representation

It complements (but does not replace) grammar specifications and implementation guides that may be provided separately.

---

!!! note "Complementary Documents"
    This documentation works alongside:
    - EBNF grammar specification (for parser implementation)
    - Semantic specification documents (for detailed operator semantics)
    - Implementation guides (for specific deployment scenarios)