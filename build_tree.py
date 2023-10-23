import json
from tree_node import tree_node
def build_tree(now_node,tree,message):
    for i in range(len(message)):
        ok=0
        for j in range(len(message[i]['step'])):
            if i==0:
                if j==0:
                    now=tree_node(now_node,[],"null",message[i]["step"][j])
                    tree.append(now)
                    tree[now_node].child.append(len(tree)-1)
                    now_node_id = tree[now_node].child[len(tree[now_node].child) - 1]
                else:
                    now=tree_node(len(tree)-1,[],'null',message[i]['step'][j])
                    tree.append(now)
                    tree[len(tree)-2].child.append(len(tree)-1)
            else:
                if ok==0 and tree[now_node_id].action["action"]==message[i]["step"][j]["action"]:
                    tree[now_node_id].action["score"]=tree[now_node_id].action["score"]+message[i]["step"][j]["score"]
                    #print(tree[now_node_id].child)
                    try:
                        now_node_id=tree[now_node_id].child[len(tree[now_node_id].child)-1]
                    except:
                        ok=1
                elif ok==1:
                    now = tree_node(len(tree) - 1, [], 'null', message[i]['step'][j])
                    tree.append(now)
                    tree[len(tree) - 2].child.append(len(tree)-1)
                else:
                    ok=1
                    now = tree_node(now_node_id, [], 'null', message[i]['step'][j])
                    tree.append(now)
                    tree[now_node_id].child.append(len(tree)-1)
            #print(now_node_id)
    return tree







