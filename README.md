# mrpen_replica
A replica to 3rd place project in EEESE18 (Electric and Electronic Engineering Students Exhibition 2018) called mr.pen

The idea of this project is to make a pen that can detect which letter you wrote with just the motion
the components of this project is:
  1-  Arduino uno
  2-  Accelerometer/gyroscope GY-521
  3-  Push button
  4-  20K ohm resistor
  5-  Lots of wires
  6-  Breadboard
 
In the arduino side when the button is pressed we simply write the readings in the serial monitor
In the python side we just collect the readings and store them in the training set
Then with the readings of GY-521 we trained a simple multi-layers perceptrons to classify which letter is written using Tensorflow/Keras
