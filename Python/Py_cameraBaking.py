#Rebuild Camera
#1,get selected camera,exit if no camera selected
selected_nodes = hou.selectedNodes()
if selected_nodes is ():
    hou.ui.displayMessage("select a CAMERA please.")
    exit()
    
selected_node = selected_nodes[0]
if selected_node.type().name() != "cam" :
    hou.ui.displayMessage("select a CAMERA please.")
    exit()

#2,create a new camera
#print selected_node.parm("tx").eval()
new_cam=hou.node('/obj').createNode('cam',"Rebuild_Camera")

#create varibles
tx = new_cam.parm('tx')
ty = new_cam.parm('ty')
tz = new_cam.parm('tz')
rx = new_cam.parm('rx')
ry = new_cam.parm('ry')
rz = new_cam.parm('rz')

#set translate and rotate
tx.setExpression("origin(\"\",\""+selected_node.path()+"\",TX)")
ty.setExpression("origin(\"\",\""+selected_node.path()+"\",TY)")
tz.setExpression("origin(\"\",\""+selected_node.path()+"\",TZ)")
rx.setExpression("origin(\"\",\""+selected_node.path()+"\",RX)")
ry.setExpression("origin(\"\",\""+selected_node.path()+"\",RY)")
rz.setExpression("origin(\"\",\""+selected_node.path()+"\",RZ)")

#set focal lenght and aperture
new_cam.parm('focal').setExpression("ch(\""+selected_node.path()+"/focal\")")
new_cam.parm('aperture').setExpression("ch(\""+selected_node.path()+"/aperture\")")

#bake keyFrames
tx.keyframesRefit(False, 0, False, False, True, 1, 0.1, True, hou.playbar.timelineRange()[0], hou.playbar.timelineRange()[-1], hou.parmBakeChop.Off)
ty.keyframesRefit(False, 0, False, False, True, 1, 0.1, True, hou.playbar.timelineRange()[0], hou.playbar.timelineRange()[-1], hou.parmBakeChop.Off)
tz.keyframesRefit(False, 0, False, False, True, 1, 0.1, True, hou.playbar.timelineRange()[0], hou.playbar.timelineRange()[-1], hou.parmBakeChop.Off)
rx.keyframesRefit(False, 0, False, False, True, 1, 0.1, True, hou.playbar.timelineRange()[0], hou.playbar.timelineRange()[-1], hou.parmBakeChop.Off)
ry.keyframesRefit(False, 0, False, False, True, 1, 0.1, True, hou.playbar.timelineRange()[0], hou.playbar.timelineRange()[-1], hou.parmBakeChop.Off)
rz.keyframesRefit(False, 0, False, False, True, 1, 0.1, True, hou.playbar.timelineRange()[0], hou.playbar.timelineRange()[-1], hou.parmBakeChop.Off)
