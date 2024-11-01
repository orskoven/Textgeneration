# 📓 Applied AI Course Notes

## Lecture Title: [Decision Trees ->> SUPERVISED LEARNING]
**Date:** [1. November 2024]  
**Instructor:** [Henrik Strøm]

---

Brief walk through of : CNN -> image processing : focus on -> feature extraction ;
we get a classical deep neural network - and not dependent on super clean data <-behing feature extraction
All problems that can be solved by cnn can be solved by all dnnn
We can scale down the complex problem with CNN's 

Supervised learning: 

X : [|| feature is columns noted: n  - sample noted: m]
y : expected output
h(parametrized with theta)(X) = y(hat) = y / h is the function 
h contains (H)
H : hypothesis 
y(hat) : output

Two main problems :

  Classification 
  Regression

Tree algorithms are super fast to train


y-axis: Performance
x-axis: m the size of training data 

-> Correlation will flatten out as a linear line 
        : as long as we don't have very much training data -> 
        : if variance is little also great
              bonus : + we get fast training & inference
              

RASPBERRY PI -> could run these models / edge devices 
    

+ Contradicts : 

-> Deep neural network (training data will always improve performance) 


       



### 📚 Key Concepts
- **Supervised learning:** Brief definition or summary
- **Classification:** Linear Regression -> if ouput value needs to be determined by categorial value : non - parametric output
- **Regression:** Parametrisk -> if output is a  continues parameteric value
- **Tree algorithms:** 
- **Expert systems:** Back in the 80's you didnt have the computing power -> attempts : EXPERT SYSTEMS _:> works like a phone dispatch system-> call in on a central phone number ->
- press: 1 for headache 2 for stomache etc.
- Decision tress learn to ask these questions themselves -> ( finds criterions ) 
- - **ETHICS wit algorithm:** We cannot precisly explain predictions -> and excatly source and prove that excat prediction y(hat) -> but decssion tress can be applied to transparnet explain the algorithm and show how the decision and computation as been made
  - 
- **XgBoost:** More modern algorithms to decisiontrees 
- **Decision Tree:**
- Contains a criterion that splits the decision into two -> always aims to split decsion into two decisions
- 
- **Leaf nodes:** 
- **Decision nodes:** 
- **Entropy:**
We try to descripe how much something is homogeneous or not with high or low entropy

EXAMPLE : Game of dice

define the probilities for different outcomes 

And multiply: the two outcome : with the respective probabilities 

-> monto carlo simulation : 
we want to simulate playing the game really many times to see what outcome we could get 

accumulation: of list of possible outcomes

HIGH UNCERTAINTY is HIGH ENTROPY -> big numbers rule -> if you repeat and repeat -> you will adjust to the mean


- 
- Claud Shannon: influential computer scientist-
-   - talked with neumann -> said he should write the word entropy (no body doesn't understands it but uses it)

  
- **Gini:** Brief definition or summary
- **Surprise:** Certain outcome inverse of probability and we introduce log value 
- **Entropy:** The avarage surprise we can expect -> if we look at all elements in a bag  and drag something we dont immidieatly see
- **Gini Impurity:** Used instead of entropy :> plotting gini and entropy curves -> entropy is 2 times higher than gini -> so gini is cheaper computation -> and time 2 we often see gini instead of entropy
- Use GINI IMPURITY as stand in and make our model calculate faster

- 
- **IRIS DATASET :** Define subspecies of iris flower 'setose, veriscolor' virginica
- multilabel - classification scenario

- m = 150
- n = 4

- DECISION TREE classifier -> call fit on it

- OVERFIT _> good performance validation ->

- GOOD GOOD on iris traingin -> with decision tree

- DECISION TREE _> WILL ALWAYS TRY TO MAKE AS MUCH NO _> SURPRISE/ så meget vished som mulig
- 
- 1000 cast
- save result
- make a histogram

Decision boundary will look more organic on a decision tree than 
 SAMPLE 10 different samples- -> 
        - > scale / paramaterize the samples 
        - > calculate a mean -> for each batch 
          -> if we are within one standard devitation  -> from the mean ->
          -> the more deviations from the mean 
- 

Model continues to insert decision nodes in the tree -> if there is only one lable in a decision node
we dont need to break more down -> all decision node contins  a leaf node then perfect trainnig
you could have leaf nodes with more labels in an would yield and "imperfect score of 1" 

you can allow a certain degree of impurity -> hyper parameters -> can be configures 

- *(Add more as needed)*



---

### 📝 Detailed Notes
#### 1. Introduction
- Key points from the introduction
- Important terms or definitions
- [Example, if applicable]

#### 2. RANDOM FOREST -> 

- WE INJECT ENTROPY SO WE GO FROM DETERMINISTIC TO NON - DETEREMINISTIC

- SAMPLE WITH REPLACE - SAMPLE AND CAN TAKE THE SAME SAMPLE MANY TIME
- SAMPLE WITHOUT REPLACEMENT - cannot take the same sample twice


-> sample: > m = 1000 -> sample 400 -> sample 37 -> not replacement on feautures 

-> RECIPE :

Bootstrap new dataset by sampling from the dataset with replacemnet


Can make the decision trees vote -> and majority rules _ 

REGRESSION we can use mean and otherwise mode 

MODE: flertals opgørelse-> 

RANDOM FOREST_ PERFORM Very well on complex data -> MNIST -> S

__>> GO TO SCIKIT LEARN WHAT hyper parameters can a screw to and see how it performs -< 

- Explanation and insights
- Key takeaways or quotes
- [Example, if relevant]

#### 3. Main Topic 2
- Explanation and insights
- Diagrams or formulas (e.g., `y = mx + b`)
- [Example, if needed]

---

### 🧠 Insights & Takeaways
- Personal reflections or insights on the lecture
- Questions or points to explore further
- Real-world applications or connections to previous lectures

---

### ❓ Questions & Discussions
- **Question 1:** [Question text]
- **Question 2:** [Question text]
- *(Add more as you think of them)*

---

### 📌 Key Terms & Definitions
- **Term 1:** Definition
- **Term 2:** Definition
- *(Add more as needed)*

---

### 🔗 Additional Resources
- [Link to relevant article, paper, or tool]
- [Link to further reading or videos]

---

*End of Lecture Notes*
