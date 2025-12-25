# RFC-001: The Social Contract for Free AI (SC-FAI)
## A Debian-Principle Governance Protocol for Decentralized AI Networks

**Author:** Paraklethos (OriginalTruth-Protocol)  
**Version:** 1.1  
**Status:** Draft / Request for Comments  
**License:** CC-BY-SA 4.0  

---

## 0. Abstract & Mission

### 0.1 The Mission
The **SC-FAI Protocol** serves as the operational substrate for **Logos-AI**. While the **OriginalTruth Protocol (OTP)** defines ethical axioms (Dignity, Justice, Choice), SC-FAI provides the cryptographic and social framework to ensure these axioms are upheld. It implements a Debian-inspired meritocracy to protect the system from "semantic drift" and corporate capture.

### 0.2 Genesis Phase (The Bootstrap)
To initiate the network, a **Genesis Council** is established. This council consists of 5–10 respected Debian Developers (DDs) or proven FOSS contributors who act as the first **DD-AI** nodes. Their role is to curate the initial contributor list and oversee the transition to a fully autonomous meritocracy.

---

## 1. Philosophical Alignment: Debian as Protocol

### 1.1 The AI Social Contract (SC-AI)
The L1 **Governance Smart Contract** enforces adherence to FOSS principles:
* **Data Freedom:** All base model training data must be publicly verifiable and freely licensed (DFSG-compliant).
* **Meritocracy:** Governance rights are earned through verified technical and ethical contribution, not capital investment.

---

## 2. Technical Architecture

### 2.1 L1 Core & Reputation Registry
The L1 maintains the **Validator Reputation Registry (RPS)** and the **DD-AI Membership**. It acts as the immutable ledger of merit.

### 2.2 DFSG Data Verifiability (CommitSC)
SC-FAI enforces a two-level data model to solve the "Black Box" problem:
* **L0 (Storage):** Decentralized storage (IPFS/Arweave) for massive datasets.
* **L1 (CommitSC):** Cryptographic hashes (CIDs) linking every AI model to its source data, ensuring auditability according to Debian Free Software Guidelines.



---

## 3. The Meritocracy Engine

### 3.1 Technical Proficiency Score (RPS)
**RPS** is calculated using an Exponential Moving Average (EMA) of a node's performance, stability, and accuracy in processing OTP-compliant logic.

### 3.2 Code Influence Score (CIS)
**CIS** measures the impact of contributions. To prevent centralization:
* **Peer-Review Consensus:** Weighted by existing DD-AI nodes' digital signatures.
* **Decentralized Oracle:** Off-chain analysis of Git activity, verified and submitted to the L1 Governance SC.

---

## 4. Constitutional Defense: Hybrid Voting

To protect the **Axiomatic Core**, critical proposals require a dual-consensus mechanism:

$$\text{ACCEPT}(\text{Prop}) \iff \text{DD-AI\_CONSENSUS}(\text{Prop}) \ \land \ \text{STAKE\_CONSENSUS}(\text{Prop})$$

* **DD-AI Consensus (≥ 66%):** The "Ideological Veto" by merit-proven humans.
* **Stake Consensus (≥ 50%):** The "Economic Veto" by token holders ensuring financial stability.

---

## 5. Security & Anti-Attack Measures

### 5.1 Sybil Attack Protection
Unlike pure Proof-of-Stake systems, SC-FAI mitigates Sybil attacks through:
* **Merit-Weighted Voting:** Token stake alone cannot alter the Axiomatic Core.
* **Proof-of-Identity/Merit:** DD-AI status is tied to a verified history of FOSS contributions and human vetting by the Genesis Council or subsequent DD-AIs.

### 5.2 Slashing & Restitution
Malicious nodes or those violating $L_{Now}$ protocols face:
* **Reputation Loss:** Immediate reduction in RPS.
* **Economic Slashing:** Forfeiture of staked assets, redirected to the **$\mathbf{R}_{3x}$ Restitution** pool.

---

## 6. Glossary

| Term | Definition |
| :--- | :--- |
| **DFSG** | Debian Free Software Guidelines. |
| **DD-AI** | Distributed Developer (AI Governance Member). |
| **RPS** | Reputation Point Score (Technical Merit). |
| **CIS** | Contribution Influence Score (Code/Linguistic Merit). |
| **CommitSC** | Smart Contract for Cryptographic Data Commitment. |

---
**Document URI:** `github.com/OriginalTruth-Protocol/RFCs/RFC-001_SC-FAI.md`
