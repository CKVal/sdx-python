from subprocess import Popen, PIPE

#execute command

process = Popen(" ".join(["ping","8.8.8.8","-c"  "2"]),
                shell=True, stdout=PIPE, stderr=PIPE)

#read STDOUT
print(process.stdout.read())

#wait for child process
rc=process.wait()
print("exit code:{}".format(rc))

#read STEDD

print("error:{}".format(process.stderr.read()))