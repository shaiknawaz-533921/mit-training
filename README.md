🤖 AI Agent Framework (Python)

This project implements a basic AI Agent framework in Python. It introduces a flexible and extensible base class called BaseAgent and two derived agent classes:
	•	GreetAgent: Greets a person with a good morning message.
	•	BirthdayAgent: Wishes someone a happy birthday.

The framework allows easy addition of new agents by simply defining new actions and agent classes.

ai-agent-framework/
├── agents.py            # Contains GreetAgent and BirthdayAgent classes
├── base_agent.py        # BaseAgent class definition
├── main.py              # Entry point to test agents
└── README.md            # Project overview and usage

🚀 Features
	•	🧱 Modular and extensible base class (BaseAgent)
	•	🤝 Custom actions passed dynamically to agents
	•	🎉 Example agents to greet and wish birthdays
	•	📦 Easy to plug and play in larger AI workflows

▶️ How to Run

1.	Clone the repository

```
    git clone https://github.com/shaiknawazz1/mit-training.git
    cd mit-training
```
2.	Run the agents
```
    python main.py
```
Example Output

[GreetAgent]: Processing request...
Good morning, Alice!
[BirthdayAgent]: Processing request...
Happy Birthday, Bob! 🎉

To add a new agent:
	1.	Define a new action function.
	2.	Create a new class inheriting from BaseAgent and pass the action.

Example:
```
    def thank_action(name: str) -> str:
        return f"Thank you, {name}!"

    class ThankAgent(BaseAgent):
        def __init__(self):
            super().__init__("ThankAgent", "Sends a thank-you message.", thank_action)
```

📄 License

This project is open source and available under the MIT License.
