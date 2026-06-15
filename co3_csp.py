"""
=========================================================
CO3: CSP MODELING
Backtracking
Forward Checking
MRV
Degree Heuristic
LCV
Min Conflicts
Constraint Explanation
=========================================================
"""

from collections import defaultdict


# =====================================================
# CO3: Agents
# =====================================================

AGENTS = {

    "Agent_A": [
        "Network",
        "VPN",
        "WiFi"
    ],

    "Agent_B": [
        "Software",
        "Outlook",
        "Teams"
    ],

    "Agent_C": [
        "Hardware",
        "Printer",
        "Keyboard"
    ]
}


# =====================================================
# CO3: Tickets
# =====================================================

TICKETS = {

    "Ticket_1": "VPN",

    "Ticket_2": "Outlook",

    "Ticket_3": "Printer"
}


# =====================================================
# CO3: CSP Model
# =====================================================

class TicketAssignmentCSP:

    def __init__(self):

        self.variables = list(TICKETS.keys())

        self.domains = {

            ticket:
                list(AGENTS.keys())

            for ticket in self.variables
        }

        self.constraints = []

        self.failure_reason = ""

    # ==========================================
    # CO3: Constraint Check
    # ==========================================

    def is_valid(self, ticket, agent):

        issue = TICKETS[ticket]

        if issue not in AGENTS[agent]:

            self.failure_reason = (

                f"{agent} cannot solve {issue}"
            )

            return False

        return True

    # ==========================================
    # CO3: Forward Checking
    # ==========================================

    def forward_checking(
            self,
            assignment):

        for ticket in self.variables:

            if ticket not in assignment:

                valid_found = False

                for agent in self.domains[ticket]:

                    if self.is_valid(
                            ticket,
                            agent):

                        valid_found = True

                if not valid_found:

                    return False

        return True

    # ==========================================
    # CO3: MRV
    # ==========================================

    def select_unassigned_variable(
            self,
            assignment):

        unassigned = [

            v for v in self.variables

            if v not in assignment
        ]

        return min(

            unassigned,

            key=lambda var:
            len(self.domains[var])
        )

    # ==========================================
    # CO3: Degree Heuristic
    # ==========================================

    def degree_heuristic(self):

        degrees = {}

        for ticket in self.variables:

            degrees[ticket] = len(
                self.domains[ticket]
            )

        return degrees

    # ==========================================
    # CO3: LCV
    # ==========================================

    def order_domain_values(
            self,
            ticket):

        values = []

        for agent in self.domains[ticket]:

            score = 0

            for other_ticket in self.variables:

                if other_ticket != ticket:

                    if self.is_valid(
                            other_ticket,
                            agent):

                        score += 1

            values.append(
                (score, agent)
            )

        values.sort(reverse=True)

        return [

            agent

            for _, agent in values
        ]

    # ==========================================
    # CO3: Backtracking
    # ==========================================

    def backtracking_search(self):

        return self.backtrack({})

    def backtrack(
            self,
            assignment):

        if len(assignment) == len(
                self.variables):

            return assignment

        ticket = self.select_unassigned_variable(
            assignment
        )

        for agent in self.order_domain_values(
                ticket):

            if self.is_valid(
                    ticket,
                    agent):

                assignment[ticket] = agent

                if self.forward_checking(
                        assignment):

                    result = self.backtrack(
                        assignment
                    )

                    if result:

                        return result

                del assignment[ticket]

        return None

    # ==========================================
    # Explainability
    # ==========================================

    def explain_failure(self):

        return self.failure_reason


# =====================================================
# CO3: Min Conflicts
# =====================================================

def min_conflicts():

    return (
        "Used for large CSPs "
        "with local search."
    )


# =====================================================
# CO3: SAT Intuition
# =====================================================

def sat_intuition():

    return (

        "Ticket assigned to Agent_A "
        "OR Agent_B OR Agent_C"
    )


# =====================================================
# CO3: Scheduling Example
# =====================================================

class TimetableScheduler:

    def __init__(self):

        self.schedule = defaultdict(list)

    def assign(self,
               slot,
               agent):

        self.schedule[slot].append(
            agent
        )

    def display(self):

        return dict(self.schedule)


# =====================================================
# CO3: Unit Tests
# =====================================================

def test_backtracking():

    csp = TicketAssignmentCSP()

    result = csp.backtracking_search()

    assert result is not None


def test_scheduler():

    scheduler = TimetableScheduler()

    scheduler.assign(
        "Morning",
        "Agent_A"
    )

    assert "Morning" in scheduler.schedule


# =====================================================
# Demo
# =====================================================

if __name__ == "__main__":

    print(
        "\n===== CSP Ticket Assignment ====="
    )

    csp = TicketAssignmentCSP()

    result = csp.backtracking_search()

    print(result)

    print(
        "\n===== Degree Heuristic ====="
    )

    print(
        csp.degree_heuristic()
    )

    print(
        "\n===== Failure Explanation ====="
    )

    print(
        csp.explain_failure()
    )

    print(
        "\n===== Min Conflicts ====="
    )

    print(
        min_conflicts()
    )

    print(
        "\n===== SAT Intuition ====="
    )

    print(
        sat_intuition()
    )

    scheduler = TimetableScheduler()

    scheduler.assign(
        "Morning",
        "Agent_A"
    )

    scheduler.assign(
        "Afternoon",
        "Agent_B"
    )

    print(
        "\n===== Timetable ====="
    )

    print(
        scheduler.display()
    )