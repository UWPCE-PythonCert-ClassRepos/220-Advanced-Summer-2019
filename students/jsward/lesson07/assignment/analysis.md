In my first attempt at threading I tried threading each insert_one() operation, which actually slowed the program
significantly.  After realizing my mistake and re-writing the code to thread by input file, rather than record
I was able to achieve significant performance gains, even with just two files.  Incorporating threading decreased 
total run time from 7.9 to 5.2 seconds.
