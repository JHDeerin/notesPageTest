# The Halting Problem

## April 14th, 2020

- Test 3 is still being graded, but the initial grades look pretty in-line with what we expected (i.e. definitely higher than last test)
    - Exam 3 grades will probably be released either tonight or tomorrow
- THE PLAN:
    - Recap of TMs
    - An Undecidable Problem
    - Decidability vs Recognizability
    - An Unrecognizable Problem
    - Proof that the Halting Problem is hard

- Also, the CIOS format has been changed for this semester to handle online classes, but that means I can't see the feedback rate, so :/
- Homework 6 is out, but remember that the lowest homework will be dropped, so it'll probably be optional for some people

- Also, the Twitch chat is asking for a Professor Peng vs Professor Vigoda Starcraft match
--------------------------------------------------------------------------------

- So, this semester, we talked about Turing Machine's at the very beginning of class; now, we're going to talk about TMs in a really abstract way to show that there are some problems that TMs CAN'T solve!
    - If you remember, a Turing Machine is basically an FSM with a tape attached to it that it can read/write to
        - Formally, we can represent it as a 7-tuple
        - Since we can rewind, non-determinism isn't necessary anymore to solve problems with TMs
    - We can make Turing Machines even MORE powerful by using multi-tape TMs and Universal TMs, which run other TMs
        - With TMs remember that there are 3 possible outcomes: accepting, rejecting, and infinitely looping on an input
        - Universal TMs, then, output the outcome of running the other TM $M$ on some input $w$

- With universal TMs, though, there's something surprising: there's a such thing as an UNDECIDABLE problem, meaning that there's no Turing Machine that will eventually accept/reject
    - What does this problem look like? Well, one example is:

        $$
            A = \{<M,w> | M \text{ is a TM, and } M \text{ accepts input } w\}
        $$

    - We can show there is no TM that can decide this problem for all inputs!
    - In contrast, RECOGNIZING just means that we need to have a TM that can simulate running a different TM on some input - "recognizer" don't have to terminate, so it's less stringent than deciding
        - In short, a TM DECIDES a language if:
            - For all inputs $w$, $M$ accepts or rejects $w$ correctly
        - A TM RECOGNIZES a language if:
            - For all $w$ IN the language, it accepts, and for all others it rejects OR keeps looping indefinitely

- (INSERT HALTING PROBLEM SLIDE HERE, YOU LAZY COWARD!)

- One TM whose halting might be difficult to tell is a TM that keeps looping over all even integers and checking if they match the Goldbach conjecture
    - A RECOGNIZER would just run this program and keep going
    - A DECIDER would tell us if the Goldbach conjecture is true or false
    - Here's a claim: a program that can recognize this language can ALSO give a decider for it
        - Suppose we run 1 TM to recognize $L$ and another it's complement $\not L$, and output the first one that terminates
        - If we run 1 TM that recognizes $L$ and another than recognizes $\not L$, then for any given input, one of the two TMs will terminate because the input is/isn't in the language (???)
            - "I won't try to talk about this too formally in this class, but I hope you get that there's computations that, if they ARE possible, imply there'd be some pretty strange things"

- Now, we talked a long time about REDUCTION, saying that A reduces to B if we can transform problem A to problem B somehow
    - If we remove even the polynomial times part, we say a TM reduces to B if there is some function computable by Turing Machines that decides a given input
        - As an example, checking if a TM M accepts ANY string at all is undecidable, since we can reduce it to the halting problem
            - We can do this by taking the mapping function $f(M, w)$ to create $M'$, where $M'$ erases its tape, writes out $w$ onto its tape at the very beginning, and then runs on input $w$
            - CLAIM: $M$ accepts $w$ = $f(M, w)$ accepting ANY input (since we it created to run on any input) (??)
        - (...I'm somewhat distracted today; need to read the textbook on this)

- So, in the last bit of time, I'm going to run through a proof (which you will NOT be required to do) showing that a language isn't decidable
    - This is mostly a syntactic proof: you assume there's a TM $M$ that decides the language, create a D(M) that accepts M if it doesn't accept M, and rejects M if it M accepts M
        - If we then run D(D), we get a contradiction; it's the equivalent of saying "this statement is false!"
        - Therefore, by contradiction, there can't be a TM that accepts this language (need to look at it more slowly)

- Alright, see you on Thursday!
