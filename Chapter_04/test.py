try:
    data=open('misiing.txt')
    print(data.readline(), end='')
except FileNotFoundError as error:
    print('File Erorr' + str(error))
finally:
    if 'data' in locals():
        data.close()
