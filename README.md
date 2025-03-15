# image_text_to_text

1. create a virutal environment
python3 -m venv myenv
source myenv/bin/activate

2. install pytesseract via pip

pip install --upgrade pip
pip install pytesseract opencv-python numpy

3. verify installation

python3 -c "import pytesseract; print(pytesseract.get_tesseract_version())"


4. check if tesseract is installed (system wide)

tesseract --version

5. if tesseract path is not found in  python
import pytesseract

Set the path to Tesseract (check with `which tesseract`)
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

print(pytesseract.get_tesseract_version())


6. run your OCR script
python3 your_script.py


source myenv/bin/activate
