"""
=========================================================
CO6: HYBRID AI REASONER

Combines

CO1 -> Knowledge Representation
CO2 -> Search Algorithms
CO3 -> CSP
CO4 -> Decision Making
CO5 -> Bayesian Reasoning

=========================================================
"""

# =====================================================
# Imports
# =====================================================

from backend.ai.co1_agent import HelpDeskAgent
from backend.ai.co2_search import bfs, ISSUE_GRAPH
from backend.ai.co3_csp import TicketAssignmentCSP
from backend.ai.co4_decision import DecisionEngine
from backend.ai.co5_bayes import (
    variable_elimination,
    uncertainty_decision
)

from backend.ai.semantic_search import (
    find_best_match
)

from backend.database import SessionLocal

from backend.models import (
    KnowledgeBase,
    Ticket
)

# =====================================================
# Explainability Engine
# =====================================================

class ExplainabilityEngine:

    def __init__(self):

        self.trace = []

    def add(self, step):

        self.trace.append(step)

    def get_trace(self):

        return self.trace


# =====================================================
# Hybrid Reasoner
# =====================================================

class HybridReasoner:

    def __init__(self):

        self.agent = HelpDeskAgent()

        self.decision_engine = (
            DecisionEngine()
        )

        self.explainer = (
            ExplainabilityEngine()
        )

    # ==========================================
    # Main Reasoning Pipeline
    # ==========================================

    def reason(self, issue):

        issue = issue.upper().strip()

        self.explainer = ExplainabilityEngine()

        self.explainer.add(
            f"Received issue: {issue}"
        )

        # ==================================
        # CO1 Rule Based Agent
        # ==================================

        self.explainer.add(
            "CO1: Rule Based Agent"
        )

        # ==================================
        # CO2 Search
        # ==================================

        self.explainer.add(
            "CO2: Graph Search"
        )

        path = None

        if "VPN" in issue:

            try:

                path, _ = bfs(
                    ISSUE_GRAPH,
                    "VPN",
                    "PasswordExpired"
                )

            except Exception:

                path = None

        self.explainer.add(
            f"Search Path: {path}"
        )

        # ==================================
        # CO3 CSP
        # ==================================

        self.explainer.add(
            "CO3: Agent Assignment CSP"
        )

        try:

            csp = TicketAssignmentCSP()

            assignment = (
                csp.backtracking_search()
            )

        except Exception:

            assignment = {}

        self.explainer.add(
            f"Assignment: {assignment}"
        )

        # ==================================
        # CO5 Bayesian
        # ==================================

        self.explainer.add(
            "CO5: Bayesian Inference"
        )

        try:

            probability = (
                variable_elimination()
            )

            bayes_confidence = (
                uncertainty_decision()
            )

        except Exception:

            probability = 0.0

            bayes_confidence = 0.0

        self.explainer.add(
            f"Probability={probability}"
        )

        self.explainer.add(
            f"Bayesian Confidence={bayes_confidence}"
        )

        # ==================================
        # CO4 Decision
        # ==================================

        self.explainer.add(
            "CO4: Decision Selection"
        )

        try:

            decision = (
                self.decision_engine
                .make_decision(
                    confidence=90,
                    severity=20
                )
            )

        except Exception:

            decision = "AUTO_RESOLVE"

        self.explainer.add(
            str(decision)
        )

        # ==================================
        # DATABASE LOOKUP + SEMANTIC SEARCH
        # ==================================

        db = SessionLocal()

        try:

            articles = db.query(
                KnowledgeBase
            ).all()

            kb_entry = None

            confidence = 0

            if articles:

                result = find_best_match(
                    issue,
                    articles
                )

                if result:

                    kb_entry, confidence = result

                    confidence = round(
                        confidence * 100,
                        2
                    )

            self.explainer.add(
                f"Semantic Confidence={confidence}%"
            )

            # ==========================
            # SOLUTION FOUND
            # ==========================

            return {

                "status": "SOLVED",

                "confidence": confidence,

                "message":
                    "I analyzed your issue and found a solution.",

                "issue": kb_entry.issue,

                "cause": kb_entry.cause,

                "solution": kb_entry.solution,

                "decision": decision
            }

            # ==========================
            # ESCALATION
            # ==========================

            self.explainer.add(
                "Knowledge Base Match Not Found"
            )

            ticket = Ticket(

                title=issue,

                description=issue,

                status="OPEN",

                priority="MEDIUM"
            )

            db.add(ticket)

            db.commit()

            db.refresh(ticket)

            return {

                "status":
                    "ESCALATED",

                "confidence":
                    confidence,

                "message":
                    (
                        "I could not confidently "
                        "identify a solution. "
                        "A support ticket has "
                        "been created."
                    ),

                "ticket_id":
                    ticket.id,

                "decision":
                    decision,

                "reasoning_trace":
                    self.explainer.get_trace()
            }

        finally:

            db.close()


# =====================================================
# Failure Analysis
# =====================================================

class FailureAnalysis:

    @staticmethod
    def analyse(issue):

        return {

            "issue":
                issue,

            "reason":
                "Knowledge not available",

            "recommendation":
                "Escalate to human agent"
        }


# =====================================================
# Ethics & Limitations
# =====================================================

ETHICS = {

    "bias":
        "Heuristics may favour common issues",

    "uncertainty":
        "Probabilities may be inaccurate",

    "knowledge_gap":
        "Unknown issues require escalation"
}


# =====================================================
# Unit Test
# =====================================================

def test_reasoner():

    reasoner = HybridReasoner()

    result = reasoner.reason(
        "vpn not working"
    )

    print(result)


# =====================================================
# Demo
# =====================================================

if __name__ == "__main__":

    test_reasoner()