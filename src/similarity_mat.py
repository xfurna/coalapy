from scipy.linalg import fractional_matrix_power

def matrix(mat_type):
    if mat_type == 'gaussian':
        Gaussian()


def matrix(mat_type):
    if mat_type == 'gaussian':
        Gaussian()


def Gaussian():
    print ("gauddd")


    
# Identity matriX
    if mat_type=='Identity':
        Identity()
def Identity(x):
    for rows in range(0,x):
        for columns in range(0,x):
            if(rows==columns):
                I[rows][columns]=1
            else:
                I[rows][columns]=0
    return I
# degree matrix
    if mat_type=='Degree'
        Degree()
def Degree_matrix(x):
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
    if mat_type == 'Laplacian'
        Laplacian()
def Laplacian(A,D):
    L=D-A
    print("laplacian matrix:")
    return L
#normalised laplacian
    if mat_type == 'Norm_Laplacian'
        Norm_Laplacian()
def normalised_laplacian(A,D):
    D_= fractional_matrix_power(D,-0.5)
    LL=D_*(D-A)*D_
    return LL
#random walk matrix
    if mat_type == 'Random_Walk'
        Random_Walk()
def Random_Walk(D,L):
    D___= fractional_matrix_power(D,-1)
    RW=D___L
    return RW
#shifted laplacian
    if mat_type == 'Shifted_Laplacian'
        Shifted_Laplacian()
def shifted_laplacian(I,D,A):
    D__=fractional_matrix_power(D,-0.5)
    SL=I+D__*(A)*D__
    return SL


    
    
   
