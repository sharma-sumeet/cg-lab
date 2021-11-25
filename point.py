{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Point:\n",
    "    \"\"\" Point Class \"\"\"\n",
    " \n",
    "    def __init__(self, xcoord, ycoord):\n",
    "        self.x = xcoord\n",
    "        self.y = ycoord\n",
    "        \n",
    "    def __init__(self,tup):\n",
    "        self.x=tup[0]\n",
    "        self.y=tup[1]\n",
    " \n",
    "    @classmethod\n",
    "    def input_point(point):\n",
    "        \"\"\" Takes X-Coord and Y-Coord from user to form a point \"\"\"\n",
    "        return point(\n",
    "            int(input('  X-Coord: ')),\n",
    "            int(input('  Y-Coord: ')),\n",
    "        )\n",
    " \n",
    "    def __str__(self):\n",
    "        \"\"\" Displays point's coordinates \"\"\"\n",
    "        return \"(\" + str(self.x) + \", \" + str(self.y) + \")\""
   ]
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
