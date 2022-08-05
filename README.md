# CMR-ES

For blackbox optimization with evolution strategies mutation rate control is essential to move efficiently in multimodal solution spaces and to allow convergence. The Rechenberg 1/5 mutation rate rule is an easy-to-implement and effective control method, but its use is restricted when objective variables scale in different ranges.
To extend the Rechenberg mutation rate control of a (1+1)-ES to problems with scaled and correlated dimensions, it is combined with a Monte Carlo-based covariance matrix estimation in this paper. Experiments conducted on a scaled version of the sphere function show the approach outperforms the isotropic approach while being easier to implement and use than the CMA-ES.
