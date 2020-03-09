# CoALa
Paper implementation of Approximate Graph Laplacians for Multimodal Data Clustering
# Introduction:
One of the important approaches of handling data heterogeneity in multimodal data clustering is modeling each modality using a separate similarity graph. Information from the multiple graphs is integrated by combining them into a unified graph. A major challenge here is how to preserve cluster information while removing noise from individual graphs. In this regard, a novel algorithm , termed as CoALa, is proposed that integrates noise-free approximations of multiple similarity graphs.
# How does it work?
* It approximates a graph using the most informative eigenpairs of its Laplacian which contain cluster information.
* The approximate Laplacians are then integrated for the construction of a low-rank subspace that best preserves overall cluster information of multiple graphs.
* However, this approximate subspace differs from the full-rank subspace which integrates information from all the eigenpairs of each Laplacian.
* Matrix perturbation theory is used to theoretically evaluate how far approximate subspace deviates from the full-rank one for a given value of approximation rank.
* Finally, spectral clustering is performed on the approximate subspace to identify the clusters.
# Matrices:
1. Normalised Laplacian	: L = D-1/2(D ?W)D-1/2 
2. Shifted Laplacian		: L = 2I ? L = I + D?1/2WD?1/2
3. Random walk		:RW=D-1L
Where D  is degree matrix and W is similarity matrix

## Proposed Method
1.Convex Combination of Graph Laplacians	: 
->Let a multimodal data set, consisting of M modalities, be given by X1, . . . ,Xm, . . . ,XM.
->Shifted Laplacian for modality Xm: Lm = I + D?1/2m WmD?1/2
->The rank r eigenspace of shifted Laplacian Lm for modality Xm is defined by a two-tuple:
    ¥ (Lrm) = <Urm, ?rm>
2. Construction of Joint Eigenspace:
->L = Z?ZT 
* Joint shifted Laplacian
* Z consists of the eigenvector of L
* ?=diag(?1,…………….., ?n)
->¥(Lr)=<Zr, ?r>
* ¥(Lr) represents that eigenspace has rank r
-> Lr*=  ??mLmr
* Lr*  represents convex combination of best rank approximation of Laplacians Lm of indivisual modality Xm..

## Proposed CoALa Algorithm
Input: Similarity matricesW1, . . . ,WM, combination vector= [?1, . . . , ?M], number of clusters k, and rank r ? k.
Output: Clusters A1, . . . ,Ak.
1: for m ? 1 to M do
2: Construct degree matrix Dm and shifted normalized Laplacian Lm.
3: Compute the eigen-decomposition of Lm.
4: Store the r largest eigenvalues in r m and corresponding eigenvectors in Urm in the rank r eigenspace of Xm.
5: end for
6: Compute initial basis U1 ? Ur1 .
7: for m ? 1 to M ? 1 do
8: Compute Sm+1, projected component Pm+1, and residual component Qm+1 .
9: ?m+1 ? Gram-Schmidt orthogonalization of Qm+1. 
10: Update basis Um+1 ?[Um ?m+1 ]
11: end for
12: For each modality Xm, compute Hm as in .
13: Compute the new eigenvalue problem H as in .
14: Solve the eigen-decomposition of H to get R and H.
15: Compute eigenvectors V ? UMR.
16: Compute joint eigenspace 	¥ (Lr?) ? (Vr,Hri).
17: Find k largest eigenvectors Vk = [v1 . . . vk].
18: Perform clustering on the rows of Vk using k-means algorithm.
19: Return clusters A1, . . . ,Ak from k-means clustering.








