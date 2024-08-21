# AugmentedRealitySL

This project demonstrates how to create an interactive system that captures spoken words, analyzes the text, and overlays corresponding sign language gestures on a live video feed. It utilizes speech recognition to convert spoken language into text, natural language processing (NLP) to analyze the text, and computer vision to detect faces and display sign language gestures.

### Features

- **Speech Recognition**: Converts spoken words into text using Google's Speech Recognition API.
- **Text Analysis**: Analyzes the text to identify key words and provides insights such as common words, part-of-speech tags, and named entities using the NLTK library.
- **Face Detection and Gesture Display**: Uses OpenCV for real-time face detection and overlays sign language gesture images on a live video feed from the webcam.

### Requirements

- Python 3.x
- OpenCV
- SpeechRecognition
- NLTK

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/sign-language-gesture-display.git
   cd sign-language-gesture-display
   ```

2. **Install Dependencies**

   Ensure you have `pip` installed, then run:

   ```bash
   pip install opencv-python-headless speechrecognition nltk
   ```

3. **Download Haar Cascade XML**

   Download the Haar Cascade XML file for face detection from [OpenCV GitHub](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml) and place it in the `haarcascades` directory.

4. **Prepare Images**

   Place your sign language gesture images in the `images` directory. Ensure the paths in the `text_to_sign` dictionary in `main.py` correspond to these images.

### Usage

1. **Run the Script**

   Execute the script from your project directory:

   ```bash
   python main.py
   ```

2. **Interact**

   Speak into your microphone. The system will analyze the spoken text, and if it matches any of the predefined words, it will overlay the corresponding sign language gesture on the live video feed.

### Project Structure

```
sign_language_project/
│
├── images/
│   ├── path_to_hello_sign_image.png
│   └── path_to_world_sign_image.png
│
├── haarcascades/
│   └── haarcascade_frontalface_default.xml
│
├── main.py
└── README.md
```

### Notes

- Ensure your microphone and webcam are properly configured.
- Adjust image paths and dictionary entries in `main.py` to match your setup.

### Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to adjust any sections to better fit your project or add any additional details you think are necessary!
