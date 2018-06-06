ctrl_bool = kwargs["ctrlclick"]

nodes = list(hou.selectedNodes())

for node in nodes:
    posx = node.position()[0]
    posy = node.position()[1]
    
    if not ctrl_bool:
        node_name = node.name()
        
    else:
        node_name = node.parent().name()
              
    null_node = node.createOutputNode('null')
    null_node.setName('Out_' + node_name)
    null_node.setPosition([posx, posy - 1])
    null_node.setColor(hou.Color((0.1, 0.1, 0.1)))
    null_node.setDisplayFlag(1)
    null_node.setRenderFlag(1)
