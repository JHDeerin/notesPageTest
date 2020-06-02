# Halting Problem (cont.)

## April 16th, 2020

- "Sorry for the delays in responding to Piazza stuff, this week has been crazy for me"

- The plan for today:
    - Undecidable problems
    - Reductions
    - Undecidability of post-correspondence

- Test 3 grades should be out, and people overall did really well! There was a mean grade of 23.01 and a median grade of 24.0

--------------------------------------------------------------------------------

- Today, I'm hoping to get across what the post-correspondence problem is
    - As we said last time, a Turing Machine is DECIDABLE if it eventually terminates for all inputs, and is RECOGNIZABLE if it eventually terminates for all valid inputs in the language (but not necessarily for inputs not in the language)
        - Notice that infinite loops are unique to Turing Machines, since the input will always terminate for NFAs/etc.
    - As we said, there's a thing known as the HALTING PROBLEM for Turing Machines that says that there are languages that aren't decidable by ANY TM

- We also have this notion of TURING REDUCTIONS, which are where we say $A$ reduces to $B$ if every instance of $A$ can be converted into an instance of $B$ (and the output can be converted back)
    - Basically, as long as we can construct a Turing Machine to do this conversion that always halts (regardless of how long it takes), we can do a reduction
    - The general strategy, then, for showing a problem is undecidable is to show an undecidable problem can be converted *to* it
        - This is really similar to NP-hardness reductions except that we don't have to worry about how efficiently the problem is solved; we're just worry about whether it can be reliably solved at all
    - In other words, what we want is some function $f()$ such that $<M, w> \in A_{TM} \leftrightarrow f(<M, w>) \in L_{HALT}$
        - We can show this by modifying a TM to go from $M$ to $M'$, so that the new TM has the same state but all reject states loop infinitely

- Here are some example of "undecidable problems"
    - One example: deciding whether a language is regular
        - You first convert the input to $M'$, and then modify its accepting state so that it accepts $0^n1^n$ by default, but if M accepts
            - Note that formal reductions can't have negations in them (why?)
            - Therefore, this Turing machine accepts 0^n1^n if it's a non-regular language, and also accepts if regular (???)
    - Whether the language a TM accepts $L(M)$ is the same as (...)

- Alright, with the last few minutes let's talk about the POST-CORRESPONDENCE PROBLEM (PCP)
    - Think of this as like dominoes, where each "block" has a top number and a bottom number

            1       13      2
            -       -       -
            21      3       1

        - We then need to order the dominoes (possibly using repetition) to see if we can get the same number by concatenating all the tops/bottoms, respectively
    - Here's a question: is this problem decidable?
        - ...as it turns out, NO, it isn't!
        - You can show this by converting a TM into a PCP instance, where the top blocks are on one tape and the bottom blocks are on another tape, and (different states for different domino positions?)
        - You can then do a proof of correctness for this reduction, which is a bit lengthy but basically says that the top/bottom string parts correspond to states of simulating TMs (i.e. the top/bottom strings act like stack traces)

- Alright, we'll stop here for the day! Have a good weekend!
