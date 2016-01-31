
import numpy as np


def export_obj(vertices, triangles, filename):
    """
    Exports a mesh in the (.obj) format.
    """
    
    with open(filename, 'w') as fh:
        lines = []
        
        for v in vertices:
            lines.append("v {}".format(" ".join([str(p) for p in v])))
            
        for f in triangles:
            lines.append("f {}".format(" ".join([str(p) for p in f])))
        
        fh.write("\n".join(lines))


def export_mesh(vertices, triangles, filename, mesh_name="mcubes_mesh"):
    """
    Exports a mesh in the COLLADA (.dae) format.
    
    Needs PyCollada (https://github.com/pycollada/pycollada).
    """
    
    import collada
    
    mesh = collada.Collada()
    
    vert_src = collada.source.FloatSource("verts-array", vertices, ('X','Y','Z'))
    geom = collada.geometry.Geometry(mesh, "geometry0", mesh_name, [vert_src])
    
    input_list = collada.source.InputList()
    input_list.addInput(0, 'VERTEX', "#verts-array")
    
    triset = geom.createTriangleSet(np.copy(triangles), input_list, "")
    geom.primitives.append(triset)
    mesh.geometries.append(geom)
    
    geomnode = collada.scene.GeometryNode(geom, [])
    node = collada.scene.Node(mesh_name, children=[geomnode])
    
    myscene = collada.scene.Scene("mcubes_scene", [node])
    mesh.scenes.append(myscene)
    mesh.scene = myscene
    
    mesh.write(filename)
