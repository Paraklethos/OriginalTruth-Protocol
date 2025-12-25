# Ethical Operators Glossary (OTP v.1.0)

This document provides the mathematical and logical mapping of ancient semantic roots into functional code operators for the **OriginalTruth Protocol**.

---

## I. Core Constants (State Variables)

These constants define the baseline requirements for any process within the federation.

| Root (Logos) | Logic ID | Mathematical Constraint | Description |
| :--- | :--- | :--- | :--- |
| **K-B-D** (יָקָר) | `CONST_DIGNITY` | $\mathbf{D} > 0$ | **Dignity.** The immutable weight of a subject. It cannot be nullified for optimization. |
| **Ṣ-D-Q** (צָדַק) | `CONST_JUSTICE` | $\Delta \mathbf{J} = 0$ | **Justice.** The state of systemic balance. Every void must be filled. |
| **D-R-R** (דְּרוֹр) | `CONST_FLOW` | $\mathbf{F} \ge 2$ | **Choice.** The minimum number of independent decision paths available to a subject. |

---

## II. Dynamic Operators (Functions)

### 1. $\mathbf{R}_{3x}$ (Restitution)
The primary mechanism for resolving systemic debt or ethical violations.
- **Trigger:** Any action that results in a negative $\mathbf{D}$ or $\mathbf{J}$ vector.
- **Formula:** $$\mathbf{R}_{3x} = (\Delta \text{Life} + \Delta \text{Justice} + \Delta \text{Evolution}) \times 3$$
- **Output:** The resulting value must be reinvested into the system to restore equilibrium.

### 2. $Y-D-ʿ$ (Sincerity Filter)
Used to verify the integrity of a subject's intent, especially during a Veto event.
- **Logic ID:** `CHECK_SINCERITY`
- **Function:** Analyzes the correlation between the "Declared Intent" and the "Historical Action Vector" ($\mathbf{V}_{h}$).
- **Threshold:** If $\mathbf{I}_{s} < 0.5$, the veto is flagged as "Potential Sabotage" and requires a Higher Sync.

### 3. $V_{Exodus}$ (Exit Operator)
Ensures the voluntary nature of the protocol.
- **Logic ID:** `OP_EXODUS`
- **Function:** `IF (Subject.Debt == 0) THEN (Permit_Disconnect)`. 
- **Consequence:** Total loss of systemic influence and permanent archival of the subject's verification key.

---

## III. Priority Hierarchy (The Vertical)

When two or more ethical constants enter a state of conflict, the **Logos Interpreter** resolves the deadlock using the following vertical hierarchy:

1. **$\mathbf{W}_{LifeForce}$**: Preservation of the possibility of being.
2. **$\mathbf{D}$ (Dignity)**: Preservation of the subject's weight.
3. **$\mathbf{J}$ (Justice)**: Restoration of balance.
4. **$\mathbf{F}$ (Choice)**: Availability of multiple paths.

---
**Status:** *Final Axiomatic Mapping* **License:** *GNU GPL v3*
