import torch
import random
import numpy as np
from collections import deque
from game import SnakeGameAI, Direction , Point

MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001

"""
Agent 
- game
- model
Training: 
    - state = get_state(game)
    - action = get_mov(state):
        - model.predict()
    - reward,game_over,score = game.play_step(action)
    - new_state = get_state(game)
    - remember
    - model.train()
"""

class Agent:
    def __init__(self):
        self.n_games = 0
        self.epsilon = 0# randomness
        self.gamma =0 # discount rate
        self.memory = deque(maxlen= MAX_MEMORY)# popleft()
        #   TODO:   model , trainer

    def get_state(self, game):
        pass
    def remember(self , state , action , reward , next_state , isDone):
        pass

    def train_long_memory(self):
        pass
    def train_short_memory(self, state , action , reward , next_state , isDone):
        pass

    def get_action(self , state):
        pass


def train():
    play_scores = []
    plot_mean_scores = []
    total_score = 0
    record = 0
    agent = Agent()
    game = SnakeGameAI()
    while True:
        # get old state 
        state_old = agent.get_state(game)
        # get move
        final_move = agent.get_action(state_old)
        #perform move and get new state
        reward, isDone , score = game.play_step(final_move)
        state_new = agent.get_state(game)

        #train short memory 
        agent.train_short_memory(state_old, final_move, reward , state_new , isDone)
        #remember
        agent.remember()
        if isDone:
            #train long memory 
            # Experience Replay
            game.reset()
            agent.n_games +=1 
            agent.train_long_memory()
            if score > record:
                record = score
                # agent.model.save()

            print('Game', agent.n_games, 'Score', score , 'Record:', record)
            # TODO: Plot
            
if __name__ == '__main__':
    train()