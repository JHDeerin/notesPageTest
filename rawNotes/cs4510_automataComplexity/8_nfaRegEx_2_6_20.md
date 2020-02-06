# NFAs / Regular Expressions

## February 6th, 2020

- "Coronavirus isn't that scary, and besides, it makes subways easier! You cough a couple times, and you have the seat to yourself!"
- So, THE PLAN (for today's lecture, at least):
    - Converting NFAs to DFAs
    - Regular Expressions
    - Regular Expressions generating regular languages
- "...I'm also strongly tempted to tell everyone to crowd up against the wi"
    - Next week, I will

- "I've also noticed that today's lecture is a little...sparse, but it's career fair week, and raining, so I can't blame people"

- Also, administrative stuff!
    - Homework 3 is OUT for your viewing and doing pleasure; as per usual, it's due next week, Thursday at noon
--------------------------------------------------------------------------------

- Last time we talked about DFAs, which you've probably seen before but maybe not in a so-formal way
    - As we said, this is basically just a Turing Machine without the tape, and are NICE because the transition function is simple
    - An NFA, though, is non-deterministic - but unlike with Turing Machines, you can convert an NFA to a DFA in polynomial time! (check this??)
        - We'll spend the first part of today talking about how we can do that, and then the rest of it talking about regular expressions and why they're actually the same thing as DFAs
        - "As we mentioned, these NFAs can also have epsilon transitions ($\epsilon$), which let you skip states by taking an edge for free, without consuming any input"
    - Also, remember that we accept if we END in an accepting state after ALL the input has been consumed (if we remember our "division by 3" example, we could have an input like "95" - if we stopped after the 1st character, we'd wrongly think 95 was divisible by 3)

- Non-determinism for finite automata, though, is less crazy than it is TMs because the tape doesn't change - only the states do!
    - The way you can track what state you could end up in for a given step is literally just by writing out all the states you could possibly be in at that step
        - "This is VERY similar to reachability checks on graphs, or dynamic programming examples"
    - A key property of DFAs and NFAs is that if we have 2 input prefixes that bring us to the same state, then they behave identically for EVERY suffix appended to them afterwards
        - i.e. "If inputs x and y bring the same DFA to the same state (or set of states, for NFAs), then for a given suffix z, DFA(xz) == DFA(yz) (i.e. ending state/set of states)"

- So, how do we convert an NFA to a DFA?
    - Remember POWER SETS from discrete math? This is basically the set of all possible subsets of a given set
        - Basically, to convert an NFA to a DFA, we create a state for EVERY possible subset of states we could end up in!
        - So, the new transition looks like:

            $$
            \delta_{DFA} = P(Q_{NFA}) \times \Sigma \implies P(Q_{NFA})
            $$

        - More specifically, for a given set of states $S$ in our NFA,
            - An EPSILON CLOSURE ($\epsilon$-closure($S$)) is the set of all things reachable from $S$ via only $\epsilon$ transitions
            - We'll make a new state for each subset of possibilities, with the appropriate transitions to reach them
        - The new starting state, then, will be $\epsilon$-closure($q_{NFA}$, 0)
    - As an example, suppose we have the following NFA:

            q0(accepting): 0-> q0 OR q1, 1-> q0
            q1: 1 -> q0

        - We'd convert this to a DFA like so:

            {q0}(accepting): 0-> {q0,q1}, 1 -> {q0}
            {q0,q1}(accepting): 0-> {q0,q1}, 1-> {q1}

        - "If you have a longer NFA, you may need to have inputs as strings rather than single characters to show a SEQUENCE of inputs is needed to reach something"

- Okay, I glossed over $\epsilon$-transitions and closures a bit, so let's cover them quick
    - Basically, this is a transition in an NFA that I'm allowed to take FOR FREE without waiting to read the next character on the tape
        - Since it's an NFA, though, you don't HAVE to take it
        - Why are these useful? That becomes more clear when we start talking about regular expressions
    - "These are called epsilon transitions because $\epsilon$ symbolizes an empty string"

- REGULAR EXPRESSIONS are basically ways of expressing "hey, I want to match any strings that match the following rules"
    - These are defined recursively, using basic rules like:
        - Unions (?)
        - Concatentation of 2+ strings
        - \* = 0 or more copies of the preceding (aka the "Kleen Star")
    - For example, 0$\Sigma$*0 means "any string that starts and ends with a 0"
        - "Regular expressions are practically super useful, but theoretically they're also one of the easiest ways of expressing out an infinite language"
    - Here's a claim I'll make: regular expressions match strings from regular languages (i.e. ones that can be accepted by DFAs)
        - PROOF: We can do this via induction
            - Let's start with the base cases of $\Sigma, \epsilon, \emptyset$
            - Our inductive hypothesis: any regular expression describes a regular language
                - From there, we can essentially show that as we add a new character to a string, our regular expression ca
                - (tries to show how we implement * in NFA? Confused?)
            - More formally, we would say something like this:
                - Let M be an NFA such that L(M) = L with starting state $q_0$ and accepting states $F$. Create M' for the language L* (i.e. the language with a * appended to the end) by creating a new starting state $q'$ and add $\epsilon$-transitions from $q'$ to $q_0$, and from each state in $F$ to $q_0$.
                - (still slightly confused about why this works?)

- Next week, we'll finish the base cases for concatenation/union and wrap up this proof - see you then!