# laplace-solver-2d

Numerical solution of the \*\*Laplace equation\*\* using \*\*Jacobi\*\* and \*\*Gauss Seidel\*\* method



\## Mathematical background

\#The 2D Laplace equation

\\\[

\\nabla^2 \\phi = \\frac{\\partial^2 \\phi}{\\partial x^2} + \\frac{\\partial^2 \\phi}{\\partial y^2} = 0

\\]



\#Finite difference discretization:

\\\[

\\phi\_{i,j} = \\frac{1}{4} \\bigl( \\phi\_{i+1,j} + \\phi\_{i-1,j} + \\phi\_{i,j+1} + \\phi\_{i,j-1} \\bigr)

\\]



\## Example result



\# Heat map

!\[Heat map](plots/heatmap.png)

\# vector field

!\[vector field](plots/vectorFields.png)



