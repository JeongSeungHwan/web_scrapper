import csv

def save_to_csv(jobs,word) :
    saving_file = open(f"{word}.csv", mode="w", encoding="utf8")
    writer = csv.writer(saving_file)
    writer.writerow(["No", "title", "company"])
    for job in jobs:
        writer.writerow(list(job.values()))
    
