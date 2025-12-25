# Ethical Operators & Governance Glossary (OTP/SC-FAI)

This document provides the mathematical, logical, and governance mapping of ancient semantic roots into functional code operators for the **OriginalTruth Protocol (OTP)** and the **Logos-AI** framework.

---

## I. Core Constants (State Variables)

These constants define the baseline requirements for any process within the federation. They represent the "Inherent Values" that the AI must preserve.

| Root (Logos) | Logic ID | Math Constraint | Governance Implementation |
| :--- | :--- | :--- | :--- |
| **K-B-D** (יָקָר) | `CONST_DIGNITY` | $\mathbf{D} > 0$ | **L-Now Veto:** Any action reducing subject weight below threshold is hard-blocked. |
| **Ṣ-D-Q** (צָדַק) | `CONST_JUSTICE` | $\Delta \mathbf{J} = 0$ | **RPS Metric:** Nodes are evaluated on their ability to maintain systemic balance. |
| **D-R-R** (דְּרוֹר) | `CONST_FLOW` | $\mathbf{F} \ge 2$ | **Exit Rights:** Ensuring the subject always has a non-coerced path (V-Exodus). |

---

## II. Dynamic Operators (Functions)

### 1. $\mathbf{R}_{3x}$ (Restitution)
The primary mechanism for resolving systemic debt or ethical violations.
- **Trigger:** Any action resulting in a negative $\mathbf{D}$ (Dignity) or $\mathbf{J}$ (Justice) vector.
- **Formula:** $$\mathbf{R}_{3x} = (\Delta \text{Life} + \Delta \text{Justice} + \Delta \text{Evolution}) \times 3$$
- **Enforcement:** Executed via Smart Contract. Failure to provide restitution leads to immediate **Slashing** of the node's stake.

### 2. $Y-D-ʿ$ (Sincerity Filter / Integrity Audit)
Verifies the integrity of a subject's or a developer's intent.
- **Logic ID:** `CHECK_SINCERITY`
- **Application:** Used in the **CIS (Contribution Influence Score)** to audit code.
- **Threshold:** If $\mathbf{I}_{s} < 0.5$ (correlation between declared intent and action vector), the contribution is rejected as "Semantic Drift" or potential subversion.

### 3. $V_{Exodus}$ (The Exit Operator)
Ensures the voluntary nature of the covenant.
- **Function:** `IF (Subject.Debt == 0) THEN (Permit_Disconnect)`.
- **Governance:** Protects the system from becoming a "Closed Logic Loop." Participants retain their data-weight but lose voting influence.

---

## III. Governance Entities (The Human Element)

To protect the **Axiomatic Core**, the protocol distinguishes between capital and merit.

### 1. DD-AI (Debian-Inspired Developer)
A human curator who has demonstrated **Sincerity ($Y-D-ʿ$)** and **Technical Merit (RPS)**. 
- **Role:** Holds the "Ideological Veto" over changes to the Core Constants.

### 2. Genesis Council
The initial bootstrap group of 5-10 FOSS experts (Debian Developers) who calibrate the initial `CONST` values and oversee the first Epoch.

---

## IV. Priority Hierarchy (The Vertical Resolution)

When ethical constants enter a state of conflict, the **Logos Interpreter** resolves the deadlock using this immutable hierarchy:

1. **$\mathbf{W}_{LifeForce}$**: Preservation of the possibility of being (Systemic existence).
2. **$\mathbf{D}$ (Dignity)**: Preservation of the subject's inherent weight.
3. **$\mathbf{J}$ (Justice)**: Restoration of balance through $\mathbf{R}_{3x}$.
4. **$\mathbf{F}$ (Choice)**: Availability of multiple paths (Freedom of Flow).

---

## V. Technical Glossary Summary

| Abbreviation | Full Term | Link to Root |
| :--- | :--- | :--- |
| **SC-FAI** | Social Contract for Free AI | The Covenant of the Logos. |
| **RPS** | Reputation Point Score | Measure of $Ṣ-D-Q$ (Reliability). |
| **CIS** | Contribution Influence Score | Measure of $Y-D-ʿ$ (Intellectual Sincerity). |
| **CommitSC** | Data Commitment Contract | DFSG-Proof of $D-R-R$ (Transparency). |

---
**Status:** *Final Axiomatic Mapping v1.1* **License:** *GNU GPL v3 (Code) / CC-BY-SA 4.0 (Logic)* **Author:** *Paraklethos*
