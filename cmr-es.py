# CMR-ES presented on ESANN 2022 
# Paper "Evolution Strategies with Rechenberg Mutation Rate Control and Covariance Matrix Estimation" 
# by Oliver Kramer, Computational Intelligence Lab, University of Oldenburg


import numpy as np

N = 5
scale = 1000.

def scalesphere(x):
	# first dimension scaled by "scale"
	w=np.ones(N)
	w[0]=scale
	x=w*x
	return np.dot(x,x)


fitfunction = scalesphere


def termination(t,fit):
	return True if (t>10000 or fit < 10e-500) else False


def CMRES():
	
	x = np.ones(N)		# objective variables initialized at (1,1,..)
	fit = fitfunction(x)
	sigma = 1.			# step size 
	t = 0

	fitlog = []
	happy = False

	print("Another CMR-ES run...")

	# covariance estimation
	X = np.array([np.random.randn(N) for i in range(2000)])
	X =np.array([x[1] for x in sorted([(fitfunction(x),x) for x in X], key=lambda x: x[0])][:20])
	C = np.cov(X.T)		# this function does the work
	print("C",C)


	# (1+1)-ES 
	while not happy:

		t+=1
		happy = termination(t,fit)
		x_ = x + sigma * np.random.multivariate_normal(np.zeros(N),C)
		fit_ = fitfunction(x_)

		# Rechenberg 1/5 success rule and selection
		if fit_ <= fit:
			x = x_
			fit = fit_
			sigma*=np.exp(4/5)
		else: 
			sigma*=np.exp(-1/5)

		fitlog.append(fit)

	return fitlog


runs = [CMRES() for i in range(10)]


print("mean",np.mean([runs_[-1] for runs_ in runs]))
print("std",np.std([runs_[-1] for runs_ in runs]))
