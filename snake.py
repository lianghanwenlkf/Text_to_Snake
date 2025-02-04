import pygame
import os
import time
import cv2
from moviepy import VideoFileClip, AudioFileClip
from tqdm import tqdm

# 贪吃蛇的路径
space_path = [(0, -3), (1, -3), (2, -3), (3, -3), (4, -3), (5, -3), (6, -3), (7, -3), (8, -3)]
a_path = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 5), (1, 6), (1, 7), (2, 7), (2, 8), (2, 9), (3, 9),
          (3, 10), (3, 11), (4, 11), (5, 11), (5, 10), (5, 9), (6, 9), (6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (8, 5),
          (8, 4), (8, 3), (7, 3), (6, 3), (5, 3), (4, 3), (3, 3), (2, 3), (1, 3), (1, 2), (2, 2), (3, 2), (4, 2),
          (5, 2), (6, 2), (7, 2), (8, 2), (8, 1), (8, 0)]
b_path = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (1, 11),
          (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (6, 10), (7, 10), (7, 9), (8, 9), (8, 8), (8, 7), (7, 7), (7, 6),
          (6, 6), (5, 6), (4, 6), (3, 6), (2, 6), (1, 6), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5),
          (7, 4), (8, 4), (8, 3), (8, 2), (7, 2), (7, 1), (6, 1), (6, 0), (5, 0), (4, 0), (3, 0), (2, 0), (1, 0)]
c_path = [(2, 0), (2, 1), (1, 1), (1, 2), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 9),
          (1, 10), (2, 10), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (7, 10), (8, 10), (8, 9), (7, 9),
          (6, 9), (6, 10), (5, 10), (4, 10), (3, 10), (3, 9), (2, 9), (2, 8), (1, 8), (1, 7), (1, 6), (1, 5), (1, 4),
          (1, 3), (2, 3), (2, 2), (3, 2), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (8, 0), (7, 0), (6, 0),
          (5, 0), (4, 0), (3, 0)]
d_path = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (1, 11),
          (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (6, 10), (7, 10), (7, 9), (8, 9), (8, 8), (8, 7), (8, 6), (8, 5),
          (8, 4), (8, 3), (8, 2), (7, 2), (7, 1), (6, 1), (6, 0), (5, 0), (4, 0), (3, 0), (2, 0), (1, 0)]
e_path = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (1, 11),
          (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (8, 10), (7, 10), (6, 10), (5, 10), (4, 10),
          (3, 10), (2, 10), (1, 10), (1, 9), (1, 8), (1, 7), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6),
          (8, 6), (8, 5), (7, 5), (6, 5), (5, 5), (4, 5), (3, 5), (2, 5), (1, 5), (1, 4), (1, 3), (1, 2), (1, 1),
          (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (8, 0), (7, 0), (6, 0), (5, 0), (4, 0), (3, 0),
          (2, 0), (1, 0), ]
f_path = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (1, 11),
          (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (8, 10), (7, 10), (6, 10), (5, 10), (4, 10),
          (3, 10), (2, 10), (1, 10), (1, 9), (1, 8), (1, 7), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6),
          (8, 6), (8, 5), (7, 5), (6, 5), (5, 5), (4, 5), (3, 5), (2, 5), (1, 5), (1, 4), (1, 3), (1, 2), (1, 1),
          (1, 0), ]
g_path = [(2, 0), (2, 1), (1, 1), (1, 2), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 9),
          (1, 10), (2, 10), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (7, 10), (8, 10), (8, 9), (7, 9),
          (6, 9), (6, 10), (5, 10), (4, 10), (3, 10), (3, 9), (2, 9), (2, 8), (1, 8), (1, 7), (1, 6), (1, 5), (1, 4),
          (1, 3), (2, 3), (2, 2), (3, 2), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (7, 4), (6, 4),
          (6, 5), (7, 5), (8, 5), (8, 4), (8, 3), (8, 2), (8, 1), (8, 0), (7, 0), (6, 0), (5, 0), (4, 0), (3, 0), ]
h_path = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (1, 11),
          (1, 10), (1, 9), (1, 8), (1, 7), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (7, 7), (7, 8),
          (7, 9), (7, 10), (7, 11), (8, 11), (8, 10), (8, 9), (8, 8), (8, 7), (8, 6), (8, 5), (8, 4), (8, 3), (8, 2),
          (8, 1), (8, 0), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (6, 5), (5, 5), (4, 5), (3, 5), (2, 5),
          (1, 5), (1, 4), (1, 3), (1, 2), (1, 1), (1, 0), ]
