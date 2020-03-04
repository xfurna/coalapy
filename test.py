"""modalities here"""
import src

W=[[-1, 3, 5], [9, 4, 2], [6, 2, -6]]

# print (W)
# m = modalities.modality(W)
# path = None
# df = src.dfhandler.dframe_csv(path, mat_type='gaussian')
df = src.modalities.modality( mat_type="gaussian")
print(df.W)