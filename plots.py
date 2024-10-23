import matplotlib.pyplot as plt

# Data from the logs
import matplotlib.pyplot as plt

tasks = list(range(1, 21))  # Adjusted to match the length of accuracy lists
top1_accuracy = [100.0, 98.38, 97.97, 96.7, 96.26, 93.6, 91.39, 92.17, 91.92, 91.33, 91.02, 88.98, 88.18, 87.32, 86.3, 86.78, 86.32, 86.33, 86.02, 85.67]
top5_accuracy = [100.0, 100.0, 99.71, 99.78, 99.82, 99.7, 99.36, 99.35, 99.24, 99.16, 99.23, 98.8, 98.82, 98.48, 98.42, 98.41, 98.27, 98.21, 97.88, 97.88]
avg_accuracy = [100.00, 99.19, 98.783, 98.265, 97.862, 97.152, 96.328, 95.808, 95.377, 94.972, 94.612, 94.143, 93.685, 93.23, 92.768, 92.394, 92.036, 91.720, 91.419, 91.132]

# Plotting the Top-1 accuracy, Top-5 accuracy, and Average accuracy
plt.figure(figsize=(10, 6))
plt.plot(tasks, top1_accuracy, label='Top-1 Accuracy', marker='o', color='b')
plt.plot(tasks, top5_accuracy, label='Top-5 Accuracy', marker='s', color='g')
plt.plot(tasks, avg_accuracy, label='Average Accuracy', marker='d', color='r')

# Graph settings
plt.title("CNN Accuracy over Tasks")
plt.xlabel("Tasks")
plt.ylabel("Accuracy (%)")
plt.xticks(tasks)
plt.ylim(70, 105)  # Optional: set y-axis limits for better visualization
plt.legend()
plt.grid(True)
plt.show()
