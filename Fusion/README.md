# Fusion — Cross-Modal Comparison

Compares classification performance of Stream A (acoustic prosody) vs Stream B (fMRI NAcc BOLD) using **independent classifiers on separate cohorts** (DAIC-WOZ vs ds000030).

## Notebook

- `02_Fusion_Analysis.ipynb` — Per-stream classification (LogReg, RF, GBT), ablation table, ROC/PR overlay, SHAP feature importance, confusion matrices

## Key Outputs

- `Results/ablation_table.csv` — Cross-modal performance comparison
- `Results/roc_pr_comparison.png` — ROC + Precision-Recall overlay
- `Results/shap_*.png` — SHAP beeswarm feature importance per stream
- `Results/confusion_matrices.png` — Held-out confusion matrices
