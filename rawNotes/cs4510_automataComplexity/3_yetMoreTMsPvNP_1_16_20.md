# Odd TMs and P/NP

## January 16th, 2020

- So, what wonders await us in Mathland today?
    - Turing Machines using only implementation details
    - Non-determinism
    - The class NP
    - Reductions and NP-hard problems

- "We seem to be converging on a microphone setting of 78 - super!"

--------------------------------------------------------------------------------

- Okay, the plan for today is to review NP-completeness - but with Turing Machines!
    - Hopefully, this'll make why you did all those 3SAT computations back in 3510 more concrete
        - "NP completeness actually comes from Turing Machines, but we shy away from that in regular algorithm classes because we now use a RAM memory model, which has much less overhead then regular TMs"

- Last time, we talked about 2 things that can help you implement Turing Machines:
    - Multi-tape Turing Machines are formally equivalent to a single-tape one, but they can simplify our implementation GREATLY by allowing us to use a 2nd tape to store variables!
        - When we have a single-tape, we have the issue that variables can be arbitrarily long - and when we have an infinitely-long tape, that means they can be INFINITELY long! There's no such thing as an integer overflow in these things!
            - "States act like flowcharts, not like variables; we can't store things in our states"
        - So, having a 2nd tape, we can actually start doing stuff like having counter variables, etc, because we now have an infinite-length tape to store them on!
            - "In your first homework, when I gave you the Turing Machine, probably everyone's first reaction was to "
            - Sidenote: "OS isn't a required class here? I chose the wrong undergrad!"
                - When you DO have a multi-tape TM, though, you can use variables by implementing a hacky version of a memory manager, similar to in OS design, and by coming up with some encoding scheme
        - Formally, though, having a multi-tape TM means that your transition function now takes an input from ALL tapes at each step
            - So, the formal definition looks like:

                $\gamma = Q \times \Gamma^2 \implies Q \times \Gamma^2 \times \{L,R\}^2$

            - And, as we mentioned before, this can be converted to a single-tape TM by essentially concatenating the tapes together and keeping track of the head positions, but you'll NEVER see people writing out the state machine for this because it makes the FSM massively complicated
                - Instead of just going from one state to another, you now need to get to the tape head of the 1st tape, switch to the proper state, go the 2nd tape head, switch to that one's proper state, then compute the resulting state from BOTH of those inputs, then modify the 1st tape, then modify the 2nd tape, then go to the new state
                    - EACH of these steps requires several states, and that's for EVERY state you had in your original state machine - "unless you're running out of graffiti ideas for a very large wall, you don't want to deal with that"
                - You'll now
        - To specify Turing Machines at a higher-level with implementation details, then, you'll set up a description for what larger operations like "rewind tape" mean, and then describe your TM in those terms
            - These won't be as formal as mathematical set theory, but you need to convince us that you COULD figure out how to write the state diagram for this stuff if you had to
            - Literally, an encoding of a TM is a binary/etc. string in your language that can represent the 7-tuple describing a TM, which you can then pass to a universal TM
            - You then specify shorthand ike "fetch variable" instead of having to list the explicit states for every single operation

- So, let's define P
    - Last time, we said a language $L$ is in TIME(f(n)) if there is a TM $M$ such that for all inputs $w$ of length $n$, $M$ correctly accepts or rejects $w$ in O(f(n)) steps
    - Using this definition, we say that POLYNOMIAL TIME, or "P", means that:

            P = $U_k$ TIME($n^k$)

        - Notice this definition has Big-O built into it!
        - Polytime got introduced as a notion for algorithmic efficiency when a researcher was working on general graph-matching, and the reason TMs are so powerful is that almost ANY kind of reduction we can do to a TM will still keep it in polynomial time - you can get CRAZY high exponents, but in general, it'll run in P!
            - Also, note that this isn't dependant on the number of tapes we have in the Turing machine; if $L$ can be decided in poly-time by a multi-tape Turing Machine with $k$ tapes, it can also be decided in polynomial time by a 1-tape TM (since it'll at most go from O($n^c$) to O($n^{2c}$), since there's only O($n^c$) extra overhead per step we do)

- One thing people didn't understand, though, was how non-determinism affected the efficiency of TMs
    - NON-DETERMINISM means that there are multiple possible transitions from a given state/input, and the TM accepts if there's a way to take the transitions to get to $q_{accept}$
        - What this means is that when there're multiple possible transitions for certain inputs, we can go down any one of them
        - This notion of non-determinism just means we're searching over ALL possible outcomes, and if there's ANY of them where it's true, we accept
            - So, it'll accept for a given string if there's ANY way to get to $q_{accept}$ for a given input eventually, imagining it chose its routes perfectly
    - We now say that a language is in non-deterministic time, or "NTIME(f(n))" if there is a TM such that for all inputs $w$ of length $n$, the TM correctly accepts/rejects in "O(f(n))" steps for ANY possible, valid sequence of transitions (i.e. I'm assuming time it takes to traverse ALL possible states it could be in, I think???)
        - We can now define NON-POLYNOMIAL TIME, or NP, using this definition:

                NP = $U_k$ NTIME($n^k$)

- "Okay, I got a LOT of questions over the break, so we probably won't get to NP hardness today"
    - Saying if a given language of a TM is P or NP is VERY difficult; it's very difficult to say what a given TM will do in advance
    - What we CAN do is, given a language specification, and a TM, we can prove that language is in one class or the other
        - Importantly, these P, NP, TIME and NTIME classes are all sets of LANGUAGES that take that much time, NOT TMs
            - P is a subset of NP, since it runs within that time
    - Now, by definition, we can say that TIME is a subset of NTIME:

            TIME(f(n)) $\subseteq$ NTIME(f(n))

        - Later, we can prove that:

                NTIME(f(n)) $\subseteq$ TIME($2^{O(f(n))}$)

- This leads into the idea of a universal turning machine
    - This is a TM that can run another TM by writing out the other Turing Machine's states/defining tuples as inputs we've encoded, and we can then put this TM on one tape and its input on another
    - "This is the same as the definition of non-determinism" (???)

- Finally, briefly, let's talk about reductions
    - If language A is poly-time reducible to another language B, then we say A $leq_{p}$ B if there's a poly-time function "f" such that:

             w \in A \iff f(w) \in B

        - In other words, if there is a function in P time that can map between an input in language A to the same input in language B
    - This'll lead to the Cook-Levin Theorem, which says that if L is NP, then it's equally as difficult as 3SAT (or, in other words, it cn be REDUCED to 3SAT)

- Okay, we'll stop there for today.