class tree_node():
    def __init__(self,father,child,environment,action,score):
        self.father=father
        self.child=child
        self.environment=environment
        self.action=action
    def add_child(self,child_id):
        self.child.append(child_id)