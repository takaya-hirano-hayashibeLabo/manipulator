import gym
from gym import wrappers
env = gym.make('Kinova-v0')
env.reset()
action = [0,0,0]
e = 0
e_sum = 0
e_diff = 0

for t in range(10000):

    time = t/10000

    e_pre = e

    env.render()
    
    obs, reward, done, info = env.step(action)
    target = [0.41711435671808716+0.1*time,1.2714255554743565+0.1*time,-0.11774358539754726+0.1*time]
    kp = [200,200,10]
    kd = [100,100,10]

    e = target - obs
    e_diff = e - e_pre 

    action = kp*e + kd*e_diff

    print(obs)
else:
    print("finished")