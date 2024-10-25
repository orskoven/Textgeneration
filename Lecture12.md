# 📓 Applied AI Notes & Reflections

---

## 📅 Date:  25. october
## 🧑‍🏫 Instructor/Source:  Henrik Strøm 
## 🔍 Session Objective  
Peer review feed back
Principal component analysis

RAW Notes : Should be transformed ->Z 

[ Jump in : henrik explains to output nodes _> when discussion of 
Softmax always the sum of 1 of a probability distribution -> and get a confidence in the result number / result -> you get to paramtric probabilty distribution in your output the probability sum is always 100 and when you have two output nodes in a binary classification _> so you have node1: 0.8 being a cat and node2:0.2 not a dog 

TWO OUPUT NODES WITH A SOFTMAX -> SOFTMAX MAKES PROBABILITY DISTRIBUTION and can be interpreted as confidenc-> 


More than two ouput nodes are not needed for binary classification 


MUST BE PRINTED TO BRAIN -> GROUND KNOWLEDGE FOR EXAM


CNN's: 

    - convolutional neual networks

 
 ###Features extraction : CNN is ment for image data -> and are really good at that 


    consists of poolings and convolutions -> look at a little area in picture 
    pooling layer : feauture extraction from convultional layer 
                      -> try to enforce strongest signals and turn down weekeast 



        The outlining layers : will take care of contrasts ->
               innner is more detailed the longer we approach the inner layers

            

### Features will become input to classfication network 

MNIST -> steril data that benefit smaller from features extraction

Feature extraction is a strong toolset in terms of picture data 



    import tensorflow as tf
    import tensorflow_datasets as tfds

    (ds_test, ds_val, ds_train), ds_info = tfds.load(
        'mnist',
        split = [ 'test', 'train[0%:17%]


### input image 

convelutional kernel -> scans each picture pixel a small piece of the picture at the time -> 

### MAX Pooling reduces the and filters square don and uses stride 2 reduces 4 x 4 to 2 x 2 







---

### 📝 Topic Overview
- **Topic:**
Peer review 
Principal componant analysis
- **Subtopics Covered:**  
Bibliography with latex 
- **Context in Course:** How does this topic relate to previous sessions or future topics?

---

### 📚 Key Concepts
| Concept        | Description/Definition                                     | Example/Context                        |
|----------------|------------------------------------------------------------|----------------------------------------|
| Bibliography   | Find google scholar to generate latex bibliography         |        |
| weights      | Generated randomely connecting line between perceptrons : reson being random : floats can give os better information as small numbers around zero                           | Example or context to illustrate       |
| Fully conected network       | All nodes are connect from input to hidden to ouput layer                            | input circles connected to hidden to output layer are all connected on each other by lines that canno extend layers       || Nodes      | input are clean input : hidden layer notes have a sum function and activatoin function ( sum function multiplies each weight from the corresponding node in the previos layer and uses the activation to scale the right weighting when we cannot make a polynomial decision boundary                          | Example or context to illustrate       || Activation function       | important                             | Example or context to illustrate       |


---

### 🧠 Techniques, Algorithms & Models
| Technique/Algorithm/Model | Purpose | Key Details | Questions & Considerations |
|---------------------------|---------|-------------|----------------------------|
| Technique 1               | What it achieves or solves | Important parameters, steps, or equations | Any lingering questions, confusions, or considerations |
| Algorithm 2               | What it achieves or solves | Important parameters, steps, or equations | Any lingering questions, confusions, or considerations |

---

### ⚙️ Practical Applications
- **Use Case 1:** Brief description of real-world application or industry use
- **Use Case 2:** Brief description of real-world application or industry use
- **Additional Notes:** Any additional thoughts on applications discussed  
- **Current Industry Relevance:** How is this applied AI concept evolving today? (Optional)

---

### 🔄 Connections to Prior Knowledge
*Link this topic to any previous knowledge or related topics.*  
- **Concepts from Previous Sessions:**  
- **Related Personal/Professional Experiences:**  
- **Areas of Improvement or Clarification:** What past concepts could you revisit to enhance your understanding?

---

### 💡 Key Takeaways & Insights
- **Main Insights:**  
- **Challenges & Limitations Discussed:**  
- **Personal Observations:** Any unique observations or perspectives that arose while learning this content?  

---

### 🎯 Action Steps for Reinforcement
- **Practice Goals:** (e.g., code exercises, building a model, implementing an algorithm)
- **Reading/Research:** Additional topics to read or research based on this session
- **Implementation Ideas:** Real or hypothetical projects to apply this concept
- **Reflection on Learning:** What strategies worked well today? Any adjustments for future learning?

---

### 🧩 Resources & Further Reading
- **Link 1:** [Title](URL) - Brief description of content  
- **Link 2:** [Title](URL) - Brief description of content  
- **Instructor’s Recommendations:** Include any references or readings suggested by the instructor

---

### ❓ Questions, Reflections & Next Steps
- **Unanswered Questions:** Any questions that remain unclear after the session  
- **Reflective Thoughts:** How has this session influenced your perspective on AI?  
- **Topics for Deeper Dive:** List topics you’d like to explore in more depth

---

### 📈 Tracking Progress (Optional)
*Use this space to track your progress and self-assess your understanding.*  
- **Self-Assessment:** Rate your understanding of today’s topic (1-5)
- **Progress Notes:** Briefly note any progress since last session
- **Challenges Faced:** Any specific difficulties that slowed down learning today

---
