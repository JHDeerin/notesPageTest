# Reductions (cont.) / Cook-Levin Theorem

## January 28th, 2020

- Okay, there's a mess of windows and stuff on the board
    - "Some people are worried about passing, but trust me, if you need to pass this class to graduate and you put in ANY effort at all, talk to me; as long as you're coming to class and trying and doing the work, I can make sure you at least pass. Maybe not with flying colors, but..."

- "Okay, homework 2 - I'll talk about it in our intermission, but first I want to wrap up our reduction discussion from last week"

- Other notes:
    - There's a review guide for Exam 1 as the lecture notes for this lecture on the course website, as well as posted solution for Homework 1 and Homework 2
    - On that note, our first exam is THIS THURSDAY (in TWO DAYS) - bring your buzzcard!
        - "I try to make my exams VERY similar to the review guide and homework questions, so I'd very much recommend reviewing those closely"
        - The most important thing to review by FAR are the homework solutions
            - "Side-note: in this class, we won't have ANY reductions involving graph theory"
            - Because of that, review question 4 is NOT going to be valid for the test; "I just got bored writing 3-SAT reductions, because they're ALL boring"
        - Because this is a proof-based class, there are unfortunately some abstract definitions that you just HAVE to memorize without specific examples (the pumping lemma is infamous for this)
            - "A lot of today's CS problems, like machine learning, are input-driven, where you always have examples of the data you're working with in advance; in this class, because it's dealing with lots of abstract proof stuff, we don't have that luxury and need to be able to think about ANY inputs we could get. I think a lot of confusion has come from people getting confused about that, and not thinking about how the input could be different from what they expect."
    - While the review topics are on the review sheet, here are the most important ones:
        - Alphabet, word, languages, complexity classes
        - Turing Machines (definition, formal and in general), tape configuration (how do you write on a tape?), input encodings
        - Multi-Tape TMs
        - Universal TMs
        - Non-deterministic TMs
        - P and NP, poly-time reductions
            - "Importantly, this first part of the class is basically about set membership; a word is a string made up of alphabet elements, a language is a set of words, and a complexity class is a set of languages"
    - The average grades on the 2 homeworks actually had about the same averages, ~19.4/25 and ~20.3/25, respectively
        - "Question 3 on HW2 actually had an average of ~70%, which was higher than I expected based on the feedback from last class"
            - Remember, we grade this class on a curve; you do NOT typically need a 90% on every question to get an A, and it's okay grade-wise if you solve something incorrectly now and then
        - "Also, while I want to be nice, here's the honest truth: this is a required class. It's not required for me to give everyone As. I grade the class on a curve and try to give everyone late days and plenty of chances to ask questions and succeed, but at the end of the day, you still have to do some work."
--------------------------------------------------------------------------------

- Last week was probably the first time you'd seen reductions in a few semesters - and I messed up! I'm sorry!
    - Formally, a LANGUAGE is a set of strings, and a problem is checking set membership: "does this specific input string belong to this language?"
    - Last time, I said that if we can do a poly-time reduction A $\leq_p$ B, then A must be EASIER than B, and B must be harder than A
        - In other words, we can convert an input for problem A to an input of problem B that'll only be solvable when it's ALSO solvable for A
        - Thus, if we have a program that can solve B, we can ALSO solve A by converting its input!
            - And, since this conversion from A to B can be done in polynomial time, it'll preserve P/NP runtimes! If we can solve B in "P", then we can also solve A in "P"!
    - Currently, there's a lot of problems in NP we don't know how to solve efficiently, which leads us to the idea of NP-Complete - a set of algorithms of the same difficulty that can ALL be reduced to one another
        - This works because of the COOK-LEVIN THEOREM, which says that if a problem L $\in$ NP, then L $\leq_p$ 3-SAT
            - "We'll explain why this works, but I will NOT test you on proving Cook-Levin; I'm just trying to show you how TMs and NP-completeness tie together"
            - First off, note that after "n" steps, our tape is still a polynomial length - and so, for a polynomial number of steps, we could theoretically store ALL of our tape's states throughout the whole program
                - As we've mentioned before, too, Turing Machines are COMPLETELY local - it only modifies 1 thing per step
            - So, between any 2 steps, we can write out all the allowable state transformations between where the head is and where it was/will go (the "gadget" of possible states that could change each step)
            - Using that, we can transform this local set of allowable changes into a 3-SAT instance by writing out all possible combinations of variables that change on our tape between steps and saying "be true if this change was allowed, and false if it was illegal"
                - This 3-SAT string gets HUGE very quickly, so it's not practical to give an example, but it's a conversion that can actually be done in polynomial time for any polynomial number of program steps
        - So, we can reduce ANY Turing Machine into a 3-SAT instance by doing this!
    - So, as SOON as we've shown a problem is NP, we know we can reduce it to 3-SAT - and then, to show it's NP-Complete, we just have to show 3-SAT can be reduced to the problem in question

- Formally, 3-SAT is NP-hard because EVERY NP problem can be reduced to it - that's what NP-hardness means!
    - NP-complete, then, means that 3-SAT can ALSO be reduced to that NP problem, meaning EVERY OTHER NP problem can be reduced to that other problem by going through 3-SAT first!

- Now, let's look at an example of a reduction
    - Let's say we have a 2nd problem "Not-all-equal 3-SAT" (NAE-3-SAT), meaning we have a satisfying assignment where EACH clause has only 1 or 2 trues (NOT 3 falses or 3 trues)
        - First, we need to show NAE-3-SAT $\in$ NP; we can do this either using a Turing Machine definition, or a verifier; here's an example verifier:
            - Take, as an input, an input assignment to x1 ... xn
            - Then, loop through all clauses and count the number of "true" literals in each clause
                - If the number of "True" literals in any clause is 0 or 3, reject
            - If we reach the end of the tape and haven't rejected, accept!
        - Then, after thinking for a bit, we can come up with the following reduction:
            - (x1 or x2 or x3) -> (x1 or x2 or c) AND (x3 or F or !c)
        - While coming up with reductions takes a bit of creativity, we can SHOW this reduction is correct by showing it's only satisfied when 3-SAT is satisfied
            - i.e. We want to show that "x1 or x2 or x3" for 3-SAT is satisfied if and only if we can choose "c" such that (x1 or x2 or c) AND (x3 or F or !c)
            - We can do this here using a proof by contradiction!
                - For this, we want to show
                - Suppose this is NOT true, and we can satisfy the clause "x1 or x2 or x3" without satisfying NAE-3-SAT
                - If x3 is false, then "x3 or F or !c" forces c = False for the clause to be true
                - However, this means "x1 or x2 or c" must all be false as well, so the new clauses are not satisfiable either - but if x3 is false, AND x1 and x2 are false, then 3-SAT isn't satisfied either! Contradiction!

- Alright, study hard for the test on Thursday!