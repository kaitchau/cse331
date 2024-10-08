import sys
import csv
import time
import hashlib

# Dictionary attack

def read_pw_db_csv(file_path):
    pw_db_rows = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # append username, pw, salt
            pw_db_rows.append((row[0],row[1],row[2]))
    return pw_db_rows

def process_com_pw():
    # NOTE: the common pw csv from kaggle has to be in same directory
    common_passwords = []
    with open("common_passwords.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            #password is in the 1st column
            common_passwords.append(row[0])
    hashed_common_passwords = {}
    for password in common_passwords:
        hashed_common_passwords[hashlib.md5(password.encode()).hexdigest()] = password
    return hashed_common_passwords

def dictionary_attack(data, hashed_com_pw):
    start_time = time.time()
    output = []
    total=0
    success_ct=0

    for user, pw, salt in data:
        if pw in hashed_com_pw:
            pt_pw = hashed_com_pw[pw]
            output.append((user,pt_pw))
            success_ct+=1
        else:
            output.append((user,"FAILED"))
        total+=1

    end_time=time.time()
    total_time = end_time-start_time

    with open("task2.csv", "w") as file:
        writer = csv.writer(file)
        for row in output:
            writer.writerow(row)
        writer.writerow([f"TOTALTIME [{total_time} seconds]"])
        success_rate = (success_ct/total)*100
        writer.writerow([f"SUCCESSRATE [{success_rate}%]"])

if __name__ == "__main__":
    pw_db_csv = sys.argv[1]
    pw_db = read_pw_db_csv(pw_db_csv)
    hashed_com_pw =  process_com_pw()
    dictionary_attack(pw_db, hashed_com_pw)