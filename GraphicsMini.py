from tkinter import *
import time
class collision:
	def __init__(self,master):
		height=master.winfo_screenheight()
		width=master.winfo_screenwidth()
		self.canvas=Canvas(master,bg="#FFFFFF", height=height-200, width=width)
		print(height,width)
		self.canvas.pack()
		self.canvas.create_text(1000,100,text="1D Collision",font=("Purisa", 100))
		self.canvas.create_text(1000,300,text="Graphics Mini Project",font=("Purisa", 100))

		# Draw Frame in the window
		frame = Frame(master)
		frame.pack()

		#Object 1
		Label(frame,text="Object 1:").grid(row=1,column=1)

		Label(frame,text="Mass of Object1 (m1):").grid(row=2,column=1)
		self.Mass1_value=StringVar()
		Entry(frame, textvariable=self.Mass1_value).grid(row=2, column=2)

		Label(frame,text="Initial Velocity of Object1 (u1):").grid(row=3,column=1)
		self.Velocity1_value=StringVar()
		Entry(frame, textvariable=self.Velocity1_value).grid(row=3, column=2)

				#Object 2
		Label(frame,text="Object 2:").grid(row=1,column=4)

		Label(frame,text="Mass of Object2 (m2):").grid(row=2,column=4)
		self.Mass2_value=StringVar()
		Entry(frame, textvariable=self.Mass2_value).grid(row=2, column=5)

		Label(frame,text="Initial Velocity of Object2 (u2):").grid(row=3,column=4)
		self.Velocity2_value=StringVar()
		Entry(frame, textvariable=self.Velocity2_value).grid(row=3, column=5)

		#Buttons
		Btn_Submit=Button(frame, text="Apply", command=lambda:self.createobjects(master)).grid(row=2, column=10)
		Btn_clear=Button(frame, text="Clear", command=lambda:self.clear_screen()).grid(row=2, column=11)

	def clear_screen(self):
		self.canvas.delete("object1")
		self.canvas.delete("object2")
		self.canvas.delete("text")

	def createobjects(self,master):

		#masses
		m1=int(self.Mass1_value.get())
		m2=int(self.Mass2_value.get())

		#initial velocity
		u1=float(self.Velocity1_value.get())
		u2=float(self.Velocity2_value.get())

		#calculating the final velocity
		if (m1!=0 and m2!=0):
			v1=(u1*(m1-m2)+(2*m2*-u2))/(m1+m2)
			v2=(-u2*(m2-m1)+(2*m1*u1))/(m1+m2)
			#displaying velocity
			self.canvas.create_text(1900,100, text="final velocity of object 1 (v1)=",font=("Purisa",20), tag="text")
			self.canvas.create_text(2220,100, text=v1,font=("Purisa",20),tag="text")

			self.canvas.create_text(1900,200, text="final velocity of object 2 (v2)=",font=("Purisa",20),tag="text")
			self.canvas.create_text(2220,200, text=v2,font=("Purisa",20),tag="text")


			print (v1,v2)
			print (m1,m2)
			self.canvas.create_rectangle(0,1000,2560,1400, width=20,fill="black")
			#first object
			object1=self.canvas.create_oval(300,990-(m1*5),(m1*5)+300,990, width=2, outline="grey", fill="blue",tag='object1')
			#second object
			object2=self.canvas.create_oval(2250-(m2*5),990-(m2*5),2250,990, width=2, outline="grey", fill="red", tag='object2')
			while True:
				self.canvas.move(object1,u1,0)
				self.canvas.move(object2,-u2,0)
				object1_pos=self.canvas.coords(object1)
				object2_pos=self.canvas.coords(object2)

				#position is left top right bottom
				#print(object1_pos[2],object2_pos[0])
				if object1_pos[2]>object2_pos[0]:
					u1=v1
					u2=-v2				
				master.update()
				time.sleep(0.03)
window=Tk()
obj= collision(window)
window.mainloop()