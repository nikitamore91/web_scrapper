import requests, webbrowser, bs4,os

search_string = input ('Enter keyword to search')
numOfimages = int(input('Enter number of images you want to download'))
print('Googling...')

if not os.path.exists('google_images'):
    os.makedirs('google_images')

url = 'http://google.com/search?q=' + ''.join(search_string) + \
'&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi76bzwupzUAhUBN48KHYSNCE8Q_AUICigB&biw=959&bih=678'

res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "lxml")

imageElem = soup.select('img')
#print imageElem
numOpen = min(numOfimages, len(imageElem))
for i in range(numOpen):
    imageUrl =  imageElem[i].get('src')
    # Download the image.
    #print('Downloading image %s...' % (imageUrl))
    res = requests.get(imageUrl)
    res.raise_for_status()
    imageFolder = open(os.path.join('google_images', os.path.basename(imageUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFolder.write(chunk)
    imageFolder.close()
print ('Done')
