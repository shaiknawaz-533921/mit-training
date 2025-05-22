# -----------------------------
# Base AI Agent and Extensions
# -----------------------------

from abc import ABC, abstractmethod
from dataclasses import dataclass, field

class BaseAgent:
    """
    Abstract base class for all agents in the system.

    Implements common functionality and defines the required interface
    for concrete agent implementations.
    """

    def __init__(self, name: str, description: str, action: callable):
        """
        Initialize the BaseAgent.

        :param name: Name of the agent.
        :param description: Short description of what the agent does.
        :param action: A callable (function) that the agent will perform.
        """
        self.name = name
        self.description = description
        self.action = action

    def process_request(self, *args, **kwargs):
        print(f"[{self.name}]: Processing request...")
        return self.action(*args, **kwargs)

    