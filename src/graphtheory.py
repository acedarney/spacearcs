import pandas as pd


class Graph:
    def __init__(self, inp):
        self.A = {}
        df = pd.DataFrame.from_csv(inp + '_EdgeList.csv',
                                   header=None,
                                   index_col=None)
        df.columns = ['FromNode', 'ToNode']
        self.M = df
        self.create_adj_mat(self.M)

    def create_adj_mat(self, df):
        A = {}
        for _, link in df.iterrows():
            if link['FromNode'] in A:
                if link['ToNode'] in A[link['FromNode']]:
                    pass
                else:
                    A[link['FromNode']].append(link['ToNode'])
            else:
                A[link['FromNode']] = [link['ToNode']]
        self.A = A


class Edge:
    def __init__(self, EdgeType, ID, FromNode, ToNode):
        self.Type = EdgeType
        self.IDNum = ID
        self.FromNode = FromNode
        self.ToNode = ToNode


graph = Graph('Lunar')
