import util


class Node:
    def __init__(self, state, parent=None, action=None, heuristic_value=0):
        self.state = state
        self.parent = parent
        self.action = action
        if parent:
            self.heuristic_value = parent.heuristic_value + heuristic_value
        else:
            self.heuristic_value = heuristic_value

    def extend(self, problem):
        """Return the successors nodes connected with the current node"""
        return [Node(succ, self, act, stepCost) for succ, act, stepCost in problem.getSuccessors(self.state)]

    def path(self):
        """Return a list of node from the current node to the root"""
        node = self
        list_n = util.Queue()
        list_n.push(node)
        while node.parent:
            list_n.push(node.parent)
            node = node.parent
        print(list_n.list[0].action)
        return list_n.list

    def inList(node, queue):
        """Check if the node is in the list queue"""
        for n in queue:
            if node.state == n.state:
                return True
        return False
