# Madlibs Generator

# Open the file in Read mode
with open("story.txt", "r") as f:
    story = f.read()

# Loop through the story and find the angled brackets
words = set()
start_of_word = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story[start_of_word : i + 1]
        words.add(word)
        start_of_word = -1

answers = {}

# Loop through the words found in the above loop and ask user to give a value for each

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

# Place those words into the story

for word in words:
    story = story.replace(word, answers[word])

print(story)
