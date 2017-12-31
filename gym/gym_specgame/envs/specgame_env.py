import gym
from gym import error, spaces

class specgame_env(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self._action_set = [0,1]
        self.action_space = spaces.Discrete(len(self._action_set))
        self.lives = 10
        #print '__init__'
        pass

    def _step(self, action):
        #print '_step'
        """

        Parameters
        ----------
        action :

        Returns
        -------
        ob, reward, episode_over, info : tuple
            ob (object) :
                an environment-specific object representing your observation of
                the environment.
            reward (float) :
                amount of reward achieved by the previous action. The scale
                varies between environments, but the goal is always to increase
                your total reward.
            episode_over (bool) :
                whether it's time to reset the environment again. Most (but not
                all) tasks are divided up into well-defined episodes, and done
                being True indicates the episode has terminated. (For example,
                perhaps the pole tipped too far, or you lost your last life.)
            info (dict) :
                 diagnostic information useful for debugging. It can sometimes
                 be useful for learning (for example, it might contain the raw
                 probabilities behind the environment's last state change).
                 However, official evaluations of your agent are not allowed to
                 use this for learning.
        """
        self._take_action(action)
        #self.status = self.env.step()
        self.status = True
        reward = self._get_reward()
        #ob = self.env.getState()
        ob = []
        episode_over = self.status != True
        return ob, reward, episode_over, {}

    def _reset(self):
        print '_reset'
        pass

    def reset(self):
        print 'reset'
        pass

    def _render(self, mode='human', close=False):
        pass

    def _take_action(self, action):
        pass

    def _get_reward(self):
        """ Reward is given for XY. """
        if self.status == False:
            return 1
        elif self.status == True:
            return 2
        else:
            return 0