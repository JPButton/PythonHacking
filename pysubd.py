import requests
import sys

sub_list = open("subdomains-100.txt").read() #set this as a local file on your attacking box
subs = sub_list.splitlines()

for sub in subs:
    url_to_check = f"http://{sub}.{sys.argv[1]}"

    try:
        requests.get(url_to_check)

    except requests.ConnectionError:
        pass

    else:
        print("Check this out... ", url_to_check)

#Still to do - look at input field for wordlist, look at saving output to file, look at threading for increased speed.