data1 = ['Notes', 'Office', 'Public', 'Private', 'Classified', 'General', 'Excel File.doc']
data2 = ['notes', 'office', 'public', 'private', 'classified', 'general', 'excelFile']

data1 = str(data1).replace(' ', '').replace('doc', '').replace('.', '').lower()
print(data1)
data2 = str(data2).replace(' ', '').lower()
print(data2)
assert data1 == data2
