Here’s a refined version of your notes with added clarity, structure, and a new section for further reading and industry examples. This improved version includes a more concise explanation of each concept, better-organized equations and code, and relevant real-world applications to solidify understanding.



# 📓 Applied AI Notes & Reflections

---

## 📅 Date:  25 October
## 🧑‍🏫 Instructor/Source:  Henrik Strøm 
## 🔍 Session Objective  
- Receive peer review feedback  
- Understand Principal Component Analysis (PCA) for dimensionality reduction  
- Explore CNNs and Softmax for image classification and probability interpretation

---

### 📝 Topic Overview
- **Topic:** Peer Review and PCA
- **Subtopics Covered:** LaTeX bibliography creation, CNN fundamentals, and Softmax for binary classification.
- **Context in Course:** These concepts build foundational skills in applied AI by helping interpret model outputs, reduce complexity in high-dimensional data, and improve classification performance for image tasks.

---

### 📚 Key Concepts

#### 1. Bibliography Creation
- **Definition:** Using Google Scholar to generate LaTeX-formatted bibliographies for efficient and accurate citations.
- **Example:** Use BibTeX format for importing citations directly into LaTeX documents.

#### 2. Weights in Neural Networks
- **Definition:** Randomly initialized values connecting nodes. This randomness helps networks generalize better by avoiding deterministic paths.
- **Example:** Weights around zero reduce bias and allow for more balanced learning, capturing small variations in the data.

#### 3. Fully Connected Networks
- **Definition:** A network structure where each node in one layer connects to every node in the next layer, allowing comprehensive feature learning across layers.
- **Example:** In a 3-layer network, every input node influences every output node, maximizing information flow.

#### 4. Activation Functions
- **Definition:** Functions that scale the output of a node to add non-linearity, allowing the network to learn complex data patterns.
- **Examples:** 
  - ReLU: \( f(x) = \max(0, x) \), commonly used in hidden layers.
  - Softmax: Converts outputs into probabilities, often applied in the final layer for classification.

**Reflection:** Understanding these fundamental components—weights, connectivity, and activation functions—reveals how neural networks operate at a basic level. McCulloch and Pitts’ early work modeled logical neurons, forming the foundation of today’s network architectures.

**Classical Paper Reference:**  
- McCulloch, W. S., & Pitts, W. (1943). A logical calculus of the ideas immanent in nervous activity. *Bulletin of Mathematical Biophysics*, 5, 115–133.

---

### 🧠 Techniques, Algorithms & Models

#### Softmax Function
The Softmax function normalizes model outputs into a probability distribution, making it particularly useful for multi-class classification tasks.

**Mathematical Equation:**

\[
\sigma(z_i) = \frac{e^{z_i}}{\sum_{j=1}^K e^{z_j}}
\]

where:
- \( z_i \) is the raw score for each class,
- \( K \) is the total number of classes.

**Python Code Example:**

