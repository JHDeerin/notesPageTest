# Reductions

## January 23rd, 2020

- Apparently, for the 3rd homework problem (based on some side discussions) remember that 2^t - even if it's a VERY large constant - is still a constant, and therefore can be ignored for O(n) purposes (and thus doesn't affect if it's P IF YOU'RE CAREFUL - the most obvious algorithm )
    - The textbook itself recommend "trying when t is a power of 2" as a hint
    - For the encoding scheme, you're literally just giving a way for you to tell "k,p,q,t" apart from one another by "encoding" it in the language {0,1,#}
        - So, use {01} to give a binary ID to each, then separate each character using "#"?

- A couple announcements:
    - I'm getting feedback from the TAs that here's a LOT of homework 2 questions in office hours; the way these homeworks are is that question 3 is MEANT to be tricky
        - It's a math, proof-style question; "when I gave this as a quiz question last year, only 4 people solved it"
        - It's VERY much a math puzzle, so I'll talk a little bit about it over intermission
            - I'm sorry people are finding this to be so difficult, but it's a mathematical question and is fundamentally in that vein; this course is required not because we're trying to learn math puzzles, and I know some people aren't interested in that at ALL, but because
            - "Tests, I'll write so that you can solve everything; for homeworks, I'll occasionally put a really hard problem like this to "
            - Here, you can't check a Turing Machine/verify that it works, so you're trying to find a way to work around that fact and construct a way to simultaneously construct the output of ALL possible Turing Machine up to a certain size
                - One concept I was surprised people didn't know was self-reducibility, which was the idea that if I can solve 3SAT, I can solve problems that reduce to 3SAT by converting the problem BACK
                -
            - 3 is actually a thinly-veiled version of converting a non-deterministic TM into a deterministic TM; instead of checking all verifiable strings, you're checking all possible Turing Machines
                - ...HOWEVER, we can represent Turing Machines as strings!
    - "Question 1, I didn't realize that people didn't know what permutations in a Turing Machine context were"
        - I thought you knew how to multiply permutations like you knew how to multiply numbers, so this was a big oversight on my part
        - I'd recommend you read about permutations again in a programming theory context; if you don't want to, just pretend they're a number you can multiply and divide, but you CAN'T add (since they're a group operation)
            - Once you do that, you can do fast exponentiation to get a P-time algorithm, since it's associative
        - Also, for how much detail you should go into: basically, give us a 3510 style algorithm in terms of how things are represented on the tape
            - So, talk about HOW you represent stuff on the tape, and then give us an abstract algorithm
                - "Convince us that you know how to solve this problem; look at section 3 in the textbook, although it's unfortunately not perfect"
            - On our end, all of these high-level solutions for the TMs are just in 3-5 lines; it's not supposed to be insane
    - There are some extra office hours tomorrow from 12:30-2:30

- People had less questions about problem 2, but:
    - Remember that P is a subset of NP, so proving something is NP just means showing it CAN be decided by a non-deterministic Turing machine (pg. 266 of the textbook)

- "I think a lot of frustration is coming from people feeling a disconnect between what we're doing in class and the homework, which comes from us not realizing that you didn't know these things we assumed were background knowledge"

- Plan for today:
    - Go over 3SAT
    - Reductions
    - Brief overview of Cook-Levin proof
    - 3SAT reduction example
--------------------------------------------------------------------------------

- Alright; some people unfortunately told me they didn't learn 3SAT in 3510, which is BAD since it's supposed to be in the syllabus - complain to those professors, please!

- Anyway, let's talk about non-deterministic polynomial time
    - Each state has multiple transitions possible; we measure non-deterministic time as the LONGEST possible sequence of operations our Turing Machine could possibly take, EVEN IF there's a sequence it could take that would result in it finishing very quickly
        - So, if it were even POSSIBLE for the non-deterministic TM to end up in an infinite loop, we'd say it will NEVER terminate
    - NP is then the UNION over all "k" NTIME time-classes from 1 ... k (I think?), which is why we write it as:

            NP = $U_k$ NTIME(n^k)

        - As we proved last time by considering branches, we showed that:

                NTIME(f(n)) $\subseteq$ TIME(2^{O(f(n))})

            - Since we assume the size of a Turing Machine is constant, we COULD check all possible outcomes at every state for a given input, keep track of the states and transitions we took on a separate tape, and then find the fastest sequence it took to accept/reject
                - "Remember how for NP, people mentioned the algorithm was still verifiable in Polynomial time? Making this verifier string and running it MUCH faster than it took to find it is an example of that!"
            - How can we run a TM backwards? This is a bit of an aside, but you basically make a recursion stack
                - "You can do it in multiple ways; there's a LOT of absurd things you can do with a Turing Machine, since they're literally computationally complete"
        - Going from a sequence of operations we took to actually doing those operations on a TM is VERY similar to the idea of a Universal Turing Machine

- Non-deterministic TMs are reducible in polynomial time to 3SAT
    - "We're covering poly-time reductions before we get to reductions in general"
    - We covered one way to write this last class; you can ALSO say $A \implies B$" in polynomial time, and it's equivalent (i.e. "you can transform some input A to a different input B in polynomial time")
        - NP-complete means that these problems are EQUALLY hard; reductions alone, however, means "if I can solve problem B in poly-time, I can ALSO solve problem A in poly-time," meaning A is an easier problem than B
    - Recapping what 3SAT is again:
        - We have x1...xn variables, and we have "clauses"/groups of 3 variables, which we combine with AND/ORs, and we're trying to find a way to
        - For the general "SAT" problem WITHOUT this grouping into clauses, we can reduce it to 3SAT bY:
            - First, splitting the bigger clauses up by adding an intermediate variable that keeps the same truth value!
                - e.g. (a or b or c or d) -> (a or b or !e) and (e or c or d)
            - Notice it makes no different if we duplicate a literal multiple times in a clause, so we can turn shorter clauses like (a or b) into (a or b or b)
            - So, writing this in pseduocode, we can say:

                    encode the input as:
                        k_i = # of variables in clause i
                        n = # of variables
                        m = # of clauses

                        <n, m, k_1, L_11 ,..., L_1k_1, ..., k_n, ... L_mk_m>

                    while there's a clause with k_i > 3:
                        Rewrite the clause into group of 3
                        Rewrite the value of "n" and "m" to keep track of our variables/clauses
                    while there's a clause with k_i < 3:
                        (...)

        - So, since we can convert SAT into a 3SAT problem, it's a reduction!
            - And, by the Cook-Levin theorem, since 3SAT is NP-complete, SAT must ALSO be NP-complete
    - How can we show such reductions are in polynomial time, though?

- Okay, we'll keep reductions purely between 3SAT for the purposes of this class; I'm sorry we didn't get as far as we wanted to today, but good luck on the homework and come to office hours if you're confused. It's due Saturday at noon.