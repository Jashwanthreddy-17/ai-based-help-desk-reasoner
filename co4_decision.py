"""
=========================================================
CO4: DECISION MAKING
Utility Functions
Minimax
Alpha-Beta Pruning
Evaluation Functions
Policy Selection
Multi-Agent Reasoning
=========================================================
"""

from dataclasses import dataclass


# =====================================================
# CO4: Utility Functions
# =====================================================

UTILITY_TABLE = {

    "AUTO_RESOLVE": 100,

    "CREATE_TICKET": 60,

    "ESCALATE": 40
}


def utility(action):

    return UTILITY_TABLE.get(
        action,
        0
    )


# =====================================================
# CO4: Evaluation Function
# =====================================================

def evaluate_state(confidence,
                   severity):

    """
    confidence:
        AI confidence 0-100

    severity:
        Issue severity 0-100
    """

    score = confidence - severity

    return score


# =====================================================
# CO4: Decision Policy
# =====================================================

def choose_policy(confidence,
                  severity):

    score = evaluate_state(
        confidence,
        severity
    )

    if score >= 40:

        return "AUTO_RESOLVE"

    elif score >= 10:

        return "CREATE_TICKET"

    else:

        return "ESCALATE"


# =====================================================
# CO4: Game State
# =====================================================

@dataclass
class DecisionState:

    confidence: int

    severity: int

    depth: int = 0


# =====================================================
# CO4: Multi-Agent Reasoning
# =====================================================

AGENTS = {

    "AI_AGENT": 90,

    "LEVEL1_SUPPORT": 70,

    "LEVEL2_SUPPORT": 50,

    "LEVEL3_SUPPORT": 30
}


# =====================================================
# CO4: Minimax
# =====================================================

def minimax(state,
            maximizing):

    if state.depth == 3:

        return evaluate_state(

            state.confidence,

            state.severity
        )

    if maximizing:

        best = float("-inf")

        for change in [10, 20]:

            value = minimax(

                DecisionState(

                    state.confidence + change,

                    state.severity,

                    state.depth + 1
                ),

                False
            )

            best = max(best, value)

        return best

    else:

        best = float("inf")

        for change in [10, 20]:

            value = minimax(

                DecisionState(

                    state.confidence,

                    state.severity + change,

                    state.depth + 1
                ),

                True
            )

            best = min(best, value)

        return best


# =====================================================
# CO4: Alpha Beta Pruning
# =====================================================

def alpha_beta(state,
               depth,
               alpha,
               beta,
               maximizing):

    if depth == 0:

        return evaluate_state(

            state.confidence,

            state.severity
        )

    if maximizing:

        value = float("-inf")

        for change in [10, 20]:

            value = max(

                value,

                alpha_beta(

                    DecisionState(

                        state.confidence + change,

                        state.severity
                    ),

                    depth - 1,

                    alpha,

                    beta,

                    False
                )
            )

            alpha = max(alpha, value)

            if beta <= alpha:

                break

        return value

    else:

        value = float("inf")

        for change in [10, 20]:

            value = min(

                value,

                alpha_beta(

                    DecisionState(

                        state.confidence,

                        state.severity + change
                    ),

                    depth - 1,

                    alpha,

                    beta,

                    True
                )
            )

            beta = min(beta, value)

            if beta <= alpha:

                break

        return value


# =====================================================
# CO4: Iterative Deepening Concept
# =====================================================

def iterative_deepening_concept():

    return (

        "Increase search depth gradually "
        "until solution found."
    )


# =====================================================
# CO4: Expectimax Concept
# =====================================================

def expectimax_concept():

    return (

        "Decision making under uncertainty "
        "using expected outcomes."
    )


# =====================================================
# CO4: Bounded Rationality
# =====================================================

def bounded_rationality():

    return (

        "Choose good enough solution "
        "within limited resources."
    )


# =====================================================
# CO4: Policy Selection Engine
# =====================================================

class DecisionEngine:

    def make_decision(self,
                      confidence,
                      severity):

        action = choose_policy(

            confidence,

            severity
        )

        return {

            "action": action,

            "utility":

                utility(action)
        }


# =====================================================
# CO4: Unit Tests
# =====================================================

def test_policy():

    result = choose_policy(

        90,

        20
    )

    assert result == "AUTO_RESOLVE"


def test_minimax():

    score = minimax(

        DecisionState(

            80,

            30
        ),

        True
    )

    assert score is not None


# =====================================================
# Demo
# =====================================================

if __name__ == "__main__":

    print(
        "\n===== Utility ====="
    )

    print(
        utility(
            "AUTO_RESOLVE"
        )
    )

    print(
        "\n===== Policy ====="
    )

    print(
        choose_policy(
            85,
            20
        )
    )

    print(
        "\n===== Minimax ====="
    )

    print(

        minimax(

            DecisionState(
                80,
                30
            ),

            True
        )
    )

    print(
        "\n===== Alpha Beta ====="
    )

    print(

        alpha_beta(

            DecisionState(
                80,
                30
            ),

            3,

            float("-inf"),

            float("inf"),

            True
        )
    )

    print(
        "\n===== Decision Engine ====="
    )

    engine = DecisionEngine()

    print(

        engine.make_decision(

            confidence=90,

            severity=20
        )
    )

    print(
        "\n===== Expectimax ====="
    )

    print(
        expectimax_concept()
    )

    print(
        "\n===== Bounded Rationality ====="
    )

    print(
        bounded_rationality()
    )