# -*- coding: utf-8 -*-

from anytree import Node, RenderTree, PreOrderIter
from anytree.dotexport import RenderTreeGraph

def parse_csv(file_name):
    input_f = open(file_name, "rt", encoding="cp1251")
    line = input_f.readline()
    try:
        root = Node('root', dep=0)
        lvl1 = {}
        for line in input_f.readlines():
            d = line.rstrip().split(";")
            print(d)
            lvl1 = None
            for pre, _, node in RenderTree(root):
                if node.name == d[1]:
                    lvl1 = node
            if lvl1 is None:
                lvl1 = Node(d[1], parent=root, dep=1)
            lvl2 = None
            for pre, _, node in RenderTree(lvl1):
                if node.name == d[0]:
                    lvl2 = node
            if lvl2 is None:
                lvl2 = Node(d[0], parent=lvl1, lines='', dep=2)
                lvl2.lines = lvl2.lines + '   ' + '"' + d[2] + '",' + '"' + d[3] + '",' + '"' + d[4] + '",' + '"' + d[5] + '"' + '\n'
            else:
                lvl2.lines =  lvl2.lines + '   ' + '"' + d[2] + '",' + '"' + d[3] + '",' + '"' + d[4] + '",' + '"' + d[5] + '"' + '\n'
        return root   
    finally:
        input_f.close()


def save_res(file_name, tree):
    out_put = open(file_name,  "w", encoding="utf-8")
    try:
        for pre, _, node in RenderTree(tree):
            #out_put.write(node.name + '\n')
            if node.dep == 1:
                out_put.write(node.name + '\n')
                out_put.write("=".ljust(len(node.name), "=") + '\n')
                out_put.write('\n')
            elif node.dep == 2:
                out_put.write(node.name + '\n')
                out_put.write("-".ljust(len(node.name), "-") + '\n')
                out_put.write('\n')
                out_put.write(".. csv-table:: \n")
                out_put.write('   :header: "Код","Возможность","Риск", "Версия" \n')
                out_put.write('   :widths: 10 70 10 10 \n \n')
                out_put.write(node.lines)
                out_put.write('\n')
    finally:
        out_put.close()    

p = parse_csv("C:/Users/Public/Documents/p30.csv")
save_res("C:/Users/Public/Documents/p30.txt", p)
print(RenderTree(p))

