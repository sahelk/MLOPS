# MLOPS
End-to-End ML Project

In this project we try to implement a production ready machine learning pipeline.

## git commands

# git add . 
# git commit -m message
# git push origin main

## environment setup
'''
conda create -n visa python =3.10 -y
conda activate visa
'''

Data file
https://www.kaggle.com/datasets/moro23/easyvisa-dataset?resource=download

Setting up logger and exception, so you don't need to configure them in each file

### from_root
It resolves paths relative to your project root, not relative to your current working directory.

So instead of worrying about where you launched your script from, you just use from_root to
specify your path relative to the project root.
