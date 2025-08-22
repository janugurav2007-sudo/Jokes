import tkinter as tk
import random

jokes = [
    "Why did the computer go to the doctor? Because it caught a virus!",
    "I told my laptop it was too hot... now it won't stop chilling!",
    "Why was the math book sad? Because it had too many problems.",
    "Parallel lines have so much in common… it’s a shame they’ll never meet.",
    "Why don’t programmers like nature? Too many bugs!"
]

def show_joke():
    label.config(text=random.choice(jokes))

def draw_gradient(canvas, color1, color2, width, height):
    (r1,g1,b1) = root.winfo_rgb(color1)
    (r2,g2,b2) = root.winfo_rgb(color2)
    r_ratio = float(r2-r1) / height
    g_ratio = float(g2-g1) / height
    b_ratio = float(b2-b1) / height
    for i in range(height):
        nr = int(r1 + (r_ratio * i))
        ng = int(g1 + (g_ratio * i))
        nb = int(b1 + (b_ratio * i))
        color = "#%04x%04x%04x" % (nr,ng,nb)
        canvas.create_line(0,i,width,i,fill=color)

def update_gradient(event):
    canvas.delete("all")  
    draw_gradient(canvas, "#89f7fe", "#66a6ff", event.width, event.height)

root = tk.Tk()
root.title("Random Joke Generator")
root.geometry("400x300")

canvas = tk.Canvas(root, highlightthickness=0)
canvas.pack(fill="both", expand=True)
canvas.bind("<Configure>", update_gradient)  

frame = tk.Frame(canvas, bg="#ffffff", bd=3, relief="ridge")
frame.place(relx=0.5, rely=0.5, anchor="center")

heading = tk.Label(frame, text="Welcome to Joke Generator!", 
                   font=("Comic Sans MS", 16, "bold"), 
                   bg="white", fg="#333")
heading.pack(pady=10)

label = tk.Label(frame, text="Click the button for a joke!", 
                 wraplength=300, 
                 font=("Helvetica", 13), 
                 bg="white", fg="#444",
                 padx=10, pady=10)
label.pack(pady=15)

btn = tk.Button(frame, text="Tell me a Joke", 
                command=show_joke, 
                font=("Arial", 13, "bold"),
                bg="#4CAF50", fg="white",
                activebackground="#45a049",
                activeforeground="white",
                padx=15, pady=6,
                relief="raised", bd=3)
btn.pack(pady=10)

footer = tk.Label(frame, text="Enjoy and Laugh!", 
                  font=("Courier", 9, "italic"), 
                  bg="white", fg="#777")
footer.pack(pady=5)

root.mainloop()