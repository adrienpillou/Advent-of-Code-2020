# Author : Adrien Pillou
# Date : 12/12/2020
# --- Day 12: Rain Risk ---
# Answer = 1496

import math
import pygame
import sys
import os

# Ferry object
class Ferry():
    def __init__(self, position:tuple):
        self.start_position = position
        self.position = position
        self.direction = (1, 0)
        self.path = []
        self.path.append(position)
    
    def receive_instruction(self, action, value):
        if action in ['N', 'S', 'E', 'W', 'F']:
            self.move(action, value)
        elif action in ['R', 'L']:
            self.rotate(action, value)

    def move(self, direction, value):
        if direction == 'N':
            angle = (0, -1)
        elif direction == 'S':
            angle = (0, 1)
        elif direction == 'E':
            angle = (1, 0)
        elif direction == 'W':
            angle = (-1, 0)
        else:# Moving along it's direction
            angle = self.direction
        x = self.position[0] + angle[0]*value
        y = self.position[1] + angle[1]*value
        self.path.append((x, y))
        self.position = (self.position[0] + angle[0]*value, self.position[1] + angle[1]*value)

    def rotate(self, action, angle):
        if action == 'R':
            for i in range(angle//90):
                self.direction = (-self.direction[1], self.direction[0])
        elif action == 'L':
            for i in range(angle//90):
                self.direction = (self.direction[1], -self.direction[0])

    def __repr__(self):
        return f"Ferry is on x:{self.position[0]} y:{self.position[1]}"

def manhattan(a:tuple):
    return abs(a[0]) + abs(a[1])

if __name__ == "__main__":
    show_graph = True

    # Read input data
    x = []
    with open("in.txt", 'r') as f:
        x = f.readlines()
    x = [l.strip() for l in x]

    # Structuring the input data
    instructions = []
    for l in x:
        obj = {}
        obj['action'] = l[0]
        obj['value'] = int(l[1:])
        instructions.append(obj)
    
    # Creating a Ferry
    ferry = Ferry((0, 0))

    for i in range(len(instructions)):
        ferry.receive_instruction(instructions[i]['action'], instructions[i]['value'])

    distance = manhattan(ferry.position)
    print(f"Answer : {distance}")

    # Plot an interactive graph
    if show_graph:
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        width = 1200
        height = 900
        window = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Rain Risk')
        clock = pygame.time.Clock()
        scale = .2
        speed = 100/scale
        offset = (width//2, height//2)
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_RIGHT:
                        offset = (offset[0] - scale*speed, offset[1])
                    if e.key == pygame.K_LEFT:
                        offset = (offset[0] + scale*speed, offset[1])
                    if e.key == pygame.K_UP:
                        offset = (offset[0], offset[1] + scale*speed)
                    if e.key == pygame.K_DOWN:
                        offset = (offset[0], offset[1] - scale*speed)
                elif e.type == pygame.MOUSEBUTTONDOWN:
                    if e.button == 4:
                        scale += .01
                    elif e.button == 5:
                        scale -= .01
                    if scale < 0.01:
                        scale = .01

            window.fill((0,0,0))
            path = ferry.path.copy()

            for i, point in enumerate(path):
                if i>0:
                    pygame.draw.line(window, (255, 255, 255), (path[i-1][0]/scale + offset[0], path[i-1][1]/scale + offset[1]), (point[0]/scale+ offset[0], point[1]/scale + offset[1]))

            # Draw boat's path
            for i, point in enumerate(path):
                if i == 0:
                    color = (0, 255, 0)
                elif i == len(path)-1:
                    color = (255, 0, 0)
                else : color = (0, 175, 200)
                pygame.draw.circle(window, color, (int(point[0]/scale + offset[0]), int(point[1]/scale + offset[1])), int(2/scale))
            
            pygame.display.update()
            clock.tick(60)

