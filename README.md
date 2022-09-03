# rename-regex
A Command Line Tool for Rename Files by Regex

## run
```bash
python rere.py
```
or (Linux only)
```bash
chmod +x rere.py
./rere
```
or (Windows only)
```cmd
rere
```

## usage
`usage: rere.py [-h] [-f] [-r] src dest`
```
  -h, --help       show this help message and exit
  -f, --force      never prompt before rename
  -r, --recursive  rename files in subdirs
```

## note
1. please add quotation marks around \<src\> and \<dest\>

   `rere "(.*)" "\1" ` - correct  
   `rere .* "\1"`      - wrong

2. group are repalced with `\{NUMBER}`
  
    e.g. for `1-5a.cpp` change to `a.1.5.cpp`
    
    run `rere "(.)-(.)(.)\.cpp" "\3.\1.\2.cpp"`

3. press enter will also be considered as `y` in `(y/n)` 

## example
```
a.cpp
b.cpp
c.cpp
d.cpp
e.cpp
```
after runing  `rere "([a-d])\.cpp" "\1.cxx" `
```
a.cxx
b.cxx
c.cxx
d.cxx
e.cpp
```
