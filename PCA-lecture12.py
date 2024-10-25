# Lecture 12 

# Dimensionalty reduction _> 

# CATEGORY : UNSUPERVISED LEARNING 



# PRINCIPAL Compnonent analysis (PCA

#USED FOR DIMENSIONALITY REDUCTION
# 2 MAIN USES
    # 1 - > VISUALISATION of HIGHDIMENSIONAL DATA TO 2Dimensions
    # 2 - > DIMENSIONALITY reduction in compression / reduction when combining number of features when training models
            # GOAL : TO reduce data size and computation time


# PCA IS POPULAR


# DATA MUST BE STANDARDIZED BEFORE APPLYING PCA
      # ---> USE StandardScaler from sklearn.preprocessing for this



# STEPS TO IMPLEMENT PCA

    #1. Compute the covariance matrix Sigma:
    #        sigma = 1 / m * X^T*X
    # X = data set
    # m = number of samples 

    #2. Use singular value decomposition to compute principal components U:
    # U, S, V = np.linalg.svd(Sigma)

    #3. Compute the projection of Z of X onto k dimensions:
    #         Z = X*Uk.  (lowered k)
    # Uk = first k columns of matrix U

# CODE IMPLEMENTATION 


import numpy as np

def pca(X, k):
   m = X.shape[0]
   Sigma = (1/float(m)) * (X.T.dot(X))
   U, S, V = np.linalg.svd(Sigma)
   U = U[:, 0:k]
   Z = X.dot(U)
   return Z


# Scikit-learn should also feature a PCA implementation

# ! heads up : features are defined in latent space from PCA 
# features can be directly interpreted indvidually. 

