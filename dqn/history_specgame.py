import numpy as np
import cfg_set

class History:
  def __init__(self, config):
    self.cnn_format = config.cnn_format

    batch_size, history_length, screen_height, screen_width = \
        config.batch_size, config.history_length, config.screen_height, config.screen_width

    #self.history = np.zeros(
    #    [history_length, screen_height, screen_width], dtype=np.float32)
    self.history = np.zeros(
      [cfg_set.num_history, 1, cfg_set.len_lane], dtype=np.int8)

  def add(self, screen):
    self.history[:-1] = self.history[1:]
    self.history[-1] = screen

  def reset(self):
    self.history *= 0

  def get(self):
    if self.cnn_format == 'NHWC':
      return np.transpose(self.history, (1, 2, 0))
      #return self.history
    else:
      return self.history
