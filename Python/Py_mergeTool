plane = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
currentGeo = plane.pwd()
pos = plane.selectPosition()
merge_node = currentGeo.createNode('merge')
merge_node.setPosition(pos)
nodes = list(hou.selectedNodes())

for node in nodes:
    merge_node.setNextInput(node)
