import ifcpatch
import ifcopenshell

path1 = "C:\\Users\\Wik\\Pictures\\testoweifc\\KPR-23-V-001.ifc"
path2 = "C:\\Users\\Wik\Pictures\\testoweifc\\KPR-23-V-002.ifc"

model = ifcopenshell.open(path2)
print(model.schema)



output = ifcpatch.execute({
    "input": "input.ifc",
    "file": model,
    "recipe": "MergeProject",
    "arguments": [path2]})