i_path = [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (3, 11), (4, 11),
          (4, 10), (4, 9), (4, 8), (4, 7), (4, 6), (4, 5), (4, 4), (4, 3), (4, 2), (4, 1), (4, 0), ]
j_path = [(2, 0), (2, 1), (1, 1), (1, 2), (0, 2), (0, 3), (1, 3), (2, 3), (2, 2), (3, 2), (3, 1), (4, 1), (5, 1),
          (6, 1), (6, 2), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10), (6, 10), (6, 11),
          (7, 11), (8, 11), (8, 10), (8, 9), (8, 8), (8, 7), (8, 6), (8, 5), (8, 4), (8, 3), (8, 2), (8, 1), (7, 1),
          (7, 0), (6, 0), (5, 0), (4, 0), (3, 0), ]
k_path = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (1, 11),
          (1, 10), (1, 9), (1, 8), (1, 7), (1, 6), (2, 6), (3, 6), (3, 7), (4, 7), (4, 8), (5, 8), (5, 9), (6, 9),
          (6, 10), (7, 10), (7, 11), (8, 11), (8, 10), (8, 9), (7, 9), (7, 8), (6, 8), (6, 7), (5, 7), (5, 6), (4, 6),
          (4, 5), (5, 5), (5, 4), (6, 4), (6, 3), (7, 3), (7, 2), (8, 2), (8, 1), (8, 0), (7, 0), (7, 1), (6, 1),
          (6, 2), (5, 2), (5, 3), (4, 3), (4, 4), (3, 4), (3, 5), (2, 5), (1, 5), (1, 4), (1, 3), (1, 2), (1, 1),
          (1, 0), ]
l_path = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (1, 11),
          (1, 10), (1, 9), (1, 8), (1, 7), (1, 6), (1, 5), (1, 4), (1, 3), (1, 2), (1, 1), (2, 1), (3, 1), (4, 1),
          (5, 1), (6, 1), (7, 1), (8, 1), (8, 0), (7, 0), (6, 0), (5, 0), (4, 0), (3, 0), (2, 0), (1, 0), ]
m_path = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (1, 11),
          (1, 10), (2, 10), (2, 9), (3, 9), (3, 8), (3, 7), (4, 7), (5, 7), (5, 8), (5, 9), (6, 9), (6, 10), (7, 10),
          (7, 11), (8, 11), (8, 10), (8, 9), (8, 8), (8, 7), (8, 6), (8, 5), (8, 4), (8, 3), (8, 2), (8, 1), (8, 0), ]
n_path = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (1, 11),
          (1, 10), (1, 9), (2, 9), (3, 9), (3, 8), (4, 8), (4, 7), (5, 7), (5, 6), (6, 6), (6, 5), (7, 5), (7, 6),
          (7, 7), (7, 8), (7, 9), (7, 10), (7, 11), (8, 11), (8, 10), (8, 9), (8, 8), (8, 7), (8, 6), (8, 5), (8, 4),
          (8, 3), (8, 2), (8, 1), (8, 0), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (6, 4), (5, 4), (5, 5), (4, 5),
          (4, 6), (3, 6), (3, 7), (2, 7), (2, 8), (1, 8), (1, 7), (1, 6), (1, 5), (1, 4), (1, 3), (1, 2), (1, 1),
          (1, 0), ]
o_path = [(2, 0), (2, 1), (1, 1), (1, 2), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 9),
          (1, 10), (2, 10), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (6, 10), (7, 10), (7, 9), (8, 9), (8, 8),
          (8, 7), (8, 6), (8, 5), (8, 4), (8, 3), (8, 2), (7, 2), (7, 1), (6, 1), (6, 0), (5, 0), (4, 0), (3, 0), ]
p_path = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (1, 11),
          (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (6, 10), (7, 10), (7, 9), (8, 9), (8, 8), (8, 7), (7, 7), (7, 6),
          (6, 6), (6, 5), (5, 5), (4, 5), (3, 5), (2, 5), (1, 5), (1, 4), (1, 3), (1, 2), (1, 1), (1, 0), ]
q_path = [(4, 0), (3, 0), (2, 0), (2, 1), (1, 1), (1, 2), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8),
          (0, 9), (1, 9), (1, 10), (2, 10), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (6, 10), (7, 10), (7, 9),
          (8, 9), (8, 8), (8, 7), (8, 6), (8, 5), (8, 4), (8, 3), (8, 2), (7, 2), (6, 2), (6, 3), (5, 3), (5, 4),
          (4, 4), (4, 3), (4, 2), (5, 2), (5, 1), (6, 1), (6, 0), (7, 0), (8, 0), ]
