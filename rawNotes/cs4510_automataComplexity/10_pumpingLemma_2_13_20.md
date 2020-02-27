# The Pumping Lemma

## February 13th, 2020

- ...okay, a TA is standing in for Professor Peng, and he's apparently mystified by how people can actually learn in a class of 250 people
    - Clearly this man is not a Georgia Tech alumnus
    - ...or, worse, perhaps he is, and he understands half the class actually has no idea what's going on until 2 days before the test

- The schedule for today:
    - Non-regular languages
    - Pumping Lemma
    - Examples of applying it

- "I'm not too familiar with all this technology, so please forgive me and let me know if something isn't working - also, I don't usually teach this class, so please tell me if I use some unfamiliar language or something"
--------------------------------------------------------------------------------

- Okay, the big goal of today is to start trying to actually understand WHAT the pumping lemma is and why it works - "questions testing WHY the pumping lemma works, not just your memory, are quite common on tests"

- Now, we know how to prove languages are regular: if you can construct a DFA or a regular expression for it, then it's regular!
    - ...but how can we prove a language is NOT regular, in general?
    - We've already seen from last time that the language $0^n1^n$ CANNOT be decided by a DFA, since we can always choose an "n" too large for the DFAs states to track
        - ...but how can we show, in general, that NO DFA can possibly solve this?
    - Last time we did a formal proof for this particular string: if a DFA $M$ exists that can solve this language with $p$ states, than the string $0^{2p}1^p$ will be accepted because, since the input is > $p$, there MUST be a loop in the states somewhere per the pigeonhole principle, so it can't tell there are more 0s than 1s! Therefore, we have a contradiction, so NO DFA $M$ can decide this

- This brings us, formally, to the PUMPING LEMMA
    - Given ANY regular language $L$, there exists an integer $p$ (the pumping length) such that for ANY string $w \in L$, with length $|w| \geq p$, we can somehow split the string into 3 parts $x, y, z$ so that:
        - $|xy| \leq p$
        - $|y| \geq 1$
        - $xy^iz \in L$ for any $i \geq 0$

- So, if a language is regular, it must satisfy the pumping lemma!
    - "Notice that this does NOT say that a language that satisfies the pumping lemma must be regular"
    - By implication, then, a language that doesn't satisfy the pumping lemma must be non-regular
        - This is IMPORTANT: we can show a language is non-regular by showing there's at least 1 string that doesn't satisfy one of those 3 criteria after splitting the string (ESPECIALLY the last one)

- Let's see how we can use this lemma to show our good ol' $0^n1^n$ example is non-regular
    - Given ANY pumping length $p$, let's suppose $w = 0^p1^p \in L$
    - So, let's consider a split that satisfies our first 2 conditions:
        - $|xy| \leq p$
        - $|y| \geq 1$
    - So, since there's $p$ 0s and $p$ 1s, and $xy$ together MUST be less than $p$, $x$ and $y$ both must all be 0s
    - Furthermore, for the 2nd part, there must be at least 1 $y$
    - Now, for the 3rd part, we have:
        - $xy^iz \in L$ for any $i \geq 0$
    - HOWEVER, if $i$ > 1 (for instance, $i = 2$), then we have a larger number of 0s than 1s in the string, so it no longer is in $L$!
        - Therefore, we've found a string in the language that can be split so that the pumping lemma is violated, so it can't be regular!

- If this is confusing, here's an alternate view of the pumping lemma: the adversary," or "demon" view ("for testing purposes, you can imagine this is your teacher")
    - Here, your *adversary* gives you some pumping length $p$
    - Then, you **choose** a string $w \in L$ such that $|w| \geq p$
    - The *adversary* then splits the string into 3 parts $x, y, z$ of its choosing
    - Then, **you** have to pick an $i$
        - If $xy^iz \not\in L$, you win! You've shown the language is non-regular!
            - Essentially, this is showing that every possible adversary strategy will fail
        - Otherwise, you haven't shown anything; you have to try again with a different $w$ or $i$

- As another proof example, let's look at the even palindrome example $L = \{aa^r | a\in \{0, 1\}\}$ (where $a^r$ means "reverse the string $a$")
    - So, I (the adversary) give you a pumping length $p$; what $w$ do you choose?
        - Let's say we choose $w = 1^p$
    - Alright; as the adversary, I'll split this so that:
        - $x = \epsilon$ (i.e. empty)
        - $y = 1^2$
        - $z = 1^{p-2}$
    - Okay, what $i$ will we choose? 1 doesn't work, 2 doesn't work, 3 doesn't work...huh, we're not having that much success. Because our adversary chose $y = 1^2$, we always get an even number of 1s, which keeps being matched and staying in the language!
        - Remember, our adversary is allowed to choose ANY split $x,y,z$ for our string to satisfy the lemma - if there's a single split for the word that will always satisfy the lemma, then that string "passes"
        - REPEAT: You are NOT allowed to choose the split
    - Instead, let's try choosing the string $w = 0^p1^{2p}0^p$
        - Let's suppose our adversary chooses *any* split
        - BUT, we see any split must have $y = 0^k$ for some $k > 0$
    - Because of that, we can pick $i = 2$, and since $y$ is only in the first half of the string, we'll get an unbalanced string!

        $$
        xy^2z = 0^{p+k}1^{2p}0^{p} \not\in L
        $$

        - $i=0$, $i=3$, etc. would also work; in fact, any $i \neq 1$ would work for this example!
    - So, we've won! We've shown $L$ is non-regular!

- Let's do a 3rd example where the language look like this: $L = \{0^i1^j | i > j\}$
    - So, the adversary chooses his predictable pumping length of $p$; so far, so good
    - What $w$ should we choose? By class suggestion, we'll go with $w = 0^{p+1}1^p$
    - So, the adversary splits the string somehow, but we know ANY split will have to have $y = 0^k$ for some $k > 0$
    - So, if we make $i = 0$, then we've *deleted* at least 0 and made the number of 0s equal to the number of 1s - which is NOT in the language!
        - Therefore, we've won! This language isn't regular!

- Alright, our 4th and final example for the day: a repeated binary string, meaning $L = \{aa | a \in \{0, 1\}\}$
    - We get our canonical pumping length of $p$ (shipped express-rate from our foe), and send back to his return address our word choice of $w = 0^p1^p0^p1^p$
    - Several days of U.S. Post bureaucracy later, we receive our split - but even before opening the envelope, we know something about the split: whatever our foe has done, $y = 0^k$ with $k > 0$
    - So, if we choose $i = 2$, we get $xy^2z = 0^{p+k}1^p0^p1^p$, which is NOT in the language!
        - Thus, even before the letter opener has crossed the threshold of the flap, we declare victory! HURRAH! The language is NON-REGULAR!!!

- But what's this? A new challenger has appeared! There's a 5th example on the slides!
    - (...yes, I would annoy myself, too, but play along. This gets good.)
    - Here, we've got $L = \{0^{n^2} | n \geq 0\}$
    - Let's choose a string of $w = 0^{p^2}$
    - ...so, what split can our adversary give us? Any number of them, but we know $y = 0^k$ for some $k > 0$
        - ...how can we keep our adversary, then, from choosing $k$ so that he gets a perfect square?
        - Because we *know* that since $xy \leq p$, $1 \leq k \leq p$!
    - Therefore, $i=2$ will give us $xy^2z = p^2 + k$ 0s, which is greater than $p^2$ but less than $p^2 + p$, which is in TURN less than $(p+1)^2$
        - Therefore, though embattled, we've won! We've triumphed, we've shown this language is non-regular once and for all!

- Okay, so that was a bunch of examples of the pumping lemma - see you later!
