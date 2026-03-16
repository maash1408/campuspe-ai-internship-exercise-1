# Accuracy
# correct_predictions = 850
# total_predictions = 1000
# accuracy = (correct_predictions / total_predictions) * 100
# print(f"Model's Accuracy : {accuracy}% ")


# target_accuracy = 0.90
# current_accuracy = 0.87

# if current_accuracy >= target_accuracy:
#     print("Model meets requirements")
# else:
#     print(f"Need {target_accuracy - current_accuracy:02%} more accuracy")


# Choosing Model based on ths task
task_type = "text_generation"
dataset_size = 50000

if task_type == "classification" and dataset_size < 10000:
    model = "Logistic regression"
    print("Using simple model for small classification task")
elif task_type == "classification" and dataset_size >= 10000:
    model = "Neural network"
    print("Using deep learning for large classification task")
elif task_type == "text_generation":
    model = "GPT-based Transformer"
    print("Using generative model for test generation")
else:
    model = "Custom model"
    print("Building custom architecture")

print(f"Selected Model: {model}")