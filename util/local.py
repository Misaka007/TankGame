from enum import Enum
# 每一块的大小
BLOCK_SIZE = 60
# 游戏窗口宽度
WINDOW_WIDTH = 13*BLOCK_SIZE
# 游戏窗口高度
WINDOW_HEIGHT = 13*BLOCK_SIZE

# 定义方向枚举
class Direction(Enum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3