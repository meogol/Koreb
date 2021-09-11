import copy


class GiveBranchsBack:
    def __init__(self):
        self.data = list()
        self.buffer = list()

    def give_branchs_back(self, item_gr):
        """
        Recoursive run throught the graph and formation of list that includes branches
        :param item_gr: the graph we're running throught
        :return: give back data list of all branches from the graph
        """
        self.buffer.append(item_gr.request)

        for item in item_gr.next_items:
            self.give_branchs_back(item)

        if len(item_gr.next_items) == 0:
            self.data.append(copy.copy(self.buffer))

        self.buffer.remove(self.buffer[len(self.buffer)-1])

        return self.data




