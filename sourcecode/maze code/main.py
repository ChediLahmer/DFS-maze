import sys
graph = {
    'A': ['B', 'F'],
    'B': ['A', 'G', 'C'],
    'C': ['B', 'H', 'D'],
    'D': ['C', 'I', 'E'],
    'E': ['D'],
    'F': ['A', 'G', 'J'],
    'G': ['F', 'J', 'L', 'B'],
    'H': ['L', 'C', 'I'],
    'I': ['L', 'H', 'D', 'Q'],
    'J': ['F', 'M', 'N', 'G'],
    'K': ['L'],
    'L': ['K', 'G', 'H', 'I'],
    'M': ['J', 'R', 'N'],
    'N': ['M', 'J', 'O', 'R'],
    'O': ['P', 'Q', 'S', 'N'],
    'P': ['O'],
    'Q': ['I', 'O', 'U', 'Z'],
    'R': ['N', 'M', 'S', 'T'],
    'S': ['T', 'R', 'O'],
    'T': ['R', 'S', 'U'],
    'U': ['V', 'T', 'W', 'Q'],
    'V': ['U'],
    'W': ['U', 'Y', 'X'],
    'X': ['W', 'Y'],
    'Y': ['W', 'X', 'Z'],
    'Z': ['Q', 'Y']
}

node_positions = {
    'A': (100, 100),
    'B': (200, 200),
    'C': (200, 300),
    'D': (200, 400),
    'E': (200, 500),
    'F': (300, 100),
    'G': (400, 200),
    'H': (400, 300),
    'I': (400, 400),
    'J': (500, 100),
    'K': (600, 200),
    'L': (600, 300),
    'M': (700, 100),
    'N': (700, 200),
    'O': (700, 300),
    'P': (650, 350),
    'Q': (800, 500),
    'R': (900, 100),
    'S': (900, 300),
    'T': (950, 200),
    'U': (1050, 300),
    'V': (1050, 150),
    'W': (1050, 400),
    'X': (1050, 500),
    'Y': (950, 450),
    'Z': (900, 600)
}
traps = set(['F', 'K', 'C', 'H', 'Q', 'T', 'X', 'M'])
goal = 'P'

entre = input('start point')
starts=[]
starts.append(entre)

#starts = ['V', 'Z', 'A', 'E']
start = []
def dfs_path(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    visited.add(start)
    path = path + [start]
    if start == goal:
        return path
    for neighbor in graph[start]:
        if neighbor not in visited and neighbor not in traps:
            new_path = dfs_path(graph, neighbor, goal, visited, path)
            if new_path:
                return new_path
    path.remove(start)
    return print('None')
for start in starts:
    path = dfs_path(graph, start, goal, set(), [])
    if path:
        print(f"Found a path from {start} to {goal}: {path}")
        break
import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
ORANGE = (255, 165, 0)
Yellow = (255, 128, 0)
pygame.init()
pygame.display.set_caption("Graph")
font = pygame.font.SysFont('Calibri', 20, True, False)
def draw_graph(graph, node_positions, path=None):
    pygame.init()

    size = (1200, 800)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Graph")
    font = pygame.font.SysFont('Calibri', 20, True, False)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        for node in graph:
            for neighbour in graph[node]:
                if path is not None and node in path and neighbour in path:
                    pygame.draw.line(screen, ORANGE, node_positions[node], node_positions[neighbour], 20)
                else:
                    pygame.draw.line(screen, WHITE, node_positions[node], node_positions[neighbour], 20)


            outer_boundary = set()
            for node in graph:
                for neighbour in graph[node]:
                    if node < neighbour:
                        outer_boundary.add((node, neighbour))


            for node, neighbour in outer_boundary:
                pygame.draw.line(screen, GRAY, node_positions[node], node_positions[neighbour], 10)

        for node, position in node_positions.items():

            if path is not None and node in path:
                pygame.draw.circle(screen, ORANGE, position, 20)
            if node in traps:

                pygame.draw.circle(screen, RED, position, 20)
            elif node == goal:

                pygame.draw.circle(screen, GREEN, position, 20)
            elif node == start:

                pygame.draw.circle(screen, Yellow, position, 20)
            else:

                pygame.draw.circle(screen, BLUE, position, 20)

            label = font.render(node, True, WHITE)
            label_rect = label.get_rect()
            label_rect.center = position
            screen.blit(label, label_rect)

        pygame.display.flip()


for start in starts:
    path = dfs_path(graph, start, goal, set(), [])
    if path:
        print(f"Found a path from {start} to {goal}: {path}")
        draw_graph(graph, node_positions, path)
        break
if(not path):
    size = (1200, 800)
    screen = pygame.display.set_mode(size)
    pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw_graph(graph, node_positions)
