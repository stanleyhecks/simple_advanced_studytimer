# simple_advanced_studytimer
Study timer that automatically starts/stops when you study depending on your studying status. Made with Python and Teachable Machine

# What do I need to try this?
You need a webcam, Teachable Machine, Python and your brain.

# How do I do this?
First of all, you need an image model.
Go to https://teachablemachine.withgoogle.com/ and select image project and then standard image model.
![image](https://github.com/stanleyhecks/simple_advanced_studytimer/assets/65809697/9f0cde53-9203-497f-92f1-382c87ee06f3)
You will see a page like this. In Class1, record yourself studying and meanwhile in Class2, record yourself not studying. Capture more than 500 samples in both classes. Once you finish capturing, click train model button and after that, export your model in the format of TensorFlow Keras. Download your model and remember the path.
Download the .py file from the repository and paste it onto IDLE. We will be using OpenCV, TensorFlow and numpy, so install them in advance.
Then paste your model's file path onto 'YOUR_KERAS_MODEL_PATH' in the .py file.
Once you complete the steps above, just click F5 and enjoy.

# Just two pieces of examples of running program
![image](https://github.com/stanleyhecks/simple_advanced_studytimer/assets/65809697/15801c6e-c148-4ac8-adab-f7aa4e460413)
![image](https://github.com/stanleyhecks/simple_advanced_studytimer/assets/65809697/83ee3e80-27d9-4b8b-8b88-c71b6d4dc591)

