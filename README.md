# PAC-MAN project
Readme sections:
- [Objectives](#objectives)  
- [Resources](#resources)  
- [Run the code](#how-to-run-the-code)  
  
## Objectives
There are two objectives in this project: 
- First, use uninformed and informed search to find feed points efficiently without ghosts. The code can be found in the [search algorithms](https://github.com/Sararl27/FIA_PAC-MAN_project/tree/main/search_algorithms) folder. 
- Secondly, make use of the minimax adversarial search algorithm and its enhancement, the minimax algorithm with alpha-beta pruning, to create a basic version of the classic game with ghosts. The code can be found in the [multi agent algorithms](https://github.com/Sararl27/FIA_PAC-MAN_project/tree/main/multi_agent_algorithms) folder.

The two subprojects were carried out using the [Project 1: Search](https://inst.eecs.berkeley.edu/~cs188/su19/project1/) and [Project 2: Multi-Agent Search](https://inst.eecs.berkeley.edu/~cs188/su19/project2/) frameworks.
## Resources
Resources of [search algorithms](https://github.com/Sararl27/FIA_PAC-MAN_project/tree/main/search_algorithms) folder:
| File name  | Description |
| :-------:  | ----------- |
| search.py  | Where all search algorithms reside. |
| node.py | Auxiliary class created for this project to recreate a state with its attributes and functions. |
| searchAgents.py |	Where search-based agents reside. |
| pacman_search.py |	The main file that runs Pacman games. This file describes a Pacman GameState type, which you use in this project. |
| game.py |	The logic behind how the Pacman world works. This file describes several supporting types like AgentState, Agent, Direction, and Grid. |
| util.py |	Useful data structures for implementing search algorithms. | 
| graphicsDisplay.py |	Graphics for Pacman. |
| graphicsUtils.py |	Support for Pacman graphics. |
| textDisplay.py |	ASCII graphics for Pacman. |
| ghostAgents.py |	Agents to control ghosts. |
| keyboardAgents.py |	Keyboard interfaces to control Pacman. |
| layout.py |	Code for reading layout files and storing their contents. |
| autograder_search.py |	Project autograder. |
| testParser.py |	Parses autograder test and solution files. |
| testClasses.py |	General autograding test classes. |
| test_cases/ |	Directory containing the test cases for each question. |
| searchTestClasses.py |	Project 1 specific autograding test classes. |

Resources of [multi agent algorithms](https://github.com/Sararl27/FIA_PAC-MAN_project/tree/main/multi_agent_algorithms) folder:
| File name  | Description |
| :-------:  | ----------- |
| multiAgents.py |	Where all multi-agent search agents reside. |
| pacman_multiAgent.py |	The main file that runs Pacman games. This file describes a Pacman GameState type, which you use in this project. |
| game.py |	The logic behind how the Pacman world works. This file describes several supporting types like AgentState, Agent, Direction, and Grid. |
| util.py |	Useful data structures for implementing search algorithms. | 
| graphicsDisplay.py |	Graphics for Pacman. |
| graphicsUtils.py |	Support for Pacman graphics. |
| textDisplay.py |	ASCII graphics for Pacman. |
| ghostAgents.py |	Agents to control ghosts. |
| keyboardAgents.py |	Keyboard interfaces to control Pacman. |
| layout.py |	Code for reading layout files and storing their contents. |
| autograder_multAgent.py |	Project autograder. |
| testParser.py |	Parses autograder test and solution files. |
| testClasses.py |	General autograding test classes. |
| test_cases/ |	Directory containing the test cases for each question. |
| searchTestClasses.py |	Project 1 specific autograding test classes. |

## How to run the code
### Search algorithms
- To test all algorithms without graphics: ``` python autograder_search.py ```.
- To execute with Depth First Search algorithm: ```python pacman_search.py -l <map> -p SearchAgent``` where _\<map\>_ can be _tinyMaze_, _mediumMaze_ or _bigMaze_.  For the _bigMaze_ map it is recommended to add the ```-z .5``` parameter at the end of the command.
- To execute with Breadth First Search algorithm: ```python pacman_search.py -l <map> -p SearchAgent -a fn=bfs``` where _\<map\>_ can be _tinyMaze_, _mediumMaze_ or _bigMaze_. For the _bigMaze_ map it is recommended to add the ```-z .5``` parameter at the end of the command.
- To execute with Unfirm Cost Search algorithm: 
  -  ```python pacman_search.py -l <map> -p SearchAgent -a fn=ucs``` where _\<map\>_ can be _tinyMaze_, _mediumMaze_ or _bigMaze_. For the _bigMaze_ map it is recommended to add the ```-z .5``` parameter at the end of the command.
  -   ```python pacman_search.py -l mediumDottedMaze -p StayEastSearchAgent``` (you should get very low path costs).  
  -   ```python pacman_search.py -l mediumScaryMaze -p StayWestSearchAgent``` (you should get very high path costs). 
-   To execute with A* algorithm: ```python pacman_search.py -l <map> -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic``` where _\<map\>_ can be _tinyMaze_, _mediumMaze_ or _bigMaze_. For the _bigMaze_ map it is recommended to add the ```-z .5``` parameter at the end of the command.

### Multi Agent algorithms
- To test all algorithms without graphics: ``` python autograder_multiAgent.py ```.
- To execute with MiniMax algorithm: 
  - ```python pacman_multiAgent.py -p MinimaxAgent -l minimaxClassic -a depth=4```. 
  - ```python pacman_multiAgent.py -p MinimaxAgent -l smallClassic -a depth=3```.  
- To execute with MiniMax with Alpha-Beta Pruning algorithm: 
  - ```python pacman_multiAgent.py -p AlphaBetaAgent -l minimaxClassic -a depth=4```. 
  - ```python pacman_multiAgent.py -p AlphaBetaAgent -l smallClassic -a depth=3```.
