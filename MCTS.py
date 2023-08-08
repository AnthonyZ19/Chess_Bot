import chess_config as cc
import numpy as np
import math
import copy

# Defines the Montre-Carlo Tree Search protocols
class mcts:
    def __init__(self, game, c_value, searches):
        self.game = game
        self.c_value = c_value
        self.searches = searches

# Simulates chess games to search for good moves/actions
    def search(self):
        # Creates/Defines the root node, node of the current position
        root_node = node(copy.deepcopy(self.game), self.c_value)

        # Conducts the specified amount of searches
        for search in range(self.searches):
            # Sets/Resets starting point to the root node
            search_node = root_node

            # Looks for a node that isn't fully expanded
            while search_node.is_expanded():
                # If the current node is fully expanded then the child with the highest UCB is chosen
                search_node = search_node.select()

            #  If the game hasn't ended then the current node is expanded and then the rest of the match is simulated
            if not cc.game_ended(self.game, True):
                # Expands the node, by selecting a random move
                search_node = search_node.expand()
                # Simulates the rest of the game by selecting random moves
                value = search_node.simulate()
            else:
                if cc.in_check(self.game, "attack", "king pos") and (len(cc.find_moves(self.game)) == 0):
                    value = (self.game).current_player_turn
                else:
                    value = 0
            
            # Backpropagates through the nodes to adjust the values
            search_node.backpropagate(value)

        # Return visit_counts
        action_probs = []
        for route in root_node.routes:
            action_probs.append([route.action, route.visit_count])
        return action_probs


class node:
    def __init__(self, game, c_value, parent = None, action = None):
        self.game = game
        self.c_value = c_value
        self.parent = parent
        self.action = action
        self.routes = []
        self.expandable_moves = cc.find_moves(game)
        self.visit_count = 0
        self.value = 0

# Checks if the node is fully expanded
    def is_expanded(self):
        if (len(self.expandable_moves) == 0) and (len(self.routes) > 0):
            return True
        else:
            return False

# Returns the UCB score for the current route    
    def ucb(self, route):
        q = (route.value / route.visit_count) * self.game.current_player_turn
        ucb = q + self.c_value * math.sqrt(math.log(self.visit_count)/route.visit_count)
        return ucb

# Selects the action with the highest UCB score from the possible actions
    def select(self):
        best_route = None
        highest_ucb = -np.inf

        for route in self.routes:
            ucb = self.ucb(route)
            if ucb > highest_ucb:
                best_route = route
                highest_ucb = ucb

        return best_route
    
    def expand(self):
        action = self.expandable_moves[np.random.randint(0, high=len(self.expandable_moves))]
        cc.make_move(self.game, action[0], action[1])
        route = node(self.game, self.c_value, self, action)
        self.routes.append(route)

        for i in range(len(self.expandable_moves) - 1):
            if self.expandable_moves[i] == action:
                self.expandable_moves.pop(i)
                break

        return route
    
    def simulate(self):
        while True:
            if cc.in_check(self.game, "attack", "king pos") and (len(cc.find_moves(self.game)) == 0):
                return (self.game).current_player_turn
            else:
                value = 0

            if cc.game_ended(self.game, True):
                return value
            
            legal_moves = cc.find_moves(self.game)
            action = legal_moves[np.random.randint(0, high=len(legal_moves))]
            cc.make_move(self.game, action[0], action[1])
            
    def backpropagate(self, value):
        self.value += value
        self.visit_count += 1

        if self.parent is not None:
            self.parent.backpropagate(value)