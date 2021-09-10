from Koreb.graphCore.graphItem import GraphItem

class GoAroundGraph:
    def __init__(self):
        self.data = list()

    def recoursive_algorithm(self, item_gr, needed_level):
        if needed_level == item_gr.level:
            self.data.append(item_gr.request)

        for item in item_gr.next_items:

            self.recoursive_algorithm(item, needed_level)

        return self.data


        #I don't know, saved this staff in case of need

        # if item.right != None:
        #     self.recoursive_algorithm(item.right)
        # if item.left != None:
        #     self.recoursive_algorithm(item.left)


