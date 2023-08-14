

import tkinter as tk
import customtkinter as ctk
import os
import openai
from PIL import Image, ImageTk
import requests, io

def generate():
    print("Hi levantrungits@outlook.com")
    
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    # user_prompt = "cat wearing red cape"
    user_prompt = prompt_entry.get("0.0", tk.END)
    user_prompt += "in style: " + style_dropdown.get()
    
    response = openai.Image.create(
        prompt = user_prompt,
        n = int(number_slider.get()),
        size = "512x512"
    )
    
    image_urls = []
    for i in range(len(response['data'])):
        image_urls.append(response['data'][i]['url'])
    
    images = []
    for url in image_urls:
        response = requests.get(url)
        image = Image.open(io.BytesIO(response.content))
        photo_image = ImageTk.PhotoImage(image)
        images.append(photo_image)
        
    def update_image(index=0):
        canvas.image = images[index]
        canvas.create_image(0, 0, anchor="nw", image=images[index])
        index = (index + 1) % len(images)
        canvas.after(3000, update_image, index)
    
    update_image()
    
    '''
        # 0. get URL of the image from OpenAI API   
        image_url = response['data'][0]['url']
        print(image_url)
        # 1. get URL of the image
        response = requests.get(image_url)
        # 2. create an Image object
        image = Image.open(io.BytesIO(response.content))
        # 3. create an ImageTk object
        image = ImageTk.PhotoImage(image)
        # 4. place it on the canvas
        canvas.image = image
        canvas.create_image(0, 0, anchor="nw", image=image)
    '''

root = ctk.CTk()
root.title("AI Image Generator")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue") 

input_frame = ctk.CTkFrame(root)
input_frame.pack(side="left", expand=True, padx=20, pady=20)

prompt_label = ctk.CTkLabel(input_frame, text="Prompt")
prompt_label.grid(row=0, column=0, padx=10, pady=10)
prompt_entry = ctk.CTkTextbox(input_frame, height=10)
prompt_entry.grid(row=0, column=1, padx=10, pady=10)

style_label = ctk.CTkLabel(input_frame, text="Style")
style_label.grid(row=1, column=0, padx=10, pady=10)
style_dropdown = ctk.CTkComboBox(input_frame, values=["Realistic", "Cartoon", "3D Illustration", "Flat Art"])
style_dropdown.grid(row=1, column=1, padx=10, pady=10)

number_label = ctk.CTkLabel(input_frame, text="# Images")
number_label.grid(row=2, column=0, padx=10, pady=10)
number_slider = ctk.CTkSlider(input_frame, from_=1, to=10, number_of_steps=9)
number_slider.grid(row=2, column=1)

generate_button = ctk.CTkButton(input_frame, text="Generate", command=generate)
generate_button.grid(row=3, column=0, padx=10, pady=10, sticky="news", columnspan=2)

canvas = tk.Canvas(root, width=512, height=512)
canvas.pack(side="left")

root.mainloop()