# bb_variability
Study the Bayesian block variability index applied to Fermi-Lat data

## Data file: `files/var_info.csv`
This is a table with index the 4FGL-DR4 name. To access as a DataFrame:
```
df = pd.read_csv('files/var_info.csv', index_col=0)
```

Relevant columns
* glat, glon : Galactic coordinates
* nbb : number of blocks
* variability: the 4FGL variability index: it should be distributed as chi-squared with 13 degrees of freedom
* uw_name: name of the uw1410 entry
* bb_var: The Bayesian block variability. Expect it to be chi-squared with nbb-1 DOF
* category: Derived from `class1` association labels. Values are bcu, bll, fsrq, psr, unid

## Objectives    
* For a subset of source that are __not__ variable, compare the variability distribution with the expectation

* BB is in principle more sensitive. Isolate a subset that are clearly variable with BB, but not the 4FGL measure, and check the associations.

