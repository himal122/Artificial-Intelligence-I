
from approvedimports import *

class DepthFirstSearch(SingleMemberSearch):
    """your implementation of depth first search to extend
    the superclass SingleMemberSearch search.
    Adds  a __str__method
    Over-rides the method select_and_move_from_openlist
    to implement the algorithm
    """

    def __str__(self):
        return "depth-first"

    def select_and_move_from_openlist(self) -> CandidateSolution:
        """void in superclass
        In sub-classes should implement different algorithms
        depending on what item it picks from self.open_list
        and what it then does to the open list

        Returns
        -------
        next working candidate (solution) taken from open list
        """

        # create a candidate solution variable to hold the next solution
        next_soln = CandidateSolution()

        # ====> insert your pseudo-code and code below here

        # Check if open_list is empty
        if not self.open_list:
            return None
        
        # pseudocode ====> my_index ← GetLastIndex(open_list)
        my_index = len(self.open_list) - 1

        # pseudocode ====> the_candidate ← open_list(my_index)
        next_soln = self.open_list[my_index]

        # pseudocode ====> RemoveFromOpenList(my_index)
        self.open_list.pop(my_index)

        # pseudocode ====> WHILE IsNotEmpty( open_list) DO
        # while (open_list != 0): # this is not working/ I am commenting it as it seems to be a distraction I don't need loops to solve this
            

        # <==== insert your pseudo-code and code above here
        return next_soln

class BreadthFirstSearch(SingleMemberSearch):
    """your implementation of depth first search to extend
    the superclass SingleMemberSearch search.
    Adds  a __str__method
    Over-rides the method select_and_move_from_openlist
    to implement the algorithm
    """

    def __str__(self):
        return "breadth-first"

    def select_and_move_from_openlist(self) -> CandidateSolution:
        """Implements the breadth-first search algorithm

        Returns
        -------
        next working candidate (solution) taken from open list
        """
        # create a candidate solution variable to hold the next solution
        next_soln = CandidateSolution()

        # ====> insert your pseudo-code and code below here

        # Check if open_list is empty
        if not self.open_list:
            return None
        
        # pseudocode ====> my_index ← GetFirstIndex (open_list)
        my_index = 0

        # pseudocode ====> the_candidate ← open_list(my_index)
        next_soln = self.open_list[my_index]

        # pseudocode ====> RemoveFromOpenList(my_index)
        self.open_list.pop(my_index)
        
        # <==== insert your pseudo-code and code above here
        return next_soln

class BestFirstSearch(SingleMemberSearch):
    """Implementation of Best-First search."""

    def __str__(self):
        return "best-first"

    def select_and_move_from_openlist(self) -> CandidateSolution:
        """Implements Best First by finding, popping and returning member from openlist
        with best quality.

        Returns
        -------
        next working candidate (solution) taken from openlist
        """

        # create a candidate solution variable to hold the next solution
        next_soln = CandidateSolution()

        # ====> insert your pseudo-code and code below here

        # pseudocode ====> IF IsEmpty( open_list) THEN RETURN None
        if not self.open_list:
            return None

        # pseudocode ====> ELSE bestChild = GetMemberWithHighestQuality (openList)
        best_index = 0
        best_quality = self.open_list[0].quality

        for i in range(1, len(self.open_list)):
            current_quality = self.open_list[i].quality

            if self.minimise:
                if current_quality < best_quality:
                    best_quality = current_quality
                    best_index = i
            else:
                if current_quality > best_quality:
                    best_quality = current_quality
                    best_index = i

        # Remove and return the best child
        best_child = self.open_list.pop(best_index)
        return best_child

        # <==== insert your pseudo-code and code above here
        return next_soln

class AStarSearch(SingleMemberSearch):
    """Implementation of A-Star  search."""

    def __str__(self):
        return "A Star"

    def select_and_move_from_openlist(self) -> CandidateSolution:
        """Implements A-Star by finding, popping and returning member from openlist
        with lowest combined length+quality.

        Returns
        -------
        next working candidate (solution) taken from openlist
        """
        
        # create a candidate solution variable to hold the next solution
        next_soln = CandidateSolution()

        # ====> insert your pseudo-code and code below here

        # pseudocode ====> IF IsEmpty( open_list) THEN RETURN None
        if not self.open_list:
            return None

        # pseudocode ====> bestChild GetMemberWithHighestCombinedScore(openList)

        best_index = 0
        best_combined = self.open_list[0].quality + len(self.open_list[0].variable_values)

        for i in range(1, len(self.open_list)):
            current_quality = self.open_list[i].quality
            current_cost = len(self.open_list[i].variable_values)
            current_combined = current_quality + current_cost

            # Minimize combined score
            if current_combined < best_combined:
                best_combined = current_combined
                best_index = i

        # pseudocode ====>RETURN bestChild
        best_child = self.open_list.pop(best_index)
        return best_child

        # <==== insert your pseudo-code and code above here
        return next_soln
wall_colour= 0.0
hole_colour = 1.0

def create_maze_breaks_depthfirst():
    # ====> insert your code below here
    #remember to comment out any mention of show_maze() before you submit your work

     # Load base maze
    maze = Maze(mazefile="maze.txt")

    maze.contents[3][4] = hole_colour  # Open path to trick DFS
    maze.contents[8][4] = wall_colour  # Block DFS at the end

    maze.contents[10][6] = hole_colour  # Another DFS trap
    maze.contents[14][6] = wall_colour  # Dead-end
    maze.contents[16][1] = hole_colour  # Dead-end
    maze.contents[19][4] = hole_colour  # Dead-end

    maze.contents[8][1] = hole_colour
    maze.contents[12][9] = wall_colour
    maze.contents[11][12] = wall_colour
    maze.contents[9][2] = wall_colour
    maze.contents[10][19] = wall_colour
    maze.contents[18][5] = wall_colour
    
    # Save the maze
    maze.save_to_txt("maze-breaks-depth.txt")

    # reload into new maze object
    print('this is the reloaded maze')
    reloaded_maze = Maze(mazefile="maze-breaks-depth.txt")
    
    # <==== insert your code above here

def create_maze_depth_better():
    # ====> insert your code below here
    #remember to comment out any mention of show_maze() before you submit your work

    # ====> insert your code below here
    #remember to comment out any mention of show_maze() before you submit your work
    maze = Maze(mazefile="maze.txt")
    maze.contents[1][8] = wall_colour
    maze.contents[9][10] = wall_colour
    maze.contents[15][6] = wall_colour
    maze.contents[13][2] = wall_colour
    maze.contents[12][13] = wall_colour
    maze.contents[2][13] = wall_colour
    maze.save_to_txt("maze-depth-better.txt")

    # <==== insert your code above here
