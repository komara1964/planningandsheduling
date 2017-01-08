# -*- coding: utf-8 -*-

import lxml.etree as et

#md = et.parse(r"/home/alexandr/Документы/planningandsheduling/diagramms/initial_model/domain_object_model.uxf")
md = et.parse(r"E:\plan_shedule\planningandsheduling\diagramms\initial_model\domain_object_model.uxf")
#out_f = open(r"/home/alexandr/Документы/planningandsheduling/diagramms/initial_model/parsing_res.txt", "w", encoding="utf-8")
out_f = open(r"E:\plan_shedule\planningandsheduling\diagramms\initial_model\parsing_res.txt", "w", encoding="utf-8")
for x in md.iter("element"):
    ids = x.find("id")
    if ids is not None and ids.text == "UMLClass":
        pnl_attr = x.find("panel_attributes")
        if pnl_attr is not None:
            d = pnl_attr.text.splitlines()
            print(d)
            out_f.write(".. py:class:: " + d[0] + '\n')
            out_f.write('\n')
            for s in d[1:]:
                if s != '--':
                    if s.find("(") < 0:
                        out_f.write('   .. py:attribute:: ' + s + '\n')
                        out_f.write('\n')
                    else:
                        out_f.write('   .. py:method:: ' + s + '\n')
                        out_f.write('\n')
                          
out_f.close()
print("все OK")            
