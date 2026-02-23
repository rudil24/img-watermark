import os
from PIL import Image
from watermarker import add_text_watermark, add_logo_watermark

def setup_test_images():
    # Create a dummy image
    test_img = Image.new('RGB', (500, 500), color='red')
    test_img.save('test_input.jpg')
    
    # Create a dummy logo
    test_logo = Image.new('RGBA', (100, 100), color=(255, 255, 255, 128))
    test_logo.save('test_logo.png')

def teardown_test_images():
    files_to_remove = ['test_input.jpg', 'test_logo.png', 'test_output_text.jpg', 'test_output_logo.jpg']
    for f in files_to_remove:
        if os.path.exists(f):
            os.remove(f)

def test_add_text_watermark():
    setup_test_images()
    try:
        result = add_text_watermark('test_input.jpg', 'Test Watermark', 'test_output_text.jpg', compress=False)
        assert result is True
        assert os.path.exists('test_output_text.jpg')
        
        # Verify it can be opened
        with Image.open('test_output_text.jpg') as img:
            assert img.size == (500, 500)
    finally:
        teardown_test_images()

def test_add_logo_watermark():
    setup_test_images()
    try:
        result = add_logo_watermark('test_input.jpg', 'test_logo.png', 'test_output_logo.jpg', compress=True)
        assert result is True
        assert os.path.exists('test_output_logo.jpg')
        
        with Image.open('test_output_logo.jpg') as img:
            assert img.size == (500, 500)
    finally:
        teardown_test_images()
