'''
Filter out unique e-mail ids from the string 
'''

data ="To: Micolayout OperationsHead <Micolayout.OperationsHead@axisbank.com>Cc: Manu Gowda <Manu.Gowda@axisbank.com>; saiful Hoda <saifhoda32@gmail.com>; Sandesha Poojary <Sandesha.Poojary@axisbank.com>; Micolayout Branchhead <Micolayout.Branchhead@axisbank.com>; Sanaul Hoda <sanaulhoda89@gmail.com>"
start =[]
end =[]
store =[]
final =[]

for i in range(len(data)):
    if data[i] == '@':
        start.append(i)
        
for x in start:
    end.append(data.find('>',x))
    
if len(start) == len(end):
    for i in range(len(start)):
        store.append(data[(start[i]):(end[i])])
else:
    print("Something is wrong with fetching the index values")
    
'''I extend the programme to filter out duplicate entries in the stored list'''

for mail in store:
    if mail not in final:
        final.append(mail)
        
print("The unique e-mail ids that I recieved an email from are - ",(final))
    