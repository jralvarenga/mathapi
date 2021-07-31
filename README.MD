# MathAPI

> Integrate math to your calculator or app became easy with MathAPI

---

## Description

With MathAPI you can send it a math problem, like a function or an ecuation sistem and get the plot, derivative or integral, even get the solution of an ecuation sistem

An open source proyect and open to contribution, built with python, sympy & numpy, the api features are:

- [Functions solutionary](mathapi/math/function)
- [Derivative](mathapi/math/derivative)
- [Integral](mathapi/math/integral)
- [Ecuation sistem solutions](mathapi/math/es)
- [Factorials](mathapi/math/factorial)
- [Euler functions](mathapi/math/euler_functions)
- [Numeric methods](mathapi/math/methods)
- And many more to be added

Go to [API Structure](#api-structure) for more information

## Usage & Contribution

MathAPI is an open source proyect and open to contribution, go to any of the api functions listed above and read the instructions to use it.

For contribution, fork the repo, create a branch and name it with the feature you're working, create a pull request and thats all. read [CONTRIBUTING.md](CONTRIBUTING.md) for more information.

## Branches structure

| Branch        | Description |
| ------------- |:-------------:|
| master        | Production branch  |
| dev           | Stagging branch (main branch)     |
| [feature-name]      | Derived from dev (new feat. to add)     |


## API Structure

| Directory     | Description |
| ------------- |:-------------:|
| [function](mathapi/math/function)      | All related to f(x) functions (solve, plot points, etc.)  |
| [derivative](mathapi/math/derivative)    | All related to the derivative of a f(x)     |
| [integral](mathapi/math/integral)      | All related to the integral of a f(x)     |
| [es](mathapi/math/es)            | Ecuation sistem solution     |
| [factorial](mathapi/math/factorial)            | Factorial of integer or fraction     |
| [euler_functions](mathapi/math/euler_functions) | All euler function related (gamma, beta, phi functions)     |
| [methods](mathapi/math/methods)       | Numeric methods     |
