# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 23:00:37 2020

@author: Dillo
"""

import streamlit as st
import random
import time
import cv2
import matplotlib.pyplot as plt

st.title('Dillon\'s Room Perspective Changer')


im_path = 'F:/RoomRotate/Images/'

d2 = cv2.imread(im_path + 'dining2.jpg')
d2_depth = cv2.imread(im_path + 'dining2_depth.png')

st.image(d2)
st.image(d2_depth)


progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()

k = random.sample( range(20,75),1)[0]

for i in range(1,k):
    k = random.sample( range(20,75),1)[0]
    status_text.text('Probability Dillon actually finishes \nthis project is: {}%'.format(i))
    progress_bar.progress(i)
    sl = random.sample([0.01, 0.09, 0.2, 0.5, 1], 1)[0]
    time.sleep(sl)
    
    
progress_bar.empty()

st.button("Re-run")

