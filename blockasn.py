#!/usr/bin/python3
import requests,json
import os,sys,subprocess

def get_IPlist(asn="9009"):
    v4=[]
    v6=[]
    request_headers={"Host":"stat.ripe.net",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0",
        "Connection": "keep-alive"}

    print("<> Requesting IP prefix data for ASN "+asn+" from stat.ripe.net...")
    req=requests.get("https://stat.ripe.net/data/ris-prefixes/data.json?resource="+asn+"&list_prefixes=true",headers=request_headers)
    resp=json.loads(req.text)
    if  "data" in resp and "prefixes" in resp["data"]:
        if "v4" in resp["data"]["prefixes"]:
            if "originating" in resp["data"]["prefixes"]["v4"]:
                print("[+] Adding "+str(len(resp["data"]["prefixes"]["v4"]["originating"]))+" IPv4 prefixes originated by ASN "+asn)
                for prefix in resp["data"]["prefixes"]["v4"]["originating"]:
                    v4.append(prefix)

        if "v4" in resp["data"]["prefixes"]:
            if "transitting" in resp["data"]["prefixes"]["v4"]:
                print("[+] Adding "+str(len(resp["data"]["prefixes"]["v4"]["transitting"]))+" IPv4 prefixes transitting ASN "+asn)
                for prefix in resp["data"]["prefixes"]["v4"]["transitting"]:
                    v4.append(prefix)


        if "v6" in resp["data"]["prefixes"]:
            if "originating" in resp["data"]["prefixes"]["v6"]:
                print("[+] Adding "+str(len(resp["data"]["prefixes"]["v6"]["originating"]))+" IPv6 prefixes originated by ASN "+asn)
                for prefix in resp["data"]["prefixes"]["v6"]["originating"]:
                    v6.append(prefix)

            if "transitting" in resp["data"]["prefixes"]["v6"]:
                print("[+] Adding "+str(len(resp["data"]["prefixes"]["v6"]["transitting"]))+" IPv6 prefixes transitting ASN "+asn)
                for prefix in resp["data"]["prefixes"]["v6"]["transitting"]:
                    v6.append(prefix)

    return v4,v6

def blockips(iplist, ipver, asn):
    if ipver == 6:
        ipt="/sbin/ip6tables"
    else:
        ipt="/sbin/iptables"
    print("<> Using: "+ipt)
    print("<> Cleanup existing chain: block-as"+asn)
    subprocess.call([ipt,"-D","INPUT","-j","block-as"+asn])
    subprocess.call([ipt,"-F","block-as"+asn])
    subprocess.call([ipt,"-X","block-as"+asn])
    print("<> Create new chain: block-as"+asn)
    subprocess.call([ipt,"-N","block-as"+asn])

    print("<> Adding IP "+str(len(iplist))+" addresses/ranges")
    for ip in iplist:
        subprocess.call([ipt,"-A","block-as"+asn,"-s",ip,"-j","REJECT"])

    print("<> Finishing chain")
    subprocess.call([ipt,"-A","block-as"+asn,"-j","RETURN"])
    print("<> Add INPUT filter")
    subprocess.call([ipt,"-I","INPUT","-j","block-as"+asn])

def main():
    if len(sys.argv)<2:
        print("Usage: blockasn.py <asn>")
        sys.exit(1)
    else:
        v4,v6=get_IPlist(sys.argv[1])
        blockips(v4, 4, sys.argv[1])
        blockips(v6, 6, sys.argv[1])
    sys.exit(0)

if __name__ == "__main__":
    main()
