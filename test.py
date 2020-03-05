# """modalities here"""
# import src

# W=[[-1, 3, 5], [9, 4, 2], [6, 2, -6]]

# # print (W)
# # m = modalities.modality(W)
# # path = None
# # df = src.dfhandler.dframe_csv(path, mat_type='gaussian')
# df = src.modalities.modality( mat_type="gaussian")
# print(df.W)\
import src.modalities as modality

path = '/hdd/Ztudy/BTP/code/CoALa/toy.csv'
x1= modality.modality(path, mat_type="gaussian")
print(x1.degree, '\n', x1.W, '\n', x1.laplacian)