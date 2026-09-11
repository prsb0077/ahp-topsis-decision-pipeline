# ahp-topsis-decision-pipeline
Automated Python implementation of AHP and TOPSIS multi-criteria decision-making algorithms with consistency validation

--------
Overview:
This tool automates multi-attribute alternative evaluation and ranking through a two-stage analytical pipeline:
1. AHP Weight Derivation: Computes criteria weights from pairwise comparison matrices using the Geometric Mean method.
2. Consistency Verification: Validates input judgments via Saaty's Consistency Index (CI) and Consistency Ratio (CR < 0.10) before proceeding.
3. TOPSIS Ranking Engine: Feeds validated weights into a normalized decision matrix, calculates separation distances from Positive and Negative Ideal Solutions (PIS/ NIS), and outputs final relative closeness scores.
   
--------

Key Features:
- Built-in Consistency Gate: Automatically calculates consistency metrics (CI, CR) and alerts the user if pairwise judgments lack transitivity
- Dynamic Sizing: Handles custom criteria matrix sizes and varying numbers of candidate alternatives.
- Objective Separation: Supports distinct handling for both benefit (+1) and cost (-1) criteria during normalization.
- Minimal Footprint: Built entirely with Python standard libraries and NumPy for fast vectorized matrix operations.

--------

Tech Stack:
Language: Python 3.x
Libraries:NumPy, Math

--------

Installation:
1. Clone the repository:
'''bash git clone [https://github.com/prsb0077/ahp-topsis-decision-pipeline.git](https://github.com/prsb0077/ahp-topsis-decision-pipeline.git)
   cd ahp-topsis-decision-pipeline

2. Install dependencies:
   pip install numpy

Usage: 
1. Run the script:
   python main.py
2. Step-by-Step work flow
   1-Define Criteria: Enter the total number of evaluation criteria.
   2-Pairwise Comparison: Input matrix comparisons using Saaty's 1–9 scale.
   3.Consistency Check: The tool calculates CI and CR. If CR < 0.10, the matrix is validated and weights are computed.
   4.Alternative Data: Enter the number of alternatives and their respective values for each criterion.
   5.Assign Polarity: Specify whether each criterion is a benefit (+1) or cost (-1).
   6.Results: The script calculates Euclidean distances to ideal solutions and prints the final ranked alternatives.

