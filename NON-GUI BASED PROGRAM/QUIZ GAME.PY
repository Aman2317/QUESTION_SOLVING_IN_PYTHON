# Creating a quiz game

print("Welcome To My Anime Quiz!")

playing = input("Do you want to play the game? (y/n): ")

# If user type anything other than "y" then it will quit.
if playing != "y":
    quit()

print("Okay! Let's Play :)")

# Dictionary to store questions and correct answers
quiz_data = {
    "In \"Attack on Titan\", what are the humanoid giants called?": ("b", "Titans"),
    "Which anime series features a character named Monkey D. Luffy, who aims to become the King of the Pirates?": ("c", "One Piece"),
    "What is the name of the powerful energy used by characters in the \"Dragon Ball\" series?": ("b", "Ki"),
    "In \"My Hero Academia\", what is the name of the school where aspiring heroes are trained?": ("c", "UA High School"),
    "Which anime features a protagonist named Naruto Uzumaki, who dreams of becoming the Hokage?": ("b", "Naruto")
}


# Multiple choice options
options = [
    ["a) Hollow", "b) Titans", "c) Shinigami", "d) Youkai"],
    ["a) Naruto", "b) Bleach", "c) One Piece", "d) Dragon Ball Z"],
    ["a) Chakra", "b) Ki", "c) Nen", "d) Stand"],
    ["a) Konoha High", "b) Soul Society Academy", "c) UA High School", "d) True Cross Academy"],
    ["a) Death Note", "b) Naruto", "c) Fullmetal Alchemist", "d) Cowboy Bebop"]
]



