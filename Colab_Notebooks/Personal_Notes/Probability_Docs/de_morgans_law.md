# De Morgan's Law and Probability

While the sources provide a foundation for understanding probability and list De Morgan's Law [12], they don't directly explain how De Morgan's Law affects probability calculations. However, we can use the information from the sources to understand its implications:

## De Morgan's Law in Set Theory:

The sources present De Morgan's Law in the context of Boolean algebra and sets [12]:

- Law 1: not (A and B) <=> not A or not B
- Law 2: not (A or B) <=> not A and not B

In set theory, these laws describe the relationships between intersections (AND), unions (OR), and complements (NOT) of sets.

## Relating Sets to Probability:

We can think of events in probability as sets of outcomes. For example:

- Event A: Rolling an even number on a die.
- Event B: Rolling a number greater than 3 on a die.

The probability of an event can be thought of as the proportion of outcomes in the sample space that belong to that event's set.

## Applying De Morgan's Law to Probability:

Using the relationships between sets and probability, we can apply De Morgan's Law to probability calculations:

- Law 1: P(not (A and B)) = P(not A or not B)

  - The probability of NOT (A and B) is the same as the probability of (not A) OR (not B).

- Law 2: P(not (A or B)) = P(not A and not B)
  - The probability of NOT (A or B) is equal to the probability of (not A) AND (not B).

## Practical Use in Probability:

De Morgan's Law helps simplify probability calculations, especially when dealing with the probability of events NOT happening:

1. Calculating Complements: Instead of directly calculating the probability of a complex event, you can often use De Morgan's Law to calculate the probability of its complement (the event NOT happening) and subtract from 1.

2. Working with the Addition Rule: De Morgan's Law can help you rearrange expressions involving the addition rule for probability.

## Example:

Let's say the probability of event A is 0.3, and the probability of event B is 0.4. A and B are independent events. What's the probability of neither A nor B happening?

- Using De Morgan's Law:

  - P(neither A nor B) = P(not A and not B)
  - Since A and B are independent, "not A" and "not B" are also independent.
  - P(not A and not B) = P(not A) _ P(not B) = (1 - 0.3) _ (1 - 0.4) = 0.42

- Direct Calculation:
  - P(neither A nor B) = 1 - P(A or B) = 1 - (P(A) + P(B) - P(A and B))
  - = 1 - (0.3 + 0.4 - (0.3 \* 0.4)) = 0.42

In this example, both methods give the same result, but using De Morgan's Law can simplify the calculation.

In summary: While not explicitly covered in the sources, De Morgan's Law, as presented in the context of sets and Boolean logic, can be extended to probability calculations. It provides a helpful tool for simplifying probabilities involving complements and combinations of events.
