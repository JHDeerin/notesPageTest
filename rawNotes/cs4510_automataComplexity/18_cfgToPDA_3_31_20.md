# Converting CFGs to PDAs

## March 31st, 2020

- We're starting late due to technical issues :(
    - "Sorry guys, I had an internet outage that set back an earlier meeting and needed to fix that"

- Okay, so welcome to "Twitch Plays Finite Automata," where I livestream this class and you probably learn stuff!
    - To chat, you have to type "!speak" and a text-to-speech thing will read it out loud to me (please don't spam it)

- THE PLAN:
    - Recap equivalence of PDAs/CFGs
    - More PDA examples

- Also, homework 5 is due THIS THURSDAY, so be aware!
    - Test 3, then, will be NEXT WEEK on Thursday; I'll release the exam at 11am and it'll be due at 1:30pm
        - "It should be similar to exam 2 but nerfed a little bit, where we'll tell you if something is/isn't context free and just ask you to prove it"
        - We'll also be sure to get the answer key for the study guide out this time; last time COVID threw a wrench in things
    - The recorded lectures from last week are on the Twitch channel, and should be helpful in providing some extra CFG pumping lemma examples
        - For one of the problems, note that building a new CFG/PDA from scratch is usually easier than trying to do a conversion
--------------------------------------------------------------------------------

 - WAAAAAYYYYY back 2 weeks ago, we covered push-down automatas and context-free grammars, and tried to show that they're equivalent; today, we're going to recap the equivalence proof and how to convert from 1 to the other
    - Remember that a CFG is a 4-tuple of variables, alphabet, rules for converting variables to words, and a starting variable
        - We then, for some starting string, repeatedly replace variables with strings/other variables until we end up with a final string

- *pesky internet lag issues + semi-heckling Twitch chat later...*
    - "Pre-recording the lecture is hard because there are no questions, so it'd just be me reading my own notes, and at that point you're better off just reading the textbook"
    - *Switching back to BlueJeans*
        - "I'd have expected Twitch to be better about livestreaming because, y'know, it's huge, but apparently not today; I prefer Twitch, but we'll use BlueJeans "

- In general, a heuristic for checking if something is a CFG is if it counts numbers 1 by 1
    - This does NOT always work, but it's a good start
    - A PUSHDOWN AUTOMATA, then, is basically an NFA that has a stack, and every transition has a pop/push operation

- So, I want to get across today that CFGs are equivalent to PDAs
    - You can convert between them by basically pushing/popping rules off of the stack
        - So, to apply a rule "A -> w", you would pop the variable "A" off of the stack and then push "w" onto the stack
        - For instance, let's say we start with "S", and have the rules:

                S -> # | 0S00

            - So, for the 1st rule, we say "If we see S, remove S from the stack and push #"
                - Or "if we see S, pop off S and then push 0S00 onto the stack" (the order of the strong you're pushing may be reversed because it's a stack, based on the convention you use)
            - So, we can convert this CFG into the following PDA:

                (TODO: get this from the textbook)

            - For this PDA, the input format is (I think?):

                    <input string char>, <char read from stack> -> <sequence pushed to stack>

                - I *think* pushing epsilon means "don't push anything"? (and same thing for pop?)
        - On this PDA, let's suppose we have the input string 00#0000
            - So, at state q0, our stack is empty
            - We'll then push an empty string AND "S" onto the stack (I think?):

                    S,''

                - We then have 2 epsilon transitions for these rules, and then (I think?) rules for consuming these on the stack IF

- For actually proving stuff, CFG to PDA conversion isn't super common, but it is a formalism
    - For the homework problem, we'll

- To go from PDA to CFG, we basically create a new rule:

        A_0s -> c_first(A_1...s-1)c_last

    - ...and then keep creating new rules to fill in that middle part
    - (might need to look at this in the textbook???)

- "Keep in mind these CFGs and PDAs are VERY non-deterministic, and rely on us using non-determinism to be lazy"

- Okay, that was really messy, so my apologies, but that's as far as we'll go today; see you guys later!
