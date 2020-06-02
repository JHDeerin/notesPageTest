# Exam 3 Review

## April 7th, 2020

- A man, a plan, a Twitch channel - Richard Peng!
    - Today's aforementioned plot:
        - CFGs, parse trees, and how to make them
        - PDAs and how to make them
        - Pumping lemma for CFG

- "Today will mostly be review, especially from Homework 5, because REMEMBER: you have a test this Thursday!"
    - The test will be from 11:00am - 1:15pm, this Thursday (April 9th, aka Maundy Thursday)
        - It should be released on the course homepage AND on Canvas
        - If you have questions during the test, we'll have TAs both on our office hour link on BlueJeans and monitoring Piazza
        - You can submit the test as a PDF, either scanned from paper or typeset on Latex (though he'd recommend not trying to do TIKZ diagrams under time pressure)
    - If you average ~80% on all the tests, I'd say that's fairly safe to be in the A range post-curve
    - The test is VERY similar in structure to Exam 2, but hopefully a bit easier
    - The study guide is up, and I'd also recommend looking at a) homework solutions, and b) questions with answers in the textbook (Chapter 2)

- "We also decided we will NOT ask you to convert between PDAs to CFGs on the test; they're really only useful as a construct for proving PDAs are equivalent to CFGs, and you'd very rarely want to actually convert between them"

- "Pigeons don't broadcast very nicely, so I don't think they'd work for streaming in the apocalypse" - Dr. Richard Peng, esteemed Georgia Tech Professor
--------------------------------------------------------------------------------

- As we've said already, CONTEXT-FREE GRAMMARS are basically where we have variables that we keep replacing recursively with some combination of other variables and/or literal characters
    - Any string we can potentially generate in this way is part of a CONTEXT-FREE LANGUAGE
    - For instance, consider the language $\{w = w^R | w \in \{0,1\}\}$ (basically, palindromes)
        - A valid CFG for this would be $S \implies \epsilon | 0 | 1 | 0S0 | 1S1$
        - "Remember, you have to not only generate all the strings in the language, but also ONLY generate all the strings in the language"
    - To think about if a certain CFG would accept a given string, you can either try to come up with a sequence of substitutions that would get you that string (S -> 0S0 -> 01S10 -> ...), or create a parse tree
        - A PARSE TREE has the starting state as the root, and then visually represents how everything gets generated, with the variables/literals represented
            - For a given string, it is possible to have multiple valid parse trees
        - You SHOULD know how to make a parse tree, but it's pretty similar to building a regular CFG derivation

- Another CFG example: $\{a^ib^jc^k | i=j OR j=k\}$
    - This one is weird because you have to deal with cases, but you can do it by adding extra variables: X = the 1st case, Y = the 2nd case

            S -> X | Y
            X -> Xc | AB
            AB -> aABb | $\epsilon$
            Y -> aY | BC
            BC -> bBCc | $\epsilon$

- Now, PDAs are basically NFAs with a stack we can push/pop characters to each transition (or not push/pop by pushing/popping $\epsilon$)
    - You can read these transitions as "(input char, popped char -> pushed char)"
    - So, a PDA for the palindrome language would look something like this:

                            (1, e -> y)   (e,1 -> e)      (1, y -> e)
                            (0, e -> x)   (e,0 -> e)      (0, x -> e)
            ->q0--(e,e -> $)--->q1--------(e,e -> e)------->q2
                                                            |
                                                            |
                                                        (e, $ -> e)
                                                            |
                                                          qAccept

    - PDAs have a few interesting things about them; for instance, they do NOT stop early (unlike Turing machines), and need to consume all of their input, and are non-deterministic

- Finally, we have the pumping lemma; you want to pick a string so that all the possible split cases are easy to handle
    - We do NOT require you to prove the pumping lemma, but you do have to use it!
    - Let's take the example of proving $\{0^i1^j0^i | i \leq j\}$ is NOT context free (from the homework)
         - For this, make your string $w = 0^p1^p0^p$
         - From there, then, there's just 2 cases - in fact, we can actually do the proof with just 1!
            - Since $|vyp| \leq p$, it can't overlap both blocks of 0s
            - Therefore, if you pump with i=0, this has less than $3p$ characters, but one of the 0 blocks still has $p$ characters - meaning either the 2nd block has less characters $\neq i$, or $j \leq i$
                - Either way, the resulting pumped string isn't in the language!

- Alright, good luck on the exam and I'll see you all later!
