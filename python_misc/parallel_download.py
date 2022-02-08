from itertools import repeat
import concurrent.futures
import wget

## define download function
def download_image(image_url, output_dir):
    try:
        wget.download(image_url, out = output_dir)
    except:
        print(f'Issue while downloading {image_url}')

## define output dir and list of urls to download images   
IMG_DIR = 'temp' ### output dir
urls_sample_new =  [] ### list of urls

## download images -------------  
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, urls_sample_new, repeat(IMG_DIR))