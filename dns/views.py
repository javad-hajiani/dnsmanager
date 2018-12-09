from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from . import vars
import json
import re
from os import path


def index(request):
    html: str = '<center><h1>Dns Manager</h1><br>'
    html += '<h3> You can use below instruction to work with your bind9</h3><br>'
    html += '<p><h2>Show Domains :</h2>'
    html += '<code><a href="{}domains/">http://{}/domains/</a></code></p>'.format(request.path, request.get_host())
    html += '<p><h2>Add Domains :</h2>'
    html += '<code><a href="{}adddomain/example.com/1.1.1.1/192.168.1.1/">http://{}/adddomain/[DomainName]/[PublicAddress]/[LocalAddress]/</a></code></p>'.format(
        request.path, request.get_host())
    html += '<p><h2>Show Records :</h2>'
    html += '<code><a href="{}showrecords/example.com/">http://{}/showrecords/[DomainName]/</a></code></p>'.format(
        request.path, request.get_host())
    html += '<p><h2>Add Records :</h2>'
    html += '<code><a href="{}addrecord/example.com/local/A/www/1.1.1.1">http://{}/addrecord/[DomainName]/[local|internet]/[RecordType]/[Key]/[Value]/</a></code></p>'.format(
        request.path, request.get_host())
    html += '<p><h2>Delete Records :</h2>'
    html += '<code><a href="{}deleterecord/example.com/www/A/">http://{}/deleterecord/[DomainName]/[RecordName]/[RecordType]/</a></code></p>'.format(
        request.path, request.get_host())
    html += '<p><h2>Refresh DNS :</h2>'
    html += '<code><a href="{}refresh/">http://{}/refresh/[DomainName]/</a></code></p>'.format(request.path,
                                                                                               request.get_host())
    html += '<br><br><br><small>Copyright <a href="http://hajiani.org">Javad Hajiani</a></small>'
    html += '<br></center>'
    return HttpResponse(html)


def showdomains(request):
    response = []
    for line in open(vars.externalzones, 'r'):
        if 'zone' in line:
            data = {"name": line.split('"')[1]}
            response.append(data)
    return JsonResponse(response, safe=False)


def adddomains(request, domain, publicip, privateip):
    response = {"status": "Ok", "variables": domain + ' ' + publicip + ' ' + privateip}
    return JsonResponse(response)


def showrecords(request, domain):
    regex = r"file \"[\/a-zA-Z-_0-9.]*"
    regex2 = r"\"[\/a-zA-Z-_0-9.]*"
    zonefile = ""
    response = []
    response = []
    if not path.isfile(vars.externalzones):
        return JsonResponse('{"Status":"ZoneConfig Not Found"}')
        exit(1)
    for line in open(vars.externalzones, 'r'):
        if domain in line:
            matched = re.search(regex, line)
            if matched:
                secondsearch = re.search(regex2, matched[0])
                zonefile = secondsearch[0].replace('"', '')
            else:
                zonefile = "Record File not found in zone line"
    if not path.isfile(zonefile):
        response={"Status":"ZoneFile Not Found"}
        return JsonResponse(response)
    with open(zonefile, 'r') as filereader:
        zone = filereader.readlines()
    for records in zone:
        record = re.split(r'(\t|\s+)', records.strip())
        q = [i for i in record if i.strip()]
        if len(q) == 4:
            data = {"recordname": q[0], "RecordClass": q[1], "RecordType": q[2], "RecordValue": q[3]}
        elif len(q) == 3:
            data = {"recordname": q[0], "RecordType": q[1], "RecordValue": q[2]}
        else:
            continue
        response.append(data)
    if len(response) == 0:
        response.append('{"Status": "No Record Found!!!"}')
    return JsonResponse(response, safe=False)


def addrecord(request, domain, zonetype, recordtype, key, value):
    response = {"status": "Ok", "variables": domain + ' ' + recordtype + ' ' + key + ' ' + value}
    return JsonResponse(response)


def deleterecord(request, domain, recordname, recordtype):
    response = {"status": "Ok", "variables": domain + ' ' + recordname + ' ' + recordtype}
    return JsonResponse(response)


def refresh(request, domain):
    response = {"status": "Ok"}
    return JsonResponse(response)
