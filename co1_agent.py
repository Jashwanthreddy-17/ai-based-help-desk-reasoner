"""
========================================================
CO1: AGENT MODEL, KNOWLEDGE REPRESENTATION & STATE SPACE
Project: Automated Help Desk Reasoner
========================================================
"""

# ======================================================
# CO1: Python Essentials
# ======================================================

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set
import heapq
import logging

# ======================================================
# CO1: Trace Logging
# ======================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

logger = logging.getLogger("HelpDeskAgent")

# ======================================================
# CO1: PEAS Model
# ======================================================

@dataclass
class PEAS:

    performance_measure: List[str]

    environment: List[str]

    actuators: List[str]

    sensors: List[str]


HELPDESK_PEAS = PEAS(

    performance_measure=[
        "Fast Resolution",
        "Accurate Diagnosis",
        "Low Escalation Rate"
    ],

    environment=[
        "Corporate Network",
        "User Devices",
        "Knowledge Base"
    ],

    actuators=[
        "Display Solution",
        "Create Ticket",
        "Escalate Ticket"
    ],

    sensors=[
        "User Query",
        "System Logs",
        "Issue History"
    ]
)

# ======================================================
# CO1: Environment Types
# ======================================================

ENVIRONMENT_TYPES = {

    "observable": "Partially Observable",

    "deterministic": "Semi Deterministic",

    "episodic": "Sequential",

    "static_dynamic": "Dynamic",

    "single_multi_agent": "Multi Agent"
}

# ======================================================
# CO1: Problem Formulation
# ======================================================

@dataclass
class State:

    issue: str

    internet: bool = False

    password_changed: bool = False

    software_installed: bool = True

    printer_online: bool = True


@dataclass
class Action:

    name: str


@dataclass
class Transition:

    current_state: State

    action: Action

    next_state: State


@dataclass
class CostFunction:

    action_costs: Dict[str, int]

    def get_cost(self, action_name: str):

        return self.action_costs.get(action_name, 100)


COST_MODEL = CostFunction(

    action_costs={

        "ASK_QUESTION": 1,

        "SEARCH_KB": 2,

        "RETURN_SOLUTION": 1,

        "CREATE_TICKET": 5,

        "ESCALATE": 10
    }
)

# ======================================================
# CO1: Knowledge Representation
# ======================================================

class KnowledgeBase:

    def __init__(self):

        self.rules = {}

        self.facts = set()

    def add_rule(self, condition, conclusion):

        self.rules[condition] = conclusion

    def add_fact(self, fact):

        self.facts.add(fact)

    def infer(self):

        results = []

        for condition, conclusion in self.rules.items():

            if condition in self.facts:

                results.append(conclusion)

        return results


# ======================================================
# CO1: Rule Set
# ======================================================

kb = KnowledgeBase()

kb.add_rule(
    "VPN_FAILURE_AND_PASSWORD_CHANGED",
    "RESET_VPN_CREDENTIALS"
)

kb.add_rule(
    "PRINTER_OFFLINE",
    "RESTART_PRINTER"
)

kb.add_rule(
    "OUTLOOK_CRASH",
    "REPAIR_PROFILE"
)

kb.add_rule(
    "DISK_FULL",
    "CLEAN_DISK"
)

kb.add_rule(
    "ACCOUNT_LOCKED",
    "UNLOCK_ACCOUNT"
)

# ======================================================
# CO1: Graph Representation
# ======================================================

ISSUE_GRAPH = {

    "VPN": [
        "Internet",
        "Credentials",
        "Firewall"
    ],

    "Printer": [
        "Network",
        "Driver",
        "Power"
    ],

    "Outlook": [
        "Profile",
        "Storage",
        "Server"
    ],

    "Login": [
        "Password",
        "Account Status"
    ]
}

# ======================================================
# CO1: Tree Representation
# ======================================================

HELPDESK_TREE = {

    "Root": {

        "Network": {

            "VPN": {},

            "WiFi": {}
        },

        "Software": {

            "Outlook": {},

            "Teams": {}
        },

        "Hardware": {

            "Printer": {},

            "Keyboard": {}
        }
    }
}

# ======================================================
# CO1: Constraint Representation
# ======================================================

CONSTRAINTS = {

    "VPN": [
        "internet=True"
    ],

    "Printer": [
        "printer_online=True"
    ]
}

# ======================================================
# CO1: Dataclass for Ticket
# ======================================================

@dataclass
class Ticket:

    title: str

    description: str

    priority: str = "Medium"

# ======================================================
# CO1: Core Data Structures
# Dict
# Set
# List
# Heap
# ======================================================

class PriorityIssueQueue:

    def __init__(self):

        self.heap = []

    def push(self, priority, issue):

        heapq.heappush(
            self.heap,
            (priority, issue)
        )

    def pop(self):

        if self.heap:

            return heapq.heappop(self.heap)

        return None

# ======================================================
# CO1: Recursion
# Tree Traversal
# ======================================================

def print_tree(tree, level=0):

    for key, value in tree.items():

        print("   " * level + key)

        if isinstance(value, dict):

            print_tree(value, level + 1)

# ======================================================
# CO1: Complexity Aware Coding
# ======================================================

class ComplexityTracker:

    def __init__(self):

        self.operations = 0

    def increment(self):

        self.operations += 1

    def report(self):

        return self.operations

# ======================================================
# CO1: Agent
# ======================================================

class HelpDeskAgent:

    def __init__(self):

        self.trace = []

    def log_step(self, message):

        self.trace.append(message)

        logger.info(message)

    def diagnose(self, issue, context):

        self.trace.clear()

        self.log_step(
            f"Issue Received: {issue}"
        )

        issue_upper = issue.upper()

        if issue_upper == "VPN":

            self.log_step(
                "Checking Internet"
            )

            if context.get("internet"):

                self.log_step(
                    "Internet Available"
                )

                if context.get("password_changed"):

                    kb.add_fact(
                        "VPN_FAILURE_AND_PASSWORD_CHANGED"
                    )

                    result = kb.infer()

                    self.log_step(
                        "Root Cause Found"
                    )

                    return result

        elif issue_upper == "PRINTER":

            kb.add_fact(
                "PRINTER_OFFLINE"
            )

            return kb.infer()

        elif issue_upper == "OUTLOOK":

            kb.add_fact(
                "OUTLOOK_CRASH"
            )

            return kb.infer()

        return ["CREATE_TICKET"]

    def get_trace(self):

        return self.trace

# ======================================================
# CO1: Unit Testing
# ======================================================

def test_vpn_reasoning():

    agent = HelpDeskAgent()

    result = agent.diagnose(

        issue="VPN",

        context={

            "internet": True,

            "password_changed": True
        }
    )

    assert "RESET_VPN_CREDENTIALS" in result


def test_printer_reasoning():

    agent = HelpDeskAgent()

    result = agent.diagnose(

        issue="Printer",

        context={}
    )

    assert "RESTART_PRINTER" in result


# ======================================================
# CO1: Demo
# ======================================================

if __name__ == "__main__":

    print("\n===== PEAS =====")

    print(HELPDESK_PEAS)

    print("\n===== TREE =====")

    print_tree(HELPDESK_TREE)

    print("\n===== AGENT =====")

    agent = HelpDeskAgent()

    result = agent.diagnose(

        issue="VPN",

        context={

            "internet": True,

            "password_changed": True
        }
    )

    print("\nSolution:")

    print(result)

    print("\nTrace:")

    for step in agent.get_trace():

        print(step)