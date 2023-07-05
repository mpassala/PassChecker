import re #reg expression #maniuplate strings (checks logic)
import tkinter as tk  #GUI
from PIL import Image, ImageTk  #Import an display image


def check_password_strength(password):
  # Check if password is 14 or more characters
  if len(password) >= 14:
    # Check if password includes uppercase, lowercase, symbols, and numbers
    if any(char.isupper() for char in password) and any(char.islower() for char in password) \
            and any(char.isdigit() for char in password) and re.search(r"[ !@#$%^&*()_+\-=[\]{};':\"\\|,.<>/?]", password):
      # Check if password is not a common word or name
      if not common_word(password) and not common_name(password):
        return "SECURE!"  # Strong password
      else:
        return "AVERAGE AT BEST"  # Password is strong but contains a common word or name
    else:
      return "AVERAGE AT BEST"  # Password missing some requirements, but also has some
  else:
    return "C'MON MAN, THAT'S TOO EASY!"  # Password too short or not complex


# How to check dictionary and name file for common phrases
# If it finds one, depending on other compoments of password it will tell you average or weak.
def common_word(password):
  with open("dictionary.txt", "r") as file:
    dictionary_words = [line.strip().lower()
                        for line in file]  #case sensitive and reads every line
  return password.lower() in dictionary_words  #case sensitive precaution


def common_name(password):
  with open("names.txt", "r") as file:
    names = [line.strip().lower()
             for line in file]  #case sensitive and reads every line
  return password.lower() in names  #case sensitive precaution


def get_password_strength():
  password = password_entry.get()
  strength = check_password_strength(password)
  strength_label.config(text="PASSWORD STRENGTH: " +
                        strength)  #label + grab strength

  # Set text color based on password strength
  if strength == "C'MON MAN, THAT'S TOO EASY!":
    strength_label.config(fg="Red")  #label color
    strength_label_suggestion.config(  #Suggestion if pass too weak
      text=
      "DON'T USE COMMON WORDS OR NAMES!\nPASSWORD SHOULD BE 14 OR MORE CHARACTERS LONG INCLUDING: \nUPPERCASE, LOWERCASE, SYMBOLS, AND NUMBERS.",
      fg="Black",  #text color
      bd="1",  #border
      relief="solid"  #border emphasis
    )
  elif strength == "AVERAGE AT BEST":
    strength_label.config(fg="Brown")  #label color
    strength_label_suggestion.config(  #Suggestion if pass too weak
      text=
      "DON'T USE COMMON WORDS OR NAMES!\nPASSWORD SHOULD BE 14 OR MORE CHARACTERS LONG INCLUDING: \nUPPERCASE, LOWERCASE, SYMBOLS, AND NUMBERS.",
      fg="Black",  #text color
      bd="1",  #border
      relief="solid"  #border emphasis
    )

  else:
    strength_label.config(fg="Green")  #label color
    strength_label_suggestion.config(
      text="CONGRATS! YOU CAN FOLLOW DIRECTIONS!",
      fg="Black",
      bd="1",
      relief="solid")
  # Display image based on password strength
  if strength == "SECURE!":
    image_path = "SuperSecure.jpg"  #Secure image grabbed
  elif strength == "AVERAGE AT BEST":
    image_path = "average.jpg"  #average image grabbed
  else:
    image_path = "Terrible.jpg"  #weak image grabbed

  image = Image.open(image_path)  #opens image path
  image = image.resize((300, 300), Image.LANCZOS)  #sizing and format of pic
  photo = ImageTk.PhotoImage(image)  #allows u to display
  image_label.config(image=photo)
  image_label.image = photo  #Prevents bad display


# Create GUI window
window = tk.Tk()  #window
window.title("LEBRON PASSWORD CHECKER")  #title

# Elements
password_label = tk.Label(window, text="ENTER PASSWORD:",
                          fg="Navy")  #label and color
password_entry = tk.Entry(window, show="*",
                          fg="Black")  #hidden text behind star
check_button = tk.Button(window,
                         text="CHECK STRENGTH",
                         fg="Navy",
                         command=get_password_strength)  #button and color
strength_label = tk.Label(window, fg="Blue")  #strength label
strength_label_suggestion = tk.Label(window, fg="Black")  #suggestion label
image_label = tk.Label(window)

# Position GUI with grid layout
#yes i completely got sizing grid template from chatgpt
password_label.grid(row=0, column=0, padx=10, pady=10)
password_entry.grid(row=0, column=1, padx=10, pady=10)
check_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
strength_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
strength_label_suggestion.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
image_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI
window.mainloop()



#Something I could do to improve it would be to do something simiar to that of one i found online. As you type your password in, it tells you how long it would take for a computer to crack your password based on it's strength_label

#https://www.security.org/how-secure-is-my-password/

# TEST WITH THESE PASSWORDS!!

# Weak Password Examples:
# "password" or "123456789" (commonly used and easily guessed)
# "abcde" (simple patterns)
# "johnsmith" (names of people)
# "111111" or "aaaaaa" (repeated characters)

# Average Password Examples:
# "Password123456" (meets length, uppercase, lowercase, and numbers, but lacks symbols)

# Strong Password Examples:
# "P@ssw0rd!!2023" (a combination of uppercase and lowercase letters, symbols, numbers, and meets the length requirement)
# "GuessMy#Passw0rd!" (a mix of uppercase and lowercase letters, symbols, numbers, and meets the length requirement)
