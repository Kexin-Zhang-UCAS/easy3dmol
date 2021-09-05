import py3Dmol
from typing import Union, List, Optional

number = Union[int, float, None]
boolean = Union[bool, None]
string = Union[str, None]

function = Optional  # undefined now
GLModel = Optional  #
GLShape=Optional
Gradient = Optional
VolumeData = Optional
ClickSphereStyleSpec = Optional
Object=Optional
Mesh=Optional

_map = {"myand": "and", "myor": "or", "mynot": "not"}


# Enum
class CAP:
    NONE = 0
    FLAT = 1
    ROUND = 2


class SurfaceType:
    VDW = 1
    MS = 2
    SAS = 3
    SES = 4




# Base
class Vector3(dict):
    def __init__(self, x: number, y: number, z: number):
        super().__init__()
        keys = locals().keys() - ['__class__', "self"]
        for key in keys:
            _key = key if key not in _map else _map[key]
            if eval(key) != None:
                self[_key] = eval(key)


class Dimensions(dict):
    def __init__(self, w: number, h: number, d: number):
        super().__init__()
        keys = locals().keys() - ['__class__', "self"]
        for key in keys:
            _key = key if key not in _map else _map[key]
            if eval(key) != None:
                self[_key] = eval(key)


class ColorSpec(str):
    def __init__(self,
                 s="0xAF10AB"):
        super().__init__()
        # TODO:
        pass


class ArrowSpec(dict):
    def __init__(self,
                 start: Vector3,
                 end: Vector3,
                 radius: number=None,
                 color: ColorSpec = None,
                 hidden: boolean = None,
                 radiusRatio: number = None,
                 mid: number = None,
                 midpos: number = None,
                 ):
        super().__init__()
        super().__init__()
        keys = locals().keys() - ['__class__', "self"]
        for key in keys:
            _key = key if key not in _map else _map[key]
            if eval(key) != None:
                self[_key] = eval(key)


class AtomSpec(dict):
    def __init__(self,
                 resn: string=None,
                 x: number=None,
                 y: number=None,
                 z: number=None,
                 color: ColorSpec=None,
                 surfaceColor: ColorSpec=None,
                 elem: string=None,
                 hetflag: boolean=None,
                 chain: string=None,
                 resi: number=None,
                 icode: number=None,
                 rescode: number=None,
                 serial: number=None,
                 atom: string=None,
                 bonds: List[number]=None,
                 ss: string=None,
                 singBonds: boolean=None,
                 bondOrder: List[number]=None,
                 properties: function=None,
                 b: number=None,
                 pdbline: string=None,
                 clickable: boolean=None,
                 callback: function=None,
                 invert: boolean=None):
        super().__init__()
        keys = locals().keys() - ['__class__', "self"]
        for key in keys:
            _key = key if key not in _map else _map[key]
            if eval(key) != None:
                self[_key] = eval(key)


class AtomSelectionSpec(AtomSpec):
    def __init__(self,
                 model: GLModel=None,
                 bonds: number=None,
                 predicate: function=None,
                 invert: boolean=None,
                 byres: boolean=None,
                 expand: number=None,
                 **kwargs):
        super().__init__(**kwargs)
        keys = locals().keys() - ['__class__', "self"]
        for key in keys:
            _key = key if key not in _map else _map[key]
            if eval(key) != None:
                self[_key] = eval(key)


class WithinSelectionSpec(dict):
    def __init__(self,
                 distance: number=None,
                 invert: boolean=None,
                 sel: AtomSelectionSpec=None):
        super().__init__()
        keys = locals().keys() - ['__class__', "self"]
        for key in keys:
            _key = key if key not in _map else _map[key]
            if eval(key) != None:
                self[_key] = eval(key)


class AtomSelectionSpec2(AtomSelectionSpec):
    def __init__(self,
                 within: WithinSelectionSpec=None,
                 myand: List[AtomSelectionSpec]=None,
                 myor: List[AtomSelectionSpec]=None,
                 mynot: AtomSelectionSpec=None,
                 **kwargs):
        super().__init__(**kwargs)
        keys = locals().keys() - ['__class__', "self"]
        for key in keys:
            _key = key if key not in _map else _map[key]
            if eval(key) != None:
                self[_key] = eval(key)


class ColorschemeSpec(dict):
    def __init__(self,
                 ssPyMOL: string=None,
                 ssJmol: string=None,
                 Jmol: string=None,
                 default: string=None,
                 amino: string=None,
                 shapely: string=None,
                 nucleic: string=None,
                 chain: string=None,
                 chainHetatm: string=None,
                 prop: string=None,
                 gradient: Gradient=None,
                 map: Object=None,
                 colorfunc: function=None):
        super().__init__()
        keys = locals().keys() - ['__class__', "self"]
        for key in keys:
            _key = key if key not in _map else _map[key]
            if eval(key) != None:
                self[_key] = eval(key)