r_path = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (1, 11),
          (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (6, 10), (7, 10), (7, 9), (8, 9), (8, 8), (8, 7), (7, 7), (7, 6),
          (6, 6), (6, 5), (5, 5), (4, 5), (3, 5), (2, 5), (1, 5), (1, 4), (2, 4), (3, 4), (4, 4), (4, 3), (5, 3),
          (5, 2), (6, 2), (6, 1), (7, 1), (7, 0), (8, 0), ]
s_path = [(0, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (6, 2), (7, 2), (7, 3), (7, 4), (6, 4),
          (6, 5), (5, 5), (4, 5), (3, 5), (2, 5), (1, 5), (1, 6), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (1, 10),
          (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (8, 10), (7, 10), (6, 10), (5, 10),
          (4, 10), (3, 10), (2, 10), (2, 9), (1, 9), (1, 8), (1, 7), (2, 7), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6),
          (7, 6), (7, 5), (8, 5), (8, 4), (8, 3), (8, 2), (8, 1), (7, 1), (7, 0), (6, 0), (5, 0), (4, 0), (3, 0),
          (2, 0), (1, 0), ]
t_path = [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (2, 10), (1, 10),
          (0, 10), (0, 11), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (7, 10), (6, 10), (5, 10),
          (4, 10), (4, 9), (4, 8), (4, 7), (4, 6), (4, 5), (4, 4), (4, 3), (4, 2), (4, 1), (4, 0), ]
u_path = [(1, 0), (1, 1), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11),
          (1, 11), (1, 10), (1, 9), (1, 8), (1, 7), (1, 6), (1, 5), (1, 4), (1, 3), (1, 2), (2, 2), (2, 1), (3, 1),
          (4, 1), (5, 1), (6, 1), (6, 2), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10),
          (7, 11), (8, 11), (8, 10), (8, 9), (8, 8), (8, 7), (8, 6), (8, 5), (8, 4), (8, 3), (8, 2), (8, 1), (7, 1),
          (7, 0), (6, 0), (5, 0), (4, 0), (3, 0), (2, 0), ]
v_path = [(3, 0), (3, 1), (2, 1), (2, 2), (1, 2), (1, 3), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9),
          (0, 10), (0, 11), (1, 11), (1, 10), (1, 9), (1, 8), (1, 7), (1, 6), (1, 5), (1, 4), (2, 4), (2, 3), (3, 3),
          (3, 2), (4, 2), (5, 2), (5, 3), (6, 3), (6, 4), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10),
          (7, 11), (8, 11), (8, 10), (8, 9), (8, 8), (8, 7), (8, 6), (8, 5), (8, 4), (8, 3), (7, 3), (7, 2), (6, 2),
          (6, 1), (5, 1), (4, 1), (4, 0), (5, 0), ]
w_path = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (1, 11),
          (1, 10), (1, 9), (1, 8), (1, 7), (1, 6), (1, 5), (1, 4), (1, 3), (1, 2), (1, 1), (1, 0), (2, 0), (3, 0),
          (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (4, 10), (4, 9), (4, 8),
          (4, 7), (4, 6), (4, 5), (4, 4), (4, 3), (4, 2), (4, 1), (4, 0), (5, 0), (6, 0), (7, 0), (7, 1), (7, 2),
          (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10), (7, 11), (8, 11), (8, 10), (8, 9), (8, 8),
          (8, 7), (8, 6), (8, 5), (8, 4), (8, 3), (8, 2), (8, 1), (8, 0), ]
x_path = [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (2, 8),
          (2, 9), (1, 9), (1, 10), (0, 10), (0, 11), (1, 11), (2, 11), (2, 10), (3, 10), (3, 9), (4, 9), (5, 9),
          (5, 10), (6, 10), (6, 11), (7, 11), (8, 11), (8, 10), (7, 10), (7, 9), (6, 9), (6, 8), (5, 8), (4, 8), (4, 7),
          (4, 6), (4, 5), (4, 4), (4, 3), (5, 3), (6, 3), (6, 2), (7, 2), (7, 1), (8, 1), (8, 0), ]
