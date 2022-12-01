import util


class Node:
    def __init__(self, state, parent=None, action=None, heuristic_value=0):
        "Create a search tree Node, derived from a parent by an action."
        self.state = state
        self.parent = parent
        self.action = action
        if parent:
            self.heuristic_value = parent.heuristic_value + heuristic_value
        else:
            self.heuristic_value = heuristic_value

    def extend(self, problem):
        return [Node(succ, self, act, stepCost) for succ, act, stepCost in problem.getSuccessors(self.state)]

    def path(self):
        node = self
        list_n = util.Queue()
        list_n.push(node)
        while node.parent:
            list_n.push(node.parent)
            node = node.parent
        print(list_n.list[0].action)
        return list_n.list

    def inList(self, queue):
        for n in queue:
            if self.state == n.state:
                return True
        return False