class LineStyleSpec(dict):
    def __init__(self,
                 hidden: boolean=None,
                 linewidth: number=None,
                 colorscheme: ColorschemeSpec=None,
                 color: ColorSpec=None,
                 opacity: number=None):
        super().__init__()
        keys = locals().keys() - ['__class__', "self"]
        for key in keys:
            _key = key if key not in _map else _map[key]
            if eval(key) != None:
                self[_key] = eval(key)


class CrossStyleSpec(dict):
    def __init__(self,
                 hidden: boolean=None,
                 linewidth: number=None,
                 radius: number=None,
                 scale: number=None,
                 colorscheme: ColorschemeSpec=None,
                 color: ColorSpec=None,
                 opacity: number=None):
        super().__init__()
        keys = locals().keys() - ['__class__', "self"]
        for key in keys:
            _key = key if key not in _map else _map[key]
            if eval(key) != None:
                self[_key] = eval(key)


class StickStyleSpec(dict):
    def __init__(self,
                 hidden: boolean=None,
                 radius: number=None,
                 singleBonds: boolean=None,
                 colorscheme: ColorschemeSpec=None,
                 color: ColorSpec=None,
                 opacity: number=None):
        super().__init__()
        keys = locals().keys() - ['__class__', "self"]
        for key in keys:
            _key = key if key not in _map else _map[key]
            if eval(key) != None:
                self[_key] = eval(key)


class SphereStyleSpec(dict):
    def __init__(self,
                 hidden: boolean=None,
                 radius: number=None,
                 scale: number=None,
                 colorscheme: ColorschemeSpec=None,
                 color: ColorSpec=None,
                 opacity: number=None
                 ):
        super().__init__()
        keys = locals().keys() - ['__class__', "self"]
        for key in keys:
            _key = key if key not in _map else _map[key]
            if eval(key) != None:
                self[_key] = eval(key)


class CartoonStyleSpec(dict):
    def __init__(self,
                 color: ColorSpec=None,
                 style: string=None,
                 ribbon: boolean=None,
                 arrows: boolean=None,
                 tubes: boolean=None,
                 thickness: number=None,
                 width: number=None,
                 opacity: number=None,
                 In: Optional=None):
        super().__init__()
        keys = locals().keys() - ['__class__', "self"]
        for key in keys:
            _key = key if key not in _map else _map[key]
            if eval(key) != None:
                self[_key] = eval(key)


class AtomStyleSpec(dict):
    def __init__(self,
                 line: LineStyleSpec=None,
                 cross: CrossStyleSpec=None,
                 stick: StickStyleSpec=None,
                 sphere: SphereStyleSpec=None,
                 cartoon: CartoonStyleSpec=None,
                 clicksphere: ClickSphereStyleSpec=None):
        super().__init__()
        keys = locals().keys() - ['__class__', "self"]
        for key in keys:
            _key = key if key not in _map else _map[key]
            if eval(key) != None:
                self[_key] = eval(key)


class BoxSpec(dict):
    def __init__(self,
                 corner: Vector3=None,
                 center: Vector3=None,
                 dimesion: Union[Vector3, Dimensions, List, None]=None):
        super().__init__()
        keys = locals().keys() - ['__class__', "self"]
        for key in keys:
            _key = key if key not in _map else _map[key]
            if eval(key) != None:
                self[_key] = eval(key)


class CurveSpec(dict):
    def __init__(self,
                 points: Vector3=None,
                 smooth: number=None,
                 radius: number=None,
                 frowArrow: boolean=None,
                 toArrow: boolean=None):
        super().__init__()
        keys = locals().keys() - ['__class__', "self"]
        for key in keys:
            _key = key if key not in _map else _map[key]
            if eval(key) != None:
                self[_key] = eval(key)


class CustomShapeSpec(dict):
    def __init__(self,
                 vertexArr: List[Vector3]=None,
                 normalArr: List[Vector3]=None,
                 faceArr: List[number]=None,
                 color: Union[ColorSpec, List[ColorSpec], None]=None):
        super().__init__()
        keys = locals().keys() - ['__class__', "self"]
        for key in keys:
            _key = key if key not in _map else _map[key]
            if eval(key) != None:
                self[_key] = eval(key)


class CylinderSpec(dict):
    def __init__(self,
                 start: Vector3=None,
                 end: Vector3=None,
                 radius: number=None,
                 fromCap: CAP=None,
                 toCap: CAP=None,
                 dashed: boolean=None):
        super().__init__()
        keys = locals().keys() - ['__class__', "self"]
        for key in keys:
            _key = key if key not in _map else _map[key]
            if eval(key) != None:
                self[_key] = eval(key)


