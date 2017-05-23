from tkinter import *
gw = 8000 #taille réelle du graphe (on scrolle dedans)
gh = 5000


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
	
def drawnode(arrangement,value,prof,c,depth):
	x0 = 50
	ww = gw-2*x0
	y0 = 20
	hh = gh-2*y0
	w=prof[depth]
	xp =  x0+ ww/prof[depth-1]*(arrangement[depth-1]-1)
	yp =  y0+ hh/h*(depth-1)
	x = x0+ ww/w*arrangement[depth]
	arrangement[depth]+=1
	y = y0+ hh/h*depth
	if(depth!=0):
		border = len(str(value))*7
		canvas.create_text((x,y),text=str(value),anchor=CENTER,fill=c)
		canvas.tag_lower(canvas.create_oval(x-border,y-10,x+border,y+10,fill="WHITE",outline="WHITE"))
		canvas.tag_lower(canvas.create_line(xp,yp,x,y,fill="GREY"))
def drawtree(root,arrangement,value,prof,depth=0):
	if(isinstance(root,dict)):
		c = "black"
	else:
		print(root)
		c = ["red","green"][root]
	drawnode(arrangement,value,prof,c,depth)
	if(isinstance(root,dict)):
		for a in root:
			drawtree(root[a],arrangement,a,prof,depth+1)

		

def drawtree_start(root):
	#global w
	global h
	prof = []
	#w=findwidth(root)
	h=finddepth(root,prof)
	w=max(prof)
	arrangements = [0.5]*h
	print("Width",w,"; Height",h)
	
	for i in root:
		drawtree(root,arrangements,i,prof)
	
	

def start(root):
	global canvas
	master = Tk()


	canvas = Canvas(master, width=1000, height=800,scrollregion=(0,0,gw,gh))
	frame = master
	hbar=Scrollbar(frame,orient=HORIZONTAL)
	hbar.pack(side=BOTTOM,fill=X)
	hbar.config(command=canvas.xview)
	vbar=Scrollbar(frame,orient=VERTICAL)
	vbar.pack(side=RIGHT,fill=Y)
	vbar.config(command=canvas.yview)
	canvas.config(width=1000,height=800)
	canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
	canvas.pack(side=LEFT,expand=True,fill=BOTH)

	"""
	w.create_line(0, 0, 200, 100)
	w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

	w.create_rectangle(50, 25, 150, 75, fill="blue")
	"""
	drawtree_start(root)
	mainloop()
	
if __name__=="__main__":
	import _Output_.graphtree_undersampled_generated as undersampled
	start(undersampled.tree)
	
	import _Output_.graphtree_discretised_generated as discretised
	start(discretised.tree)
	
	
