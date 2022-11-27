

# file write 

file_write = open("sample.txt", "w")
file_write.write("this is the first line of this sample text file\n")
file_write.write("this is to be writen on the next line of the page\n")
file_write.write("i dont actually know what i can type i am just typing anything that i like\n")
file_write.write("dont know why but maybe cus am hungry or somthn :)\n ")
file_write.write("yawm chew crunch ....... crunch......\n")
file_write.write("hey 5th line what happend to you\n")
file_write.write("5th line reply 'hey there shhhhh!!!!!!!! someones trying to eat'")
file_write.close()


file_read = open("sample.txt", "r")
text = file_read.read()
print(text)
file_read.close()
