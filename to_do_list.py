import json

# Global task list acting as our agent's task queue
tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Added: '{task}'")

def list_tasks():
    if not tasks:
        print("\nNo tasks currently in the queue.")
        return
    
    print("\n--- Current Agent Task Queue ---")
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")
    print("--------------------------------")

def remove_task(index):
    # Convert human-readable 1-based index (e.g., 1, 2, 3) to Python's 0-based index
    internal_index = index - 1
    
    if 0 <= internal_index < len(tasks):
        removed = tasks.pop(internal_index)
        print(f"Removed task: '{removed}'")
    else:
        print(f"Error: Task number {index} is invalid.")

def save_tasks_to_json(filename="agent_tasks.json"):
    # Saves the tasks list to a JSON file using indent=4 for clean formatting
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)
    print(f"\nTasks successfully saved to '{filename}' as JSON!")

# ==========================================
# Testing the Agent Task Manager
# ==========================================

# 1. Add tasks
add_task("Collect user query")
add_task("Call LLM")
add_task("Return result")

# 2. View tasks
list_tasks()

# 3. Remove task #2 ("Call LLM")
print("\nRemoving task #2...")
remove_task(2)

# 4. View updated tasks
list_tasks()

# 5. Save remaining tasks to a JSON file
save_tasks_to_json()