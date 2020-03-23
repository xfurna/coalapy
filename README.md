# CoALa
Paper implementation of- [Approximate Graph Laplacians for Multimodal Data Clustering](https://ieeexplore.ieee.org/document/8859233)

# How does it work?
* It approximates a graph using the most informative eigenpairs of its Laplacian which contain cluster information.
* The approximate Laplacians are then integrated for the construction of a low-rank subspace that best preserves overall cluster information of multiple graphs.
* However, this approximate subspace differs from the full-rank subspace which integrates information from all the eigenpairs of each Laplacian.
* Matrix perturbation theory is used to theoretically evaluate how far approximate subspace deviates from the full-rank one for a given value of approximation rank.
* Finally, spectral clustering is performed on the approximate subspace to identify the clusters.

> Refer to [the papaer](https://ieeexplore.ieee.org/document/8859233) for more detailed mathematical analysis.

# Contribution
Unwelcomed