# Customer Segmentation via Unsupervised Clustering

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
[![Stars](https://img.shields.io/github/stars/your_username/clustering_project.svg)](https://github.com/your_username/clustering_project/stargazers)

---

## 🎯 Business Challenge

Many times we make mistakes by treating all leads the same, wasting budget on uninterested segments and missing high-value prospects. My goal is in this project is to **discover distinct customer personas** from bank marketing data so campaigns can be finely targeted, driving higher conversion rates and ROI.

---

## 🧩 Why Unsupervised Clustering?

- **Discover Hidden Structure**: Uncover natural groupings (e.g. “high-balance managers,” “young students”) without pre-labeled segments.  
- **Actionable Insights**: Centroids ↔ “average” customer profiles simplify narrative and campaign design.  
- **Flexibility**: Compare partition-based (K-Means), density-based (DBSCAN), and model-based (GMM) methods to fit spherical, irregular, or overlapping clusters.

---
## ❓How Did i evaluated which is best clustering model ?

| Algorithm | Chosen K/Params   | Silhouette | Calinski-Harabasz | Noise % | Run-time | Interpretability  |
| --------- | ----------------- | ---------- | ----------------- | ------- | -------- | ----------------- |
| K-Means   | K = 4             | 0.145      | 2350              | 0 %     | 0.2 s    |  Very high       |
| DBSCAN    | eps = 1.1, min=10 | 0.180      | 980               | 25 %    | 0.5 s    |  Moderate        |
| GMM       | K = 6 (BIC min)   | 0.221      | 2100              | 0 %     | 1.5 s    |  Softer clusters |

**Stability tests:**

* K-Means assignments were > 95 % identical across 10 random restarts at K=4.
* DBSCAN labeling varied \~10 % when subsampling 50 % of data, indicating sensitivity to local densities.
* GMM responsibilities changed < 5 % under bootstrap resamples, showing good robustness but slightly more overlap.

---

## 🚀 Project Goals

1. **Data Ingestion & Exploration**  
   - Schema checks, missing-value audit, univariate EDA, correlation analysis.  
2. **Data Cleaning & Preprocessing**  
   - IQR outlier capping, log1p transforms, binary mapping, missingness flags.  
3. **Feature Transformation**  
   - Ordinal/frequency encoding, cyclic sin/cos for dates, one-hot for nominal cats.  
4. **Scaling & Dimensionality Reduction**  
   - StandardScaler → PCA for ≥90% variance (≈10 components).  
5. **Modeling**  
   - K-Means (K = 2…10), DBSCAN (eps/min_samples tuning), GMM (BIC selection).  
6. **Evaluation**  
   - Silhouette, Calinski-Harabasz, stability across runs.  
7. **Model Selection**  
   - **K-Means (K=4)** chosen for speed, interpretability, and stability.  
8. **Deployment Prep**  
   - `sklearn.Pipeline` for clean→feat→scale→PCA→cluster, artifact serialization.  

---

## 🔧 Installation & Quick Start


# 1. Clone repo
```bash
git clone https://github.com/your_username/clustering_project.git
cd clustering_project
```
# 2. Create & activate venv
```bash
python3 -m venv venv
source venv/bin/activate
```

# 3. Install dependencies
```bash
pip install -r requirements.txt
```
# 4. Run full pipeline
```bash
python src/data.py   --input data/raw/bank.csv    --output data/processed/clean.csv
python src/features.py  --input data/processed/clean.csv --output data/processed/features.csv
python src/models.py  --mode run_all_models   --input data/processed/features.csv
```
---

## 📖 Documentation & Notebooks
Detailed analyses live in notebooks:

 - data_exploration: EDA and schema checks

 - preprocessing: Missingness, outlier capping, binary mapping

 - feature_engineering: Log transforms, encoding strategies

 - modeling_clustering and evaluation: PCA, K-Means vs. DBSCAN vs. GMM.

---
⭐ Support
If this project helped you, please ⭐ star the repository and share!

---

## 📑 Key References
 - Jain, A. K., & Dubes, R. C. (1988). Algorithms for Clustering Data. Prentice-Hall.

 - Ester, M., Kriegel, H.-P., Sander, J., & Xu, X. (1996). A density-based algorithm for discovering clusters in large spatial databases with noise (DBSCAN). KDD.

 - Rousseeuw, P. J. (1987). Silhouettes: A graphical aid to the interpretation and validation of cluster analysis. Journal of Computational and Applied Mathematics.
