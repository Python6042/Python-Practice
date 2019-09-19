

{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Introduction to Numpy\n",
    "What is Numpy?\n",
    "\n",
    "Numpy is a Mutlidimentional array proceesing package. It  is an Open source libray available python. \n",
    "It is used in mathimatical and scientific computic and highly used in Data science.\n",
    "\n",
    "What are the advances of Numpy over the list ?\n",
    "\n",
    "Numpy data structures perform better in:\n",
    "Size - Numpy data structures take up less space. Bttter utilization of cache\n",
    "Performance - they have a need for speed and are faster than lists\n",
    "Functionality - SciPy and NumPy have optimized functions such as linear algebra operations built \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: numpy in c:\\users\\admin\\anaconda3\\lib\\site-packages (1.16.4)\n"
     ]
    }
   ],
   "source": [
    "# How to install Numpy\n",
    "\n",
    "!pip install numpy\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting numpy\n",
      "  Downloading https://files.pythonhosted.org/packages/bd/51/7df1a3858ff0465f760b482514f1292836f8be08d84aba411b48dda72fa9/numpy-1.17.2-cp37-cp37m-win_amd64.whl (12.8MB)\n",
      "Installing collected packages: numpy\n",
      "  Found existing installation: numpy 1.16.4\n",
      "    Uninstalling numpy-1.16.4:\n",
      "      Successfully uninstalled numpy-1.16.4\n",
      "Successfully installed numpy-1.17.2\n"
     ]
    }
   ],
   "source": [
    "# how to upgrade Numpy\n",
    "!pip install numpy --upgrade"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3]\n"
     ]
    }
   ],
   "source": [
    "# How to work on Numpy arrays. To work on Numpy import Numpy library/package using the below stmt\n",
    "\n",
    "import numpy as np # np is alias name given to numpy\n",
    "\n",
    "# Example of one dimentional array\n",
    "a=np.array([1,2,3])\n",
    "print(a)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2 3]\n",
      " [4 5 6]]\n"
     ]
    }
   ],
   "source": [
    "# Example of two dimentional array\n",
    "b=np.array([[1,2,3],[4,5,6]])\n",
    "print(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Self learnt: Not coved in the class\n",
    "# How to find dimention of array \n",
    "a.ndim"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b.ndim"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(2, 3)"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# how to find shape of the array\n",
    "b.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}