# CFGs (cont.) / Pushdown Automata

## March 5th, 2020

- Okay, some admin stuff:
    - Test 2 grades are out, and while they were a little rough, DON'T PANIC: there's a decently generous curve (as long as you got over ~50%, you're in the B range)
    - The median grade on the test was 17/25 (i.e. D+); my advice would be that if you have ~30 point COMBINED between test 1+2, you're probably in the B-range; if you have 40+ points between the two, I'd say you're safely in the A range for this class
        - "I try to avoid giving Cs to more than ~15% of the class, and a lot of people right now are hovering ~25 points total across both tests, which is concerning"

- Topics for today:
    - Pushdown Automata (formally equivalent to CFGs)
    - Converting CFG to PDAs
--------------------------------------------------------------------------------

- So, we left off last time talking about parse trees, representing all the substitutions we've made for our CFG
    - "As a side note, the reason we call this stuff 'context free' grammars is because we just replace symbols without looking at any of the other symbols around it, meaning none of the sub-problems of replacing the string are dependent on one another"
    - Remember, formally a CFG is a 4-tuple, although we can write them in shorthand form like "C -> $\epsilon$ | (C) | CC" for parenthesis-matching

- Let's look at one more CFG example, for addition/multiplication expressions
    - The language here would look like this:
        - V = {E}
        - $\Sigma$ = {a, (, )}
        - Rules:
            - E -> a
            - E -> E + E
            - E -> E x E
            - E -> (E)
    - One thing we can do here is that we can also create a parse tree BACKWARDS, to get the derivation for a particular expression we're trying to get
        - Let's say we want to form the expression "a + a x a"; how would we make that?
            - For the first addition part we must've gone from E -> a, and before THAT must've gone from "E -> E + E"

                    E
                   /|\
                  E | E
                  | | |
                  a + a

            - Then, we need to add in the multiplication to the tree, and we're done!
                       E
                     / | \
                    E  x  E
                   /|\    |
                  E | E   a
                  | | |
                  a + a

            - HOWEVER, if we evaluate this from left-to-right then we wouldn't get correct expression, since we'd add first to get 2a, THEN multiply to get $2a^2$, when the correct answer should be $a + a^2$
                - To create a correctly-evaluating parse tree, then, we'd need to have multiplication occur FIRST (i.e. lower down) in the parse tree, and THEN add the addition operation
            - "The order in which you generate a sequence from a CFG DOES MATTER," but grammars are ambiguous, so how can we avoid this kind of ordering problem?
                - Well, we can avoid this issue by adding operator precedence to our grammar (which is VERY common in compiler design) via having 2 different kinds of variables:
                    - Products happen between "a" numbers directly
                    - Sums ONLY happen indirectly as sums of products
                - This rewritten grammar would look like:
                    - V = {SUM, PRODUCT}
                    - $\Sigma$ = {a, b}
                    - Rules:
                        - SUM -> PRODUCT | SUM + SUM
                        - PRODUCT -> PRODUCT x PRODUCT | a | b
                    - Start: SUM
                - Now, this'll work because products will always be a child of a "SUM" operation, meaning there will never be multiplications with sums inside them - which is what we want! That's basically what precedence means! 
                    - We can add parentheses back in by adding an additional rule:

                            PROD -> (SUM)

- Now, CFGs are great, but with a slight modification we can also get a DFA that can do everything they can: PUSHDOWN AUTOMATA (PDA)!
    - "This is basically just an NFA with a stack"
    - The idea here is that at every step/state transition we can pop AND push something from it:

        $$
        \delta: Q \times \Sigma \Gamma_\epsilon \implies P(Q \times \Gamma_\epsilon)
        $$

        - ...where $\Gamma_\epsilon$ is something getting popped/pushed off the stack, respectively (you can pop/push $\epsilon$ to not do so, I think?)
    - PDAs have no way to check if their stack is actually empty or not, although you can put an "ending character" that only appears when nothing else is in the stack to get around this
    - Then, the state transitions can be written as "Input read, character popped -> character pushed"
    - Formally, we can define a PDA as a 6-tuple:
        - Q, $\Sigma$, F, and $Q_0$ are all the same as for a DFA
        - $\Gamma$ are your stack symbols
        - $\delta$ is your transition function, changed per the above
    - Formally, then, you start with an empty stack, and accept an input string if you end in an accepting state
        - To verify that your transition function is valid, verify that for every move $i$, there exists an $a_i$ (popped), $b_i$ (pushed), and string (?) $temp_i$ so that:

            $$
            stack_i = temp_i a_i
            stack_{i+1} = temp_i b_i
            (state_{i+1}, b_i) \in 
            $$

- Now, with the last few minutes, let's talk about how CFGs are equivalent to PDAs
    - The basic idea is VERY similar to traversing a tree using a stack, where you can traverse the parse tree left-to-right

- Alright, we'll stop here for now; see you next week!
