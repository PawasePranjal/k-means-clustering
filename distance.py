#
# X = np.lin-space(0, 10, 6).reshape(3, 2)
# print(X)
# Y = X[np.random.choice(3, size=2)]
# print(Y)
# # DXX = metrics.pairwise_distances(X, metric="euclidean")
# # print(DXX)
# DYX = metrics.pairwise_distances(X, Y, metric="euclidean")
# print(DYX)
#
# df = pd.DataFrame(DYX, columns=["column_1", "column_2"])
# print("\nPandas DataFrame: ")
# print(df)
# df["column_3"] = ''
# print(df)
# for i in range(len(df)):
#     if df.loc[i, "column_1"] < df.loc[i, "column_2"]:
#         df.loc[i, "column_3"] = df.loc[i, "column_1"]
#     else:
#         df.loc[i, "column_3"] = df.loc[i, "column_2"]
# print(df)

# df["column_3"]=df[["column_1","column_2"].min(axis=1)]
# df["column_3"]=df.apply(min,axis=1)
# print(df)


# DYY = metrics.pairwise_distances(Y, metric='euclidean')
# print(DYY)
# import numpy as np
# import pandas as pd
# A = np.arange(0, 20, 2).reshape(5, 2)
# # print(A)
# B=np.random.choice(3,size=2)
# # print(B)
# df = pd.DataFrame(A, columns=["A", "B"])
# # print(df)
# C = [1, 1, 2, 1, 2]
# df["C"] = C
# print(df)
import numpy as np

# tolerance=0.05
A = np.arange(4, 20, 2).reshape(4, 2)
print(A)
# A = A>0
# print(A)
C = np.all(A > 5)
print(C)

# B = np.arange(20, 40, 2).reshape(5, 2)
# print(B)
# C=np.subtract(A,B)
# print(C)
import numpy as np
import pandas as pd

# A = np.arange(0, 20, 2).reshape(5, 2)
# # print(A)
# B = np.random.choice(3, size=2)
# # print(B)
# df = pd.DataFrame(A, columns=["A", "B"])
# # print(df)
# C = [1, 1, 2, 1, 2]
# df["C"] = C
# # print(df)

# groups = df.groupby(["C"])
# # print(df_1)
#
# for group_name, group in groups:
# print(group_name)
# print(group)
