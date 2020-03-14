# Context-Free Grammars

## March 3rd, 2020

- ...people, apparently, did not like Exam 2 (it was harder than the first test for sure, but I thought it was still pretty fair)
    - "Exam grades should be finished sometime tomorrow, or by Friday at the latest; so far, it looks like the last question was very hard for most people (which we expected) and the 2nd to last question was also pretty hard (which we didn't expect)"
        - In retrospect, we probably ended up giving more complicated pumping lemma examples than we intended to avoid being too close to the easier ones we gave on the homework, which surprised people on the homework
        - Question 1, too (converting an NFA to a DFA) had an average of ~70%, when it was supposed to average ~90%
    - "The first time I taught this class, I realized that it was impossible to give a test that was too easy, and it basically turned into everyone who got the pumping lemma got an A and those who didn't get it got a B; this test was me trying to add some more nuance and get some differences between people who kinda got pumping lemma and people who got it really well"
        - I actually thought there was more material on Test 1, but I think I didn't give you enough hard examples of pumping lemma, and I think some of you haven't had much exposure to mathematical proofs before

- THE PLAN:
    - Context-free grammar
    - Pushdown automata

--------------------------------------------------------------------------------

- So, the last 2 weeks or so we've been showing strings like "0^n1^n" can't be decided by DFAs - so what CAN decide them? Basically, a DFA with a stack - better known as context free grammars!
    - A CONTEXT-FREE GRAMMAR can be formally described as a 4-tuple, as follows
        - A set of variables $V$, 
        - An alphabet of characters $\Sigma$
        - A set of rules for mapping a variable to a new variable, $R$
        - A starting variable $S$
    - For instance, we can build this string by saying "w -> 0w1"
        - This'll grow like:

            $$
            \epsilon \\
            01 \\
            0011 \\
            (...)
            $$

        - More formally, we can define the language $L = 0^n1^n$ as:
            - $V = \{S\}$
            - $\Sigma = \{0,1\}$
            - $R: S \implies 0S1; S \implies \epsilon$
            - $S = \epsilon$
        - In this case we'll apply the same rule over and over OR remove the middle variable, leaving just 0s and 1 - so, we can have CFGs with more than 1 rule
    - As another example, we can define a CFG for balancing parentheses like this:
        - $V = \{x\}$
        - $\Sigma = \{0,1\}$
        - $R: x \implies \epsilon, x \implies (), x \implies xx$
            - "We need the 3rd rule to allow for 2 sets of brackets to be next to one another, like '()()'"
        - $S = x$
            - At each step, then, we can choose which rule to apply to get any set of matched parentheses, and we just keep applying rules recursively until we don't have a rule for any input in our string - "it's recursion gone mad!"
    - Basically, context-free grammars work by continually substituting things for other things, eventually getting strings in your language

- Let's look at a 3rd example; "now, in all the examples I've given so far the variable set has just been the starting state; that's NOT always true!"
    - One thing I want to introduce before the end of the class is what's called a PARSE TREE (it does not appear we will get to the parse tree)
    - Let's do the example of balanced parentheses followed by some number of 0s
        - To define this, we can't just have a single variable "x" (at least not without massvely complicating the rules); instead, we need to distinguish the 1st part of the string from the 2nd part
            - We can do this by introducing a 2nd variable we're allowed to have in our grammar!
        - This CFG would look like:
            - $V = \{s,x,y\}$
            - $\Sigma = \{0, 1\}$
            - $R: s \implies xy, x \implies \epsilon, x \implies (x), x \implies xx, y \implies y0, y \implies \epsilon$
            - $S = s$
    - Now, with our extra variables, we can decide this language pretty easily!

- Now, in our last few minutes, let's talk about parse trees
    - Basically, a PARSE TREE is a record of the operations it took to build something in a CFG; for instance, "x -> (x) -> (xx)" would have a parse tree like:

                x
              / | \
             (  x  )
               / \
              x   x
               ...

    - The thing about parse trees is that there's a natural ordering based on which order we do our substitutions in, with the final string being all the leaves of the tree taken together from left-to-right

- Okay, we'll keep talking about this on Thursday and what it had to do with DFAs - see you soon!

