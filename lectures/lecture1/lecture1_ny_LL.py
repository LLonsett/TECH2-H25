{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2d067db8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Max. value is 7 located at index 3\n"
     ]
    },
    {
     "ename": "ValueError",
     "evalue": "attempt to get argmax of an empty sequence",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mValueError\u001b[39m                                Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[1]\u001b[39m\u001b[32m, line 57\u001b[39m\n\u001b[32m     52\u001b[39m     imax = argmax([])\n\u001b[32m     55\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[34m__name__\u001b[39m == \u001b[33m'\u001b[39m\u001b[33m__main__\u001b[39m\u001b[33m'\u001b[39m:\n\u001b[32m     56\u001b[39m     \u001b[38;5;66;03m# Run the main function if this script is executed\u001b[39;00m\n\u001b[32m---> \u001b[39m\u001b[32m57\u001b[39m     \u001b[43mmain\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[1]\u001b[39m\u001b[32m, line 52\u001b[39m, in \u001b[36mmain\u001b[39m\u001b[34m()\u001b[39m\n\u001b[32m     49\u001b[39m \u001b[38;5;28mprint\u001b[39m(\u001b[33mf\u001b[39m\u001b[33m'\u001b[39m\u001b[33mMax. value is \u001b[39m\u001b[38;5;132;01m{\u001b[39;00mvmax\u001b[38;5;132;01m}\u001b[39;00m\u001b[33m located at index \u001b[39m\u001b[38;5;132;01m{\u001b[39;00mimax\u001b[38;5;132;01m}\u001b[39;00m\u001b[33m'\u001b[39m)\n\u001b[32m     51\u001b[39m \u001b[38;5;66;03m# Check that function raises an error for empty sequences\u001b[39;00m\n\u001b[32m---> \u001b[39m\u001b[32m52\u001b[39m imax = \u001b[43margmax\u001b[49m\u001b[43m(\u001b[49m\u001b[43m[\u001b[49m\u001b[43m]\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[1]\u001b[39m\u001b[32m, line 19\u001b[39m, in \u001b[36margmax\u001b[39m\u001b[34m(values)\u001b[39m\n\u001b[32m     17\u001b[39m \u001b[38;5;66;03m# Check that the sequence is not empty\u001b[39;00m\n\u001b[32m     18\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m N == \u001b[32m0\u001b[39m:\n\u001b[32m---> \u001b[39m\u001b[32m19\u001b[39m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\u001b[33m'\u001b[39m\u001b[33mattempt to get argmax of an empty sequence\u001b[39m\u001b[33m'\u001b[39m)\n\u001b[32m     21\u001b[39m \u001b[38;5;66;03m# Initialise the maximum location and value\u001b[39;00m\n\u001b[32m     22\u001b[39m imax = \u001b[32m0\u001b[39m\n",
      "\u001b[31mValueError\u001b[39m: attempt to get argmax of an empty sequence"
     ]
    }
   ],
   "source": [
    "def argmax(values):\n",
    "    \"\"\"\n",
    "    Return the location and value of the maximum contained in a given sequence.\n",
    "\n",
    "    Parameters\n",
    "    ----------\n",
    "    values : Sequence of numbers\n",
    "\n",
    "    Returns\n",
    "    -------\n",
    "    imax : int\n",
    "        Location of the maximum\n",
    "    \"\"\"\n",
    "\n",
    "    N = len(values)\n",
    "\n",
    "    # Check that the sequence is not empty\n",
    "    if N == 0:\n",
    "        raise ValueError('attempt to get argmax of an empty sequence')\n",
    "\n",
    "    # Initialise the maximum location and value\n",
    "    imax = 0\n",
    "    vmax = values[0]\n",
    "\n",
    "    # Loop through the sequence to find the maximum\n",
    "    for i in range(1, N):\n",
    "        v = values[i]\n",
    "        # If the current value is greater than the maximum found so far,\n",
    "        # update the maximum location and value\n",
    "        if v > vmax:\n",
    "            imax = i\n",
    "            vmax = v\n",
    "\n",
    "    return imax\n",
    "\n",
    "\n",
    "def main():\n",
    "    \"\"\"\n",
    "    Main function to test argmax().\n",
    "    \"\"\"\n",
    "\n",
    "    # Create list of values to test argmax()\n",
    "    values = [2, 3, -1, 7, 4]\n",
    "\n",
    "    # Use argmax() to locate the maximum\n",
    "    imax = argmax(values)\n",
    "    # Print the maximum value and its index\n",
    "    vmax = values[imax]\n",
    "    print(f'Max. value is {vmax} located at index {imax}')\n",
    "\n",
    "    # Check that function raises an error for empty sequences\n",
    "    imax = argmax([])\n",
    "\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    # Run the main function if this script is executed\n",
    "    main()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "TECH2",
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
