# Weird TMs and NP-Completeness

# January 21st, 2020

- Okay, grades and solutions for homework 1 should have been released earlier today; you have 2 weeks to submit a regrade request
    - I personally messed up pretty hard on the last problem (forgot to consider the case of 2 valid strings glued together, which'll make it fail), and also made a silly mistake on 1b (missed a counter-example for my proof)
        - 1b especially frustrates me that I missed it; "A(B and C)" is NOT the same as "AB and AC", since A={a,aa}, B={b,c}, C={ab,c}
            - Since A(B and C) = {ac, aac}, but AB and AC = {ac, aab, aac}
            - i.e. fails when one of the sets already contains a string that's a combination of the strings in the other sets
        - Apparently, my proof holds for one direction (that A(B and C) is a subset of AB and AC), but NOT for the other
- Also, homework 2's due date has been changed to THIS SATURDAY, the 25th, at noon
    - Homework 2 focuses on specifying TMs and doing arithmetic operations with them
    - "Apparently, our changes made the homework make LESS sense"
        - For HW2, I'm not expecting you to write out the state diagrams for your TMs; instead, think of it as 3510 homework
        - This class is meant to be an introduction to the theory of computing, and how to think about algorithms in a formal, mathematical way
            - If you're confused about how formal your homework should be, look at the examples in the textbook; when in doubt, make it as formal as you did in 3510
        - HW2 can result in you getting CRAZY large numbers; problem 1, where P and Q are permutations and you're taking the power of Q (i.e. applying it to itself multiple times), can be hard because "t" could be 1000 or a million or whatever; you can't simulate the permutation repeatedly and keep it in P, so you can do it FASTER using fast exponentiation
            - i.e. a^1024 mod 100 or something can be computed by first computing a^2, then squaring it and taking mod 100, then squaring it again and mod 100, etc., letting us compute this in logarithmic time (successive squaring algorithm)
        - Think about how a TM can apply a permutation; if you're in a hurry, you can take advantage of the fact that accessing a TM is very analogous to accessing an array, and basically you can just add a 2nd tape and access it like an array
    - Question 3 doesn't use the words "non-deterministic TM", but it's basically that; it's like the infinite monkeys producing Shakespeare, where you just try everything possible
        - It's slightly more meta, since you're also generating the TMs, but it's the same idea
- Plan for today:
    - "People have told me I'm doing too much theory; I thought 3510 did a lot of the theory we covered from last time, but it turns out I was wrong, so I apologize for that; we'll go over that stuff"
        - Everything we're doing right now has a direct analog from 3510; we are trying to show that the definition of a non-deterministic Turing machine is the SAME THING as saying something is NP
    - Example of a non-trivial non-deterministic TM
    - Simulating non-deterministic TMs using deterministic TMs
    - Example of a reduction
--------------------------------------------------------------------------------

- Okay, by now you should be familiar with a Turing Machine: I've got a tape, and a tape head with a bunch of states
    - Regular Turing Machines are polytime, which is great! We can square the runtime and still technically be in polynomial time!
        - This is why our textbook sweeps conversions between binary/ternary/etc. encodings under the rug, since these conversions can still be done in polynomial time
    - The trouble with non-deterministic Turing Machines is that, since we have multiple options for different steps, we get BRANCHING possibilities that grow exponentially
        - It will then check the leafs of all the branches, and if ANY of the possible conclusions will "accept" the string, then we accept it!
            - In other words, you can think of this as a brute-force search!
        - If you think back to 3-SAT, the canonical NP-hard problem,
    - So, the definition of non-deterministic time is the maximum amount of time a non-deterministic TM could potentially take to check a given input (i.e. not just the length of the longest branch, but to traverse the whole "tree" of possibilities)
        - So, for a language "L", we say "L" is in NTIME()
    - By definition, we say NP = $U_kNTIME(n^k)$
        - Therefore, TIME(f(n)) $\subset$ NTIME(f(n))
        - We'll prove this: NTIME(f(n)) $\subset$ TIME($2^{O(f(n))}$)
            - The "2" here just comes from using binary; we can convert it to a different base if we wanted
            - We can prove this by just taking all possible branches, and then writing a "cheater tape" that records the correct sequence we should take (???)

- To write this cheater tape, we need a Universal Turing Machine, running another TM on it
    - So, you generate all your branches from your input Turing Machine, write them onto your "cheating tape," and record the moves you need to do to get the shortest correct accept path
        - In tree pruning, we want to cut our search as short as possible, but theoretically there's very little difference in the runtime from doing this; all you're doing is (???)
        - So, theoretically there's no difference between generating all branches ahead of time and checking them on the fly (they're both NP, I think?), but practically it gives HUGE savings
            - If we brute-forced 3-SAT, we'd never get above ~20 variables; practically, though, we can do problems with several thousand variables quite easily, and have gone into the millions
    - That's how you can implement non-deterministic Turing Machines that'll correctly accept/reject an input string!
        - Essentially, you're running a "P" Turing Machine for each possible branch of the input, and then finding a branch that works

- So, all we know right now is that P is a subset of NP

- With a few minutes left, let's talk about reductions
    - Formally, we say a language A is poly-time reducible to B if there is a poly-time function "f" such that w $\in$ A $\iff$ f(w) $\in$ B
        - IMPORTANTLY, the Cook-Levin Theorem says that EVERY non-deterministic Turing Machine can be reduced to 3-SAT
    - As a reminder, 3-SAT is a problem where:
        - We have variables x1 ... xn, and have a set of combinations of 3 of each one:

                (x1 ^ !x2 ^ x3) ^ (...)

        - We then want to figure out if there are values of x1 ... xn that will make the overall statement true
    - There are 2 reasons we define everything in this class in terms of Turing Machines:
        - Deterministic TMs are reducible to polynomial operations (I think?)
        - You can write a SAT instance corresponding to all the tape contents of the TM, and transform the problem from "Should this input be accepted?" to "Does this 3-SAT problem have a solution?"
    - We don't have time to go through the proof here, but this is proven in Chapter 7 of the textbook
    - You CAN, however, prove that 3-SAT is NP (on the slides)
        - With the Cook-Levin problem, we can then say that 3-SAT is NP-COMPLETE, meaning it's both NP and any other NP problem can be reduced to it
            - An "NP-hard" problem means that all NP problems can be reduced to it
                - While unusual, there are some weird problems that ARE NP-hard without being NP themselves
            - NP complete, then, meets a problem is both in NP and NP-hard

- Okay, we'll get to examples of reducibility next time!