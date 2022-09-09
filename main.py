from tkinter import *
import requests


def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Kanye Truth Speaker 3000")
window.config(padx=100, pady=100)

canvas = Canvas(width=400, height=514)
background_img = PhotoImage(file="background.png")
canvas.create_image(200, 257, image=background_img)
quote_text = canvas.create_text(200, 257, text="      Kanye West\nTruth Speaker 3000", width=250, font=("Arial", 20), fill="black")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()
