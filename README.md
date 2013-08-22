# CombineAndMinify

A Python script that combines JavaScript files into one large file and creates a master and minified version. Lets the developer work with multiple files and build one large include for the browser.

### Created

2012

### Version

1.0

## Release Notes

##### 1.0 (2012)

- Initial build

## Usage

1. Clone CombineAndMinify into an existing project
2. Add to .gitignore to exclude (GitHub)
3. Edit paths in process.py
4. Add files to source in files.txt.
5. Run `$ python process.py` to combine and minify

process.py

```python
fileList = 'files.txt'
jsPath = '../client/public/js/'
jsMaster = jsPath + 'master.js'
jsMinify = jsPath + 'minify.js'
```

files.txt

```txt
################ Comments Are Ignored ################
externaljs.js
externaljs2.js
```

Include master.js or minify.js in your project. All source files can be left separate and intact. After editing an include just run process.py again to rip off a new minify and master.

## License

GNU GENERAL PUBLIC LICENSE Version 2, June 1991