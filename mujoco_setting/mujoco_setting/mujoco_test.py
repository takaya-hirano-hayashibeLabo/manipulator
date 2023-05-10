import gym
import time

def main():

    env=gym.make("Ant-v3")
    env.reset()
    for _ in range(100):
        s,_,_,_,=env.step(env.action_space.sample())
        env.render()
        time.sleep(0.05)
    env.close()

if __name__=="__main__":
    main()