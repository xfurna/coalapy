# CoALa
Paper implementation of Approximate Graph Laplacians for Multimodal Data Clustering.Here we are developing a python package to make everyone's life easy. 
## Introduction:
One of the important approaches of handling data heterogeneity in multimodal data clustering is modeling each modality using a separate similarity graph. Information from the multiple graphs is integrated by combining them into a unified graph. A major challenge here is how to preserve cluster information while removing noise from individual graphs. In this regard, a novel algorithm , termed as CoALa, is proposed that integrates noise-free approximations of multiple similarity graphs.
## How does it work?
* It approximates a graph using the most informative eigenpairs of its Laplacian which contain cluster information.
* The approximate Laplacians are then integrated for the construction of a low-rank subspace that best preserves overall cluster information of multiple graphs.
* However, this approximate subspace differs from the full-rank subspace which integrates information from all the eigenpairs of each Laplacian.
* Matrix perturbation theory is used to theoretically evaluate how far approximate subspace deviates from the full-rank one for a given value of approximation rank.
* Finally, spectral clustering is performed on the approximate subspace to identify the clusters.
## Matrices:
1. Normalised Laplacian	:![cc](https://latex.codecogs.com/gif.latex?%3A%20L%20%3D%20D%5E%7B1/2%7D%28D%20-%20W%29D%5E%7B-1/2%7D)
2. Shifted Laplacian	:![dfea](https://latex.codecogs.com/gif.latex?L%20%3D%202I%20-%20L%20%3D%20I%20&plus;%20D%5E%7B-1/2%7DWD%5E%7B-1/2%7D)
3. Random walk		:![vsdv](https://latex.codecogs.com/gif.latex?RW%3DD%5E%7B-1%7DL)
Where D  is degree matrix and W is similarity matrix

## Proposed Method

### Convex Combination of Graph Laplacian

- Let a multimodal data set, consisting of M modalities, be given by X1, . . . ,Xm, . . . ,XM
- Shifted Laplacian for modality ![fbewgfbfb](https://latex.codecogs.com/gif.latex?X_%7Bm%7D%3A%20L_%7Bm%7D%20%3D%20I%20&plus;%20D%5E%7B-1/2%7D_%7Bm%7D%20W_%7Bm%7DD%5E%7B-1/2%7D)
- The rank r eigenspace of shifted Laplacian Lm for modality Xm is defined by a two-tuple:
 ![bfbdfbew](https://latex.codecogs.com/gif.latex?%5CPsi%20%28L%5E%7Br%7D_%7Bm%7D%29%20%3D%20%3CU%5E%7Br%7D_%7Bm%7D%5E%7B%7D%2C%5Csum%5E%7Br%7D_%7Bm%7D%3E)
### Construction of Joint Eigenspace:
* ![fewDVFSf](https://latex.codecogs.com/gif.latex?L%3DZ%5CGamma%20Z%5E%7BT%7D)
    * Joint shifted Laplacian
    * Z consists of the eigenvector of L
    * ![..](https://latex.codecogs.com/gif.latex?%5CGamma)=diag(![..](https://latex.codecogs.com/gif.latex?%5Cgamma%20_%7B1%7D.........%5Cgamma%20_%7Bn%7D))
* ![..vdsfvwv.](https://latex.codecogs.com/gif.latex?%5CPsi%20%28L%5E%7Br%7D%29%20%3D%20%3CZ%5E%7Br%7D%2C%5CGamma%5E%7Br%7D%3E)
    * ![...vf.](https://latex.codecogs.com/gif.latex?%5CPsi%20%28L%29%5E%7Br%7D) represents that eigenspace has rank r
* ![..vv...](https://latex.codecogs.com/gif.latex?L%5E%7Br%5E%7B*%7D%7D%3D%5Csum_%7Bm%3D1%7D%5E%7BM%7D%5Calpha%20_%7Bm%7DL_%7Bm%7D%5E%7B%5E%7Br%7D%7D)
    * ![.a.a.a.](https://latex.codecogs.com/gif.latex?L%5E%7Br%5E%7B*%7D%7D)  represents convex combination of best rank approximation of Laplacians Lm of indivisual modality Xm..

## Proposed CoALa Algorithm
*  **Input:** Similarity matrices ![d.lalsacad](https://latex.codecogs.com/gif.latex?W_%7B1%7D%2C.......%2CW_%7BM%7D) combination vector= ![.a.s.d.sca](https://latex.codecogs.com/gif.latex?%5B%5Calpha%20_%7B1%7D%2C.......%2C%5Calpha%20_%7BM%7D%5D) number of clusters k, and rank r >= k.
*  **Output:** Clusters ![dbb.it](https://latex.codecogs.com/gif.latex?%5BA_%7B1%7D%2C.......%2CA_%7Bk%7D%5D)
* for m=1 to M do
* Construct degree matrix Dm and shifted normalized Laplacian Lm.
* Compute the eigen-decomposition of Lm.
* Store the r largest eigenvalues in r m and corresponding eigenvectors in Urm in the rank r eigenspace of Xm.
* end for
* Compute initial basis![ffccc](https://latex.codecogs.com/gif.latex?U_%7B1%7D%20%5Cleftarrow%20U_%7Br%7D)
* for m = 1 to M - 1 do
* Compute Sm+1, projected component Pm+1, and residual component Qm+1 .
* ![tfcfc fcsac,c.c.c.ccdss](https://latex.codecogs.com/gif.latex?%5Cgamma%20_%7Bm&plus;1%7D%5Cleftarrow) Gram-Schmidt orthogonalization of Qm+1
* Update basis ![v](https://latex.codecogs.com/gif.latexU_%7Bm&plus;1%7D%5Cleftarrow%20%5B?U_%7Bm%7D%20%5Cgamma%20_%7Bm&plus;1%7D%5D)
* <strong>end for</strong>
* For each modality Xm, compute Hm 
* Compute the new eigenvalue problem H.
* Solve the eigen-decomposition of H to get R and H.
* Compute eigenvectors ![p](https://latex.codecogs.com/gif.latex?V%5Cleftarrow%20U_%7BM%7DR)
* Compute joint eigenspace 	![salkcndandsnvd](https://latex.codecogs.com/gif.latex?%5CPsi%20L%5E%7Br%5E%7B*%7D%7D%5Cleftarrow%20%3CV%5E%7Br%7D%20%5CPi%20%5E%7Br%7D%3E)
* Find k largest eigenvectors Vk = [v1 . . . vk].
* Perform clustering on the rows of Vk using k-means algorithm.
* Return clusters A1, . . . ,Ak from k-means clustering.

---

## Contribution

Not accepting.

## Notes
- Code has been written considering that the raw modality table has nodes in columns and features in rows.