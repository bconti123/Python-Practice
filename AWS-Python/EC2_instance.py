for i in ec2.instances.all():
    if i.state['Name'] == 'stopped':
        i.start()




