#!/usr/bin/python
# 

import gym

env = gym.make('MsPacman-v0')
print (env.action_space)
print (env.observation_space)
# env.monitor.start('/tmp/atari-experiment')
# env = gym.wrappers.Monitor(env, '/tmp/atari-experiment')
# env.reset()

for episode in range(100):
    observation = env.reset()
    total_reward = 0;
    for time in range(1000):
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        total_reward = total_reward + reward
        if done:
            print ("Episode {}:".format(episode))
            print ("  completed in {} steps".format(time+1))
            print ("  total reward was {}".format(total_reward))
            break

env.monitor.close()
