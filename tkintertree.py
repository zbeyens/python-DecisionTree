from tkinter import *
gw = 1000
gh = 800


def findwidth(root,prof,depth):
	values = [1]
	if(isinstance(root,dict)):
		for a in root:
			values.append(findwidth(root[a]))
		values.append(len(root))
	return max(values)
	
def finddepth(root,prof,depth=0):
	values = [0]
	if(len(prof)<=depth):
		prof.append(0)
	prof[depth]+=1
	if(isinstance(root,dict)):
		for a in root:
			values.append(finddepth(root[a],prof,depth+1))
			
	return max(values)+1
	

def drawnode(root,arrangement,value,prof,depth=0):
	x0 = 50
	ww = 900
	y0 = 20
	hh = 750
	w=prof[depth]
	xp =  x0+ ww/prof[depth-1]*(arrangement[depth-1]-1)
	yp =  y0+ hh/h*(depth-1)
	x = x0+ ww/w*arrangement[depth]
	arrangement[depth]+=1
	y = y0+ hh/h*depth
	
	canvas.create_line(xp,yp,x,y)
	canvas.create_text((x,y),text=str(value),anchor=CENTER)
	
	if(isinstance(root,dict)):
		for a in root:
			drawnode(root[a],arrangement,a,prof,depth+1)
	

def drawtree(root):
	#global w
	global h
	prof = []
	#w=findwidth(root)
	h=finddepth(root,prof)
	w=max(prof)
	arrangements = [0]*h
	print("Width",w,"; Height",h)
	
	for i in root:
		drawnode(root,arrangements,i,prof)
	
	

def start(root):
	global canvas
	master = Tk()

	canvas = Canvas(master, width=gw, height=gh)
	canvas.pack()

	"""
	w.create_line(0, 0, 200, 100)
	w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

	w.create_rectangle(50, 25, 150, 75, fill="blue")
	"""
	drawtree(root)
	mainloop()