y_path = [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (2, 6), (2, 7), (1, 7), (1, 8), (0, 8), (0, 9),
          (0, 10), (0, 11), (1, 11), (1, 10), (1, 9), (2, 9), (2, 8), (3, 8), (3, 7), (4, 7), (5, 7), (5, 8), (6, 8),
          (6, 9), (7, 9), (7, 10), (7, 11), (8, 11), (8, 10), (8, 9), (8, 8), (7, 8), (7, 7), (6, 7), (6, 6), (5, 6),
          (4, 6), (4, 5), (4, 4), (4, 3), (4, 2), (4, 1), (4, 0), ]
z_path = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (1, 4), (2, 4), (2, 5), (3, 5), (3, 6), (4, 6), (4, 7), (5, 7),
          (5, 8), (6, 8), (6, 9), (7, 9), (7, 10), (6, 10), (5, 10), (4, 10), (3, 10), (2, 10), (1, 10), (0, 10),
          (0, 11), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (8, 10), (8, 9), (8, 8),
          (7, 8), (7, 7), (6, 7), (6, 6), (5, 6), (5, 5), (4, 5), (4, 4), (3, 4), (3, 3), (2, 3), (2, 2), (1, 2),
          (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (8, 0), (7, 0), (6, 0), (5, 0), (4, 0),
          (3, 0), (2, 0), (1, 0), ]

# 食物位置
space_food = []
a_food = [(0, 5), (4, 11), (8, 5), (1, 3)]
b_food = [(0, 11), (8, 8), (1, 6), (8, 3)]
c_food = [(2, 0), (0, 4), (4, 11), (8, 9), (4, 10), (1, 7), (3, 1), (8, 0)]
d_food = [(0, 7), (4, 11), (8, 6), (8, 5), (5, 0)]
e_food = [(0, 11), (8, 10), (1, 8), (8, 6), (1, 1), (8, 0), ]
f_food = [(0, 11), (8, 10), (1, 8), (8, 5), ]
g_food = [(2, 0), (0, 2), (2, 11), (8, 9), (5, 10), (1, 7), (3, 1), (7, 4), (8, 0), ]
h_food = [(0, 11), (1, 6), (7, 6), (7, 11), (7, 0), (7, 5), (1, 5), ]
i_food = [(3, 11)]
j_food = [(2, 0), (0, 2), (3, 1), (7, 3), (6, 10), (7, 0), ]
k_food = [(0, 11), (1, 6), (7, 11), (4, 6), (8, 2), (2, 5), ]
l_food = [(0, 11), (1, 1), (8, 0), ]
m_food = [(0, 11), (3, 8), (7, 11), (8, 0), ]
n_food = [(0, 11), (2, 9), (6, 5), (8, 11), (7, 0), (7, 4), (1, 8), ]
o_food = [(2, 0), (0, 2), (0, 9), (4, 11), (8, 8), (8, 3), (5, 0)]
p_food = [(0, 11), (6, 11), (8, 8), (5, 5), ]
q_food = [(4, 0), (0, 2), (2, 11), (8, 9), (6, 2), (4, 4), (8, 0), ]
r_food = [(0, 11), (8, 8), (5, 5), (1, 4), (8, 0), ]
s_food = [(0, 1), (7, 3), (0, 7), (2, 11), (8, 10), (1, 8), (7, 6), (5, 0), ]
t_food = [(3, 10), (0, 11), (7, 10), ]
u_food = [(1, 0), (0, 11), (3, 1), (7, 3), (8, 11), (7, 1), ]
v_food = [(3, 0), (0, 3), (1, 11), (4, 2), (7, 5), (7, 11), (4, 0), ]
w_food = [(0, 11), (2, 0), (3, 10), (6, 0), (7, 11), ]
x_food = [(0, 1), (3, 4), (3, 8), (0, 11), (4, 9), (8, 11), (4, 8), (4, 3), ]
y_food = [(3, 6), (0, 10), (4, 7), (8, 11), (4, 6), ]
z_food = [(0, 3), (6, 9), (0, 11), (8, 10), (1, 1), (8, 0), ]


