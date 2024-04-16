"""Lorem ipsum for now."""

# 
import csv, json, gzip
from jobSchema import job_schema

# 
f = open('python-scripts/enforms-2024-04-12.json')
enforms = json.load(f)
new_list = []
job_list = []

# 
for obj in enforms:
    if 'EnForms' in obj:
        for form in obj['EnForms']:
            new_list.append(form)
        del obj['EnForms']
        new_list.append(obj)
    else:
        new_list.append(obj)

# 
for obj in new_list:
    if 'channelID' in obj:
        job = job_schema
        job['job_id'] = obj['channelID']
        if 'subForm' in obj:
            if obj['subForm'] == 'DISPATCH':
                job['dispatch'] = obj
            elif obj['subForm'] == 'CASH JOB LANDED':
                job['cash_job_landed'] = obj
            elif obj['subForm'] == 'INSURANCE JOB LANDED':
                job['insurance_job_landed'] = obj
            elif obj['subForm'] == 'NOT LANDED':
                job['not_landed'] = obj
            elif obj['subForm'] == 'NO ACCESS':
                job['no_access'] = obj
            elif obj['subForm'] == 'CANCELED':
                job['canceled'] = obj
            elif obj['subForm'] == 'COMP ASSESSMENT':
                job['comp_assessment'] = obj
            elif obj['subForm'] == 'RENO JOB LANDED':
                job['reno_job_landed'] = obj
            elif obj['subForm'] == 'RENO JOB NOT LANDED':
                job['reno_job_not_landed'] = obj
            elif obj['subForm'] == 'INSURANCE UPDATE':
                job['insurance_update'] = obj
            elif obj['subForm'] == 'PM POST RBD MTG':
                job['pm_post_rbd_mtg'] = obj
            elif obj['subForm'] == 'FS to FE Handoff':
                job['fs_to_fe_handoff'] = obj
            elif obj['subForm'] == 'INSTALL':
                job['install'] = obj
            elif obj['subForm'] == 'CHECK-IN':
                job['check_in'] = obj
            elif obj['subForm'] == 'PULL':
                job['pull'] = obj
            elif obj['subForm'] == 'APPROVAL NEEDED':
                job['approval_needed'] = obj
            elif obj['subForm'] == 'POM COMPLETION':
                job['pom_completion'] = obj
            elif obj['subForm'] == 'SERVICE REQUEST':
                job['service_request'] = obj
            elif obj['subForm'] == 'CAPS AND LEAKS':
                job['caps_and_leaks'] = obj
            elif obj['subForm'] == 'UPDATE':
                job['update'] = obj
            elif obj['subForm'] == 'TECH SPILL':
                job['tech_spill'] = obj
            elif obj['subForm'] == 'FS HOME VISIT':
                job['update'] = obj
            job_list.append(job)
        
# 
final_data = json.dumps(job_list)
with open('python-scripts/final_data.json', 'w') as of:
    of.write(final_data)     
with gzip.open('python-scripts/final_data.json.gz', 'w') as f:
    f.write(bytes(source=final_data, encoding='utf-8'))