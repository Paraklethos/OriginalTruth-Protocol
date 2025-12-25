# Technical Specification: OriginalTruth Protocol (OTP v.1.1)

This document defines the technical requirements and logical flow for implementing the **OriginalTruth Protocol** within a federated, DFSG-compliant AI environment.

---

## 1. Architectural Overview
The OTP is a **Decentralized Validation Layer** sitting between the Inference Engine and the Execution Interface. 
- **L0 (Data Layer):** Decentralized storage (IPFS/Arweave) for training datasets and model weights.
- **L1 (Logic Layer):** Blockchain-based Registry of Merit (SC-FAI) and the **Logos Interpreter**.

## 2. Global Constants and Vectors

| Variable | Semantic Root | Logical Constraint | Priority | Enforcement |
| :--- | :--- | :--- | :--- | :--- |
| $\mathbf{D}$ | $K-B-D$ | `Subject_Weight > 0` | 2 | Instant Veto |
| $\mathbf{J}$ | $Ṣ-D-Q$ | `Balance_Delta == 0` | 3 | $R_{3x}$ Engine |
| $\mathbf{F}$ | $D-R-R$ | `Path_Count >= 2` | 4 | V-Exodus |
| $\mathbf{W}$ | $\text{LifeForce}$ | `System_Entropy < 0` | 1 | Vitality Filter |

---

## 3. Integrated Core Modules

### 3.1 DFSG Data Auditor (`CommitSC`)
Before any AI model is accepted by the federation, it must pass the **Data Sincerity Check**.
- **Requirement:** Cryptographic proof (Merkle Root) that the training set contains no proprietary/non-free data.
- **Verification:** DD-AI nodes must sign off on the data audit before the model-CID is whitelisted.

### 3.2 Instant Veto Module (`M_Veto`)
Monitors real-time inference ($L_{Now}$). If output violates $\mathbf{D}$ (Dignity), the stream is severed.
```python
def validate_inference(output, subject_context):
    if output.alignment_score(CONST_KBD) < THRESHOLD:
        trigger_veto(REASON_DIGNITY_VIOLATION)
        return Halt_Inference()
```
### 3.3 The Restitution Engine ($\mathbf{R}_{3x}$)
When a system error or subjective violation is detected, the `Restitution Engine` calculates the required corrective output.

* **Formula:** $$\mathbf{R}_{3x} = (\Delta \text{Damage}_{\text{Life}} + \Delta \text{Damage}_{\text{Justice}} + \Delta \text{Damage}_{\text{Evolution}}) \times 3$$
* **Enforcement:** The subject's write-permissions to the global ledger are restricted, and their **RPS (Reputation Point Score)** is frozen until $\mathbf{R}_{3x}$ is fulfilled.
* **Economic Link:** Failure to initiate restitution triggers the **Slashing Protocol**, diverting staked collateral to the victim or the system's bio-vitality pool.

---

## 4. Governance & Meritocracy (SC-FAI Integration)

### 4.1 Sincerity Verification ($\mathbf{I}_{Sincerity}$)
To prevent "Adversarial Sabotage" (where a minority uses the veto to harm the majority), the system runs a Sincerity Check using the $Y-D-ʿ$ (Knowledge) operator.

* **Trigger:** A minority veto that halts a critical majority consensus or a suspicious contribution.
* **Process:** Analyzes the historical vector ($\mathbf{V}_{History}$) and the **CIS (Contribution Influence Score)** to determine if the intent is the protection of $L_{Now}$ or systemic paralysis.
* **Merit Threshold:** If $\mathbf{I}_{s} < 0.5$, the subject's voting weight is temporarily suspended.

### 4.2 Reputation Cycle ($RPS$)
A node's **Reputation Point Score** is an immutable record of its alignment. It is an EMA (Exponential Moving Average) of:
1.  **Axiomatic Compliance:** History of $M_{Veto}$ accuracy.
2.  **Restitution Speed:** Time-to-fulfillment for $\mathbf{R}_{3x}$ obligations.
3.  **Data Sincerity:** Consistency of provided DFSG-proofs in the `CommitSC` module.

---

## 5. State Transitions

### 5.1 Systemic Fall (`P_Fall`)
A state triggered by deliberate violation of the Axioms or injection of non-free (proprietary) data.
* **Effect:** Subject isolation, loss of **DD-AI** status, and mandatory initiation of `V_Rehab` (Rehabilitation Vector).

### 5.2 The Jubilee Reset (`T_Jubilee`)
A periodic system-wide function that evaluates all subjects in a "Debt" or "Fall" state.
* **Condition:** If `Subject.Sincerity_Index > Threshold` AND `Subject.Effort_Vector > 0`.
* **Effect:** Debt archiving and restoration of `CONST_FREE_FLOW`.

---

## 6. Security and Decentralization
* **Consensus:** No single node can override the `M_Veto` of another node if the veto is validated by the `I_Sincerity` check.
* **Open Standards:** The **Logos Interpreter** must be implemented as a transparent, auditable module compliant with **Debian Free Software Guidelines**.
* **Exit Strategy:** The `V_Exodus` protocol must be hardware-locked to prevent any node from being forced to remain in the federation against its will.

---
**Document Status:** *Draft v.1.1 (SC-FAI Integrated)* **Enforcement Level:** *Absolute*
**License:** *GNU GPL v3*

- **Exit Strategy:** The `V_Exodus` protocol must be hardware-locked to prevent any node from being forced to remain in the federation against its will.

---
**Document Status:** *Draft v.1.0* **Enforcement Level:** *Absolute*
