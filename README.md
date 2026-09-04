# dslr

**Project Overview**
- **Summary**: Data Science × Logistic Regression — a small project that implements data exploration, visualization, and a multi-class logistic regression (one-vs-all) to reproduce a Sorting Hat classifier for Hogwarts houses.

**What I Built**
- **Data analysis**: custom `describe`-style routines to compute count, mean, std, percentiles without using convenience helpers.
- **Data visualization**: histogram, scatter plot, and pair-plot scripts to explore feature relationships and distributions.
- **Modeling**: a logistic regression implemented from scratch with gradient descent (one-vs-rest) to produce house predictions.

**Tech & Skills Demonstrated**
- **Languages & Libraries**: Python, NumPy, Matplotlib/Seaborn (for plots).
- **Core skills**: data cleaning & exploration, feature selection, implementing ML algorithms from first principles, model training and prediction pipelines.

**Key Files**
- Data analysis: [data_analysis/data_analysis.py](data_analysis/data_analysis.py)
- Visualization scripts: [data_visualization/histogram.py](data_visualization/histogram.py), [data_visualization/scatter_plot.py](data_visualization/scatter_plot.py), [data_visualization/pair_plot.py](data_visualization/pair_plot.py)
- Modeling: [model/logistic_regression.py](model/logistic_regression.py), [model/functions.py](model/functions.py)
- Higher-level entry points / pages: [pages/Describe.py](pages/Describe.py), [pages/Data_Visualization.py](pages/Data_Visualization.py), [pages/Magic_Hat.py](pages/Magic_Hat.py)

**Quick Start (for recruiters / technical reviewers)**
1. Create a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Run the data analysis / describe program (examples are in `pages/Describe.py` and `data_analysis/data_analysis.py`).

3. Generate visualizations to inspect features:

```bash
python data_visualization/histogram.py dataset_train.csv
python data_visualization/scatter_plot.py dataset_train.csv
python data_visualization/pair_plot.py dataset_train.csv
```

4. Train the logistic regression model and save weights (see [model/logistic_regression.py](model/logistic_regression.py)):

```bash
python model/logistic_regression.py --train dataset_train.csv --out weights.csv
```

5. Predict and produce the submission file `houses.csv`:

```bash
python model/logistic_regression.py --predict dataset_test.csv --weights weights.csv --out houses.csv
```

**Results & Notes**
- The implementation trains a one-vs-rest logistic regression using batch gradient descent as required by the project brief.
-- Evaluation is performed by generating `houses.csv` (format: `Index,Hogwarts House`) and can be scored with standard accuracy metrics (e.g., scikit-learn `accuracy_score`).



