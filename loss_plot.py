import matplotlib.pyplot as plt
import numpy as np

# Sample log data (replace this with your actual log data)
log_data = """
2024-10-19 15:01:16,735 [ease.py] => Task 0, Epoch 20/20 => Loss 0.279, Train_accy 91.58
2024-10-19 15:01:16,735 [ease.py] => Task 0, Epoch 20/20 => Loss 0.279, Train_accy 91.58
2024-10-19 15:01:16,735 [ease.py] => Task 0, Epoch 20/20 => Loss 0.278, Train_accy 91.85
2024-10-19 15:01:16,735 [ease.py] => Task 0, Epoch 20/20 => Loss 0.275, Train_accy 91.85
2024-10-19 15:01:16,735 [ease.py] => Task 0, Epoch 20/20 => Loss 0.274, Train_accy 91.93
2024-10-19 15:01:16,735 [ease.py] => Task 0, Epoch 20/20 => Loss 0.273, Train_accy 92.02
2024-10-19 15:46:40,974 [trainer.py] => CNN top1 curve: [91.58, 92.85, 93.27, 93.71, 94.02, 94.33, 94.80, 95.03, 95.23, 95.45, 95.67, 95.78, 95.83]
2024-10-19 15:46:47,530 [trainer.py] => CNN top5 curve: [99.67, 98.92, 97.83, 96.78, 95.46, 94.07, 93.55, 92.46]
"""

# Parse the log data
epochs = []
loss = []
top1_curve = []
top5_curve = []

for line in log_data.strip().split('\n'):
    if 'Epoch' in line:
        epoch_info = line.split('Epoch ')[1].split(' => ')[0].strip().split('/')
        epoch_num = int(epoch_info[0])  # Current epoch number
        epochs.append(epoch_num)

        # Parse loss and accuracy
        loss_value = float(line.split('Loss ')[1].split(',')[0])
        acc_value = float(line.split('Train_accy ')[1])
        loss.append(loss_value)
    elif 'CNN top1 curve:' in line:
        top1_data = line.split(': ')[1].strip('[]').split(',')
        top1_curve = list(map(float, top1_data))
    elif 'CNN top5 curve:' in line:
        top5_data = line.split(': ')[1].strip('[]').split(',')
        top5_curve = list(map(float, top5_data))

# Create a figure and axes for plotting
fig, axs = plt.subplots(3, 1, figsize=(10, 12))

# Plot Loss
axs[0].plot(epochs, loss, marker='o', color='red', label='Loss')
axs[0].set_title('Loss over Epochs')
axs[0].set_xlabel('Epoch')
axs[0].set_ylabel('Loss')
axs[0].grid()
axs[0].legend()

# Plot Top-1 Accuracy
axs[1].plot(top1_curve, marker='o', color='blue', label='Top-1 Accuracy')
axs[1].set_title('Top-1 Accuracy over Tasks')
axs[1].set_xlabel('Task Index')
axs[1].set_ylabel('Top-1 Accuracy (%)')
axs[1].grid()
axs[1].legend()

# Plot Top-5 Accuracy
axs[2].plot(top5_curve, marker='s', color='green', label='Top-5 Accuracy')
axs[2].set_title('Top-5 Accuracy over Tasks')
axs[2].set_xlabel('Task Index')
axs[2].set_ylabel('Top-5 Accuracy (%)')
axs[2].grid()
axs[2].legend()

# Adjust layout
plt.tight_layout()
plt.show()
