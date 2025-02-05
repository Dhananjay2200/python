import argparse
import requests

def download_file(url,local_time):
    if local_time is None:
        local_time = url.split('/')[-1]

    with requests.get(url,stream = True) as r:
        r.raise_for_status()
        with open(local_time,'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                #if you have chunk encoded response uncomment if and set chunk_size parameter to none
                #if chunk:
                f.write(chunk)
    return local_time

parser = argparse.ArgumentParser()

# Add command linearguments
parser.add_argument("url",help = "Url of the file to download")
# parser.add_argument("output",help = "by which name do you want to save your file ")
parser.add_argument("-o","--output",type=str, help = "Name of file",default = None)

#parser argument
args = parser.parse_args()

#use argument in code 
print(args.url)
print(args.output,type(args.output))
download_file(args.url,args.output)


# for download command "python 85_command_line_utility.py https://imagej.net/images/2D_Gel.jpg -o dk.jpg"