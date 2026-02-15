# **BA2-Ct/JNK3-Nt unbiased MD and REHT inputs**

This repository contains the input files required to reproduce the unbiased molecular dynamics (MD) and enhanced-sampling simulations (Replica Exchange With Hybrid Tempering, REHT) described in:

*A selective JNK3-targeting miniprotein confers neuroprotection in a mouse model of ischemic stroke.*


## **Scientific Context**

Ischemic stroke remains a leading cause of death and long-term disability. Although reperfusion therapies restore blood flow, they do not prevent progressive neuronal loss driven by intracellular stress pathways. The neuron-restricted kinase c-Jun N-terminal kinase 3 (JNK3) is a key mediator of ischemia-induced neuronal death, but therapeutic inhibition has been limited by poor isoform selectivity and toxicity.

To enable selective targeting of pathological JNK3 signaling, we used structural modeling and atomistic simulations to identify binding determinants between the C-terminal domain of human β-arrestin2 (BA2-Ct) and the N-terminal tail of JNK3 (JNK3-Nt). Importantly, JNK3-Nt is an intrinsically disordered region (IDR), whose conformational heterogeneity complicates conventional structural characterization.

Unbiased MD and REHT were employed to enhance sampling of IDR-mediated interactions and to map JNK3-Nt residue-level binding hotspots on BA2-Ct. Contact probability analyses across the conformational ensemble enabled identification of a minimal BA2-derived interface region, which was subsequently extracted to engineer SIMBA2, a brain-penetrant miniprotein that selectively inhibits JNK3 signaling and confers sustained neuroprotection in vivo.

## **Repository Contents**

Included:

- unbiased MD inputs (.gro, .tpr, .mdp, topology files)
- REHT input generation, equilibration and production files (32 replicas)
- contact map analysis Python script used to quantify BA2-Ct/JNK3-Nt intermolecular interactions


## **Software Requirements**

Simulations were performed and analyzed using:

- GROMACS 2022.5 patched with PLUMED 2.9.0
- Python3: numpy, MDAnalysis, mdtraj, matplotlib 

See folder-specific README files for details.


### **Upstream Method**

The REHT workflow was adapted from:
ReplicaExchangeWithHybridTempering
https://github.com/codesrivastavalab/ReplicaExchangeWithHybridTempering
