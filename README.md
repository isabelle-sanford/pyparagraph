# PyParagraph

![Language](Images/language.png)

This repository contains a Python script to automate the analysis of any arbitrary paragraph using the metrics below. Here's what it does:

* Imports a text file filled with a paragraph of your choosing.

* Assesses the passage for each of the following:

  * Approximate word count

  * Approximate sentence count

  * Approximate letter count (per word)

  * Average sentence length (in words)
 
 And outputs the results to the console. 
 

* As an example, this passage:

> “Adam Wayne, the conqueror, with his face flung back and his mane like a lion's, stood with his great sword point upwards, the red raiment of his office flapping around him like the red wings of an archangel. And the King saw, he knew not how, something new and overwhelming. The great green trees and the great red robes swung together in the wind. The preposterous masquerade, born of his own mockery, towered over him and embraced the world. This was the normal, this was sanity, this was nature, and he himself, with his rationality, and his detachment and his black frock-coat, he was the exception and the accident a blot of black upon a world of crimson and gold.”

...would yield these results:

```output
Paragraph Analysis
-----------------
Approximate Word Count: 122
Approximate Sentence Count: 5
Average Letter Count: 4.6
Average Sentence Length: 24.0
```

This repository was made as part of the USC Viterbi Data Analytics Boot Camp. 
