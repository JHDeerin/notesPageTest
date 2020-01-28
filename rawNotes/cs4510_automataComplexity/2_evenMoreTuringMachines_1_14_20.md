# Turing Machines (cont.)

## January 14th, 2020

- Today's agenda, prominently displayed:
    - TM for L = {w#w | w $\in$ {0,1}}
    - Multiple tapes
    - TM running TMs running TMs
    - Non-determinism

- So, for office hours right now, we're basically playing a giant game of hide-and-seek in the CoC; the main common area is crowded, so we're going to bounce back-and-forth between several rooms that're less commonly used
    - Also, note that homework 1 has been updated to have some clarifications; the problems themselves haven't been changed, so don't worry if you already started working on it
    - The homework shouldn't be too bad; "the set questions just depend on the definition of a set, not on any theorems, and should be pretty similar to discrete math stuff you've seen in the past"
        - You don't have to be AS formal as you were in discrete math, following a template - you just have to be mathematical and show proofs
        - For $q_{reject}$, we don't care if your tape head goes left or right, since we didn't specify that behavior
        - For the 3rd question, you do NOT need to prove your Turing Machine is correct; that's formal verification, and that's a WHOLE separate topic
            - Instead, you just need to show your algorithm itself is correct
            - Also, "deciding" for a Turing Machine means that the program will eventually terminate

- Remember: the homework is due this Thursday at NOON!
    - You do have a late day, should you choose to use it, but you might as well save that up just in case
    - "I recommend you use these late days sparingly, if you can; we know we've messed up and made a homework too hard when we get a bunch of late submissions, and we pay for it by only having 2-3 days to grade late stuff"

--------------------------------------------------------------------------------

- So, remember that a Turing Machine is formally defined as a 7-tuple; it's essentially a state machine with an infinite tape of data attached
    - As we mentioned, for each tape symbol we read, the output action is a symbol we do/do not replace it with and the tape head moving left/right
        - What makes this interesting is that the state machine itself doesn't really have memory; if we want to remember things long-term aside from trivial state changes, we need to use the tape itself
    - Now, the algorithm we've been talking about is actually an O(n^2) algorithm, since we need to go to the 1st character, traverse the whole string to find a match, go to the 2nd character, traverse the whole string again, etc.
        - In the state machine for this algorithm, the whole top part is it using its states to remember if it's seen a 0 or not
        - You then skip all the already-matched, happy-face characters
        - The bottom part, then, is just to rewind the tape once we've actually found a match
    - "I know we're going through this Turing Machine state example very slowly, but the whole concept of a TM is ESSENTIAL to the rest of this class, and I want to make sure you all understand it"
        - We can then handle 1 by essentially mirroring the top states and flipping them to work for 1
        - *spends some time debugging the machine to correctly reject different-length strings, so that it has to traverse ALL happy faces before it returns that the strings match*

- This is the essential part of a Turing Machine: you use the states to set up a badly-formatted if-statement/for-loop to remember what we need to be doing
    - Designing Turing Machines gets a little crazy because you have to think about EVERY possible computation path, meaning they're very bug-prone
    - In this class, we'll also assume that if a state transition isn't specified, it automatically counts as a "rejected" state
    - "The reason we work with Turing Machines is because they only work in polynomial time; it isn't an accurate representation of real-world computer memory, so Turing Machines are basically never used to design efficient algorithms"

- Okay; I know this was SUPER slow, but the rest of the class is actually less diagram-intense, and should move a little bit faster

- So, since we can't draw state diagrams practically for super-huge state spaces, we'll talk about Turing Machines more abstractly now
    - What if we have a TM with TWO tapes?
        - You can simulate this on a single-tape TM by just concatenating the 2+ tapes together, with some special character separating them AND a special character marking where the tapehead is for each tape, and then making a bunch of extra states for when you're on the 1st/2nd/etc, tape
        - "These are Turing Machines that're too complicated to actually implement for most purposes (since your input state is now every possible PAIR of characters), but we can think about them at a high-level"
            - One thing that DOES help us is that Turing Machine computation is purely local, so we don't need to remember every state combination
            - "Don't treat Turing Machines as a computer; treat them as very low-level programs with a very limited instruction set"
        - With multi-tape Turing Machines, we basically can implement (in a very inefficient way) random-access memory - cool!
    - In this class, always give us the high-level description of what your Turing Machine actually does and what the different pieces of the FSM do
        - Then, just give us the implementation details instead of all the explicit states (unless we ask for you to do that)

- From this, you can also build something cool: the UNIVERSAL TURING MACHINE!
    - These are where we take a Turing Machine "M" as an input ALONG with a given tape "x," and returns he results of running "M" on x
        - It's possible for M to have even more states than our universal TM itself (which we can solve by encoding those extra states in some way on a tape)

- So, the last thing we'll talk about is Time Complexity!
    - We say a given language $L$ is in Time(f(n)) if there exists some Turing Machine such that for ALL inputs of length $n$, the TM accepts/rejects the input within O(f(n)) steps
    - Turing Machines play nice with this because they are GUARANTEED to run in POLYNOMIAL TIME (I think?) under certain conditions, meaning we can write its runtime as O(n^k) for some finite "k"
        - In other words, P means the language is:

                TIME($n^k$)

    - If the input to our Turing Machine is polynomial, then it'll complete in polynomial time (I THINK?)

- Alright, next time we'll talk about non-determinism - stay tuned!