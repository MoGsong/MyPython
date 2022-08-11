import optparse
parse = optparse.OptionParser()
parse.usage = "web_brute.py -u url -user user_file -pass pass_file -t num"
parse.add_option("-s","--site",dest="website",help="website test",action="store",type="string",metavar="URL")
parse.add_option("-u","--user_file",dest="userfile",help="username from file",action="store",type="string",metavar="USERFILE")
parse.add_option("--pass","--pass_file",dest="passfile",help="passname from file",action="store",type="string",metavar="PASSFILE")
parse.add_option("-t","--thread",help="number of thread",dest="thread",action="store",type="string",metavar="THREADS")
(options, args) = parse.parse_args()
print(options.website)