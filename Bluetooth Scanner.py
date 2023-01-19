import asyncio, pandas as pd, os
from bleak import BleakScanner, BleakClient
from csv import reader, writer
myList = []
newList = []
myCSV = 'BluetoothData.csv'

async def main():
    global myList, newList, myCSV
    devices = await BleakScanner.discover()
    for device in devices:
        device = str(device)
        myList.append(device)
    for key in myList:
        newList.append(key.split(': ', 1))
    for i in range(len(newList)):
        del newList[i][1::2]
    myList = flatten(newList)
    print(myList)
    if_exists(myList)
#Next Step: Create a handler for each item that appears in myList
def flatten(lis):
    flat_list = []
    # Iterate through the outer list
    for element in lis:
        if type(element) is list:
            # If the element is of type list, iterate through the sublist
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list
def if_exists(lis):
    global myList, newList, myCSV
    if os.path.exists(os.getcwd()+"\\"+myCSV):
        for element in lis:
            with reader(myCSV) as f:
                if element not in f:
                    f.write(element)
    else:
        df = pd.DataFrame(lis)
        df.to_csv(myCSV, index=False)
asyncio.run(main())
