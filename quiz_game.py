print("================================")
print("       🧠 PYTHON QUIZ GAME")
print("================================")

score = 0

# Question 1
print("\n1. Which language is mainly used for Data Science?")
print("A. C++")
print("B. Python")
print("C. HTML")
print("D. CSS")

answer = input("Enter your answer: ")

if answer.lower() == "b":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! Correct answer is B.")

# Question 2
print("\n2. What does CPU stand for?")
print("A. Central Processing Unit")
print("B. Computer Processing Unit")
print("C. Central Program Unit")
print("D. Control Processing Unit")

answer = input("Enter your answer: ")

if answer.lower() == "a":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! Correct answer is A.")

# Question 3
print("\n3. Which one is a Python library?")
print("A. Windows")
print("B. Linux")
print("C. Pandas")
print("D. Chrome")

answer = input("Enter your answer: ")

if answer.lower() == "c":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! Correct answer is C.")

# Question 4
print("\n4. What is the output of 2 + 3 * 2?")
print("A. 10")
print("B. 12")
print("C. 8")
print("D. 7")

answer = input("Enter your answer: ")

if answer.lower() == "c":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! Correct answer is C.")

# Question 5
print("\n5. Which symbol is used for a comment in Python?")
print("A. //")
print("B. <!-- -->")
print("C. #")
print("D. **")

answer = input("Enter your answer: ")

if answer.lower() == "c":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! Correct answer is C.")

# Final Result
print("\n================================")
print("           RESULT")
print("================================")

print("Score:", score, "/ 5")

percentage = (score / 5) * 100
print("Percentage:", percentage, "%")

if score == 5:
    print("🔥 Perfect Score!")
elif score >= 3:
    print("👍 Good Job!")
else:
    print("📚 Keep Practicing!")