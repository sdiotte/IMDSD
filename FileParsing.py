#Import DAT File
with open('BATERRCT.DAT') as dat:
    contents = dat.read()
    print(contents)

#Import FMT File
with open('BATERR.FMT') as fmt:
    contents = fmt.read()
    print(contents)

#DAT to FMT Array
dat_to_fmt = []