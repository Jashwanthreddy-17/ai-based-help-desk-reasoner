"""
=========================================================
CO2: BFS, DFS, UCS, GREEDY, A*
Automated Help Desk Reasoner
=========================================================
"""

from collections import deque
import heapq
import time


# =====================================================
# CO2: Issue Search Graph
# =====================================================

ISSUE_GRAPH = {

    "VPN": {
        "Internet": 1,
        "Credentials": 2,
        "Firewall": 3
    },

    "Internet": {
        "DNS": 2,
        "Router": 2
    },

    "Credentials": {
        "PasswordExpired": 1,
        "AccountLocked": 1
    },

    "Firewall": {
        "PortBlocked": 2
    },

    "DNS": {},

    "Router": {},

    "PasswordExpired": {},

    "AccountLocked": {},

    "PortBlocked": {}
}


# =====================================================
# CO2: Profiling
# =====================================================

class SearchMetrics:

    def __init__(self):

        self.nodes_expanded = 0

        self.runtime = 0

        self.max_frontier = 0

    def report(self):

        return {

            "nodes_expanded":
                self.nodes_expanded,

            "runtime_ms":
                round(self.runtime * 1000, 2),

            "peak_frontier":
                self.max_frontier
        }


# =====================================================
# CO2: BFS
# =====================================================

def bfs(graph, start, goal):

    metrics = SearchMetrics()

    start_time = time.time()

    queue = deque()

    queue.append((start, [start]))

    visited = set()

    while queue:

        metrics.max_frontier = max(
            metrics.max_frontier,
            len(queue)
        )

        node, path = queue.popleft()

        metrics.nodes_expanded += 1

        if node == goal:

            metrics.runtime = time.time() - start_time

            return path, metrics.report()

        visited.add(node)

        for neighbor in graph[node]:

            if neighbor not in visited:

                queue.append(
                    (
                        neighbor,
                        path + [neighbor]
                    )
                )

    metrics.runtime = time.time() - start_time

    return None, metrics.report()


# =====================================================
# CO2: DFS
# =====================================================

def dfs(graph, start, goal):

    metrics = SearchMetrics()

    start_time = time.time()

    stack = [(start, [start])]

    visited = set()

    while stack:

        metrics.max_frontier = max(
            metrics.max_frontier,
            len(stack)
        )

        node, path = stack.pop()

        metrics.nodes_expanded += 1

        if node == goal:

            metrics.runtime = time.time() - start_time

            return path, metrics.report()

        visited.add(node)

        for neighbor in graph[node]:

            if neighbor not in visited:

                stack.append(
                    (
                        neighbor,
                        path + [neighbor]
                    )
                )

    metrics.runtime = time.time() - start_time

    return None, metrics.report()


# =====================================================
# CO2: UCS
# =====================================================

def ucs(graph, start, goal):

    metrics = SearchMetrics()

    start_time = time.time()

    pq = []

    heapq.heappush(
        pq,
        (0, start, [start])
    )

    visited = set()

    while pq:

        metrics.max_frontier = max(
            metrics.max_frontier,
            len(pq)
        )

        cost, node, path = heapq.heappop(pq)

        metrics.nodes_expanded += 1

        if node == goal:

            metrics.runtime = time.time() - start_time

            return cost, path, metrics.report()

        if node in visited:
            continue

        visited.add(node)

        for neighbor, edge_cost in graph[node].items():

            heapq.heappush(

                pq,

                (
                    cost + edge_cost,
                    neighbor,
                    path + [neighbor]
                )
            )

    metrics.runtime = time.time() - start_time

    return None, None, metrics.report()


# =====================================================
# CO2: Heuristic Design
# =====================================================

HEURISTIC = {

    "VPN": 4,

    "Internet": 3,

    "Credentials": 2,

    "Firewall": 3,

    "DNS": 0,

    "Router": 0,

    "PasswordExpired": 0,

    "AccountLocked": 0,

    "PortBlocked": 0
}


# =====================================================
# CO2: Greedy Search
# =====================================================

def greedy_search(graph, start, goal):

    pq = []

    heapq.heappush(

        pq,

        (
            HEURISTIC[start],
            start,
            [start]
        )
    )

    visited = set()

    while pq:

        _, node, path = heapq.heappop(pq)

        if node == goal:

            return path

        visited.add(node)

        for neighbor in graph[node]:

            if neighbor not in visited:

                heapq.heappush(

                    pq,

                    (
                        HEURISTIC[neighbor],
                        neighbor,
                        path + [neighbor]
                    )
                )

    return None


# =====================================================
# CO2: A*
# =====================================================

def a_star(graph, start, goal):

    pq = []

    heapq.heappush(

        pq,

        (
            HEURISTIC[start],
            0,
            start,
            [start]
        )
    )

    visited = set()

    while pq:

        f, g, node, path = heapq.heappop(pq)

        if node == goal:

            return g, path

        visited.add(node)

        for neighbor, edge_cost in graph[node].items():

            if neighbor not in visited:

                new_g = g + edge_cost

                new_f = (

                    new_g +

                    HEURISTIC[neighbor]
                )

                heapq.heappush(

                    pq,

                    (
                        new_f,
                        new_g,
                        neighbor,
                        path + [neighbor]
                    )
                )

    return None, None


# =====================================================
# CO2: Closed/Open Set Concept
# =====================================================

class OpenClosedTracker:

    def __init__(self):

        self.open_set = set()

        self.closed_set = set()

    def add_open(self, node):

        self.open_set.add(node)

    def add_closed(self, node):

        self.closed_set.add(node)


# =====================================================
# CO2: IDA* Concept
# =====================================================

def ida_star_concept():

    return (
        "Memory bounded search "
        "using iterative deepening."
    )


# =====================================================
# CO2: Unit Testing
# =====================================================

def test_bfs():

    path, _ = bfs(

        ISSUE_GRAPH,

        "VPN",

        "PasswordExpired"
    )

    assert path is not None


def test_astar():

    cost, path = a_star(

        ISSUE_GRAPH,

        "VPN",

        "PasswordExpired"
    )

    assert cost is not None


# =====================================================
# CO2: Demo
# =====================================================

if __name__ == "__main__":

    print("\n========== BFS ==========")

    path, metrics = bfs(

        ISSUE_GRAPH,

        "VPN",

        "PasswordExpired"
    )

    print(path)

    print(metrics)

    print("\n========== DFS ==========")

    path, metrics = dfs(

        ISSUE_GRAPH,

        "VPN",

        "PasswordExpired"
    )

    print(path)

    print(metrics)

    print("\n========== UCS ==========")

    cost, path, metrics = ucs(

        ISSUE_GRAPH,

        "VPN",

        "PasswordExpired"
    )

    print(cost)

    print(path)

    print(metrics)

    print("\n========== GREEDY ==========")

    print(

        greedy_search(

            ISSUE_GRAPH,

            "VPN",

            "PasswordExpired"
        )
    )

    print("\n========== A* ==========")

    cost, path = a_star(

        ISSUE_GRAPH,

        "VPN",

        "PasswordExpired"
    )

    print(cost)

    print(path)