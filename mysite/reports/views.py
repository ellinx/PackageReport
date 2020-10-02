from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

import json
import datetime
from .models import PackageInfo, MailGroup


def index(request):
    package_list = PackageInfo.objects.all()
    group_list = list(set([package.mail_group.name for package in package_list]))
    context = {
        'group_list': group_list,
    }
    return render(request, "reports/index.html", context)

def detail(request, package_id):
    package = get_object_or_404(PackageInfo, pk = package_id)
    return render(request, "reports/detail.html", {"package": package})

def group(request):
    print(request.GET)
    package_list = PackageInfo.objects.filter(group = request.GET["groups"])
    name_package_map = dict()
    for package in package_list:
        if package.name not in name_package_map:
            name_package_map[package.name] = []
        name_package_map[package.name].append(package)
    context = {
        "name_package_map": name_package_map,
    }
    return render(request, "reports/index.html", context)


##################################################

#retrieve all packages of certain user
@csrf_exempt
def wx_all(request):
    req_data = json.loads(request.body)
    print(req_data)
    package_list = PackageInfo.objects.filter(oid = req_data["oid"])
    group_set = set([package.mail_group.name for package in package_list])
    data = dict()
    for package in package_list:
        info = dict()
        info["pk"] = package.pk
        info["name"] = package.name
        info["logistics"] = package.logistics
        info["tracking"] = package.tracking
        info["weight"] = package.weight
        info["volume"] = package.volume
        info["item_info"] = package.item_info
        info["comment"] = package.comment
        info["last_update"] = package.last_update
        info["status"] = package.status
        data[package.mail_group.name] = data.get(package.mail_group.name, list()) + [info]
    return JsonResponse(data)

#update a list of package information
@csrf_exempt
def wx_update(request):
    req_data = json.loads(request.body)
    print(req_data)
    for each in req_data:
        package = PackageInfo.objects.get(pk = each["pk"])
        if "logistics" in each:
            package.logistics = each["logistics"]
        if "tracking" in each:
            package.tracking = each["tracking"]
        if "weight" in each:
            package.weight = each["weight"]
        if "volume" in each:
            package.volume = each["volume"]
        if "item_info" in each:
            package.item_info = each["item_info"]
        if "comment" in each:
            package.comment = each["comment"]
        if "status" in each:
            package.status = each["status"]
        package.last_update = datetime.datetime.now()
        package.save()
    return JsonResponse({"msg": "wx_update"})

#create a list of new package information
@csrf_exempt
def wx_create(request):
    req_data = json.loads(request.body)
    print(req_data)
    for each in req_data:
        package = PackageInfo(name=each["name"],logistics=each["logistics"],tracking=each["tracking"])
        package.mail_group = MailGroup.objects.get(pk = each["mail_group_pk"])
        package.last_update = datetime.datetime.now()
        package.status = each["status"]
        if "weight" in each:
            package.weight = each["weight"]
        if "volume" in each:
            package.volume = each["volume"]
        if "item_info" in each:
            package.item_info = each["item_info"]
        if "comment" in each:
            package.comment = each["comment"]
        package.save()
    return JsonResponse({"msg": "wx_create"})

#delete a list of package information
@csrf_exempt
def wx_delete(request):
    req_data = json.loads(request.body)
    print(req_data)
    for each in req_data:
        package = PackageInfo.objects.get(pk = each["pk"])
        package.delete()
    return JsonResponse({"msg": "wx_delete"})
