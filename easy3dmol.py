from IPython.display import publish_display_data
from typing import Dict, Optional
import json
import time
import random


def seed():
    return time.strftime("%Y%m%d%H%M%S", time.localtime()) + str(random.randint(10, 99))


# TODO: 测试下作用域
class view():
    def __init__(self, width="600pt", height="400pt", position="relative", divstyle: Optional[Dict] = None,
                 js="https://3dmol.org/build/3Dmol.js"):
        self.id = seed()
        self.style = "".join([i + ":" + divstyle[i] + ";" for i in divstyle]) if divstyle != None else ""
        self.startjs = f'<script src="{js}"></script>\n' \
                       f'<div id="{self.id}" style="width: {width}; height: {height};position: {position};{self.style}"></div>\n' \
                       f'<script>\n$(function() {{\n\tviewer = $3Dmol.createViewer($("#{self.id}"));\n\tviewer.zoomTo();\n'
        self.updatejs = ""
        self.endjs = "\tviewer.render()\n});\n</script>"

    def __getattr__(self, item):
        def makejs(*args):
            cmd = '\tviewer.%s(' % item
            for arg in args:
                cmd += '%s,' % json.dumps(arg)
            cmd = cmd.rstrip(',')
            cmd += ');\n'
            self.updatejs += cmd
            return self.viewer

        return makejs  # return from getattr

    def js(self):
        return self.startjs + self.updatejs + self.endjs

    def show(self):
        publish_display_data({'text/html': self.js()})


if __name__ == "__main__":
    from rdkit import Chem
    from rdkit.Chem import AllChem

    a = view()
    m = Chem.AddHs(Chem.MolFromSmiles("C"))
    AllChem.EmbedMolecule(m)
    m = Chem.MolToMolBlock(m)
    a.addModel(m, 'mol')
    print(a.js())
