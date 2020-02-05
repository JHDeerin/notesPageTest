# Finite Automata

## February 4th, 2020

- If Dr. Peng were a supervillain he'd do a pretty cruddy job, for HE HAS ALREADY REVEALED HIS MASTER PLAN:
    - Finite automata: no more tape!
    - Regular languages = Languages recognized by DFAs
    - Non-deterministic finite automata (NFA)
    - Converting NFAs to DFAs

- "I see a lot less panic than a week ago. Probably a good thing."
    - The plan for the next 2 months is to take apart the Turing Machines we've been thinking about at a high-level
        - This probably caused some confusion, because algorithms usually aren't a formal thing, while with Turing Machines we asked you to give formal proofs; many people asked me "how formal do I have to be?", and the answer is really, well, just convince me it'll work
            - Those reduction proofs we did were still somewhat informal, since defining an algorithm was involved
        - We start with these things FIRST because I want to give you a high-level overview of all the topics before we start digging into the more formal details
        - The plan for the next month, then, is to get rid of our Turing Machine's tape and start investigating finite state machines, which are MUCH more restricted (you can even convert NFAs TO DFAs!)
            - "However, you can still do some cool stuff with them; we'll show FSMs are formally equivalent to regular expressions, and then get into the really formal stuff by showing there are some things regular expressions CAN'T do (since finite states don't handle aperiodic behavior well)"
        - We'll then talk about something terrible and confusing called the pumping lemma next week

- More presently, Test 1 grades are out - and people did pretty well!
    - The class average was a 21/25, with a slightly higher median (~22.5 or so)
        - "I think you've convinced me that it's hard to make a test that as a CLASS is too hard, but individual "
    - ...I mean, he did make the test very reasonable (as an understatement)...
    - As per usual, you have 1 week to submit any regrade requests, and we'll try to make the grading scheme more clear

--------------------------------------------------------------------------------

- So, what's a finite automata?
    - Basically, a DETERMINISTIC FINITE AUTOMATA (DFA) is a Turing Machine that can ONLY move to the right and has a read-only tape
        - This means our transition function simplifies from:

            $$
                Q \times \Sigma \implies Q \times \Sigma \times \{L,R\}
            $$

        - ...to...

            $$
                Q \times \Sigma \implies Q
            $$

        - So, our transitions are MUCH simpler now: we see an input in some state, go to another state! That's IT!
            - One weird thing here, though: you COULD have multiple accepting states, and can keep running even when it has accepted
            - When we run a DFA, it just runs until the input tape is entirely used up, and accepts if it's in an accepting state when that happens (and rejects otherwise)
    - "Notice that this is a strict subset of a Turing Machine; a DFA doesn't do anything a TM can't"

- So, to write down what steps a DFA has gone through, we literally only have to write out the states it's been in (e.g. q1->q2->q3->q2->q3->q2...)

- Let's now talk about regular languages
    - REGULAR LANGUAGES are those that for some DFA "M" are the set of strings that can be accepted by "M"
    - Let's give an example of this
        - One classic arithmetic trick is that to figure out if a number is divisible by 3, you can add all the digits and check if that number is divisible by 3
        - Let's express this trick via the following:

                X -> x0, x1     // x0 is if we see a 0 as the next character, x1 is if we see 1 as the nxt character
                x0 = 2x
                x1 = 2x+1

            - So, to decide if a binary string is divisible by 3, we can do this:

                    x mod 3 | x0 mod 3  | x1 mod 3
                    ------------------------------
                    0       |   0       | 1
                    1       |   2       | 0
                    2       |   1       | 2

                - As an example of why this works, on the input 100101, the decimal number would be:

                        1       = 1                     q1
                        10      = 2 = 2*(1)             q2
                        100     = 4 = 2*(2)             q1
                        1001    = 9 = 2*(4) + 1         q0
                        10010   = 18 = 2*(9)            q0
                        100101  = 37 = 2*(18) + 1       q1

            - If we then treat this as the transition table for a 3-state DFA, we can accept any string that's divisible by 3! Therefore, this "binary string's divisible by 3" is a regular language

- Now, we can show that ANY finite language (i.e. a language with a finite number of strings in it) can be encoded in a DFA - and, therefore, is a regular language!
    - The basic idea behind this is that you can make a trie, then extend it, to exactly label each possible string in the language, so that you'll only reach an accepting state if we EXACTLY see the sequence of characters for one of the strings in our language
        - If we ever fall out of sequence, just go to a $q_{reject}$ state and stay there in a loop!
        - *someone points out a bug in his slides;* "I'm averaging 1 mistake per example - not bad!"
    - If you wanted to go deep, you could generalize this into an algorithm for making an automata for any regular language - but we'll skip over that

- With the last few minutes, let's talk about non-deterministic finite automata
    - This is the same deal as for TMs, where we can have multiple possible transitions for a given input and take any of them
        - The only new thing is what's called EPSILON transitions, which mean possible transitions we can take WITHOUT reading anything on the tape (basically letting us skip a state)
            - These just make writing NDFAs easier
        - The caveat here is that we accept if there's at least 1 way to take the transitions to get to an accepting state, while consuming the whole input
            - *hears email alerts on computer;* "Are those all the regrade requests? Already?"
    - Many of these NDFAs allow us to look for sub-strings, which is a SUPER common task in regular expressions
        - However, we can't run NDFAs directly - we need to convert them to DFA! Can we do that?
        - Well, we can do it by creating a state for EVERY possible subset of states we could be in, and accept if any state in the subset end in an accepted state

- Alright, we'll keep talking about this next class!


