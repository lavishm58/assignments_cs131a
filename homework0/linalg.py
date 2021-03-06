import numpy as np
import math

def dot_product(a, b):
    """Implement dot product between the two vectors: a and b.

    (optional): While you can solve this using for loops, we recommend
    that you look up `np.dot()` online and use that instead.

    Args:
        a: numpy array of shape (x, n)
        b: numpy array of shape (n, x)

    Returns:
        out: numpy array of shape (x, x) (scalar if x = 1)
    """
    out = np.zeros(shape=(a.shape[0],b.shape[1]))
    ### YOUR CODE HERE
    for i in range(0,a.shape[0]):
        for j in range(0,b.shape[1]):
            out[i][j]=0
            for k in range(0,a.shape[1]):
                out[i][j]+=a[i][k]*b[k][j]
    ### END YOUR CODE
    return out


def complicated_matrix_function(M, a, b):
    """Implement (a.T * b) * (M * a.T).

    (optional): Use the `dot_product(a, b)` function you wrote above
    as a helper function.

    Args:
        M: numpy matrix of shape (x, n).
        a: numpy array of shape (1, n).
        b: numpy array of shape (n, 1).

    Returns:
        out: numpy matrix of shape (x, 1).
    """
    X = dot_product(np.transpose(a),b)
    Y = dot_product(M,a)
    out = dot_product(Y,X)
    ### YOUR CODE HERE
    ### END YOUR CODE

    return out


def svd(M):
    """Implement Singular Value Decomposition.

    (optional): Look up `np.linalg` library online for a list of
    helper functions that you might find useful.

    Args:
        M: numpy matrix of shape (m, n)

    Returns:
        u: numpy array of shape (m, m).
        s: numpy array of shape (k).
        v: numpy array of shape (n, n).
    """
    R = dot_product(M,np.transpose(M))
    w, ar = np.linalg.eig(R)
    
    u = ar
    s = np.zeros(shape=(w.shape[0],w.shape[0]))
    
    for i in range(w.shape[0]):
        s[i][i] = math.sqrt(w[i])
    v = np.transpose(ar)
    ### YOUR CODE HERE
    ### END YOUR CODE

    return u, s, v


def get_singular_values(M, k):
    """Return top n singular values of matrix.

    (optional): Use the `svd(M)` function you wrote above
    as a helper function.

    Args:
        M: numpy matrix of shape (m, n).
        k: number of singular values to output.

    Returns:
        singular_values: array of shape (k)
    """
    u,s,v = svd(M)
    singular_values = np.zeros(shape=(1,s.shape[0]))
    ### YOUR CODE HERE
    for i in range(s.shape[0]):
        singular_values[0,i] = s[i][i]
    ### END YOUR CODE
    return singular_values[0,0:k]


def eigen_decomp(M):
    """Implement eigenvalue decomposition.

    Args:
        matrix: numpy matrix of shape (m, n)

    Returns:
        w: numpy array of shape (m, m) such that the column v[:,i] is the eigenvector corresponding to the eigenvalue w[i].
        v: Matrix where every column is an eigenvector.
    """
    w,v = np.linalg.eig(M)

    ### YOUR CODE HERE

    ### END YOUR CODE
    return w, v


def get_eigen_values_and_vectors(M, k):
    """Return top k eigenvalues and eigenvectors of matrix M. By top k
    here we mean the eigenvalues with the top ABSOLUTE values.

    (optional): Use the `eigen_decomp(M)` function you wrote above
    as a helper function.

    Args:
        M: numpy matrix of shape (m, m).
        k: number of eigen values and respective vectors to return.

    Returns:
        eigenvalues: list of length k containing the top k eigenvalues
        eigenvectors: list of length k containing the top k eigenvectors
            of shape (m, 1)
    """
    w,v = eigen_decomp(M)
    eigenvalues = w[0:k]
    eigenvectors = v[0:k,:]
    ### YOUR CODE HERE
    ### END YOUR CODE
    return eigenvalues, eigenvectors
