function u = uexact(x,epsilon)

u=(1-exp(-(x+1)/(2*epsilon)))/(1-exp(-1/epsilon));