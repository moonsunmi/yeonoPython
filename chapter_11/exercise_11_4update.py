def cp(src, dst):

    with open(src, 'r') as read_file, open(dst, 'w') as write_file:
        write_file.write(read_file.read())


cp('original.txt', 'clone.txt')