class FileFormats(dict):
    def __init__(self, ):
        super().__init__()
        ...


class IsoSurfaceSpec(dict):
    def __init__(self,
                 isoval: number=None,
                 color: ColorSpec=None,
                 opacity: number=None,
                 wireframe: boolean=None,
                 linewidth: number=None,
                 smoothness: number=None,
                 coords: List=None,
                 seldist: number=None,
                 voldata: VolumeData=None,
                 volscheme: Gradient=None,
                 volformat: string=None,
                 clickable: boolean=None,
                 callback: function=None):
        super().__init__()
        keys = locals().keys() - ['__class__', "self"]
        for key in keys:
            _key = key if key not in _map else _map[key]
            if eval(key) != None:
                self[_key] = eval(key)


class LabelSpec(dict):
    def __init__(self,
                 font: string=None,
                 fontsize: number=None,
                 fontColor: ColorSpec=None,
                 fontOpacity: number=None,
                 borderThickness: number=None,
                 borderColor: ColorSpec=None,
                 borderOpacity: number=None,
                 backgroundColor: ColorSpec=None,
                 backgroundOpacity: number=None,
                 position: Vector3=None,
                 screenOffset: Vector3=None,
                 inFront: boolean=None,
                 showBackground: boolean=None,
                 fixed: boolean=None,
                 useScreen: boolean=None,
                 backgroundImage: Object=None,
                 alignment: string=None,
                 frame: number=None,
                 ):
        super().__init__()
        keys = locals().keys() - ['__class__', "self"]
        for key in keys:
            _key = key if key not in _map else _map[key]
            if eval(key) != None:
                self[_key] = eval(key)


class LineSpec(dict):
    def __init__(self,
                 start: Vector3=None,
                 end: Vector3=None
                 ):
        super().__init__()
        keys = locals().keys() - ['__class__', "self"]
        for key in keys:
            _key = key if key not in _map else _map[key]
            if eval(key) != None:
                self[_key] = eval(key)


class ParserOptionsSpec(dict):
    def __init__(self):
        super().__init__()


class ShapeSpec(dict):
    def __init__(self,
                 color: ColorSpec=None,
                 alpha: number=None,
                 wireframe: boolean=None,
                 hidden: boolean=None,
                 linewidth: number=None,
                 clickable: boolean=None,
                 callback: function=None,
                 frame: number=None):
        super().__init__()
        keys = locals().keys() - ['__class__', "self"]
        for key in keys:
            _key = key if key not in _map else _map[key]
            if eval(key) != None:
                self[_key] = eval(key)


class SphereShapeSpec(dict):
    def __init__(self,
                 center: Vector3=None,
                 radius: number=None):
        super().__init__()
        keys = locals().keys() - ['__class__', "self"]
        for key in keys:
            _key = key if key not in _map else _map[key]
            if eval(key) != None:
                self[_key] = eval(key)


class SurfaceStyleSpec(dict):
    def __init__(self,
                 opacity: number=None,
                 colorscheme: ColorschemeSpec=None,
                 color: ColorSpec=None,
                 voldata: VolumeData=None,
                 volscheme: Gradient=None,
                 volformat: string=None,
                 map: Object=None):
        super().__init__()
        keys = locals().keys() - ['__class__', "self"]
        for key in keys:
            _key = key if key not in _map else _map[key]
            if eval(key) != None:
                self[_key] = eval(key)


class UnitCellStyleSpec(dict):
    def __init__(self,
                 box: LineStyleSpec=None,
                 astyle: ArrowSpec=None,
                 bstyle: ArrowSpec=None,
                 cstyle: ArrowSpec=None,
                 alabel: string=None,
                 alabelstyle: LabelSpec=None,
                 blabel: string=None,
                 blabelstyle: LabelSpec=None,
                 clabel: string=None,
                 clabelstyle: string=None):
        super().__init__()
        keys = locals().keys() - ['__class__', "self"]
        for key in keys:
            _key = key if key not in _map else _map[key]
            if eval(key) != None:
                self[_key] = eval(key)


class ViewerGridSpec(dict):
    def __init__(self,
                 rows: number=None,
                 cols: number=None,
                 control_all: boolean=None):
        super().__init__()
        keys = locals().keys() - ['__class__', "self"]
        for key in keys:
            _key = key if key not in _map else _map[key]
            if eval(key) != None:
                self[_key] = eval(key)


class ViewerSpec(dict):
    def __init__(self):
        super().__init__()


class VolumetricRendererSpec(dict):
    def __init__(self):
        super().__init__()
