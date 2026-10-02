# Aphid Insecticide Resistance Analysis
Aphids are a worldwide common crop pest typically managed through the use of insecticides. However, since 2013 resistance to these insecticides has been observed at a growing rate.
This project investigates the proteomic differences between susceptible and resistant Aphid populations (_Sitobion Avanae_), and which biological processes are associated with resistance.

The scope of the project explores:
1. Do resistant and susceptible aphids have differing proteomes overall?
2. Which proteins are more or less abundant in both biotypes.
3. Are any biological processes associated with the resistant biotype in particular?
4. Which proteins or pathways may contribute to pyrethroid resistance?

# Dataset
This project uses a quantitative proteomics dataset generated from English grain aphid (_Sitobion Avenae_) biotypes.
- Biological context: pyrethroid-susceptible SA27 (SS) vs pyrethroid-resistant SA3 (SR)
- Platform: Thermo Fisher Q Exactive LC-MS/MS
- Data type: LFQ proteomics
- Samples: 5 SS replicates & 5 SR replicates

### Expected Data Input
The workflow expected a protein-level dataset (tab-delimited) exported from MaxQuant, containing protein identifiers and LFQ intensity values for each sample.

# Project Summary
The workflow performs:
1. LFQ proteomics data preprocessing and quality control.
