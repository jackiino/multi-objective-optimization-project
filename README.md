Consider the following multi-objective optimization problem:

$$\min_{x\in F} \{ f_1(x), f_2(x), \dots, f_k(x)\}$$

where $k \ge 2$, $f_i:\mathbb{R^n} \rightarrow \mathbb{R}$, for $i = 1, \dots, k$ and $F$ is the $\textit{eligible region}$.\
The space $\mathbb{R^n}$ is called $\textit{decision variable space}$, while the space $\mathbb{R^k}$ is called $\textit{objective space}$.

For each decision vector $x\in\mathbb{R^n}$  is associated a vector $z = (f_1(x), f_2(x),\dots,f_k(x))^T\in\mathbb{R^k}$ (objective vector) in the objective space.\
Let $F\subseteq\mathbb{R^n}$ the eligible region in the decision space, let
$$Z = f(F) = \{ z\in\mathbb{R^k} : \exists x\in F, z = f(x)\}$$
then a vector $z\in\mathbb{R^k}$ is said to be $\textit{eligible}$ when $z\in Z$.


# A problem of production

A company produce three types of product $P_i,\ i = 1,2, 3$. For each product we consider:\
-unitary profit (euro/item);\
-working hours;\
-quantity of raw material;\
-level of pollution generated.

## Objectives and constraints

Assumining that the company has 1300 working hours and 1000 unity of raw material, the goals of the company is to:\
-maximaze the profit;\
-minimize the level of pollution.

## Formulation

-Variables. The variables are $x = (x_1, x_2, x_3)$ where $x_i = P_i$, for $i = 1, 2, 3$.

-Constraints. We have two types of constraints, one for the availability of raw material and the second one for the working hours:
$$b_1x_1 + b_2x_2 + b_3x_3 \le 1300 $$
$$c_1x_1 + c_2x_2 + c_3x_3 \le 1000 $$

-Objectives. We wanto to maximize the profit:
$$\max_{x\in\mathbb{R}^3} \{a_1x_1 + a_2x_2 + a_3x_3 \}$$
and to minimize the pollution:
$$\min_{x\in\mathbb{R}^3} \{d_1x_1 + d_2x_2 + d_3x_3\} $$

In summary, we have the following formulation
$$\min_{x\in\mathbb{R}^3}\{-a_1x_1 - a_2x_2 - a_3x_3,\ d_1x_1 + d_2x_2 + d_3x_3\}$$
$$b_1x_1 + b_2x_2 + b_3x_3 \le 1300 $$
$$c_1x_1 + c_2x_2 + c_3x_3 \le 1000 $$
$$x_1, x_2, x_3 \ge 0$$


Since we want to minimize both the objective functions, we notice that there is not an ideal vector $z^{id}$ defined as following:
$$z^{id}_i = \min_{x\in F} f_i(x),\ \ \ \ \ \ \text{for}\ i = 1, 2, 3.$$
Thus
$$z^{id}\not\in F.$$
This means that the functions $f_1(x)$ and $f_2(x)$ are in contrast.


## Pareto front
Since we can't find $z^{id}$ we have to define, clearly, what finding an optimal solution in a multi-objective problem means. The following definition was proposed by Edgeworth in 1881. Then, in 1896 Vilfredo Pareto elaborated it.

Given two vectors $z^1,z^2\in\mathbb{R}^k$, we say that $z^1$ Pareto dominates $z^2$ ($z^1 \le_{P} z^2$) when 
$$z^1_i\le z^2_i\quad \text{for every}\ i=1,2,\dots,k$$
$$z^1_j < z^2_j\quad \text{for at least}\ j\in\{1,\dots,k\}$$
The binary relation $\le_P$ is a partial order in the space of $k$-uple of real numbers.

$\mathbf{Def.}$ A decision vector $x^*\in F$ is a Pareto optimal if no exists a vector $x\in F$ such that
$$f(x)\le_P f(x^*)$$

It is evident that attaining an optimal solution is unfeasible, necessitating the consideration of trade-offs. To address this, we turn to multi-objective optimization (MOO) algorithms. We will employ the widely-used NSGA II algorithm to solve the problem initially. 

Subsequently, we will extend the complexity of the problem by applying it to a more substantial dataset and introducing an additional objective. This expansion allows for a more comprehensive evaluation of the algorithm's performance. 

In the final stage, we will compare the outcomes with optimized algorithms derived from the robust Python library, pyomoo. This comparative analysis aims to assess the effectiveness of NSGA II against other sophisticated optimization techniques available in pyomoo.

# NSGA II

Why NSGA II?\
Several algorithm have been developed, but some of this may be inefficient. For example, using objectives weighting we lack of diversity of solutions.

Non-dominated Sorting GA II promote the diversity of the solutions using the crowding distance, which is a "measure" of diversity.


## NSGA II Algorithm Steps

1. **Initialize Parent Population $P_i$**
   - Generate a population of individuals.


2. **Iterate the Following $n$ Times:**
   
   2.1. *Crossover:* Create offspring $Q_i$ from $P_i$ via crossover. Combine genes from two parents to create a new offspring.
  
   2.2. *Mutation:* Create offspring via mutation by adding o subtracting a random number to all the gene.

   2.3. *Optional Local Search:* Optionally create offspring via local search by adding random finite displacements to some parent genes and checking if the solution is better.

   2.4. *Combine Populations:* Combine $P$ and three groups of $Q$ into one population set.

   2.5. *Evaluation:* Calculate fitness for each individual in the population.
   
   2.6. *Selection:*  
   - i. Find subset of individuals that constitute Pareto front.  
   - ii. Calculate crowding.  
   - iii. Randomly remove some individuals from Pareto front using crowding index for diversity.


3. **Evaluate Fitness of Resulted Population:**
   - Assess the fitness of the final population.

4. **Find Final Pareto Efficient Solutions:**
   - Identify the Pareto-efficient solutions from the final population.

