# Assignment-1/student_scores_visualization.py
import json
import matplotlib.pyplot as plt

# Student data load karna
with open("data/students.json") as f:
    students = json.load(f)

names = [s["name"] for s in students]
scores = [s["score"] for s in students]

# Average score calculate
avg_score = sum(scores) / len(scores)
print("Average Score:", avg_score)

# Bar chart plot
plt.bar(names, scores, color='skyblue')
plt.xlabel("Students")
plt.ylabel("Scores")
plt.title("Test Scores of Students")
plt.show()
