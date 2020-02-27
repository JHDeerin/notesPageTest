# Complements / Pumping Lemma (cont.)

## February 18th, 2020

- Okay, CX 4220 has likely bloodied my head but not yet cast me down; the test was a bit rocky, but definitely recoverable if I study my eyes out
    - Depending on the curve, I'll have to get between an 88% and 96% on the remaining exams to keep an A; one of those is "okay, you're doing just fine" and the other is full-on "CHALLENGE ACCEPTED MORTAL"

- On the docket for today:
    - Operations on regular languages
    - More pumping lemma

- "Okay, welcome to the hectic part of the term!"
    - We went through a LOT of stuff about DFAs and definitions in the last few weeks, and some of you might've thought we went through that stuff quickly; this week, we'll start bringing in some more proof-based stuff

- One question I got yesterday: why does it matter if we can classify languages?
    - Ever hear of neural nets? Back when they were first being researched, people wanted to figure out what they theoretically could do with them - and without this kind of math, we'd never be sure if we could use them to actually solve certain problems we care about!
    - So, we can show even very simple problems CAN'T be computed by finite automata
        - One number you may not know: on average, there are about 40 separate computers in a new car today, most of which are DFA type controllers that handle control-theory-esque stuff, because they DO work for those applications - which we can prove, letting us save money by not using a $500 laptop for every task
--------------------------------------------------------------------------------

- There's a very generic idea of wanting to do an operation on an entire language, and there's 1 set theory operation we haven't talked about: taking the COMPLEMENT of a language $L$ (i.e. accepting everything that's NOT in $L$)
    - This is one of the simplest ways to create and interestingly language, but it also lets us do a new proof:
    - THEOREM: A language $L$ is regular if and only if $\{w \not\in L\}$ is also regular
        - To prove this, let $M$ be the DFA that accepts $L$; then the complement $M'$ that accepts $L'$ will just be $M$ with all the non-accepting states accepting and all the accepting states replaced with rejections!
    - As a side-note, concatenation is another operation we can do - and note that concatenating 2 non-regular languages can possibly get you a regular language as an output
        - e.g. $L^2$, where $L$ is $\{w \text{has different number of 0s and 1s} \}$; this is actually a regular language, even though $L$ itself is not!
            - Why? Because $L^2$ isn't just $0^n1^m$ (mixed in some way), but $0^{n+i}1^{m+j}$ mixed in some way, meaning we could now have the same OR a different number of 0s and 1s, making it regular!
            - We can also prove that the complement $L$ isn't regular (i.e. same number of 0s and 1s), since that would mean the complement of the complement would have to be regular - which we know it's not!
                - Once we know $L$ and $L^c$ are not regular, it actually turns out to be easier to show $((L^c)^2)^c$ is regular, although we won't show the full proof here (but think about the sets of strings this implies)
        - Squaring languages is one of those tricky cases where you have to be careful about what you're setting out to prove; 3 lefts could turn into a right!
            - So, BE CAREFUL - you can't assume that just because something is non-regular everything it touches will also be "poisoned" with non-regularity
        - On the other hand, if $L_1$ and $L_2$ are regular, then $L_1L_2$ is definitely still regular (since they can be decided by some NFAs, you can add transitions to get from $M_1$ to $q_{start}$ of $M_2$ to decide the concatenation)

- ...okay, what I was just trying to do there was to show that statements like "$L^2$ of a regular language is regular" aren't obvious; we actually have to prove them!

- Now, with the 2nd half of class, let's try to prove why pumping lemma works for regular languages and "fails" for non-regular ones
    - As an example, consider $L = \{w \text{with odd number of 0s}\}$
    - Let's arbitrarily choose p = 3, and show we can get a "good split" for this language that satisfies the pumping lemma
        - To show that a language IS regular, as opposed to not regular, we need to show that ALL values $i \geq 0$ will satisfy $xy^iz \in L$
            - "Think about the statement 'there are no penguins in the North Pole'; to show that's false, I just have to find 1 penguin there, but to prove it's TRUE I need to search the ENTIRE North Pole"
        - So, let $w$ be a word in $L$; if the first 3 characters have a 1, we can pump 1 without changing the number of 0s, so we're still good!
            - If there's no 1 in the first 3 characters, then the first 3 characters are all 0s; so, set $y=00$, and then however many 0s we pump it'll be + (some even number), meaning it's still odd!
        - Therefore, in either case, the pumping lemma will hold!
    - Here, we've applied pumping lemma in reverse to show it DOES hold for a regular language (although we haven't quite proved it holds for ALL regular languages yet)
        - Keep in mind, though, that you can't use pumping lemma to show a language is regular; you can just show that regular languages satisfy the pumping lemma
            - "All penguins are black and white, but not all black-and-white things are penguins"

- Side-note: for languages with a finite number of strings, we can just set "p" to be larger than the longest string, and then the "All $w$ where $|w| > p$" set is empty, so you can use the null hypothesis to technically show that all the words in that set satisfy the pumping lemma!
    - "It's like the old statement 'All flying pigs are whistling' - it's technically true because there ARE no flying pigs!"

- Now, let's finish up with a weird pumping lemma example: show that $L = \{0^k1u0^k | k \geq 1, u \in \{0, 1\}\}$ is NOT regular ("which is tricky, because that u string can eat up a bunch of 0s, meaning that $0^ku0^k$ actually IS regular")
    - So, languages can be VERY close to regular while actually being non-regular, so we've gotta be careful
    - How can we prove this? For any $p$, let's consider the string $0^p10^p$
    - Now, we need to show that ANY split will break this - but notice that since the first "p" characters are 0s, $y$ will always be all 0s, so we can just set $i=2$ and end up with the number of 0s being unequal!

- Alright, we'll meet again on Thursday! Bye!
