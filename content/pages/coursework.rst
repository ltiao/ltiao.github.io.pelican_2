==========
Coursework
==========

:status: hidden

Semester 2 - 2014
-----------------

- COMP3161 - Concepts of Programming Languages

  * Assignment 1

    Implemented an interpreter for "MinHS", a functional 
    programming language in the spirit of Haskell, 
    fabricated for instructional purposes.

    Interpreter implemented in **Haskell**.

  * Assignment 2

    Added type inference for MinHS by implementing 
    Hindley-Milner type inference algorithm (aka "Algorithm W".)
    
    (Implementation in **Haskell**.)

- COMP4418 - Knowledge Representation and Reasoning
  
  * Assignment 1

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
  * Assignment 2

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

  * Assignment 3

    Modeling and solving complex constraint satisfaction & optimization 
    problems in **MiniZinc**, a medium-level constraint modelling language 
    developed by NICTA. Furthermore, benchmarking performance with respect 
    various utility methods (i.e. objective functions), input sizes, and 
    optimizing models using techniques such as symmetry breaking.

+------------+------------+-----------+ 
| Header 1   | Header 2   | Header 3  | 
+============+============+===========+ 
| body row 1 | column 2   | column 3  | 
+------------+------------+-----------+ 
| body row 2 | Cells may span columns.| 
+------------+------------+-----------+ 
| body row 3 | Cells may  | - Cells   | 
+------------+ span rows. | - contain | 
| body row 4 |            | - blocks. | 
+------------+------------+-----------+

.. [Hao1961] http://onlinelibrary.wiley.com/doi/10.1002/j.1538-7305.1961.tb03975.x/abstract