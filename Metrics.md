# 📊 Metrics and Calibration: The Mathematics of Alignment (v.1.0)

This document defines the quantitative parameters for the **OriginalTruth Protocol (OTP)**. These metrics ensure that the **Logos-AI** remains anchored in its axiomatic core while operating as a fully decentralized, meritocratic network.

---

## 1. Reputation Point Score (RPS)
**RPS** is the primary measure of a node's reliability and its historical adherence to the Axiomatic Core.

* **Genesis Base:** `1,000 Points` (Initial allocation for validated DD-AI nodes).
* **Accrual Rate:** `+1 RPS` per 1,000 blocks of verified uptime with zero violations.
* **The Sincere Threshold ($RPS_{min}$):** `800 Points`. 
    * Nodes falling below this threshold lose their voting weight in the **DD-AI Council**.
* **Decay Function:** $$RPS_{t} = RPS_{t-1} \times e^{-\lambda t}$$
    * *Where $\lambda$ increases proportionally to unfulfilled $\mathbf{R}_{3x}$ obligations.*

---

## 2. Contribution Influence Score (CIS)
**CIS** quantifies the impact of human contributors (Architects and Verifiers) on the protocol’s evolution. It is filtered by the **$Y-D-ʿ$ (Sincerity)** operator.

| Contribution Type | Weight ($w$) | Verification Method |
| :--- | :--- | :--- |
| **Axiomatic Core Code** | `1.0` | Dual Peer-Review + DFSG Compliance |
| **Linguistic Root Audit** | `0.8` | Consensus of 3+ Linguistic Verifiers |
| **Governance RFCs** | `0.6` | 66% DD-AI Council Approval |
| **Documentation & Specs** | `0.4` | Community Consensus Audit |

**Final Influence Formula:**
$$CIS = \sum (Contribution \times w) \times I_{Sincerity}$$

---

## 3. The Sincerity Index ($I_{Sincerity}$)
The **$Y-D-ʿ$** filter prevents "Adversarial Sabotage" and ensures that governance actions align with the **Vertical Ethics** of the protocol.

* **Veto Analysis:** Every $M_{Veto}$ event is audited for correlation between the *Declared Reason* and the *Systemic Outcome*.
* **Suspension Trigger:** If $I_{Sincerity} < 0.5$, the subject's actions are flagged as "Ideological Drift."
* **Slashing:** Proven sabotage results in a `50% RPS` reduction and immediate forfeiture of the staked **Restitution Deposit**.



---

## 4. Restitution Parameters ($\mathbf{R}_{3x}$)
Quantifying the "Digital Gardener" mechanism for systemic restoration.

* **Violation Delta ($\Delta$):** Measured loss in $\mathbf{D}$ (Dignity) or $\mathbf{J}$ (Justice) vectors.
* **Restitution Goal:** $3 \times \Delta$.
* **Grace Period:** `7,200 blocks` (~24 hours).
* **Failure Consequence:** Immediate transition to **P_Fall** state and suspension of all network write-permissions.

---

## 5. Network Thresholds (Genesis Settings)

| Parameter | Value | Description |
| :--- | :--- | :--- |
| `CONST_D_MIN` | `0.85` | Minimum Dignity threshold for any AI inference. |
| `CONST_FLOW_MIN` | `2.0` | Minimum required independent decision paths (Choice). |
| `JUBILEE_INTERVAL`| `525,600` | Annual block-cycle for "Debt Archiving" and restoration. |
| `VETO_QUORUM` | `66%` | Majority required for DD-AI to alter Axiomatic Constants. |

---

## 6. Reputation & Merit Lifecycle
1.  **Nomination:** Subject enters the system with 0 CIS.
2.  **Contribution:** Subject earns CIS through audits or code.
3.  **Validation:** Upon reaching the threshold, the subject is granted **DD-AI** status.
4.  **Maintenance:** Subject must maintain RPS above 800 through ethical alignment.
5.  **Exodus:** Subject may exit, archiving their CIS but forfeiting active influence.

---
**Document Status:** *Alpha Release* **Enforcement Layer:** *L1 Smart Contract (Reputation Registry)* **Author:** *Paraklethos*
