
# 3D printed microfluidics lysate expression

[High-Throughput Experimentation Using Cell-Free Protein Synthesis Systems] (https://link.springer.com/protocol/10.1007/978-1-0716-1998-8_7)

# Ruby notes and papers

## GPLVMs
For implementing GPLVMs I use GPflow package which my supervisor helped to create. They have an implementation of the GPLVM and the Bayesian GPLVM. I would warn you the initialisation of the GPLVM makes a big difference to how good the results are so might be worth checking out how Titsias and Lawerence do it in the GPy implementation (which is the package Neil Lawerence's group created for their research).
Also, I'm not sure how much time you've spent working on these models and understanding the variational inference of the Bayesian GPLVM, but I recommend looking up Neil Lawrence's talks on GPLVM and deep GPs for a good explanation.

## Papers on design of experiments, GPs, and Bayesian optimisation for biology:
* Statistical Design of Experiments for Synthetic Biology https://pubs.acs.org/doi/10.1021/acssynbio.0c00385 - a very general paper mainly focusing on traditional design of experiments methods but I think it mentions Bayesian optimisation.

* This paper gives bit of an overview to Bayes Opt for molecule design https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7023065/
* This paper might be of interest to you: https://www.cell.com/cell-systems/pdfExtended/S2405-4712(20)30364-1, it's been a while since I read it so can't remember exactly what they do but they are using Bayesian optimisation, Gaussian processes and t-SNE (a dimensionality reduction technique) for protein engineering.
* This paper is using the Bayesian GPLVM for single cell data. Estimating pseudotime is quite a common use case for the GPLVM. https://academic.oup.com/bioinformatics/article/35/1/47/504775

* This paper is close to what I'm doing: using GPs for Bayesian optimisation when we have both observed and latent inputs https://www.nature.com/articles/s41598-020-60652-9
