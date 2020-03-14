#

##

- Plan for today:
    - Pumping lemma for CFGs (example)
    - Equivalence between PDA/CFG

- "Okay, we actually don't have that much more material for this section; the main thing we didn't cover yet is the connection between pushdown automatas and CFGs; we won't require you to know the formal proof for this, but there WILL be a question on converting from PDAs to CFGs, and vice-versa"

- Remember, Homework 5 is due on March 26th (the Tuesday that you get back)
    - "Currently, I have a test scheduled for the week you come back; I'm probably going to push that back a week, but stay tuned on Piazza to be sure"

- "Also, for when classes inevitably get canceled from coronavirus, do you want me to stream on Twitch or YouTube?"
--------------------------------------------------------------------------------

- Both the textbook AND the notes skip some details in the "ww" proof from last time, so I want to spend a little more time on it

- As we mentioned last time, there's this pumping lemma for CFGs proof involving the parse tree, where the branches go to the left/right, with "u/v" to the left, "y/z" to the right, and "x" right in the middle
    - This let's us find a split $w = uvxyz$ such that $|w| > p$ so that it violates the pumping lemma for all splits
        - Remember, the splits fulfill the conditions:
            - $|vxy| <= p$
            - $|vy| > 0$
        - And the new string is:
            - $uv^ixy^iz$
    - So, the middle bit is "vxy", but $u$ and $z$ can be arbitrarily long/short - yet the $vxy$ block being guaranteed to be at most $p$ long means we can still use this!
        - However, there are more cases than for the last pumping lemma, since that block of characters can slide around the whole string

- So, let's return to our proof from yesterday: show that $L = \{ww | w \in \{0, 1\}\}$ isn't a CFG
    - So, for any p, let's say $s = 0^{2p}1^{2p}0^{2p}1^{2p}$
        - Remember, we're showing that this string after being pumped is NOT in the language at all, not just that it breaks the format we originally set here; forgetting that is a VERY common mistake
    - For this, we've got 4 possible cases:
        - $vxy$ is completely in a 1-character block
            - If this is the case, then we first need to prove a lemma: if $i,j,k,l > 0$, then $s \in L$ iff $i == j, j == l$
                - The proof: If i == j and k == l, then then number of 0s/1s are equal. If this is not true, then we can use 2 grams!
                    - An n-gram is a VERY useful way of looking at languages (and comes up in NLP); a 2-gram is just a pair of 2 consecutive characters
                - If we look at these 2-grams, there'll be 1 copy of 10 and (need to look at proof??)
            - With this lemma, we can show that if $i=2$, then only the length of that character block changes, so $i \neq j$ or $k \neq l$ - therefore, by our lemma, it's not in the language!
        - $vxy$ spans the 0/1 block in the 1st string
            - If $i=0$, then we change the lengths of $i$ and $k$ but can only delete at most $p$ characters, so we can't totally delete either one! Therefore, $0 < i < j$ and $0 < k < l$, so by our lemma it's not in the language!
        - $vxy$ spans the 0/1 block in the 2nd string
            - Similarly, only the lengths of $j$ and $l$ change, so the lemma proves this can't be in the language!
        - $vxy$ spans the 0/1 block between the duplicated strings
            - Here, again, if you pump down to $i=0$, then we delete some 1s and 0s, but since each block is $2p$ in size, we can't delete the whole block - therefore, we reduced the length of $j$ and $k$ but not $i$ or $l$, so, by our lemma, this isn't in the language!

- "This is a pretty ridiculous case, so you won't see something this hard on a test (especially since you have to figure out you need to pump DOWN); however, a proof with 2+ cases may still be fair game"
    - The main thing here is that you need to be VERY careful about what kinds of strings you've actually proved aren't in the language, and consider all these cases

- We don't have time to go through it, but try to prove that $L = \{0^i1^j | i = j^2\}$ isn't a CFG (this one's tricky since you have to prove things about squares)

- Now, to turn a parse tree into a PDA, you basically just do a depth-first search of the tree with a stack, from left-to-right
    - To turn a PDA into a CFG, you have to take all the states out there and turn them into rules, and it basically boils down to the saying "what goes up must come down" - if it's on the stack, it's gotta come off
        - Basically, create a CFG variable for all possible pairs of states, then create a rule for each of of those states that represent the transition from state 1 to state 2, with the stack represented via variables staying in the rule's output string
            - e.g. The states:

                    ...---->p----c1, $\epsilon \implies x$--->q----(...)--->r---c2, $x \implies $--->s

                - Would go to the CFG rule:

                    $$
                    A_{ps} \implies c_1A_{qr}c_2
                    $$

- Alright, have a good break and stay safe out there!
