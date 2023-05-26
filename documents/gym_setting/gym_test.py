import gym
import time

import os
os.add_dll_directory("")

def main():

    env=gym.make("CartPole-v1",render_mode="human")
    env.reset()
    for _ in range(100):
        s,_,_,_,_=env.step(env.action_space.sample())
        env.render()
        time.sleep(0.05)
    env.close()

if __name__=="__main__":
    main()