# -*- coding: utf-8 -*-

import lxml.etree as et

md = et.parse("/home/alexandr/Документы/planningandsheduling/diagramms/initial_model/domain_object_model.uxf")

out_f = open("/home/alexandr/Документы/planningandsheduling/diagramms/initial_model/parsing_res.txt", "w", encoding="utf-8")

for x in md.iter("element"):
    ids = x.find("id")
    if ids is not None and ids.text == "UMLClass":
        pnl_attr = x.find("panel_attributes")
        if pnl_attr is not None:
            s = pnl_attr.text
            ind = s.find("--")
            if ind <= 0:
                out_f.write(".. py:class:: " + pnl_attr.text.rstrip() + '\n')
                out_f.write('\n')
            else:
                out_f.write(".. py:class:: " + pnl_attr.text[:ind].rstrip() + '\n')
                out_f.write('\n')
                d = pnl_attr.text[ind:].splitlines()
                for s in d:
                    if s != '--':
                        out_f.write('   .. py:attribute:: ' + s + '\n')
                        out_f.write('\n')
                
            
out_f.close()
print("все OK")            
