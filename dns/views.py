from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
def index(request):
    html: str = '<center><h1>Dns Manager</h1><br>'
    html += '<h3> You can use below instruction to work with your bind9</h3><br>'
    html += '<p><h2>Show Domains :</h2>'
    html += '<code><a href="{}domains/">http://{}/domains/</a></code></p>'.format(request.path, request.get_host())
    html += '<p><h2>Add Domains :</h2>'
    html += '<code><a href="{}adddomain/">http://{}/adddomain/[DomainName]/[PublicAddress]/[LocalAddress]/</a></code></p>'.format(request.path, request.get_host())
    html += '<p><h2>Show Records :</h2>'
    html += '<code><a href="{}showrecords/">http://{}/showrecords/[DomainName]/</a></code></p>'.format(request.path, request.get_host())
    html += '<p><h2>Add Records :</h2>'
    html += '<code><a href="{}addrecord/">http://{}/addrecord/[DomainName]/[RecordType]/[Key]/[Value]/</a></code></p>'.format(request.path, request.get_host())
    html += '<p><h2>Delete Records :</h2>'
    html += '<code><a href="{}deleterecord/">http://{}/deleterecord/[DomainName]/[RecordName]/[RecordType]/</a></code></p>'.format(request.path, request.get_host())
    html += '<p><h2>Refresh DNS :</h2>'
    html += '<code><a href="{}refresh/">http://{}/refresh/[DomainName]/</a></code></p>'.format(request.path, request.get_host())
    html += '<br></center>'
    return HttpResponse(html)