def find_path(item_str):
    if item_str == 'a':
        return a_path
    elif item_str == 'b':
        return b_path
    elif item_str == 'c':
        return c_path
    elif item_str == 'd':
        return d_path
    elif item_str == 'e':
        return e_path
    elif item_str == 'f':
        return f_path
    elif item_str == 'g':
        return g_path
    elif item_str == 'h':
        return h_path
    elif item_str == 'i':
        return i_path
    elif item_str == 'j':
        return j_path
    elif item_str == 'k':
        return k_path
    elif item_str == 'l':
        return l_path
    elif item_str == 'm':
        return m_path
    elif item_str == 'n':
        return n_path
    elif item_str == 'o':
        return o_path
    elif item_str == 'p':
        return p_path
    elif item_str == 'q':
        return q_path
    elif item_str == 'r':
        return r_path
    elif item_str == 's':
        return s_path
    elif item_str == 't':
        return t_path
    elif item_str == 'u':
        return u_path
    elif item_str == 'v':
        return v_path
    elif item_str == 'w':
        return w_path
    elif item_str == 'x':
        return x_path
    elif item_str == 'y':
        return y_path
    elif item_str == 'z':
        return z_path
    else:
        return space_path


def find_food(item_str):
    if item_str == 'a':
        return a_food
    elif item_str == 'b':
        return b_food
    elif item_str == 'c':
        return c_food
    elif item_str == 'd':
        return d_food
    elif item_str == 'e':
        return e_food
    elif item_str == 'f':
        return f_food
    elif item_str == 'g':
        return g_food
    elif item_str == 'h':
        return h_food
    elif item_str == 'i':
        return i_food
    elif item_str == 'j':
        return j_food
    elif item_str == 'k':
        return k_food
    elif item_str == 'l':
        return l_food
    elif item_str == 'm':
        return m_food
    elif item_str == 'n':
        return n_food
    elif item_str == 'o':
        return o_food
    elif item_str == 'p':
        return p_food
    elif item_str == 'q':
        return q_food
    elif item_str == 'r':
        return r_food
    elif item_str == 's':
        return s_food
    elif item_str == 't':
        return t_food
    elif item_str == 'u':
        return u_food
    elif item_str == 'v':
        return v_food
    elif item_str == 'w':
        return w_food
    elif item_str == 'x':
        return x_food
    elif item_str == 'y':
        return y_food
    elif item_str == 'z':
        return z_food
    else:
        return space_food


# 游戏主函数
def draw_snake_and_food(snake, food, screen, background_color, food_color, body_color, block_size, screen_height):
    screen.fill(background_color)

    # 绘制食物
    for food_pos in food:
        pygame.draw.rect(screen, food_color,
                         pygame.Rect(food_pos[0] * block_size, screen_height - (food_pos[1] + 1) * block_size,
                                     block_size, block_size))

    # 绘制贪吃蛇
    for segment in snake:
        pygame.draw.rect(screen, body_color,
                         pygame.Rect(segment[0] * block_size, screen_height - (segment[1] + 1) * block_size, block_size,
                                     block_size))

    pygame.display.update()


def save_image(step, output_folder, screen):
    filename = f"{output_folder}/{str(step + 1).zfill(4)}.png"
    pygame.image.save(screen, filename)

def save_video(image_folder, music_file, output_video_file):
    # 获取文件夹中所有图片的路径，并按文件名排序
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg") or img.endswith(".png")]
    images.sort()  # 根据文件名排序，如果需要按时间排序可以根据时间戳排序

    # 获取第一张图片的尺寸，假设所有图片尺寸相同
    first_image_path = os.path.join(image_folder, images[0])
    frame = cv2.imread(first_image_path)
    height, width, layers = frame.shape

    # 设置视频编写器，参数：输出文件名、编码器、帧率、尺寸
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 使用mp4编码
    fps = 15  # 设置帧率
    video_writer = cv2.VideoWriter('temp_video.mp4', fourcc, fps, (width, height))

    # 将所有图片逐帧写入视频
    for image in images:
        img_path = os.path.join(image_folder, image)
        img = cv2.imread(img_path)
        video_writer.write(img)

    # 释放视频编写器
    video_writer.release()

    # 加载视频并添加音乐
    video_clip = VideoFileClip('temp_video.mp4')
    audio = AudioFileClip(music_file)

    # 设置音频的持续时间与视频相同
    audio = audio.subclipped(0, video_clip.duration)

    # 设置音频
    video_with_audio = video_clip.with_audio(audio)

    # 输出最终视频
    video_with_audio.write_videofile(output_video_file, codec='libx264')


