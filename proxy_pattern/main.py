from Homework_18.proxy_pattern.proxy_txt_reader_writer import TxtProxyReaderWriter
from Homework_18.proxy_pattern.txt_reader import TxtReader
from Homework_18.proxy_pattern.txt_writer import TxtWriter
from random import randint

txt_reader = TxtReader('users.txt')
txt_writer = TxtWriter('users.txt')
proxy_reader_writer = TxtProxyReaderWriter(txt_writer, txt_reader)

proxy_reader_writer.write_file(f'{"test_" + str(randint(1, 1000000000))}\n')
print(proxy_reader_writer.read_file())


