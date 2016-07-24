class System:
    def __init__(self, sys_type, location):
        self.Type = sys_type
        self.Location = location
        self.NodeList = []
        self.EdgeList = []

    def FindEdges(self, sys, sys_map):
        """ Find edges that the given system, sys, traverses.

        :param sys: input the system ID number
        :type sys: int
        :param sys_map: system map in a dictionary
        :type sys_map: dict
        :return: list of edge indices that the given system traverses
        :rtype: list
        .. todo:: ensure that sys ID numbers are correct when implemented

        """
        return sys_map[sys]

    # def FindSystems(self, ix, M):
    #     sysarray = []
    #     for j in range(M):
    #         if M(ix, j) == -1:
    #             sysarray.append(find(M(:, j) == 1))
    #             return sysarray

    def FindStack(self, edge, sys_map):
        """ Find all of the vehicles that traverse a given edge.

        :param edge: edge ID number
        :type edge: int
        :param sys_map: system map in a dictionary
        :type sys_map: dict
        :return: list of system indices that also traverse the given edge
        :rtype: list

        """

        sysarray = []
        for sys in sys_map:
            if edge in sys_map[sys]:
                sysarray.append(sys)
        return sysarray


if __name__ == '__main__':
    test_sys = System('type', 'name')
    system_map = {1: [1, 2, 3, 4], 2: [2, 3, 5, 6], 3: [5, 6, 7, 8, 9], 4: [1, 3, 6]}
    print(system_map)
    a = test_sys.FindStack(3, system_map)
    b = test_sys.FindEdges(2, system_map)
    print(a)
    print(b)
