#Import DAT File
with open('BATERRCT.DAT') as dat:
    contents = dat.read()
    print(contents)

#Import FMT File
with open('BATERR.FMT') as fmt:
    contents = fmt.read()
    print(contents)

#Import text files
def source():
    
with open (source) as source:
    contents = source.read()
    print (contents)
#add code: if file is fmt, remove #'s and anything after...perhaps have it import the old fields and place under new fields on header. Maybe with acronym for system in the front with dot or dash

    
#DAT to FMT Array
#dat_to_fmt = []