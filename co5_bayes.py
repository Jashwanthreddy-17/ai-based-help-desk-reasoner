"""
=========================================================
CO5: PROBABILISTIC REASONING
Bayes Rule
Bayesian Networks
Variable Elimination
Expected Utility
Markov Chains
HMM Intuition
Sensor Fusion
=========================================================
"""

from dataclasses import dataclass


# =====================================================
# CO5: Probability Basics
# =====================================================

def probability(event_count,
                total_count):

    if total_count == 0:
        return 0

    return event_count / total_count


# =====================================================
# CO5: Bayes Rule
# =====================================================

def bayes_rule(
        p_b_given_a,
        p_a,
        p_b):

    """
    P(A|B)

    = P(B|A) * P(A)
      ----------------
           P(B)
    """

    if p_b == 0:
        return 0

    return (

        p_b_given_a *

        p_a

    ) / p_b


# =====================================================
# CO5: Help Desk Bayesian Network
# =====================================================

class BayesianNetwork:

    def __init__(self):

        self.nodes = {}

        self.cpt = {}

    def add_node(self,
                 node):

        self.nodes[node] = []

    def add_edge(self,
                 parent,
                 child):

        self.nodes[parent].append(
            child
        )

    def add_probability(
            self,
            node,
            value):

        self.cpt[node] = value

    def get_probability(
            self,
            node):

        return self.cpt.get(
            node,
            0
        )


# =====================================================
# Help Desk Bayesian Network
# =====================================================

network = BayesianNetwork()

network.add_node(
    "PasswordChanged"
)

network.add_node(
    "VPNFailure"
)

network.add_node(
    "CredentialIssue"
)

network.add_edge(
    "PasswordChanged",
    "CredentialIssue"
)

network.add_edge(
    "CredentialIssue",
    "VPNFailure"
)

network.add_probability(
    "PasswordChanged",
    0.60
)

network.add_probability(
    "CredentialIssue",
    0.80
)

network.add_probability(
    "VPNFailure",
    0.90
)

# =====================================================
# CO5: Variable Elimination
# =====================================================

def variable_elimination():

    """
    Simplified Example
    """

    p_password = network.get_probability(
        "PasswordChanged"
    )

    p_credential = network.get_probability(
        "CredentialIssue"
    )

    p_vpn = network.get_probability(
        "VPNFailure"
    )

    result = (

        p_password *

        p_credential *

        p_vpn
    )

    return round(
        result,
        4
    )


# =====================================================
# CO5: Sensor Fusion
# =====================================================

def sensor_fusion(
        internet_ok,
        password_changed,
        firewall_ok):

    score = 0

    if internet_ok:
        score += 0.3

    if password_changed:
        score += 0.5

    if firewall_ok:
        score += 0.2

    return round(
        score,
        2
    )


# =====================================================
# CO5: HMM Intuition
# =====================================================

@dataclass
class HiddenState:

    state: str

    probability: float


class HMMTracker:

    def __init__(self):

        self.states = [

            HiddenState(
                "Healthy",
                0.8
            ),

            HiddenState(
                "Problem",
                0.2
            )
        ]

    def predict(self):

        return max(

            self.states,

            key=lambda s:
            s.probability
        )


# =====================================================
# CO5: Markov Chain
# =====================================================

class MarkovChain:

    def __init__(self):

        self.transitions = {

            "Healthy": {

                "Healthy": 0.8,

                "Problem": 0.2
            },

            "Problem": {

                "Healthy": 0.3,

                "Problem": 0.7
            }
        }

    def next_state(
            self,
            current):

        probabilities = self.transitions[
            current
        ]

        return max(

            probabilities,

            key=probabilities.get
        )


# =====================================================
# CO5: Expected Utility
# =====================================================

def expected_utility():

    utility_auto = 100

    utility_ticket = 60

    p_success = 0.85

    p_failure = 0.15

    value = (

        p_success *

        utility_auto +

        p_failure *

        utility_ticket
    )

    return round(
        value,
        2
    )


# =====================================================
# CO5: Uncertainty Aware Decision
# =====================================================

def uncertainty_decision():

    probability_issue = variable_elimination()

    if probability_issue > 0.4:

        return "HIGH_CONFIDENCE"

    elif probability_issue > 0.2:

        return "MEDIUM_CONFIDENCE"

    return "LOW_CONFIDENCE"


# =====================================================
# CO5: Help Desk Example
# =====================================================

def vpn_probability_example():

    """
    P(CredentialIssue | VPNFailure)
    """

    result = bayes_rule(

        p_b_given_a=0.9,

        p_a=0.8,

        p_b=0.7
    )

    return round(
        result,
        4
    )


# =====================================================
# CO5: Unit Tests
# =====================================================

def test_bayes():

    result = bayes_rule(

        0.9,

        0.8,

        0.7
    )

    assert result > 0


def test_expected_utility():

    assert expected_utility() > 0


# =====================================================
# Demo
# =====================================================

if __name__ == "__main__":

    print(
        "\n===== Bayes Rule ====="
    )

    print(
        vpn_probability_example()
    )

    print(
        "\n===== Variable Elimination ====="
    )

    print(
        variable_elimination()
    )

    print(
        "\n===== Sensor Fusion ====="
    )

    print(

        sensor_fusion(

            internet_ok=True,

            password_changed=True,

            firewall_ok=False
        )
    )

    print(
        "\n===== HMM ====="
    )

    hmm = HMMTracker()

    print(
        hmm.predict()
    )

    print(
        "\n===== Markov Chain ====="
    )

    mc = MarkovChain()

    print(
        mc.next_state(
            "Problem"
        )
    )

    print(
        "\n===== Expected Utility ====="
    )

    print(
        expected_utility()
    )

    print(
        "\n===== Confidence ====="
    )

    print(
        uncertainty_decision()
    )