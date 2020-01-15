import censys.certificates
import censys.ipv4
import censys

def search_domain_ipv4(domain,api_id,api_secret):
    try:
        api = censys.ipv4.CensysIPv4(api_id=api_id, api_secret=api_secret)
        results = censys.ipv4.CensysIPv4.search(api,domain)
    except Exception as ex:
        print("error : ",ex)
    return results

def convert(results):
    filtered_ = []
    cnt = 0
    for result in results:
        f = []
        cnt += 1
        f.append(result['ip'])
        a = ""
        for i in result['protocols']:
            a += i+","    
        f.append(a[:-1])
        filtered_.extend(f)
        if cnt == 1000:
            break
    return filtered_,cnt
def nonconvert(results):
    non_filtered = []
    cnt = 0
    for result in results:
        cnt += 1
        non_filtered.extend(result)
        if cnt == 1000:
            break

