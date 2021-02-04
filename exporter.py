import csv

def save_to_file(jobs):
    file = open("jobs.csv", mode="w") # mode를 쓰기만 설정해줌
    writer = csv.writer(file)
    writer.writerow(['title','company','location','link'])
    
    # job은 dictionary 형태이다. -> list형태로 변형 필요
    for job in jobs:
        print(job)
        writer.writerow(list(job.values()))
    
    return