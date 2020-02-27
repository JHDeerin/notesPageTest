# Regular Expressions and NFAs

## February 11th, 2020

- Alright, today's plan:
    - Convert regular expressions to NFAs
    - Convert NFAs to regular languages
    - Pumping Lemma
        - "This is getting very far into proof-territory, and you really can't think in terms of input examples or the input alphabet, since they'll be infinite; instead, you have to think of these in terms of your known states"
        - With a small number of states, we can accept any number of strings

- Also, don't forget homework 3 is due this Thursday!
--------------------------------------------------------------------------------

- As we mentioned, regular expressions are defined recursively as regular languages with 3 operations:
    - UNION, accepting either of 2 possible strings (e.g. accept "(b or c)at")
    - CONCATENATION, sticking 2 strings together
    - KLEEN STAR (*), which means there are 0+ copies of the preceding character/characters
        - "L*" means 0 or more copies of a word in some language "L"
        - "$\Sigma$*" means the language also containing the characters from $\Sigma$
            - Essentially, $\Sigma$ is the set of characters, but we treat each character as its own string so it's technically treated as a language
            - So, if L = {000}, then L* = {$\epsilon$, 000, 000000, ...}

- Alright; let's keep trying to prove that regular expressions give regular languages, meaning that they can be accepted by an NFA/DFA!
    - We do this by starting out with the base case of the empty string $\epsilon$, a single character $\Sigma$, or the empty set (which always rejects, since there are NO states/characters now)
    - Then, by induction, we assume the hypothesis is true and show that this holds as we add more characters!
        - For Kleen Star, in words, the proof is like this:
            - Let M be an NFA such that L(M) = L with starting state q0 and some accepting states
            - Then, create M' for L* by:
                - Creating a new starting state q'
                - Adding $\epsilon$ transitions from:
                    - q' to q0
                    - All the accepting states to q0
            - However, we still need to prove that if w is accepted by M', then w can be written as a sequence w1 ... wk, such that each is in "L"
                - We ALSO need to show the other way: if a string "w" is in L*, that it WILL be accepted by M'
            - "You CAN do this proof by bijections instead, but I wouldn't do it, because it's confusing"
        - For union, it's simpler; you just take Q_start, then split into 2 separate branches, one using L1's machine "M1" and the other using L2's machine "M2"
        - For concatenation, you go from your accepting state to the start of the "L2" string (using M2s accepting machine) via $\epsilon$-transitions
            - There's 1 tricky case that's similar to our 1st homework: if L1 = {a, aa} and L2 = {ab}, then you don't want to falsely reject "aab"
            - To deal with this, you have to go from ALL accepting states in the 1st language to the starting state of the second language
    - So, in all cases, we can convert it into a DFA - so they're equivalent!

- Okay, let's look at an example!
    - Let's suppose we have a fairly simple regular expression:

            (a or b)*aba

        - So, to start off with our union, we'd do an $\epsilon$-transition split from our starting state to either "a" or "b," and go to an accepting state like so (no character for transition means $\epsilon$-transition):

                q1--a->q2_accept
                |
                q0
                |
                q3--b->q4_accept

        - To handle the Kleen Star "*", then, we need to create a new accepting state "q5" and take an $\epsilon$-transition from our current accepting states to it - and make our old accepting states no longer accept - to make that part optional:

                q1--a----->q2
                |           |
                q0<---q5_accept
                |           |
                q3--b----->q4

            - "Note that, right now, q2/q4 are kinda redundant, since you can skip it and go straight to q5"
                - So, we could simplify this NFA, but that would make our transformations we're doing less clear
        - Finally, to handle concatenation, we need to go from our current accepting states (i.e. q5) to the set of new states that'll accept the concatenated string "aba":

                q1--a----->q2
                |           |
                q0<---q5_accept--->q6--a->q7--b->q8--a->q9_accept
                |           |
                q3--b----->q4

- Okay, let's now cover the other direction and convert from NFAs to regular expressions
    - First, we can simplify our NFA to a single accepting state by adding $\epsilon$-transitions, making it a GENERALIZED NFA
        - This means that instead of single characters being our transitions, we can think of entire regular expressions being our transitions
        - e.g.:

                q0--x->q1--y->q2
                       ||
                        z

            - The "z" here is a self-loop on q1 when we see a "z" character
        - Goes to:

                q0---xz*y---->q2

            - "Implicitly, there's also the union here of all other transitions from q0 to q2 that we DON'T see"
            - Side-note: (a or b)* is NOT the same thing as a\*b\*, since in the latter, we can't have strings like "aba" where the characters are mixed
    - Once we've done this, we can keep eliminating edges more and more until we eventually just end up with 2 states: the starting state, the accepting state, and the regular expression for the NFA connecting them

- "Okay - what I want to talk about for the rest of this class is how to prove a language is NOT regular"
    - Here's an example of a non-regular language:

            L = {0^n1^n | n >= 0}

        - How can we do this? Well, first, let's assume "L" is regular, meaning it has a DFA "M" that can accept L
            - Remember: DFAs by definition have a FINITE number of states
        - Let M have "p" number of states
        - Then, consider the string 0^(p+1)1^(p+1)
            - Since there are p+1 "0" characters in this string, but only "p" states, it MUST have looped at some point - in fact, it must have looped when it was ONLY reading 0s
            - THEREFORE, we CAN'T keep track of the exact number of 0s we've seen using only our "p" states, meaning the DFA can't verify that the number of 0s matches the number of 1s
                - TMs can handle this since they can write stuff down/edit the string, but DFAs ONLY have states - they're stuck!
        - Therefore, no DFA "M" can decide this language, so it isn't regular!
            - "Notice, here, that you don't get to design your machine around some known input - instead, I get to be mean and AFTER you've designed your machine, I can pick ANY input that causes it to fail!"
    - So, we've got a proof by contradiction that this language can't be regular!

- This looping idea is at the core of something super important, called the PUMPING LEMMA!
    - ...which states: "If A is regular, then there exists some p such that for any w $\in$ A with |w| > p, there is a split of w = xyz with |xy| <= p such that for all i >= 0, $xy^iz$ $\in$ A"
        - Breaking this down:
            - If A is regular,
            - then there exists some p such that
            - for any w $\in$ A with |w| >= p
            - there is a split w = xyz with |xy| <= p, |y| > 0
            - such that for all i >= 0
            - $xy^iz$ $\in$ A
        - TODO: Double-check I copied this correctly?

- We'll go through PLENTY more descriptions of this over the next week; stick with me, and let's go!
