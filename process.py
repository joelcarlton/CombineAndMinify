#!/usr/bin/python

# FILE MANAGEMENT
import os.path
# SHELL
#import subprocess
# POST
import urllib
import urllib2
# TIME
import time

# Clear screen for new run
#subprocess.Popen('cmd')

# Start script
print '\nInitiating Minification'
start = time.time()

# Files
fileList = 'files.txt'
inPath = '../client/public/js/'
outPath = '../client/private/js/'
jsMaster = outPath + 'master.js'
jsMinify = outPath + 'master.min.js'

# Read in order file
order = open(fileList, 'r')

# Create Array
orderArray = []
# Get List of files
for line in order:
    if not '#' in line:
        # Remove newlines
        if '\r' in line:
            line = line.replace('\r', '')
        if '\n' in line:
            line = line.replace('\n', '')
        # Add to array
        orderArray.append(line)

# Create Array
masterArray = []
# Get contents of files
for entry in orderArray:
    file = open(inPath + entry, 'r')
    masterArray.append(file.read())

# Check for old master then remove
if os.path.isfile(jsMaster):
    print 'Trashing Old Master File'
    os.remove(jsMaster)

# Create new master file
master = open(jsMaster, 'a')
# Add contents of files to master
for i in masterArray:
    master.write(i)

# Close master and reopen for reading
master.close()
master = open(jsMaster, 'r')

# Set up POST
print 'Sending JavaScript for Minification'
url = 'http://marijnhaverbeke.nl/uglifyjs'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'js_code': master.read()}
headers = {'User-Agent': user_agent}
data = urllib.urlencode(values)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)

# Add minified output to minify file
print 'Saving Minified Version'
minify = open(jsMinify, 'w')
minify.write(response.read())

# Clean up
order.close()
master.close()
minify.close()

# Calculate and display run time
end = time.time()
time = round(end - start, 2)
print '\nOperation Compleated in ' + str(time) + ' seconds.\n'