```python
import tensorflow as tf

# Example logits for 3 classes
logits = tf.constant([2.0, 1.0, 0.1])

# Apply Softmax
softmax_output = tf.nn.softmax(logits)

print("Softmax output:", softmax_output.numpy())

Reflection: The Softmax function, discussed by Bridle (1990), enhances our ability to interpret neural network outputs by framing them as probabilities. This is crucial in tasks like image classification, where we need confidence measures for each class.

Classical Paper Reference:

	•	Bridle, J. S. (1990). Probabilistic interpretation of feedforward classification network outputs. Neurocomputing, 227-236.

Principal Component Analysis (PCA)

PCA is a statistical technique for dimensionality reduction, useful for simplifying large datasets by focusing on the main variance directions.

Key Steps in PCA:

	1.	Compute the Covariance Matrix:
[
\Sigma = \frac{1}{n} \sum_{i=1}^{n} (x_i - \mu)(x_i - \mu)^T
]
	2.	Eigenvalue Decomposition:
Calculate eigenvectors ( \mathbf{u}_k ) and eigenvalues ( \lambda_k ) to find principal components.

Python Code Example:

from sklearn.decomposition import PCA
import numpy as np

# Example data
data = np.array([[2.5, 2.4], [0.5, 0.7], [2.2, 2.9], [1.9, 2.2], [3.1, 3.0]])

# Apply PCA to reduce to 1 component
pca = PCA(n_components=1)
principal_components = pca.fit_transform(data)

print("Principal components:", principal_components)

Reflection: PCA, developed by Pearson (1901) and expanded by Hotelling (1933), remains a core tool for data pre-processing. It simplifies models by retaining key information, improving efficiency without sacrificing accuracy.

Classical Paper References:

	•	Pearson, K. (1901). On lines and planes of closest fit to systems of points in space. Philosophical Magazine, 2(11), 559–572.
	•	Hotelling, H. (1933). Analysis of a complex of statistical variables into principal components. Journal of Educational Psychology, 24(6), 417.

⚙️ Practical Applications

	•	CNN in Image Classification: Used in tasks like facial recognition, self-driving cars, and medical imaging to detect patterns in image data.
	•	PCA in Data Pre-processing: PCA helps in reducing the feature space for complex datasets, enhancing the efficiency of algorithms without significant loss of information.

Reflection: Real-world applications showcase the versatility of CNNs and PCA. For instance, PCA is widely used in finance to analyze time series data, while CNNs have become industry standards for visual recognition tasks.

🔄 Connections to Prior Knowledge

	•	Previous Sessions: Builds on neural network structures and activation functions.
	•	Personal/Professional Experiences: Applied in object detection projects and dimensionality reduction tasks.
	•	Areas for Improvement: Further explore Softmax interpretation in multi-class settings to strengthen understanding of output probabilities.

💡 Key Takeaways & Insights

	•	Main Insights: Softmax aids in probabilistic interpretation, while PCA and CNNs offer critical tools for dimensionality reduction and image classification.
	•	Challenges & Limitations: Overfitting is a risk in CNNs, but regularization can mitigate this. PCA may lose information if not applied carefully.
	•	Observations: Binary classification benefits from Softmax as it enhances interpretability by displaying clear confidence levels.

🎯 Action Steps for Reinforcement

	•	Practice Goals: Work on coding exercises for CNN and PCA in TensorFlow.
	•	Reading/Research: Deepen understanding of CNN architectures and Softmax applications in real-world settings.
	•	Implementation Ideas: Test PCA and CNN on new datasets to observe effects of dimensionality reduction and classification accuracy.

🧩 Further Reading & Industry Examples

	1.	CNN Architectures
	•	Krizhevsky, A., Sutskever, I., & Hinton, G. E. (2012). ImageNet classification with deep convolutional neural networks. Advances in Neural Information Processing Systems, 25, 1097-1105. This paper introduced AlexNet, a breakthrough in image classification, paving the way for CNN use in industries from tech to healthcare.
	2.	Softmax Applications in NLP
	•	Devlin, J., Chang, M. W., Lee, K., & Toutanova, K. (2018). BERT: Pre-training of deep bidirectional transformers for language understanding. arXiv preprint arXiv:1810.04805. BERT uses Softmax in its token classification tasks, an example of Softmax’s versatility beyond image classification.
	3.	PCA in Finance
	•	Litterman, R., & Scheinkman, J. (1991). Common factors affecting bond returns. Journal of Fixed Income, 1(1), 54–61. PCA simplifies financial data analysis by identifying dominant factors, improving trading and investment strategies.

Reflection: These classic papers highlight PCA, CNNs, and Softmax’s impact across industries, from technology to finance. Engaging with these studies enriches our understanding of AI’s versatility and emphasizes the importance of grounding new methods in established research.

❓ Questions, Reflections & Next Steps

	•	Unanswered Questions: How does PCA affect model interpretability when applied to very high-dimensional datasets?
	•	Reflective Thoughts: Understanding CNNs has deepened my appreciation for structured feature extraction’s role in AI.
	•	Topics for Further Exploration: Dropout for regularization and alternative activation functions like leaky ReLU.

📈 Progress Tracking

	•	Self-Assessment: 4/5 - Strong grasp on CNNs and PCA; further review on Softmax’s multi-class implications needed.
	•	Progress Notes: Improved understanding of layer structures and feature extraction.
	•	Challenges: Softmax’s probability interpretation in multi-class settings remains challenging.



This refined version includes a **Further Reading & Industry Examples** section, connecting concepts to real-world applications and foundational research, enhancing both theoretical and practical understanding.
