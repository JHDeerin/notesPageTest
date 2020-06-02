# PDAs to CFGs

## April 2nd, 2020

- We have survived the Fool's Day without incident; let the cruelest month begin

- "I'm not doing webcam anymore, because of the internet"

- TODAY'S PLAN:
    - Convertings CFGs to PDAs
    - Recap converting PDA to CFG
    - More CFG examples

- Last time, we talked a little about going from a PDA to a CFG; today, we'll recap that and hopefully go the other way, too
--------------------------------------------------------------------------------

- As we've mentioned before, a PDA is just an NFA with a stack we can push/pop from, and as we've said, CFGs and PDAs are formally equivalent; you can convert from one to the other
    - These conversions tend to NOT be reversible; since CFGs and PDAs are both non-deterministic, a conversion just shows that if there's a sequence of operations in one that accepts, there's some sequence of operations in the other that also accepts - but not necessarily the SAME sequence (e.g. there may not be a 1-to-1 correspondence between substitutions and stack pushes/pops)
    - In other words, if f(CFG) = PDA, and g(PDA) = CFG, then f(g(PDA)) doesn't necessarily give me the same "PDA," even though it'll recognize the same language
        - Note, too, that CFGs and PDAs aren't unique for a given language; we can always add some dummy rules to get a different one

- The general rules for conversion are that:
    - What goes up, must come down: is something gets pushed onto the stack, it should be popped eventually
    - For PDAs, you can always simplify down to 1 accepting state by using epsilon transitions
        - You can simplify things more by not popping AND pushing in a single state, but just doing 1 at a time
        - THEN, since there's just 1 starting state and 1 accepting state, we can convert to a CFG by starting with the variable $A_{q_{0}q_{accept}}$
            - We then basically reduce each path from start/end to a single rule - "if you remember the Floyd-Warshall path algorithm, it's a similar procedure to that"
            - Along each path, we start with an empty stack and end with an empty stack
        - For the transition from state $p$ to $s$, then, there's 2 possibilities:
            - If we pushed nothing, then we just went from 1 state to another without changing the state
            - If we pushed some symbol X, then x was either:
                - Popped from an intermediate state at state $q$
                    - This gives us the rule $A_{ps} \implies A_{pq}{qs}$
                - Never popped until just before the ending state $s$, meaning we can ignore it for the intermediate states (since it's just lying at the bottom of the stack not doing anything!)
                    - This gives us the rule $A_{ps} \implies c_1A_{qr}c_2$
                    - $c_1/c_2$ are literal characters we've processed so far
        - So, we essentially just keep building up rules for this PDA to convert it to a CFG
        - So, we get 3 cases for our CFG (from a base case of $A_{pp} \implies \epsilon$):
            - 1: For rules of the form (p, c, $\epsilon$) -> (q, $\epsilon$), we have $A_{ps} \implies cA_{qs}$
            - 2a: For the triple p, q, s, $A_{ps} \implies A_{pq}A_{qs}$
            - 2b: For the tiples p, q, r, s, and rules:

                    (p, c1, x) -> (q, e)
                    (r, c2, $\epsilon$) -> (s, x)

                - ...we add the rule $c_1A_{qr}c_2$

- Okay, let's see an example for converting from a PDA to CFG
    - Suppose we have the language $L = \{ww^R | w \in \{0, 1\} \}$
        - A PDA that can decide this language looks something like this (using our rule of "the same state can't push and pop in the same transition"):

                start-->a--($\epsilon, \epsilon$ -> \$)-->b

                    (self-loop)
                b--(0, $\epsilon$ -> x)-->b--($\epsilon, \epsilon -> \epsilon$)->c
                   (1, $\epsilon$ -> y)

                c--(0, x -> $\epsilon$)-->c--($\epsilon, \$ -> \epsilon$) -> D_ACCEPT
                   (1, y -> $\epsilon$)

            - So, we push everything, non-deterministically decide when to "split," then try popping everything off
        - How do we convert this to a CFG? Let's think!
            - We have 6 state transitions we need to create variables for: $A_{ab}, A_{ac}, A_{ad}, A_{bc}, A_{bd}, A_{cd}$
            - Our starting variable will be $A_{ad}$
            - Then, for our rules:
                - For case 1, where the stack doesn't change, we have 2 rules:

                    $$
                    A_{bd} \implies A_{cd}, A_{bc} \implies b_{cc}
                    $$

                - For case 2, there's a TON of cases (4^3=64), since we need to worry about all triples of state combination
                    - For case 2b, for each "x" on the stack, we'll have:

                        $\$: A_{ad} \implies A_{bc}$
                        $x: A_{bc} implies 0A_{bc}0$
                        $y: A_{bc} \implies 1A_{bc}1$

- So, this is a LOT of trouble we went through just to, basically, generate the CFG "S -> 0S0 | 1S1 | $\epsilon$" - which is why coming up with a new CFG from scratch is usually faster
