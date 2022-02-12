import subprocess

#turns all cookies into sets so order doesn't matter
def convert(s):
    L=s[2:].split("\\r\\n")
    L.pop()
    return(set(L))

#running command line arguments and extracting the raw output
def test(file,date,answer):
    output=subprocess.Popen("python most_active_cookie.py " + file + " -d "+ 
                            date, stdout=subprocess.PIPE)
    output=convert(str(output.stdout.read()))
    assert(output==answer)
    return

c1={"AtY0laUfhglK3lC7"}
c2={'SAZuXPGUrfbcn5UA', '4sMM2LxV07bPJzwf', 'fbcn5UAVanZf6UtG'}
c3={"a","b","c","d","e","f","g","h","i","j","k"}
test("cookie_log.csv","2018-12-09",c1)
test("cookie_log.csv","2018-12-08",c2)
test("cookie_log.csv","2018-12-07",{"4sMM2LxV07bPJzwf"})
test("cookie_log.csv","2018-12-06",{"no cookies were found on 2018-12-06"} )
test("cookie_log2.csv","2018-12-08",{"A","B","C","D"})
test("cookie_log2.csv","2018-12-07",{"B"})
test("cookie_log2.csv","2018-11-08",c3)
print("all test pass")