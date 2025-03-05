# Dame

Code accompanying the paper Distribution-Aware Mean Estimation under User-level Local Differential Privacy

https://openreview.net/attachment?id=ThADV3tAIn&name=pdf.

# Install 

Clone the repository

`git clone https://github.com/hugorichard/dame.git`

Move into the dame directory

`cd dame`

Install DAME

`pip install -e .`
    
# Requirement

The dependencies are the following:

- "scipy>=0.18.0"
- "numpy>=1.12"
- "scikit-learn>=0.23"
- "joblib>=1.1.0"
- "matplotlib>=2.0.0"
- "pytest>=6.2.5"

# Experiment

Move into the dame directory

`cd dame`

## Experiment 1
To reproduce the experiment in the paper where the number of samples are chosen according to a power law:

Run the experiment using
`python expe_power_law.py`

Plot the result using 
`python plotting_power_law.py`

It creates a pdf file `fig_power.pdf`.


## Experiment 2
To reproduce the experiment in the paper where the number of samples is $m_1$ with proba $\rho$ and $m_2$ with proba $1 - \rho$:

Run the experiment using
`python expe_bernoulli.py`

Plot the result using 
`python plotting_bernoulli.py`

It creates a pdf file `fig_bernoulli.pdf`.


# Cite 
If you use this code please cite us (Pla, AISTATS 2024).


