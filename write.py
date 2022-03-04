# with open('write_file.txt' ,'w') as x:
#     x.write("shruti")
    


lines_data=['rashi\n','katiyar\n']
with open('write_file.txt' ,'w') as x:
     x.write("shruti\n")
     x.writelines(lines_data)

