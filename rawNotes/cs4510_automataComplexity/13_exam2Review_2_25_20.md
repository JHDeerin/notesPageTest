# Exam 2 Review

## February 25th, 2020

- Professor Peng (who shall henceforth be dubbed "Professor Peng-uin" in my screaming imagination) has entered the lecture hall with a mere 2 minutes to spare

- Today's plan is to do a quick review for your upcoming test:
    - DFA, NFA, equivalence
    - Regular languages and operations
    - Pumping Lemma

- We have a test THIS THURSDAY, i.e. 2 days from now - PLEASE study if you know what's good for you!
    - There'll be a lot of pumping lemma questions, and it should be a similar format to the 1st test
        - "If you don't understand pumping lemma and are asking questions like 'why can't we specify the value of p?', you're gonna lose 8 to 10 points on the test, so go to office hours NOW. I don't mean to scare you, but the TAs are VERY SPECIFIC about pumping lemma mistakes"
    - "One thing we noticed on the homeworks: do NOT use 'let' if you can help it, since it's inherently ambiguous; you need to specify if you mean 'for all X, let...' or if you just mean 'there exists some...'"
        - Even if you got full points on the homework, try to be careful and look at how we do things on the class solutions; some TAs give people the benefit of the doubt when your proof is ambiguous, while other TAs won't and'll mark you off

- Annoyingly, I got points off on my homework because you have to EXPLICITLY list all state transitions in a DFA (i.e. you can't use the "unmarked transitions count as rejections" shorthand like we did for TMs)
--------------------------------------------------------------------------------

- The main thing we did in these last 3-4 weeks was to take away the tape from our Turing Machine, and then to see what we could do with a plain ol' state machine
    - ALL of this revolved around finite automata, where we have a set of states and EVERY step we read a character off the input string and move to the right until we get to the end of the string
        - We need to have a transition defined for EVERY state/input combination in our DFA to have it be valid (no "free" rejection states like for TMs; we have to explicitly create a self-looping rejection state if we want to do something like that in DFAs)
        - We also have to consume the ENTIRE input string before accepting/rejecting the string (we can't stop in the middle of the string, like TMs)
    - NFAs, non-deterministic finite automata, make things a little more flexible since we CAN have the same input go to multiple different states
        - This means it IS okay to have missing states for an NFA, since the transition function is now a power set:

            $$
            P(Q) \times (\Sigma \cup \epsilon) \implies P(Q)
            $$

            - ...meaning we CAN have the empty set as a transition
        - So, mapping an NFA where we just initially go to some state, and then have to transform it to a DFA (by taking every subset of state combinations), we'd end up going to an accepting state, then a self-looping reject state for everything else!

                --->q0_accept

                --->q0_accept---{0,1}--->emptySet(self-loop)

            - Here, the empty set is implicitly there in our NFA as an output state; we just have to represent it explicitly in a DFA!
            - Remember, $\epsilon$ is an empty string but it's STILL a string (and therefore a set of size 1), while the empty set has a size of 0 and nothing inside it - although it can be counted as a state
        - For NFAs, we also mentioned something called the "epsilon closure" ($\epsilon-closure$); this is the set of states we can reach from a given state in an NFA WITHOUT consuming any inputs (this INCLUDES the node itself)

- Then, we went to regular expressions/languages
    - One thing we weren't very careful about is that we can apply regular languages to DFAs!
        - for instance, let's say we have a DFA that recognizes L1 and another DFA that recognizes L2; how can we recognize the union of L1 and L2?
            - To do this, we basically want to run 2 DFAs simultaneously, where we apply the L1 and L2 transition independently to the same character
            - Then, at the end, our accepting states will be if EITHER DFA ends in an accepting state

- Finally, let's look at an example of converting an NFA to a DFA (this example is on page 53 of the textbook, figure 1.36)
    - Formally, to do this conversion, you'd write out all the states in your NFA, then the power set: all possible subsets of them (INCLUDING the empty set); these subsets will be the states of your DFA
        - If a transition doesn't exist in a state for some input, it goes to the empty set
        - Epsilon transitions enlarge the set of states we could end up in
        - If there are no transitions to/from a given state, then we can just ignore it in our DFA!
    - "I won't get to finish this example, but I'd highly encourage everyone to look at it and make sure they understand it"

- Alright, good luck on the test! See you Thursday!
