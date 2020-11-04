import csv

def save_to_csv(jobs) :
    saving_file = open("jobs.csv", mode="w", encoding="utf8")
    writer = csv.writer(saving_file)
    writer.writerow(["No", "title", "company"])
    for job in jobs:
        writer.writerow(list(job.values()))
    