# 时间格式化函数，转换为时分秒
def convert_seconds_to_hms(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = seconds % 60
    return f"{hours}h {minutes}m {seconds:.4f}s"


def make_snake(lines, block_size, screen_width, screen_height, background_color, food_color, body_color, output_folder, main_i, main_len, name):
    # 初始化 Pygame
    pygame.init()
    snake_path = [(0, (len(lines) - 1) * 17), (1, (len(lines) - 1) * 17), (2, (len(lines) - 1) * 17)]
    food_positions = []
    for tt, line in enumerate(lines):
        x3 = 0
        y3 = 0
        for index, item in enumerate(line):
            modified_path = [(index * 10 + x + 3, (len(lines) - tt - 1) * 17 + y + 3) for x, y in find_path(item)]
            modified_food = [(index * 10 + x + 3, (len(lines) - tt - 1) * 17 + y + 3) for x, y in find_food(item)]
            (x0, y0) = modified_path[0]
            (x1, y1) = modified_path[-1]
            (x2, y2) = snake_path[-1]
            if item != ' ':
                for j in range(x0 - x2):
                    snake_path.append((x2 + j + 1, y0 - 3))
                for k in range(3):
                    snake_path.append((x0, y2 + k))
                for position in modified_path:
                    snake_path.append(position)
                snake_path.append((x1, y1 - 1))
                snake_path.append((x1, y1 - 2))
                snake_path.append((x1, y1 - 3))
            else:
                for j in range(x0 - x2):
                    snake_path.append((x2 + j + 1, y0))
                for position in modified_path:
                    snake_path.append(position)
            x3 = x1
            y3 = y1 - 3

            if item != ' ':
                for position in modified_food:
                    food_positions.append(position)
                food_positions.append((x1, y1 - 3))
            else:
                food_positions.append((x1, y1))

        for index in range(int(screen_width / block_size - x3)):
            snake_path.append((x3 + index, y3))
        snake_path.append((0, y3 - 17))
    for tt in range(int(screen_width / block_size)):
        snake_path.append((tt, screen_height-1))

    # 创建保存图片的文件夹
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 设置屏幕
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("贪吃蛇模拟")
    snake = snake_path[:3]  # 初始贪吃蛇的长度为3
    food = [food_positions[0]]  # 从第一个食物开始
    food_index = 1  # 下一个食物的索引
    step = 0  # 步数

    # 游戏循环
    for i in tqdm(range(3, len(snake_path)), desc=f"{main_i+1}/{main_len}:{name} is processing"):  # 从第4个位置开始走
        # 更新蛇的位置
        snake.append(snake_path[i])

        # 检查蛇是否吃到食物
        if snake[-1] == food_positions[food_index - 1]:  # 检查是否吃到当前食物
            if food_index < len(food_positions):  # 如果还有下一个食物
                food.append(food_positions[food_index])  # 加入下一个食物
                food_index += 1  # 更新食物索引

        # 绘制并保存当前状态
        draw_snake_and_food(snake, food, screen, background_color, food_color, body_color, block_size, screen_height)
        save_image(step, output_folder, screen)

        # 增加步数
        step += 1

        # 事件处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

    pygame.quit()


def main():
    name_list = [
        ['liu','wang'],
        ['huang','li jin'],
        ['fang','wei']
    ]
    block_size = 30
    background_color = (255, 255, 255)
    body_color = (0, 0, 0)
    food_color = (255, 0, 0)
    output_folder = "output"
    music_file = 'STAYC - Bubble.mp3'

    start_time = time.time()
    for i, name in enumerate(name_list):
        loop_start_time = time.time()
        line_1 = name[0]
        line_2 = name[1]
        line_3 = 'happy'
        line_4 = 'the year'
        line_5 = 'of snake'

        image_folder = f'{output_folder}/{line_1} {line_2}/image'
        output_video_file = f'{output_folder}/{line_1} {line_2}.mp4'

        lines = [line_1, line_2, line_3, line_4, line_5]

        # 游戏窗口设置（宽度和高度）
        screen_width = (10 * max(len(line_1), len(line_2), len(line_3), len(line_4), len(line_5)) + 6) * block_size
        screen_height = 17 * block_size * len(lines)

        make_snake(lines, block_size, screen_width, screen_height, background_color, food_color, body_color, image_folder, i, len(name_list), f'{line_1} {line_2}')
        save_video(image_folder, music_file, output_video_file)

        loop_end_time = time.time()
        loop_duration = loop_end_time - loop_start_time
        print(f"Loop {i + 1}/{len(name_list)} took {convert_seconds_to_hms(loop_duration)}")
    end_time = time.time()
    total_duration = end_time - start_time
    print(f"Total time for execution: {convert_seconds_to_hms(total_duration)}")


if __name__ == "__main__":
    main()
