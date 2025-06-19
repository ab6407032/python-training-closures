"""
Use Case: ✅ Callback Functions with Closures
--------------------------------------------
In GUI or asynchronous programming, you often pass callbacks as handlers.
Closures help keep context like user ID, settings, or flags for these callbacks.

🧠 Real-life Analogy:
When setting a timer, you preset the time and action. 
Later, when the alarm rings, it remembers what you told it to do.

"""

def make_button_click_handler(username):
    def on_click():
        print(f"Welcome back, {username}!")
    return on_click

# Simulating GUI framework behavior
login_button_handler = make_button_click_handler("Alice")
login_button_handler()  # ➜ Welcome back, Alice!
