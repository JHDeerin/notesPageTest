# Turing Machines (cont.)

## January 9th, 2020

- Professor Peng, PowerPoint on-screen, seems to have corrected his mistake of bringing markers to a 250 person lecture hall
    - The first slide even has an eraser on it that says "for really big mistakes"
    - "I brought my StarCraft mouse to this class, so let's see how this goes"
- On the board, listed:
    - More TMs (Turing Machines)
    - What's a tape?
    - What's a state?

- "Past that, the plan for today is:"
    - Give TM Examples
    - How to represent TM configurations
    - Variants of TMs
        - "We defined Turing Machines last time as pretty simple entities; I want to give you a glimpse today of the Church-Turing hypothesis, which says we can represent ANY computation as a Turing Machine"
        - Multiple tape TMs
            - "We can show this is actually the SAME as a regular Turing Machine"
        - TMs that run OTHER TMs
        - Non-determinism

- Also, some administrative stuff:
    - You should all have GradeScope accounts for this class now! Check and make sure!
    - Homework 1 has been released!
        - Homeworks are always due Thursday at noon, a week after they're released; you can submit homeworks up to 2 days late
            - You have 6 free late day submissions across all the homeworks
        - "Whenever I ask you for a proof, assume that I want discrete math levels of proof, i.e. totally formal mathematical proofs"
    - "I will post my notes, but the textbook for this class is really good; no PDF I can produce will be as detailed as that textbook, and as for free copies, well, Google can produce some wonderful things..."
        - On the course home page, the section numbers for each textbook chapter we're covering
    - I'll have office hours on Friday, from 5-6pm at Klaus 2144; I'll try to find some additional hours on Monday as well, and the TAs will post their own hours as well

--------------------------------------------------------------------------------

- As we said yesterday, this class is automata and complexity, where we're going to analyze the algorithms from 3510 mathematically

- Last time, we started talking about Turing Machines - but what ARE these things?
    - TURING MACHINES are, basically, tape recorders with a couple extra buttons; the idea is that you have a VERY large amount of storage on a single-unit-wide "tape," and a CONTROL UNIT sits on top of the tape and can move left, right, and read/write characters to the tape
        - This "control unit," in other words, is basically just a giant state machine - but unlike the tape, it IS finite
            - "No one wants to draw 600 states when they're designing a computer, so your ALU on your computer often still has a fairly small number of instructions"
            - When people have very intricate circuitry that they need to verify is correct (like, say, launching a rocket), they can go through and check every possible state; for computers with 2^(stupid huge number), though, that's WAY too many states to practically check
                - "The most expensive integer overflow in history happened during the Arian 5 rocket launch, where they used an outdated piece of the software, the weight was heavier than expected, and it exploded"
        - For a Turing Machine, you typically first design a finite alphabet, create your (probably much larger) language set, and THEN design your Turing Machine's states after you know the alphabet
            - Since the alphabet has a finite size, you can add a state to your control unit for EACH character in the alphabet to remember it or figure out what to do when you see it, and that's powerful!
            - "Since we have an infinite size tape but a finite number of states in our control unit, we can't record all possible states or have every possible combination; we have to be cleverer than that"
    - FORMALLY, a Turing Machine is actually scary - it's a 7-tuple!
        - States Q
        - Alphabet $\Sigma$
            - This is the set of all characters that can be valid in our problem's language
        - Tape Symbols $\Gamma$
            - This is a SUPERSET of the alphabet where we add additional "control characters" to control our Turing Machine (I think?)
                - "L and R are usually NOT considered part of this, but are considered outside and special...although if you want to do that, and make life hard, feel free"
        - Transition function $\delta$: Q X $\Gamma$ -> Q X $\Gamma$ X {L,R}
            - In other words, for ANY input combination of our machine's state and the tape character its over, will result in some change to the state, the current tape character, and moving left/right one unit
            - This transition function is probably the most important part of a Turing Machine, representing how it actually gets from one state to another
            - "Remember, this multiplication is a SET multiplication, where we take all combinations between the 2 sets"
            - Technically, Turing Machines can potentially NEVER terminate even for valid algorithms, but we won't deal with that until the very end
        - Starting state $q_0$
            - So, combined with our transition state, the first state will be $q_0$
            - Then, the 2nd state will be $\delta$($q_0$, tape[0]).state
            - The 3rd will be $\delta$($\delta$($q_0$, tape[0]).state, tape[0 + $\delta$($q_0$, tape[0]).shift])
                - Not sure what shift is?
        - Accept/Final state(s) $q_{accept}$
        - Rejection/Failure state(s) $q_{reject}$
    - "When we're drawing FSM diagrams, typically all the states are drawn as circles, and the tape symbols/transition functions are drawn as arrows"

- Yesterday, we had the example of a Turing Machine that would return if 2 strings matched one another, separated by a hash
    - So here, our alphabet is $\Sigma$={0,1,#}, and our language is L = {w#w | w \in {0,1}}
    - The Turing Machine is tracking 2 things with the tape: what symbols are on it, and where the "tape head" reader currently is
        - The tape is infinite, so we'll fill it with some null character initially
            - This empty character will be part of our tape symbols, NOT our problem alphabet
        - We'll assume the tape head will ALWAYS start on the leftmost non-null character, where we're starting computation
        - ALSO: in general, if you don't have a transition for a certain character, go to a rejected state
    - Now, to represent your Turing Machine's current configuration, the general shorthand is this:

            Previous tape part | Machine state | Next tape part

        - Where the FIRST character in the "next" part is the one our machine is about to read/write to
    - So, for a simple machine that writes 0 to all the characters, it might look like:

            $q_{0}$0101
            0$q_{0}$101
            00$q_{0}$01
            000$q_{0}$1
            0000$q_{0}$
            0000_$q_{1}$

    - So, for repeated strings, we essentially check one character at each "pass" through the strings, and if they match, we replace the first characters we've seen in each string with our checked character symbol
        - So, our tape symbols will now include our alphabet PLUS our null and "checked character" symbols

            $\Gamma$ = {0,1,#,:),NULL}

        - We can now design the state machine for this!
            - *state machine on the slides*
            - $q_4$, here, is our "rewind" button; after we've
            - "This only has the logic right now for matching 0s, rather than 1s"
                - "We RARELY draw out our Turing Machines since, basically, they're spaghetti code"

- Okay, we'll FINALLY finish going through this on Tuesday; see you then! Have a good weekend!
