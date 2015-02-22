==========
Coursework
==========

:status: hidden

Semester 2 - 2014
-----------------

COMP6741: Parameterized and Exact Computation
***********************************************

- Description: [COMP6741]_
- Grade: **Distinction**
- Assignments:
  
  * **Assignment 1**

    Using conventional techniques to solve NP-Complete problems
    related to scheduling, SAT solving, and computing domatic numbers.

    The following techniques were used:

    + Dynamic programming
    + Branch and bound
    + Inclusion-exclusion

  * **Assignment 2**

    Solving NP-Complete problems relating to the generalization of
    the Independent Set problem, coined "d-packing", where instead
    of requiring all vertices to be nonadjacent, we require their
    (geodesic) distance to be greater than d. I.e. 1-packing is equivalent
    to Independent Set.

    The following techniques were involved:
    
    + Branch and bound
    + Inclusion-exclusion
    + Fixed-parameter tractable (FPT) algorithms
    + Construction FPT reduction algorithms to prove W[1]-hardness
    + Prove FPT, parameterized by treewidth through
      treewidth decomposition / formalization in Monadic
      Second Order logic and Courcelle's theorem 

  * **Assignment 3**

    + Devising a randomized FPT algorithm for solving subgraph isomorphism problems. 
    + Exercises relating to the Composition Theorem, a tool for proving.
      kernel lower bounds (i.e. the nonexistence of a polynomial kernel).
    + Devising an iterative compression algorithm to solve feedback vertex set problems
      in tournament graphs.

COMP4418: Knowledge Representation and Reasoning
************************************************

- Description: [COMP4418]_
- Grade: **High Distinction**
- Assignments: 

  * **Assignment 1**

    + Exercises and proofs on propositional logic, first-order
      logic, and unit propagation rules.
    
    + Implemented logician Hao Wang's automated theorem prover 
      [Hao1961]_ based on Gentzen's Sequent Calculus.

      (Implementation in **Prolog**).
    + Analyzing the empirical hardness of SAT, with respect to 
      clause-to-variable ratio.

      (Random SAT instance generation in **Python**, solved using
      **pycosat**, a Python interface for **PicoSAT** and analysis
      performed in **IPython Notebook** with **pandas** and **matplotlib**) 
      
  * **Assignment 2**

    + Solving automated planning problems using the classical representation
      and subsequently the Graphplan algorithm.

      (Visualization of Graphplan algorithm in **tikz**)

    + Using Answer Set Programming to solve automated planning problems.

      (Using the **Potassco** toolkit for Answer Set Programming, specifically 
      **clingo**, an amalgamation of **gringo** and **clasp**.)

    + Modeling the actions, fluents and the situations of a automated planning 
      problem domain in Situational Calculus and implementation in **GOLOG**, 
      a **Prolog**-based logic programming language based on the situation calculus.

    + Formalizing the game Morra in **Game Description Language (GDL)** to support
      General Game Playing systems.

  * **Assignment 3**

    Modeling and solving complex constraint satisfaction & optimization 
    problems in **MiniZinc**, a medium-level constraint modelling language 
    developed by NICTA. Furthermore, benchmarking performance with respect 
    various utility methods (i.e. objective functions), input sizes, and 
    optimizing models using techniques such as symmetry breaking.

COMP3161: Concepts of Programming Languages 
*******************************************

- Description: [COMP3161]_
- Grade: **High Distinction**
- Assignments: 

  * **Assignment 1**

    Implemented an interpreter for "MinHS", a functional 
    programming language in the spirit of Haskell, 
    fabricated for instructional purposes.

    Interpreter implemented in **Haskell**.

  * **Assignment 2**

    Added type inference for MinHS by implementing 
    Hindley-Milner type inference algorithm (aka "Algorithm W".)
    
    (Implementation in **Haskell**.)

.. [Hao1961] http://onlinelibrary.wiley.com/doi/10.1002/j.1538-7305.1961.tb03975.x/abstract
.. [COMP4418] Knowledge Representation and Reasoning (KRR) is at the core of Artificial Intelligence. It is concerned with the representation of knowledge in symbolic form and the use of this knowledge for reasoning. This course presents current trends and research issues in Knowledge Representation and Reasoning (KRR). It enables students interested in Artificial Intelligence to deepen their knowledge in this important area and gives them a solid background for doing their own work/research in this area. The topics covered may include: Belief revision, Boolean satisfiability, Constraint programming, Description logics and ontologies, Mathematical programming, Planning, Reasoning about action.
.. [COMP3161] Programming language paradigms: imperative, object oriented, declarative (i.e., functional and logic). Theoretical foundations of programming languages: syntax, operatational, axiomatic and denotational semantics. Implementation aspects of central language features, such as dynamic and strong typing, polymorphism, overloading and automatic memory management. Abstracting over programming languages and architectures: byte code approach, component software.
.. [COMP6741] The course focuses on algorithms for exactly solving NP-hard computational problems. Since no polynomial time algorithm is known for any of these problems, the running time of the algorithms will have a super-polynomial dependence on the input size or some other parameter of the input. 

  The first part presents algorithmic techniques to solve NP-hard problems provably faster than brute-force in the worst case, such as branching algorithms, dynamic programming across subsets, inclusion-exclusion, local search, and measure & conquer. We will also see lower bounds for algorithms and how to rule out certain running times assuming the (Strong) Exponential Time Hypothesis.

  Whereas the first part presents "default" algorithms that one would use without knowing much about the instances one is about to solve, the second part acknowledges that the complexity of an instance does not only depend on its size n. A parameter k is associated with each instance and the parameterized complexity framework aims at designing fixed-parameter algorithms whose running times are f(k)*poly(n) for a computable function f. This gives efficient algorithms for small values of the parameter obtained via techniques such as branching, colour coding, iterative compression, and kernelization (preprocessing). We will also see problems that are not fixed-parameter tractable and not kernelizable to polynomial kernels subject to complexity-theoretic assumptions.
