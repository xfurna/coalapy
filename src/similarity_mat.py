from scipy.linalg import fractional_matrix_power
import numpy as np

def matrix(mat_type):
     if mat_type == 'gaussian':
        Gaussian()
     if mat_type=='Identity':
        Identity()
     if mat_type=='Degree'
        Degree()
     if mat_type == 'Laplacian'
        Laplacian()
     if mat_type == 'Norm_Laplacian'
        Norm_Laplacian()
     if mat_type == 'Random_Walk'
        Random_Walk()
     if mat_type == 'Shifted_Laplacian'
        Shifted_Laplacian()

def Gaussian():
    print ("gauddd")


    
# Identity matriX
def Identity(x):
    for rows in range(0,x):
        for columns in range(0,x):
            if(rows==columns):
                I[rows][columns]=1
            else:
                I[rows][columns]=0
    return I
# degree matrix
    
def Degree(x):
    for rows in range(0,x):
        for columns in range(0,x):
            sum=sum+A[columns]
        for columns in range(0,x):
            if(rows==columns):
                D[rows][columns]=sum
            else:
                D[rows][columns]=0
        sum=0
    return D
#Laplacian matrix
#L=D-A
def Laplacian(A,D):
    L=D-A
    print("laplacian matrix:")
    return L
#normalised laplacian
#L=D−1/2(D −W)D−1/2
def Norm_laplacian(A,D):
    D_= fractional_matrix_power(D,-0.5)
    #a = np.array([[1, 0],[0, 1]])
    #b = np.array([[4, 1],[2, 2]])
    #c=np.matmul(a, b)
    #ANS:[[4 1][2 2]]
    Q=np.matmul(D_,L)
    LL=np.matmul(Q,D_)
    return LL
#random walk matrix
#RW=D-1L
def Random_Walk(D,L):
    D___= fractional_matrix_power(D,-1)
    RW=np.matmul(D___,L)
    return RW
#shifted laplacian
#SL = I + D−1/2 WD−1/2 .
def Shifted_Laplacian(I,D,A):
    D__=fractional_matrix_power(D,-0.5)
    F=np.matmul(D__,A)
    G=np.matmul(F,D__)
    SL=I+G
    return SL


    
    
   
