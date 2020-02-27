# Pumping Lemma (cont.)

## February 20th, 2020

- 3 minutes to go, and Professor Peng is utterly missing! The GALL!
- 1 minute to go, and - wait, he's just arrived! He's stepping up to the podium! HE SHOOTS! HE MISSES! No, wait, he SCORES!
    - ...actually, he's just pulling a PowerPoint up off of OneDrive, but it's still mildly majestic (in the same way tying one's shoes is)- "It's a blackboard with the magic property of giving me a random font size for whatever I write"

- Also, Exam 2 (non-cumulative, on the past 2 homeworks) is going to be next Thursday - keep your eye on it!

- THE PLAN:
    - Pumping Lemma proof
    - Yet Another Pumping Lemma Example (YAPLE)
        - It's like MAPLE but without the imprecision errors (*sick burn*)
            - ...no, I have never used Maple. Yes, I am a sad human being. Sometimes.
--------------------------------------------------------------------------------

- Alright, let's get started!
    - We're gonna talk about the proof for the pumping lemma, then go over a few fine details of how to use the pumping lemma

- "Remember, the pumping lemma in a positive form says that if a language is regular, it'll fulfill a set of criteria - which means that if a language doesn't fulfill the criteria, we can show a language is NOT regular!"
    - So, to prove a language is non-regular, we just have to negate the pumping lemma, flipping all the statements to show that:
        - For ALL $p$, there exists some $w \in L$ with $|w| \geq p$ such that for ALL splits $w = xyz$ (such that $|xy| \leq p$ and $|y| > 0$), there exists some $i \geq 0$ so that $xy^iz \notin L$
    - Notice here that this has to hold for ALL valid splits of your word - a VERY common mistake is to choose a single split and say "this doesn't fulfill the pumping lemma, so the language is non-regular," but you have to show it holds for ALL splits of the word you chose
    - You then have to do a sub-proof that the resulting string from your choice of $i$ will NEVER be in the language, which you'll often have to do a proof by contradiction for
        - For instance, for the language $L = \{ww |w \in 0^n1^n \}$, we can't just say when $i=0$ that "$0^{p-1}1^p0^p1^p \neq 0^p1^p0^p1^p$", since that's only 1 possible $w$ - maybe your original $w$ - when you need to show this can't be ANY other string in the language!
        - Instead, you need to phrase it as a proof by contradiction to be formally correct! "Suppose $ww = 0^{p-1}1^p0^p1^p$; then there are a total of 2p 1s and 2p-1 0s. Therefore, if we split the string in half, the first $w$ must end in the 2nd section of 0s - but, by our language definition, $w \in L$ must end in 1. Contradiction!"

- Okay, let's take a quick look at the pumping lemma proof
    - The intuition behind pumping lemma is that if we have a finite number of states, then a long enough string will eventually force the states to loop, which can possible cause a DFA to fail
        - Let's say we have a DFA $M$ that recognizes the language $L$, with states $Q$
        - Let $p = |Q| + 1$, and consider some $w \in L$
            - For the input $w$ of length $n$, then, the DFA will traverse the states $q_0, ..., q_n$
            - If we traverse $p$ characters, though, then there must've been a loop somewhere in those first $p$ characters!
                - Therefore, $q_a = q_b$ for some $a < b < p$, at which point we'll keep traversing the loop $q_{a+1} ... q_b$
                - This is where $|xy| \leq p$ comes from
            - This "loop" of characters $q_{a+1} ... q_b$ is the same sequence of characters as $y$!
                - Then the sequence of characters before that is $x$, and the sequence of characters after that segment is $z$
        - So, what this implies is that if there's some $i$ where, if we repeat the segment of states $y$ for a valid input string $w$ that many times and can STILL end up not accepting the input string somehow, the language can't be regular, since it wasn't properly decided by the NFA when we looped!
            - Note that $|y| > 0$ comes from the fact that to have a loop, we need to pass through at least 1 state, and we said earlier that $a < b$!

- So, if we had to prove an individual language wasn't regular on our own, we'd have to make a giant proof-by-contradiction for each one proving that any length we choose for a loop will make the language invalid
    - The pumping lemma encapsulates this intuition and let's us apply it ready-made to a bunch of languages, saving a BUNCH of time!

- Alright, with the last few minutes let's do some more pumping language examples
    - Show $L = \{a^nba^mba^{n+m} | n,m \geq 1\}$ is NOT regular
        - To do this, let's consider the string $w = a^pba^pba^{2p}$
            - "This looks magical, right, because I'm just pulling a string out of thin air and it works - but actually, I want to find $n$ and $m$ so that ANY split of $w=xyz$ has some guaranteed simple characteristics for $x$ or $y$, which usually means trying to make it all 1 character or nearly all 1 character
        - Here, we can say that any split with $|xy| \leq p$ has to have a $y$ completely made up of "$a$"s
        - Therefore, for any $i \neq 1$, $xy^i \neq xy$!
        - So, by contradiction with the pumping lemma, this language can't be regular!

- This "working backward" step in the pumping lemma is important, so that for the string we choose we can know some things about ALL possible splits we could make

- So, next week we'll try to wrap up automata - see you all then!
