# Numerical-Integration

## Abstract
This assignment involves the computation of the mass of a hypothetical spherically-symmetric star using two numerical integration methods: the trapezoidal rule and the Monte Carlo method. The first part of the assignment compares the computational costs of the two methods to achieve a precision of 10^-3. In the second part, the star is assumed to be given in a three-dimensional coordinate system. The 3-dimensional numerical integration is performed using two methods. The results obtained from each method are compared and discussed in terms of their computational cost and accuracy.

## Introduction
In the first part the density function of the star is given in the spherical coordinate system, where r is the distance from the center and the radius of the star is at r = 3. First, I define all the necessary functions and then I use them in order to compute the value of mass using these functions and compare their computational costs.

In the second part the density function is given in rectangular coordinate system. I do the same operations as in the first part.

## Methods
Mass of the star can be found using the formula:


$$ M = \int_0^{2\pi} \int_0^\pi \int_0^R f(r) \cdot \sin(\phi) \cdot r^2 \; dr \; d\phi \; d\theta=4 \pi \int_0^R ρ(r) r^2 \; dr = 4 \pi\int_0^R exp(-r^3) r^2 \; dr$$


So, we should use the trapezoidal rule and MC method for this integral.

Another method

I used the following integral to evaluate the mass of the star


$$ M = \int dm =\int \int \int \rho \;dV =\int_{-R}^R \int_{-R}^R \int_{-R}^R f(x,y,z) \; dx \; dy \; dz $$


![Screenshot from 2023-07-17 17-02-01](https://github.com/leilaakisheva/Numerical-Intgration/assets/128895782/c63e5243-c1c3-46a6-ac06-f8445443f092)

## Results
As it can be seen the trapezoidal rule was computationally more efficient for the first part than the Monte Carlo method, requiring significantly less time to achieve the same level of precision. While for the second part where 3 positional variables were given, MC method works much more efficiently. However, time taken for computation in both methods is significantly smaller for the Trapezoidal rule.

## Conclusion
In conclusion, we have shown that numerical integration methods such as the trapezoidal rule and the Monte Carlo method can be used to compute the mass of a star, given its density function. It was demonstrated that the Trapezoidal rule is more computationally efficient than the Monte Carlo method for the spherical coordinates. On the other hand, it was also figured out that the Monte Carlo method is more efficient for the rectangular method.
