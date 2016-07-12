#uniprotmapper

A little package for running mapping requests through UniProt's online
API.

##installation
Download the .zip to your favorite directory on your local machine, `cd`
there and run the command:

```
$ python setup.py install
```

Alternatively, one can:

```
$ pip install uniprotmapper
```
##example
Here is an example:

```python
import uniprotmapper as um

mymapper = um.Mapper()
mymapper.params.update({"to":"WORMBASE_ID", 
                        "from":"ID", 
                        "organism":"6239",
                        "format":"tab"})
                        
myquery = {"query":["some gene", "some gene", "some gene", "some gene"]}
response = mymapper.get_data(myquery)

#alternatively

mymapper.params.update(myquery)
response = mymapper.get_data()
```

Have fun! :D