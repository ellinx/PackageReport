from django.db import models


class UserRight(models.Model):
    oid = models.CharField(max_length = 40)
    role = models.CharField(max_length = 20, blank = True)

class MailGroup(models.Model):
    name = models.CharField(max_length = 40)
    owner = models.CharField(max_length = 100, blank = True)
    passcode = models.CharField(max_length = 10, blank = True)
    address = models.CharField(max_length = 160, blank = True)
    created = models.DateTimeField('created at')

    def __str__(self):
        ret = ""
        ret += "Group name:" + self.name + ", "
        ret += "Owner:" + self.owner + ", "
        ret += "Passcode:" + self.passcode + ","
        ret += "Address:" + self.address + ", "
        ret += "Created at:" + str(self.created)
        return ret

class PackageInfo(models.Model):
    name = models.CharField(max_length = 160)
    logistics = models.CharField(max_length = 50)
    tracking = models.CharField(max_length = 20)
    weight = models.IntegerField(default = 0, blank = True)
    volume = models.CharField(max_length = 20, blank = True)
    item_info = models.CharField(max_length = 200, blank = True)
    comment = models.CharField(max_length = 400, blank = True)
    mail_group = models.ForeignKey(MailGroup, on_delete = models.CASCADE)
    oid = models.CharField(max_length = 30, blank = True)
    last_update = models.DateTimeField('last update')
    status = models.CharField(max_length = 20, default = "0")
    image = models.CharField(max_length = 60, blank = True)

    def __str__(self):
        ret = ""
        ret += "name:" + self.name + ", "
        ret += "logistics:" + self.logistics +", "
        ret += "tracking:" + self.tracking + ", "
        ret += "weight:" + str(self.weight) + ", "
        ret += "volume:" + self.volume + ", "
        ret += "item_info:" + self.item_info + ", "
        ret += "comment:" + self.comment + ", "
        ret += "mail_group:" + self.mail_group.name + ", "
        ret += "oid:" + self.oid + ", "
        ret += "last_update:" + str(self.last_update) + ", "
        ret += "status:" + self.status + ", "
        ret += "image:" + self.image
        return ret 
