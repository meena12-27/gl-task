class ConversationMemory:
    def __init__(self):
        self.history = []

    def add_message(self, role, content):
        self.history.append({
            "role": role,
            "content": content
        })

    def get_history(self):
        return "\n".join(
            f'{msg["role"]}: {msg["content"]}'
            for msg in self.history
        )

    def clear(self):
        self.history = []

    def last_user_message(self):
        for msg in reversed(self.history):
            if msg["role"] == "user":
                return msg["content"]
        return None

    def last_assistant_message(self):
        for msg in reversed(self.history):
            if msg["role"] == "assistant":
                return msg["content"]
        return None